# React interoperability

Contents: `ReactCompat` and `OctaneCompat` basics, compiler ownership, boundaries and context, SSR, and limits.

Both adapters are named exports from `octane/react`. Each renderer owns its own subtree — neither API aliases React to Octane, and there are no atomic cross-root commits.

- `ReactCompat` hosts one real React component inside Octane. Install matching `react`/`react-dom` 19.2 or newer in the React 19 series. React owns the island's hooks, state, events, refs, and descendants — including support for React class components, which native Octane lacks.
- `OctaneCompat` hosts one compiled Octane component inside React 19: `<OctaneCompat><NativePanel /></OctaneCompat>`. The child stays an Octane component with native events and Octane hooks.

## `ReactCompat` usage

Prefer the child form:

```tsrx
// App.tsrx — compiled by Octane.
import { ReactCompat } from 'octane/react';
import { Counter } from './Counter.react';

export function App() @{
	<ReactCompat><Counter start={3} /></ReactCompat>
}
```

```tsx
/** @jsxImportSource react */
// Counter.react.tsx — compiled by React's JSX transform.
import { useState } from 'react';

export function Counter({ start }: { start: number }) {
	const [count, setCount] = useState(start);
	return <button onClick={() => setCount(count + 1)}>{count}</button>;
}
```

- `<ReactCompat component={Counter} props={{ start: 3 }} />` is the alternate form — do not combine it with an element child.
- One function, class, `memo`, `lazy`, or `forwardRef` component is accepted. Put fragments, DOM elements, arrays, or multiple roots inside a React component. React children passed through props must be React renderables, not Octane template blocks.
- `ReactCompat` creates one React root inside a `div` — place it only where a div is valid.
- Prop updates preserve React state and nodes; changing the child key/type replaces the component; changing the outer boundary key replaces the whole root. Prefer one useful React subtree over a boundary for every small widget.

## Compiler ownership in mixed builds

Use both compilers with `requireDirective: true` on the Octane integration:

- `.tsrx` belongs to Octane — no marker needed.
- Octane-owned `.tsx` and native hook/context helper modules open with `/** @jsxImportSource octane */`.
- React-owned `.tsx` keeps React's JSX transform and `/** @jsxImportSource react */`.
- Do not alias React or React DOM to Octane.

## Context bridging

- **Octane → React:** define `themeBridge = bridgeReactContext(OctaneTheme, ReactTheme)` once, then pass `contexts={[themeBridge]}` to `ReactCompat`. React descendants read `ReactTheme` with `use`/`useContext`. Keep source/target identities and their order stable, or replace the boundary key.
- **React → Octane:** inside `OctaneCompat`, Octane's `use`/`useContext` reads a real React context directly — no reverse mapping needed.

## Scheduling and errors

- React work starts or updates after the Octane host commits. Octane `flushSync()` does not flush the separate React root, and an Octane transition is not a transaction shared with React. React-local transitions keep React's behavior.
- Authored React Suspense and error boundaries handle their own descendants first; escaped suspension and render/effect errors reach the nearest Octane pending/catch boundary. Event-handler errors follow React's normal reporting.
- During projected pending work, new parent props/context snapshots publish on reveal; delete the boundary or change its outer key to replace a pending island.

## SSR

- Both server implementations use `octane/react/server`; Octane's server compiler retargets `octane/react` automatically. React-owned server entries that bypass that compiler must select the server entry explicitly.
- `ReactCompat` needs an owned Octane asynchronous or streaming render request to produce complete React server HTML. It buffers each complete React island up to 8 MiB and hydrates it with React `hydrateRoot`. A surrounding Octane stream may send its fallback while waiting; React's own progressive reveal scripts are not streamed separately. A synchronous Octane render can emit an outer fallback but cannot await the island.
- The request owns cancellation, abort, timeout, and cleanup. Nested React→OctaneCompat→ReactCompat server rendering is unsupported; client nesting works in both directions.

## Limits

These adapters coordinate separate renderer commits. They do not provide atomic cross-root commits or universal compatibility with every React integration. For a React library without a native port, prefer `ReactCompat` over rewriting — see [bindings.md](./bindings.md) for native `@octanejs/*` equivalents.
