---
name: octane
description: Build, edit, migrate, or debug Octane apps — the compiled React-model UI framework (successor to Inferno). Covers .tsrx/.tsx components, compiler-inferred dependency arrays, conditional hooks, native DOM events (onInput, not synthetic onChange), scoped style blocks, signals (octane/signals), SSR and deferred hydration, React interoperability (ReactCompat/OctaneCompat), strong mode, Vite/Rspack/Rsbuild setup, the octane CLI, and @octanejs/* bindings for React libraries.
---

# Octane

Octane is a JavaScript UI framework with React's programming model — same hooks, `memo`, context, portals, Suspense, transitions, actions — compiled ahead of time to template clones and direct DOM writes. No virtual DOM, no diffing, no rules of hooks. It is beta software; APIs can still change.

## Import map

| Import | Provides |
| --- | --- |
| `octane` | Runtime: hooks, `Hydrate`, `createResizeObserver`, `attachBehaviorRoot`, transitions, `use()` |
| `octane/signals` | `signal$`, `derived$`, `query$`, `skip`, `optimistic$`, `action$`, scopes |
| `octane/signals/client` | `useSignal$` for component-owned state |
| `octane/react` | `ReactCompat`, `OctaneCompat`, `bridgeReactContext` |
| `octane/behavior` | `attachBehaviorRoot` without the renderer |
| `octane/hydration` | Hydration strategies: `load`, `idle`, `visible`, `media`, `interaction`, `condition`, `never` |

## Facts that bite

Apply these on every Octane edit before reaching for a reference file.

- **No synthetic `onChange`.** Events are native and delegated. Text inputs use `onInput` per edit; native `change` fires on commit (usually blur). Direct `onChange` on a text `<input>`/`<textarea>` triggers the `OCTANE_NATIVE_TEXT_ONCHANGE` warning — keep it only for deliberate commit-on-blur and add `suppressNativeChangeWarning`; never add a noop `onInput`. Controlled `value`/`checked` follow React semantics; `defaultValue`/`defaultChecked` are uncontrolled.
- **No rules of hooks.** Hooks work behind conditions and after early returns (compiler-assigned call-site slots). A hook inside a plain JS loop is a compile error — use keyed `@for` or a child component. `use()` and `useContext` are exempt.
- **Dependency arrays are optional and inferred.** Omit them on `useEffect`/`useLayoutEffect`/`useInsertionEffect`/`useMemo`/`useCallback`/`useImperativeHandle` and the compiler derives them from the closure. Explicit arrays keep React semantics; `null` means every render/recompute. Imported or non-transparent custom hooks need an explicit list.
- **`ref` is a prop.** `ref={cb}`, `ref={obj}`, or multi-ref `ref={[a, b]}`. There is no `forwardRef`.
- **`useState`/`useReducer` return a third member:** `[state, update, getState]` — a stable getter for the latest scheduled state. Use it instead of syncing a ref for stale-closure reads.
- **`class`/`className` compose clsx-style:** strings, numbers, arrays, objects, nesting; falsy values drop out.
- **Components are just functions** used at `<F/>` sites. They return JSX, a primitive (coerced to text), `null`, or an array. No class components, no Server Components, no StrictMode double-invoke.
- **Checkbox/radio activation is native** `click` → `input` → non-cancelable `change`. `preventDefault()` in `onChange` cannot undo activation; cancel in `onClick` when rollback is intended.
- **`use()` in render is supported and idiomatic.** Creating promises during render is fine — the compiler memoizes each creation feeding a `use()`, keyed on its inputs. Do not hoist fetches into effects or add React's `cache()`.
- **Module ownership is per-compiler.** `.tsrx` is always Octane's. In mixed toolchains, Octane `.tsx`/`.ts`/`.js` needs a leading `/** @jsxImportSource octane */` pragma and `requireDirective: true` on the integration; React files keep `/** @jsxImportSource react */`.

## Authoring cheat sheet (`.tsrx`)

```tsrx
export function Counter() @{
	const [count, setCount, getCount] = useState(0);
	<button onClick={() => setCount((c) => c + 1)}>{count as string}</button>
}
```

- `@{ … }` desugars to `return <jsx>` — setup and output sit together; the block ends with exactly one output node. Blocks producing no JSX yield `null`; a top-level early `return` may return JSX or `null`.
- Dynamic text needs `{expr as string}` unless the expression is provably a string.
- `{foo}` in attribute position means `foo={foo}`; dynamic tag names use `<{expr}>…</{expr}>`.
- Template control flow: `@if (c) {} @else if {} @else {}`, `@for (const x of xs; index i; key x.id) {} @empty {}`, `@switch (v) { @case 'a': {} @default: {} }`, `@try {} @pending {} @catch (error, reset) {}`. Plain JS control flow stays in setup.

## Start here

- Read [references/setup-and-tooling.md](./references/setup-and-tooling.md) before scaffolding (`npm create octane`), wiring Vite/Rspack/Rsbuild, running the `octane` CLI (`doctor`, `analyze`, `init`, `add`, `explain`), profiling, publishing libraries, or checking browser support.
- Read [references/authoring.md](./references/authoring.md) before writing or editing components: `.tsrx` vs `.tsx` choice, `@{ … }` result rule, JSX conveniences, text holes, directive control flow, hook placement and dependency inference, state hooks, `useLinkedState`, `use()` data flow, and legacy `.tsrx` migration.
- Read [references/events-and-forms.md](./references/events-and-forms.md) before touching event handlers, controlled/uncontrolled inputs, checkbox/radio rollback, or observer callbacks (`createResizeObserver`).
- Read [references/styling.md](./references/styling.md) before adding `<style>` blocks, themes (`apply`, `$class` maps), or `:global()` selectors, or when hitting `STYLE_*`/`CSS_*` diagnostics.
- Read [references/signals.md](./references/signals.md) before using `signal$`/`derived$`/`query$`/`useSignal$`, explicit scopes, streams, optimistic actions, transitions over signals, or signal SSR/seeding.
- Read [references/ssr-and-hydration.md](./references/ssr-and-hydration.md) before working with `renderToPipeableStream`/`renderToReadableStream`, `<Hydrate>` strategies/prefetch/splitting, `attachBehaviorRoot`, or streamed signal bootstrap.
- Read [references/react-interop.md](./references/react-interop.md) before hosting React components in Octane (`ReactCompat`), Octane in React (`OctaneCompat`), bridging contexts, or configuring mixed-compiler projects.
- Read [references/strong-mode.md](./references/strong-mode.md) before enabling `"use strong"` or fixing `OCTANE_STRONG_*` diagnostics.
- Read [references/bindings.md](./references/bindings.md) when looking for a native Octane port of a React library (`@octanejs/*`) or checking porting/parity policy.

## Defaults

- Prefer `.tsrx` for collection-heavy or new UI; `.tsx`/`.jsx` also compile but `@for`'s keyed fast path is `.tsrx`-only.
- Prefer `useLinkedState` over effects or render-time setters when editable state should follow a changing source.
- Prefer `createResizeObserver` for resize callbacks that set state or write geometry.
- Prefer a matching `@octanejs/*` binding over porting; prefer `ReactCompat` over rewriting a working React component.
- Octane targets current evergreen browsers and publishes modern ESM; it does not polyfill DOM/JS APIs.
