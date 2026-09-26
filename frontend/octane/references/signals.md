# Signals

Contents: imports and naming, declarations (`signal$`, `derived$`, `query$`), reading in components, `useSignal$`, explicit scopes and `createResource`, availability reads, optimistic actions and transitions, SSR/seeding/streamed results, limits and errors.

Signals are a stable API working with the standard compiler and its Vite/Rspack/Rsbuild integrations — no `nativeReads` option needed.

- Import `signal$`, `derived$`, `query$`, `skip`, `optimistic$`, `action$`, `createScope`, `createResource`, `query` from `octane/signals`.
- Import `useSignal$` from `octane/signals/client` for component-local state. Server compilation selects `octane/signals/server` automatically.
- Module declarations resolve to request-local cells on the server and document-local cells in the browser — unmounting one root does not dispose document-global state.

## Naming and native reads

- Name handles, properties, and helpers that return handles or expose live reads with a trailing `$`: `count$`, `props.user$`, `readCount$()`. Sampled values keep ordinary names.
- Every module consuming native reads needs a runtime import from a signals entry — a type-only import or a `$` name alone is insufficient. For imported handles, a side-effect `import 'octane/signals'` enables compilation.
- Native reads during rendering subscribe the render scope. Effects and event callbacks read imperatively and create no render subscriptions.
- Explicit arrays are never rewritten: `[count$]` in a memo sees only the stable handle. Sample during render (`const count = count$.get()`) and use `[count]` for explicit deps. `null` keeps its every-render meaning.

## Declarations

```ts
// user-data.ts — compile with Octane.
import { derived$, query$, signal$, skip } from 'octane/signals';

export type User = { id: number; name: string; revision: number };
export const selectedId$ = signal$<number | null>(1);
export const user$ = query$<number, User>(
	() => selectedId$.get() ?? skip,
	async (id, { signal }) => {
		const response = await fetch(`/api/users/${id}`, { signal });
		if (!response.ok) throw new Error(`User request failed: ${response.status}`);
		return response.json() as Promise<User>;
	},
);
export const greeting$ = derived$(async ({ read, signal }) => {
	const user = await read(user$);
	const locale = await read(locale$); // dependency tracked after await
	const response = await fetch(`/api/greeting/${user.id}?locale=${encodeURIComponent(locale)}`, { signal });
	if (!response.ok) throw new Error(`Greeting request failed: ${response.status}`);
	return response.text();
});
```

- `signal$(initial)` is writable; `.set(value)` or `.set(updater)` uses `Object.is` equality. Replace objects/arrays — deep mutation is not tracked.
- `derived$(compute)` is read-only and accepts an immediate value, Promise, async iterable, or Promise of an async iterable. Synchronous calculations stay immediate.
- `query$(select, load)` tracks its synchronous selector; the loader is untracked and starts only after selection succeeds. `skip` means no request and an `idle` snapshot; `undefined` is a valid argument. Strict idle reads throw `SignalIdleError`. Canonically equal selected arguments deduplicate within the owner.
- `user$.refetch()` retains a usable same-selection value with `refreshing: true`; `user$.reset()` makes strict reads pending. Loaders receive `{ signal, previous }` — an optional prior ready value. Changed selection, refetch/reset, or disposal revokes obsolete publication even when cancellation is ignored.
- Async `derived$` uses its attempt-bound `read(handle$)` to await and track dependencies, including after `await`. Dependency changes abort the attempt and invalidate obsolete resolutions/errors/yields. Proven async native reads work; opaque helpers need explicit `read`. There is no ambient dependency context across arbitrary async code.
- Optional trailing `{ key }` gives explicit identity: `signal$('', { key: 'draft' })`. The compiler supplies declaration identities; uncompiled declarations require nonempty explicit keys. `signal$('draft')` stores a string — it is not a positional key. Function initial values are data; `handler$.set(() => nextHandler)` stores a function.

### Streams

- `query$(select, load, { kind: 'stream' })` accepts an async iterable or a promise of one; `derived$` can just return an async iterable (no `kind` option).
- Before first yield: pending/connecting. Yields are ready/open. Completion retains the last value with closed/complete; completing without a yield is an error. Cancellation requests abort and iterator closure.

## Reading in components

Handle `idle` separately, then use a pending/error boundary:

```tsrx
import 'octane/signals';
import { user$ } from './user-data';

export function UserCard() @{
	<section>
		@if (user$.snapshot().status === 'idle') {
			<p>Choose a user.</p>
		} @else {
			@try {
				<p>{user$.get().name as string}</p>
			} @pending {
				<p>Loading user…</p>
			} @catch (error) {
				<p role="alert">{String(error)}</p>
			}
		}
	</section>
}
```

Availability reads:

| Read | Contract |
| --- | --- |
| `handle$.get()` | Ready value, pending thenable, or thrown idle/source error. Use `@try`/`@pending`/`@catch` or `Suspense`/`ErrorBoundary` for pending/error UI |
| `handle$.latest(fallback)` | Whole last successful calculation, or `fallback` (default `undefined`). Never hides disposed owners or invalid adoption frames |
| `handle$.snapshot()` | Immutable `idle`/`ready`/`pending`/`error` record; ready has `value`, error has `error`. Also `refreshing`, `connection`, `complete`, optional `requestKey` |
| `scope.isPending(read)` | Whether that expression suspends; ordinary errors still throw. A successful `latest(fallback)` is not pending even when a strict read would suspend |

`undefined`, `null`, `false`, and empty strings are usable values. A retained result need not have appeared in committed UI — keep its identity, values, and commands in the same derived result (do not combine an old user's retained card with a new user's delete command). Retained results stay valid only while their contributing owners are alive.

## `useSignal$`: component-owned state

```tsrx
import { useSignal$ } from 'octane/signals/client';

export function Counter() @{
	const count$ = useSignal$(0);
	<button onClick={() => count$.set((count) => count + 1)}>{String(count$.get())}</button>
}
```

Accepts a value or lazy initializer and returns a stable writable handle owned by its compiler-assigned hook slot; unmounting disposes it. Conditional hooks work; use keyed `@for` or a child component for loops. Local derived and async hooks are not available.

## Explicit scopes

For manually managed shared state, create a scope at the data owner's lifetime boundary, pass handles through props/context, and dispose it when that owner ends:

```ts
import { createResource, createScope, query } from 'octane/signals';

const account = createScope({ scopeKey: 'account' });
const userId$ = account.signal$('user-id', 1);
const doubled$ = account.derived$('doubled', () => userId$.get() * 2);
const fetchUser = query('user', async (id: number, { signal }) => {
	const response = await fetch(`/api/users/${id}`, { signal });
	if (!response.ok) throw new Error(`User request failed: ${response.status}`);
	return response.json() as Promise<{ id: number; name: string }>;
});
const user$ = createResource(account, 'user', () => fetchUser(userId$.get()));
```

- Keys are nonempty strings unique within a scope; equal textual `scopeKey` values do not share live state. `scope.get(handle$)`/`scope.set(handle$, value)` require the handle to belong to that scope.
- `scope.derived$(key, compute)` is synchronous only — use the declaration `derived$` for async work. A computation may read another scope's handles without owning them.
- Writes are immediately readable. `scope.batch(fn)` delays notifications until the outer synchronous batch ends; `scope.action(fn)` wraps a function with the same batching rule and preserves `this`, arguments, and result. Neither rolls back writes or batches across `await`. Writes during rendering, derived evaluation, updater callbacks, and historical adoption are rejected.
- `handle$.subscribe(notify)` returns an unsubscribe function and does not notify initially.
- `scope.dispose()` is idempotent: cancels requests/streams, releases subscriptions and retained state. Escaped handles then throw `ScopeDisposedError`. Unmounting one consumer does not dispose an explicit shared scope.
- `createResource(scope, key, describe)` eagerly tracks the synchronous request-selection callback; the query loader is untracked and cannot publish obsolete results after selection changes, retry, or disposal. Equivalent query arguments share in-flight work within one scope; there is no idle cache of historical keys. Reusing a query key with an incompatible loader is rejected.
- `resource$.retry()` refreshes while preserving a usable current value; `retry({ pending: true })` makes strict reads suspend. Data retry and UI error-boundary reset are separate operations.
- `query(key, loader, { kind: 'stream' })` follows the same stream lifecycle as declaration `query$`.

## Optimistic actions and transitions

`optimistic$(source$)` layers operation-owned tentative state over a writable or query source. Write inside `action$`:

```ts
import { action$, optimistic$ } from 'octane/signals';
import { user$ } from './user-data';
import { mayHaveReachedServer, updateUser } from './api';

export const visibleUser$ = optimistic$(user$, {
	compareAuthority: (incoming, current) => incoming.revision - current.revision,
});
export const saveUser = action$('user.save', async (operation, name: string) => {
	const id = user$.get().id;
	visibleUser$.set((user) => ({ ...user, name }));
	try {
		const saved = await updateUser({ id, name, operationId: operation.id });
		operation.adopt(saved);
	} catch (error) {
		if (mayHaveReachedServer(error)) return operation.uncertain();
		throw error;
	}
});
```

- Render `visibleUser$.get()`; invoke `saveUser(name)` from an event or form action. The first write pins the owner and exact query-selection generation — late adoption cannot overwrite a different selection, including A→B→A.
- `compareAuthority` must be pure and finite; positive means newer, zero/negative settles without replacing authority. It governs action receipts, not independently fetched/streamed updates.
- The synchronous action prefix is batched. Opaque code after `await` uses `operation.set(visibleUser$, update)` — ambient operation state is synchronous.
- `operation.uncertain()` retains the overlay and returns an uncertain receipt; an `OCTANE_RPC_UNCERTAIN` error becomes `ActionUncertainError`; `isActionUncertain` recognizes either form. No mutation retry, durable idempotency, or receipt storage is automatic — retain the operation for reconciliation, then `adopt(value)` or `reject()` after an authorized receipt lookup. Deferred handlers must receive inputs captured when the command occurred, not reread a newer draft.
- Native setters inside an explicit renderer `startTransition`/`useTransition` stage a private candidate: committed reads, public subscriptions, and affected DOM bindings keep old values until presentation can accept the candidate. Works for local writable/derived/query producers and local streams after first value; receiver-owned server streams and historical adoption frames reject transition participation. `scope.action` alone only batches synchronous writes.

## SSR, seeds, and streamed results

- Module declarations use the server request owner; explicit scopes must be created per request. Match scope/signal identities between server and client; distinct owners in one presented graph need distinct scope keys.
- Native completed reads serialize ready values, retained `latest` values, and ready snapshots. Hydration adopts historical values without rewinding live state. A matching completed resource seed avoids a duplicate client load; an incomplete ready resource in seed-only transport starts a quiet client attempt. Server-local `useSignal$` lasts one render pass and is not shared-state seed data.
- `scope.serialize()` returns a `ScopeSeed`. For explicit embedding, `scope.beginAdoption(seed)` returns a frame with synchronous `run(read)`, `retain()` for another lease, and `release()` for cleanup.
- Serializable values: undefined, null, booleans, finite numbers, strings, dense arrays, acyclic plain objects with enumerable string data properties. Arguments are copied/frozen and object keys canonicalized. Cycles, sparse arrays, accessors, symbols, custom prototypes, and nonfinite numbers are rejected.
- Ready-state seeds do not transport pending producers or error objects. Server output that samples a pending/error snapshot or displays an `isPending` result is diagnosed — use a boundary or a serializable `latest` projection. Pending/catch arms without seedable data render fresh within their owned hydration range.

### Streamed results and early controls

Accepted results may arrive before the query module loads. Matching document/instance/selection/attempt identities attach to the later query without a duplicate browser request. For custom hosts, bootstrap before importing modules that read document signals:

```ts
import { bindSignalControl } from 'octane/signals';
import { bootstrapStreamedSignalResults, type NativeSignalManifest } from 'octane/hydration/streamed-signals';

export async function attachEditor(bootstrap: {
	buildId: string;
	documentId: string;
	initialSignals: NativeSignalManifest;
}) {
	const page = bootstrapStreamedSignalResults(bootstrap);
	try {
		const { draft$ } = await import('./draft-state');
		const textarea = document.querySelector<HTMLTextAreaElement>('#draft')!;
		const stop = bindSignalControl(textarea, 'value', draft$);
		return {
			signalOwner: page.signalOwner,
			releaseControl: stop, // before transferring this node to an island
			dispose() { stop(); page.dispose(); }, // only when the document owner ends
		};
	} catch (error) {
		page.dispose();
		throw error;
	}
}
```

- The host supplies matching build/document identities and the initial response's native manifest, installs it once before live reads, and uses the same bundled signal engine for early/later consumers. Early edits win; late/duplicate installation throws.
- Server hosts emit `earlySignalBootstrapScript({ nonce })` from `octane/server` before controls/results and use `earlySignalBootstrap: 'external'` on fragment renderers.
- Use `bootstrapStreamedSignalHydration` instead when `receiver.registerRegion` places streamed HTML; one bootstrap per document. Later roots join `page.signalOwner`; custom owners need `runWithSignalOwner` around behavior callbacks.
- `bindSignalControl` projects `value` on text inputs/textareas/selects or `checked` on checkboxes/radios; writable handles adopt captured edits and receive native writeback, readonly handles only project. It creates no renderer root. Call `releaseControl()` before replacing the node or handing it to an island.
- Keep cached HTML and client/server compiler output from matching builds.

## Limits, inspection, and errors

- Native rendering supports DOM client/server. Deep stores, local derived/async hooks, cross-root atomic reveal, and native reads in non-DOM renderers remain outside the API.
- `scope.inspect()` reports metadata without evaluating dormant computations or exposing values/callbacks. `createScope({ scopeKey, debug: { traceLimit: 256 } })` enables bounded tracing; profiling builds expose native reads in DevTools.
- Public errors: `ScopeDisposedError`, `SignalCycleError`, `SignalFrameError`, `SignalIdleError`, `SignalSerializationError`, `SignalStreamError`, `SignalWriteError`, `ActionUncertainError`.
- The separate `@octanejs/alien-signals` binding keeps its existing API.
