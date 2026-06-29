---
name: react
description: Build and review client-only React 19 code that treats components as pure UI projections, uses TanStack Query for server state, and avoids effect-driven orchestration and speculative optimization.
---

# React

React components should be boring: they project state into UI.

```tsx
UI = f(state)
```

This skill assumes a client-only React 19 app with React Compiler and TanStack Query. Do not suggest SSR, React Server Components, Server Actions, React DOM static prerender APIs, hydration-specific patterns, or promise-based component data fetching.

## Core Contract

- Feature components render UI, derive display values, and call event handlers. Data flow, request lifecycles, subscriptions, browser integration, and cross-component coordination belong in TanStack Query, owner components, adapter hooks, or reusable infrastructure.
- Feature/application components must not call effect-family hooks: `useEffect`, `useLayoutEffect`, or `useInsertionEffect`.
- Store only source-of-truth UI state. Derive filtered, sorted, grouped, selected, counted, labeled, permissioned, and boolean values during render.
- Do not mirror query data into component state unless creating explicit draft or optimistic state with separate ownership.
- User-caused behavior belongs in the handler for the action that caused it.
- Do not create state whose only purpose is to trigger later behavior.
- Reset component state with ownership boundaries and `key`, not synchronization logic.
- Use refs for imperative DOM access. If lifecycle is tied to a specific DOM node, use a callback ref with cleanup instead of an effect.
- Use `lazy()` at feature boundaries, not component boundaries. It is for loading less JavaScript, not making renders faster.
- `useMemo` and `useCallback` are banned unless they satisfy a documented third-party identity contract, fix a confirmed correctness bug, or address a measured performance regression. The adjacent comment must name the concrete reason.

## Ownership Model

When an effect seems necessary, choose the matching owner instead.

| Need | Owner |
| --- | --- |
| Compute a value | Render derivation |
| Respond to a user action | Event handler |
| Read server state | TanStack Query `useQuery` |
| Write server state | TanStack Query `useMutation` from a handler |
| Reset local state | Component `key` |
| Keep duplicated values aligned | One source of truth |
| Subscribe to or listen to external systems | Adapter hook |
| Run lifecycle tied to a DOM node | Callback ref with cleanup |
| Integrate browser APIs or third-party widgets | Adapter hook |
| Set simple document title or metadata | Render `<title>`, `<meta>`, or `<link>` |
| Defer code the user may never need this session | `lazy()` plus a coherent `<Suspense>` boundary |

If no row fits, question the component boundary before adding an escape hatch.

## React 19 Defaults

- For new function components, accept `ref` as a normal prop. Do not introduce `forwardRef` in new code; leave existing `forwardRef` code alone unless already touching it.
- Callback refs may return cleanup. Use that for DOM-node attach/detach work, and avoid implicit-return ref callbacks because accidental return values are meaningful.
- Render simple document metadata where it is known instead of mutating `document` from effects. Use the app's metadata library for complex route-level precedence.
- Prefer `<Context value={value}>` over `<Context.Provider value={value}>` in new code.
- Read context with `use(Context)` only when a conditional context read is genuinely useful. Do not use `use` for data fetching or promises in this codebase.
- Use `preload`, `preinit`, `preconnect`, and `prefetchDNS` from `react-dom` only for concrete resources or origins with known benefit. Do not scatter speculative resource hints.

## Server State

TanStack Query owns server state. Components consume query results and invoke mutations; they do not implement request lifecycles.

- Query keys must encode every value that changes the read.
- Use `enabled` or conditional query inputs for conditional reads, not state flags and effects.
- Put server writes in event handlers using `useMutation`.
- Put invalidation, cache writes, optimistic server updates, and rollback in mutation callbacks or shared mutation helpers.
- Use React Actions, `useActionState`, and function-valued form `action` props only for local UI workflows that do not need query invalidation, cache writes, or shared server-state consistency.
- Use `useOptimistic` only for local, temporary UI optimism. Optimism for shared server state belongs in TanStack Query.

## Strategic Code Splitting

Use `lazy()` to defer expensive feature code where the user may never visit that UI in the current session. Good boundaries include routes, large modals, drawers, wizards, admin panels, dashboards, charts, maps, editors, previews, PDF viewers, media tools, 3D/canvas experiences, rarely used settings panels, authenticated-only features, and feature-flagged surfaces.

Do not lazy-load buttons, form fields, icons, tiny presentational components, initial shell layout, always-visible content, or components whose fallback would be more disruptive than the chunk savings.

Declare lazy components at module scope. Render them under a `<Suspense>` boundary whose fallback matches the product loading sequence; avoid scattered spinners around small children.

`lazy()` loads code. TanStack Query loads server state. Keep `useQuery` and `useMutation` inside the lazy feature as usual; do not use Suspense as a reason to bypass Query.

For high-value lazy features, preload code and data when the user shows intent, such as hover, focus, or navigation. Do that in event handlers, not effects, and pair code preloading with `queryClient.prefetchQuery` when useful.

## Adapter Hooks

Wrap external stores, event sources, browser APIs, and third-party widgets once, then expose a domain-level hook to components. Adapter hooks may use effect-family hooks only to synchronize with non-React systems. They must expose a declarative API and must not become feature-specific orchestration buckets.

## Responsiveness

Use `useDeferredValue`, including its `initialValue` form, for render responsiveness. Do not use it as a data-fetching debounce. For remote search, use TanStack Query query keys, `enabled`, and app-approved debounce utilities.

## Review Gate

Reject new code that introduces:

- Effect-family hooks in feature/application components.
- Component-level manual fetching or request lifecycle state.
- Derived or duplicated state, including query data mirrored into local state without explicit draft or optimistic ownership.
- Effect-driven state machines or state flags that exist only to trigger behavior.
- New `forwardRef` wrappers instead of `ref` props.
- Implicit-return callback refs such as `ref={(node) => (instance = node)}`.
- Effects that mutate `document.title` or simple metadata.
- `lazy()` for tiny, initial, always-visible, or purely presentational components.
- Lazy components declared inside another component.
- Fragmented Suspense boundaries that do not match a coherent product loading sequence.
- `useMemo` or `useCallback` without an adjacent comment documenting an identity contract, correctness bug, or measured regression.
- React Actions, `useActionState`, or form Actions for server-state writes that need Query cache consistency.
- `use` for data fetching or promises.
- External subscriptions, event listeners, or browser integration implemented directly in feature components.
- SSR, RSC, Server Actions, React DOM static prerender APIs, hydration-specific code, or other server-rendering guidance.
