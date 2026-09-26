# Authoring Octane components

Contents: choosing `.tsrx` vs `.tsx`, component shape, `@{ … }`, text holes, template control flow, hook rules, dependency inference, state hooks, and async data with `use()`.

## `.tsrx` vs `.tsx`/`.jsx`

Both dialects compile through the Octane compiler. Prefer `.tsrx` for new UI — it unlocks the compiler's best output:

- `@{ … }` function bodies
- Directive control flow (`@if`, `@for`, `@switch`, `@try`)
- `@for` compiles rendered lists to a keyed fast path (a compiled per-item body + the raw array) instead of allocating a descriptor per row — the main reason to prefer `.tsrx` for collection-heavy UI.
- Text holes, sibling-scoped `<style>` blocks (see [styling.md](./styling.md))

`.tsx`/`.jsx` keeps ordinary JSX returns and passes `<style>{css}</style>` through untouched (no scoping).

## Components

A component is any function used at a `<F/>` site — not a special declaration. It renders whatever it returns: a JSX root, a primitive (coerced to text), `null`, or an array.

```tsrx
export function Greeting({ name }: { name: string }) @{
	<h1>Hello, {name as string}</h1>
}
```

`@{ … }` desugars to `{ … return <jsx> }`: setup (hooks, locals) sits next to the output. The `@{ … }` scope ends with exactly one output node — a JSX element or fragment `<>…</>`. Multiple trailing outputs are a parser error.

## Text holes

- `{expr as string}` is a dynamic text hole. The cast is required unless the expression is provably a string (string/template literal, `+`-concatenation involving a string, or a local tracked back to a string).
- A bare `{expr}` that is not provably a string is a renderable hole (element, component, array), not text.

## Template control flow

Directives replace JSX-era ternaries/`map` inside markup; plain JS control flow stays in setup.

```tsrx
@if (status === 'loading') {
	<p>Loading…</p>
} @else {
	<p>{label as string}</p>
}

@for (const item of items; key item.id) {
	<li>{item.text as string}</li>
} @empty {
	<li>Nothing here.</li>
}

@switch (tab) {
	@case ('a') { <PanelA /> }
	@default { <PanelB /> }
}

@try {
	<Profile id={id} />
} @pending {
	<p>Loading profile…</p>
} @catch (error) {
	<p role="alert">{String(error)}</p>
}
```

Inside JSX children, `@{ const x = …; <markup/> }` opens a nested setup block beside its JSX. A JSX-only nested block is transparent until it gets setup; moving a hook into a nested block gives the hook that block's local lifetime. Hooks/effects used only by conditional, keyed, switch, or try arms may stay in the parent scope to keep the parent's lifetime.

## Hooks

### No rules of hooks

Hooks are tracked by a compiler-assigned call-site slot, not call order. A hook may sit behind a condition or after an early return. A hook in a plain JS loop is a compile error — every iteration would share one slot. Loop with keyed `@for` or extract a child component. `use()` and `useContext` are exempt (not slot-keyed).

Standard hooks match React: `useState`, `useEffect`, `useLayoutEffect`, `useInsertionEffect`, `useMemo`, `useCallback`, `useRef`, `useId`, `useTransition`, `useDeferredValue`, `useImperativeHandle`, `useContext`, `use`, `useSyncExternalStore`-era APIs, plus `memo`, context, portals, Suspense, transitions, and the actions API.

### Dependency inference

Omit the dependency argument and the compiler derives it from the closure:

- `useEffect`, `useLayoutEffect`, `useInsertionEffect` — infer from the setup closure.
- `useMemo`, `useCallback` — infer from the factory/callback closure.
- `useImperativeHandle` — infers from the handle factory (third argument); ref identity is still tracked separately.

Rules:

- Explicit arrays are authoritative and never rewritten: `[]` = mount/stable-only, `[a, b]` = exactly those values, `null` = every render/recompute.
- Locally declared custom hooks in full-compiled `.tsrx`/`.tsx` modules qualify when they transparently forward a callback and final dependency parameter to an inferable hook. Plain `.ts`/`.js`, imported/method, or transforming wrappers need an explicit list — compile shared custom hooks through Octane too.
- The analysis understands lexical captures and proven-stable setters, dispatchers, refs, and state getters. Effect Events are omitted because they are non-reactive despite fresh wrapper identity.
- In production compiles, eligible `useMemo`/`useCallback` declarations become inline caches — no per-render closure or deps-array allocation, identical semantics.

## State hooks

- `useState(initial)` → `[state, setState, getState]`. `setState` accepts a value or functional update; `getState()` is a stable getter reading the latest scheduled hook-cell value without rendering. The compiler emits it only when tuple index 2 is observed — ordinary two-item destructuring allocates no getter.
- `useReducer(reducer, initialArg, init?)` → `[state, dispatch, getState]`; same third-member rule.
- `useLinkedState(source, calculate, options?)` → `[value, setValue, getValue]`. Keeps a value editable while its source stays the same, then resets/adjusts immediately when the source changes — no effect or render-time setter. `calculate(source, previous)` gets `undefined` on first render, then the previous `{ source, value }`. `sourceEqual`/`valueEqual` default to `Object.is` via `options`.

Reach for `getState()` in delayed, async, or long-lived callbacks instead of syncing a ref. During pending work a state getter can be newer than the committed DOM; it is not a subscription mechanism.

## Async data with `use()`

Creating promises during render is the supported pattern — the compiler memoizes every creation feeding a `use()`, keyed on its inputs:

```tsrx
function Avatar({ id }: { id: number }) @{
	const user = use(fetchUser(id));
	<img src={user.avatarUrl} alt={user.name} />
}
```

- Local promise chains are included: `const p = fetchUser(id); const t = p.then((u) => u.thumbnail()); use(t)` fetches once, survives re-renders and suspense replays, refetches exactly when `id` changes.
- Independent `use()` reads start in parallel and suspend once per stratum; true data dependencies stay sequential. Descendant fetch trees prefetch (`__warm`) while an ancestor suspends.
- Do not hoist fetches into effects/state or add React's `cache()` to avoid re-creation. Do not restructure into manual promise hoisting to "fix" waterfalls — the compiler already eliminates the avoidable ones.

## Refs and classes

- `ref` is a prop (React-19 style): `ref={callback}`, `ref={refObject}`, or `ref={[a, b]}` for multi-ref. No `forwardRef`.
- `class`/`className` accept clsx-style values: strings, numbers, arrays, objects, arbitrary nesting; falsy values drop out.
