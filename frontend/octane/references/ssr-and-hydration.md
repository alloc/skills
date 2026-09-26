# SSR, deferred hydration, and behavior roots

Contents: SSR/streaming, `<Hydrate>` strategies and code splitting, `attachBehaviorRoot` for externally owned DOM.

## Server-side rendering

Octane provides full SSR and byte-stable hydration, including streaming SSR via `renderToPipeableStream`/`renderToReadableStream` that flushes each Suspense boundary out-of-order as its data resolves.

## Deferred hydration with `<Hydrate>`

`Hydrate` is an experimental core API for initial server-rendered content. It preserves visible server HTML while postponing component execution, refs, effects, and events. A boundary first mounted after the app is already running renders normally on the client.

```tsrx
import { Hydrate } from 'octane';
import { visible } from 'octane/hydration';

export function ProductPage() @{
	<Hydrate when={visible({ rootMargin: '400px' })}>
		<Reviews />
	</Hydrate>
}
```

Every boundary makes three performance decisions:

1. **`when` (required)** — when preserved server HTML becomes interactive. Strategies from `octane/hydration`: `load()`, `idle({ timeout? })`, `visible({ rootMargin?, threshold? })`, `media(query)`, `interaction({ events? })` (replays the triggering event), `condition(booleanOrGetter)`, `never()`. A function form may choose a strategy from client-only information — it is not called on the server and must return synchronously:

   ```tsrx
   <Hydrate when={() => window.matchMedia('(pointer: coarse)').matches ? interaction() : visible()}>
   ```

2. **`split`** — defaults to `true`. The compiler extracts direct children into a generated chunk that Vite/Rsbuild do not eagerly module-preload. Use literal `split={false}` when the code is already required elsewhere or a separate request is not worthwhile.

3. **`prefetch`** — starts the split chunk or custom preparation before `when` activates. Strategy prefetch accepts `load()`, `idle()`, `visible()`, `media()`, `interaction()`; `condition()`, `never()`, and function-form strategies are activation-only. Strategy prefetch loads code but leaves the DOM inert:

   ```tsrx
   <Hydrate when={interaction()} prefetch={idle()}>
   	<RecommendationEditor />
   </Hydrate>
   ```

   A procedural prefetch can prepare code and data. Awaited work blocks activation if `when` resolves first; `signal` aborts when the boundary is removed. The context also exposes `waitFor(strategy)` and the persistent boundary `element`:

   ```tsrx
   <Hydrate
   	when={visible()}
   	prefetch={async ({ preload, signal }) => {
   		await preload();
   		await warmReviews({ signal });
   	}}
   >
   	<Reviews />
   </Hydrate>
   ```

   Procedural prefetch works with either split mode; strategy prefetch requires splitting.

Remaining props: `fallback` (client-only loading UI for a later client mount or suspension — initial server HTML stays visible while its strategy or first activation suspension waits; `fallback` does not replace it), `onHydrated` (called once after the child commits on the client), and `children` (the server-rendered subtree).

## Behavior-only roots and external ownership

`<Hydrate split={false} when={never()}>` preserves externally managed server DOM without a wrapper, but its descendant client component graph is deliberately erased — component event handlers inside that range never attach. To add separately owned behavior without hydrating, rendering, replacing nodes, or taking reconciliation ownership, use `attachBehaviorRoot` from `octane/behavior` (or the same API from `octane`):

```ts
import { attachBehaviorRoot } from 'octane/behavior';
import { articleStream } from './article-stream.js';

const lifetime = new AbortController();
const owner = Symbol('article stream');
const root = attachBehaviorRoot(document.querySelector('#app')!, {
	signal: lifetime.signal,
});

root.registerExternalRange(document.querySelector('#article')!, {
	owner,
	ready: articleStream.allReady,
});

root.registerBehavior({
	id: 'article-annotations',
	owner,
	target: '[data-annotation]',
	events: ['click'],
	ready: import('./annotations.js').then((module) => {
		activateAnnotation = module.activateAnnotation;
		observeAnnotation = module.observeAnnotation;
	}),
	adopt(element, { signal }) {
		return observeAnnotation(element, signal);
	},
	handleEvent(event, element) {
		activateAnnotation(event, element);
	},
});

await root.ready;
root.dispose(); // abort behavior and preserve the existing DOM
```

- Behavior roots neither render nor hydrate. Existing nodes, protected attributes, HTML/SVG/MathML namespaces, and independent streamed updates remain externally owned. Selector targets discover subsequently inserted matching elements.
- `registerExternalRange(element, { owner, ready?, signal?, replace? })` explicitly declares external ownership; the closest registered nested range wins. A second owner for the same element requires `replace: true`; an already-aborted replacement never evicts a live owner. Root and range identity are scoped to their document and container.
- `registerBehavior({ target, adopt, id?, owner?, events?, ready?, dependencies?, conflicts?, signal?, handleEvent? })` accepts a selector or element. `adopt(element, { signal, event?, range? })` may return synchronous or asynchronous cleanup; named dependencies must already exist, and conflicts or duplicate IDs fail deterministically. Adoption waits for behavior, dependency, and matching range readiness.
- Delegated interactions are observed immediately, including before asynchronously loaded behavior or externally streamed ranges become ready. `handleEvent` receives the exact original same-document `Event` and its genuine `isTrusted` value — Octane never redispatches it, invents trusted events, repeats native link/form activation, or restores expired transient user activation. This direct delivery is distinct from `<Hydrate when={interaction()}>` replay.
- `root.ready` snapshots active ranges and behaviors; each registration exposes its own `ready`, `signal`, and idempotent `dispose()`. Root cancellation aborts pending work, ignores stale async completions, disconnects listeners/observers, and runs adopted cleanup exactly once. `root.dispose()` preserves DOM by default; `dispose({ preserveDOM: false })` explicitly clears descendants. Replacing a live root on the same container requires `attachBehaviorRoot(container, { replace: true })`.
