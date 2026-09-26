# Authoring Octane components

Contents: choosing `.tsrx` vs `.tsx`, component shape, the `@{ … }` result rule, JSX conveniences, text holes, directive control flow, hook rules, dependency inference, state hooks, async data with `use()`, and legacy `.tsrx` syntax.

## `.tsrx` vs `.tsx`/`.jsx`

TSRX is TypeScript + JSX with opt-in `@` syntax for JSX-producing templates; existing TypeScript and JSX keep their meanings. Octane compiles both dialects — prefer `.tsrx` for new UI because it unlocks the compiler's best output:

- `@{ … }` function bodies and nested setup blocks
- Directive control flow (`@if`, `@for`, `@switch`, `@try`)
- `@for` compiles rendered lists to a keyed fast path (a compiled per-item body + the raw array) instead of allocating a descriptor per row — the main reason to prefer `.tsrx` for collection-heavy UI.
- Text holes and sibling-scoped `<style>` blocks (see [styling.md](./styling.md))

`.tsx`/`.jsx` keeps ordinary JSX returns and passes `<style>{css}</style>` through untouched (no scoping).

To render syntax markers as text, use JSX string expressions like `{'@if'}`.

## Components

A component is any function used at a `<F/>` site — not a special declaration. It renders whatever it returns: a JSX root, a primitive (coerced to text), `null`, or an array.

```tsrx
export function Greeting({ name }: { name: string }) @{
	<h1>Hello, {name as string}</h1>
}
```

Function declarations and arrow functions may use `@{ … }` bodies:

```tsrx
const Card = (props: CardProps) => @{
	<View {...props} />
}
```

A top-level early `return` exits the function and may return JSX, `null`, or a TSRX `@` block; otherwise the final JSX-producing statement supplies the output:

```tsrx
function Dashboard({ user }: { user: User | null }) @{
	if (!user) return <p>Please sign in.</p>;
	<h1>Welcome, {user.name as string}</h1>
}
```

## The `@{ … }` result rule

`@{ … }` creates a local scope whose final statement may produce JSX:

```tsrx
@{
	const value = compute();
	<View value={value} />
}
```

- Any TSRX block that produces no JSX output evaluates to `null` — `@{}` templates, control-flow branches, loop iterations, `@try`/`@pending`/`@catch` blocks, and TSRX function bodies. Useful for side-effect-only statements such as logging.
- Final JSX-producing forms: a JSX element, a fragment, `@if`, `@for`, `@switch`, or `@try`. Wrap final text or expression values in a fragment: `<>{label}</>`.
- `return` is available only in top-level TSRX function bodies. Other TSRX blocks yield their final JSX-producing statement.
- In JSX child position, mirror the formatter's shape: `<div>@{ … }</div>` inline.

Nested `@{ }` blocks also work in expression position — Octane gives the block a local lifetime for any hooks it declares (see Hooks below); a JSX-only nested block is transparent until it gets setup.

## JSX conveniences

- JS comments may appear directly in JSX: `// …` and `/* … */`.
- `{foo}` in attribute position means `foo={foo}`: `<Input {value} {onInput} />`.
- Dynamic tag names use expression tags: `<{props.as}>…</{props.as}>` or self-closing `<{props.icon} />`. Opening and closing expressions must match syntactically.

## Text holes

- `{expr as string}` is a dynamic text hole. The cast is required unless the expression is provably a string (string/template literal, `+`-concatenation involving a string, or a local tracked back to a string).
- A bare `{expr}` that is not provably a string is a renderable hole (element, component, array), not text.

## Template control flow

Directives replace JSX-era ternaries/`map` inside markup; plain JS control flow stays in setup. Each branch or iteration may run local JS statements before producing output.

### `@if` / `@else if` / `@else`

```tsrx
@if (status === 'loading') {
	const label = compute();
	<p>{label as string}</p>
} @else if (status === 'idle') {
	<p>Idle.</p>
} @else {
	<p>Ready.</p>
}
```

`@else` is optional in root and nested positions; if no branch matches the result is `null`.

### `@for` / `@empty`

```tsrx
@for (const item of items; index i; key item.id) {
	<Item item={item} index={i} />
} @empty {
	<Empty />
}
```

- The suffix after `;` may declare `index`, `key`, or `index` then `key`. The `index` variable is in scope for `key`. A `key` propagates to rendered elements, including through shorthand fragments. Octane compiles keyed `@for` to its fast path — always supply `key` for dynamic collections.
- `@empty` renders for empty iterables.
- `break` and `continue` are excluded from `@for` bodies — use keyed extraction or a child component for conditional item output.

### `@switch`

```tsrx
@switch (status) {
	@case 'warning':
	@case 'error': {
		<Alert />
	}
	@default: {
		<Info />
	}
}
```

`@case` and `@default` use a trailing `:`. Stacked `@case` labels share the next block (the replacement for fallthrough — `break` is omitted). `@default` is optional; if no branch matches the result is `null`.

### `@try` / `@pending` / `@catch`

```tsrx
@try {
	<Content />
} @pending {
	<Loading />
} @catch (error, reset) {
	<ErrorState error={error} onRetry={reset} />
}
```

`@try` protects the main render tree, `@pending` supplies async fallback UI, and `@catch` supplies error UI with `error` and an optional `reset` callback. Use empty `@pending {}` or `@catch (…) {}` blocks when there is no fallback UI — do not add an empty fragment to satisfy the block.

## Hooks

### No rules of hooks (Octane divergence)

Octane hooks are tracked by a compiler-assigned call-site slot, not call order — a hook may sit behind a condition or after an early return. Generic TSRX guidance restricts hooks to unconditional top-level statements because its other targets enforce rules of hooks; that restriction does not apply to Octane.

- A hook in a plain JS loop is a compile error — every iteration would share one slot. Loop with keyed `@for` or extract a child component. `use()` and `useContext` are exempt (not slot-keyed).
- Hooks/effects used only by conditional, keyed, switch, or try arms may stay in the parent scope to keep the parent's lifetime; moving a hook into a nested `@{…}` block gives it that block's local lifetime.

Standard hooks match React: `useState`, `useEffect`, `useLayoutEffect`, `useInsertionEffect`, `useMemo`, `useCallback`, `useRef`, `useId`, `useTransition`, `useDeferredValue`, `useImperativeHandle`, `useContext`, `use`, plus `memo`, context, portals, Suspense, transitions, and the actions API.

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

## Legacy `.tsrx` code

When maintaining files written for older TSRX dialects, migrate to the current forms:

| Legacy | Current |
| --- | --- |
| `component Name(props) { … }` | `function Name(props) @{ … }` |
| Statement-position JSX throughout | Standard JSX plus explicit `@` templates |
| Multiple top-level JSX statements | One final JSX-producing statement, usually a fragment |
| Local JS inside JSX children | `@{ … }` statement containers or `@` control blocks |
| Quoted text child `"Text"` | Standard JSX text |
| `<tsrx>…</tsrx>` / `<tsx>…</tsx>` islands | `@{ … }` or ordinary JSX/fragments |
| `if`/`for`/`switch`/`try` keywords in templates | `@if`/`@for`/`@switch`/`@try` directives |
| `switch` fallthrough with `break` | Stacked `@case` labels sharing a block |
| Guard fallback + bare `return;` | `return <Fallback />` or `return null` |
| `continue`/`break` in loop bodies | Removed from `@for` — extract or restructure |
| `{text expr}`, `{html expr}`, `{style "…"}` | Removed — use text holes and target APIs |
| `{ref expr}`, `inputRef={ref x}` | Removed — use `ref` props |
