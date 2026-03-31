# preact-sigma API Details

This file contains extended API documentation for `preact-sigma`, an extension to `SKILL.md`.

## Runtime Exports

Import runtime APIs from `preact-sigma`.

```typescript
import {
  SigmaType,
  action,
  batch,
  computed,
  effect,
  freeze,
  immerable,
  isSigmaState,
  listen,
  query,
  ref,
  replaceState,
  setAutoFreeze,
  snapshot,
  untracked,
  useListener,
  useSigma,
} from "preact-sigma";
```

## Type Exports

- `AnyDefaultState`: Describes the object accepted by `.defaultState(...)`.
- `AnyEvents`: Describes an event map from event names to payload objects or `void`.
- `AnyResource`: Describes a supported setup cleanup resource.
- `AnySigmaState`: Describes the public shape shared by all sigma-state instances.
- `AnySigmaStateWithEvents`: Describes a sigma-state instance with a typed event map.
- `AnyState`: Describes the top-level state object for a sigma type.
- `InferEventType`: Infers the supported event names for a target used with `listen(...)` or `useListener(...)`.
- `InferListener`: Infers the listener signature for a target and event name.
- `InferSetupArgs`: Infers the `setup(...)` argument list for a sigma-state instance.
- `SigmaObserveChange`: Describes the object received by `.observe(...)` listeners.
- `SigmaObserveOptions`: Describes the options object accepted by `.observe(...)`.
- `SigmaState`: Describes the public instance shape produced by a configured sigma type.

## `get(key)`

`instance.get(key)` returns the underlying `ReadonlySignal` for one top-level state property or computed.

Behavior:

- state-property keys return that property's signal
- computed keys return that computed getter's signal

## `computed`

Computeds are added with `.computed({ ... })`.

Behavior:

- each computed is exposed as a tracked getter property
- computed getters are non-enumerable on the public instance
- `this` inside a computed exposes readonly state plus other computeds
- computeds do not receive query or action methods on `this`
- computeds cannot accept arguments

## `queries`

Queries are added with `.queries({ ... })`.

Behavior:

- queries may accept arbitrary parameters
- `this` inside a query exposes readonly state, computeds, and other queries
- queries do not receive action methods on `this`
- when a query runs inside an action, it reads from the current draft-aware state
- query results are reactive at the call site but are not memoized across calls
- prefer `.queries({ ... })` for commonly needed instance methods
- not every calculation belongs in `.queries({ ... })`; keeping a calculation local to the module that uses it is often clearer until it becomes a common use case
- query wrappers are shared across instances
- query typing only exposes computeds and queries that were already present when its `.queries(...)` call happened

## `observe`

Observers are added with `.observe(listener, options?)`.

Behavior:

- each observer runs after a successful action commit that changes base state
- observers do not run for actions that leave base state unchanged
- `change.newState` is the committed base-state snapshot for that action
- `change.oldState` is the base-state snapshot from before that action started
- `this` inside an observer exposes readonly state, computeds, and queries
- observers do not receive action methods or `emit(...)` on `this`
- same-instance sync nested action calls produce one observer notification after the outer action commits
- patch generation is opt-in with `{ patches: true }`
- when patch generation is enabled, `change.patches` and `change.inversePatches` come from Immer
- applications are responsible for calling `enablePatches()` before using observer patch generation
- observer typing only exposes computeds and queries that were already present when that `.observe(...)` call happened

## `setup`

Setup is added with `.setup(fn)`.

Behavior:

- setup is explicit; a new instance does not run setup automatically
- each `.setup(...)` call adds another setup handler
- `useSigma(...)` calls `.setup(...)` for component-owned instances that define setup
- calling `.setup(...)` again cleans up the previous setup first
- one `.setup(...)` call runs every registered setup handler in definition order
- the public `.setup(...)` method always returns one cleanup function
- `this` inside a setup handler exposes the public instance plus `emit(...)`
- each setup handler returns an array of cleanup resources
- setup typing only exposes computeds, queries, and actions that were already present when that `.setup(...)` call happened

Supported cleanup resources:

- cleanup functions
- objects with `[Symbol.dispose]()`
- `AbortController`

When a parent setup wants to own a nested sigma state's setup, call the child sigma state's `setup(...)` method and return that cleanup function.

Cleanup runs in reverse order. If multiple cleanup steps throw, cleanup rethrows an `AggregateError`.

## `ref(value)`

`ref(value)` returns `value` unchanged and marks its type so sigma's `Draft` and `Immutable` helpers keep that value by reference.

Behavior:

- it has no runtime effect
- it only changes sigma's local `Draft` and `Immutable` typing
- it prevents type-level recursive immerization for that value
- it does not change whether Immer drafts or freezes the value at runtime

## Public Instance Shape

A sigma-state instance exposes:

- one readonly enumerable own property for every state property
- one tracked non-enumerable getter for every computed
- one method for every query
- one method for every action
- `get(key): ReadonlySignal<...>` for state-property and computed keys
- `setup(...args): () => void` when the builder has at least one setup handler
- `on(name, listener): () => void`
- `Object.keys(instance)` includes only top-level state properties

## Reactivity Model

- each top-level state property is backed by its own Preact signal
- public state reads are reactive
- signal access is reactive, so reading `.value` tracks like any other Preact signal read
- computed getters are reactive and lazily memoized
- queries are reactive at the call site, including queries with arguments
- query calls are not memoized across invocations; each call uses a fresh `computed(...)` wrapper and does not retain that signal

## Actions details

- actions create drafts lazily when reads or writes need draft-backed mutation semantics
- actions may call other actions, queries, and computeds
- same-instance sync nested action calls reuse the current draft
- any other action call starts a different invocation and is a draft boundary
- `emit()` is a draft boundary
- `await` inside an async action is a draft boundary
- `this.commit()` publishes the current draft immediately
- `this.commit()` is only needed when the current action has unpublished draft changes and is about to cross a draft boundary
- a synchronous action does not need `this.commit()` when it finishes without crossing a draft boundary
- declared async actions publish their initial synchronous draft on return
- after an async action resumes from `await`, top-level reads of draftable state and state writes may open a hidden draft for that async invocation
- non-async actions must stay synchronous; if one returns a promise, sigma throws
- if an async action reaches `await` or `return` with unpublished changes, the action promise rejects when it settles
- if an action crosses a boundary while it owns unpublished changes, sigma throws until `this.commit()` publishes them
- if a different invocation crosses a boundary while unpublished changes still exist, sigma warns and discards them before continuing
- successful publishes deep-freeze draftable public state and write it back to per-property signals while auto-freezing is enabled
- custom classes participate in Immer drafting only when the class opts into drafting with `[immerable] = true`
- actions can emit typed events with `this.emit(...)`
- action wrappers are shared across instances
- action typing only exposes computeds, queries, and actions that were already present when its `.actions(...)` call happened

Nested sigma states stored in state stay usable as values. Actions do not proxy direct mutation into a nested sigma state's internals.

## Events

Events are emitted from actions or setup through `this.emit(name, payload?)`.

Behavior:

- the event map controls allowed event names and payload types
- `void` events emit no payload
- object events emit one payload object
- `.on(name, listener)` returns an unsubscribe function
- listeners receive the payload directly, or no argument for `void` events

## Advanced Utilities

- **`immerable`**: Re-exported from Immer so custom classes can opt into drafting with `[immerable] = true`. Unmarked custom classes stay outside Immer drafting and deep-freezing. Plain objects, arrays, `Map`, and `Set` work by default.
- **`setAutoFreeze(autoFreeze)`**: Controls whether sigma deep-freezes published public state at runtime (enabled by default).
- **`snapshot(instance)`**: Returns a shallow snapshot of an instance's committed public state (does not include computeds, queries, or recurse into nested sigma states).
- **`replaceState(instance, snapshot)`**: Replaces committed public state from a plain snapshot object, notifying observers. Throws if an action still owns unpublished changes. When observer patch generation is enabled, also delivers patches and inverse patches.
- **`query(fn)`**: Creates a standalone tracked query helper, useful for helpers that are large or rarely needed and can live outside the sigma state.

## Hooks & Listeners

- **`useSigma(create, setupParams?)`**: Creates one sigma-state instance for a component and manages setup cleanup. Calls `create()` once per mounted instance. Reruns setup when params change.
- **`listen(target, name, listener)`**: Adds an event listener (for sigma-states or DOM targets) and returns a cleanup function.
- **`useListener(target, name, listener)`**: Attaches an event listener inside a component via `useEffect`. Handles unsubscribe automatically.
- **`isSigmaState(value)`**: Checks whether a value is a sigma-state instance.
