# Strong mode

Strong mode is opt-in. A leading `"use strong"` directive before a module's imports, or `compiler: { strong: true }` in `octane.config.ts` for all application-owned modules, asserts immutable snapshots and pure rendering — enabling compiler checks and fully conditioned production memoization for user-authored render operations. Vite, Rspack, and Rsbuild also accept `strong: true` in their Octane plugin options. Installed dependencies keep their existing behavior unless their own source opts in.

## What strong modules reject

Statically provable patterns become compile errors:

| Diagnostic | Rejected pattern |
| --- | --- |
| `OCTANE_STRONG_RENDER_STATE_UPDATE` | Calling a `useState`/`useReducer`/`useLinkedState` updater during render |
| `OCTANE_STRONG_EFFECT_STATE_UPDATE` | Calling one of those updaters synchronously during effect setup |
| `OCTANE_STRONG_RENDER_REF_WRITE` | Writing `ref.current` during render |
| `OCTANE_STRONG_RENDER_EFFECT_EVENT_CALL` | Calling a known `useEffectEvent` result during render |
| `OCTANE_STRONG_EFFECT_EVENT_DEPENDENCY` | Including a known Effect Event in explicit hook dependencies |
| `OCTANE_STRONG_RENDER_SNAPSHOT_MUTATION` | Mutating a provable state snapshot during render |
| `OCTANE_STRONG_RETAINED_ROW_MUTATION` | Mutating a binding declared outside a retained keyed `@for` row from that row. Fresh setup-local and row-local scratch data stay valid |
| `OCTANE_STRONG_RENDER_IMPURE_CALL` | Reading a known clock or random source during render |
| `OCTANE_STRONG_HOOK_LOCALITY` | Declaring a built-in hook value or its dependent effect outside the sole nested `@{…}` block that uses it |
| `OCTANE_STRONG_EVENT_HANDLER_LOCALITY` | Declaring a named native event handler outside the sole deeper nested `@{…}` block containing its direct `onX` use |

## The contract

`"use strong"` asserts that rendering is referentially transparent: the same witnessed inputs produce the same output with no application-visible side effects. Production client builds apply that assertion to all user-authored render operations — local, imported, member, computed, and call-produced callees; callback-bearing calls; construction; and tagged templates.

- A `use*` name is not a purity oracle and does not reintroduce Rules of Hooks. Actual hooks belong in component or custom-hook setup, where compiler-assigned slots allow conditional hooks.
- Checks follow provable synchronous calls through local helpers, `useCallback`/`useEffectEvent` results, and functions returned by analyzable `useMemo` factories. These hooks remain supported — creating a callback is not itself an error.
- Effect Events are non-reactive: omit them from dependencies. Other explicit dependency arrays remain authoritative and are never rewritten.
- Built-ins are recognized by import provenance, including optional calls; same-module custom hooks and function-valued bindings resolve by lexical binding to a transitive fixed point, preserving context, state, suspension, and effect lifecycles through aliases and cycles.
- Memo guards witness the callable, its receiver, and explicit arguments; component and list projection inputs compare with `Object.is` (distinguishing signed zero, stabilizing `NaN`).

## What stays valid

- `useCallback`, `useMemo`, `useEffectEvent`, and effects that synchronize external systems.
- Updating state in event handlers; `useLinkedState` for editable state that should follow a changing input.
- Genuinely deferred callbacks, effect cleanup, and normal DOM or timer refs — when they run outside rendering.

## Analysis bounds

The analysis is deliberately bounded. Unknown factory returns and complex control flow stay opaque, and unknown calls are assumed pure instead of disabling Strong memoization. Dependency checks follow literal arrays — an aliased or externally produced array is not assumed unchanged.

A call that hides ref contents, a state getter, mutable module/global data, a live external store, a clock, randomness, mutation, or another changing source violates the Strong contract. Keep live accessors in compatibility mode, or pass an actual snapshot into a separate Strong component.

Do not rely on render-operation counts: production, development, HMR, profiling, server rendering, hydration, retries, and aborted work can evaluate different amounts of code.
