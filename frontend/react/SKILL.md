---
name: react
description: Build and review client-only React code that treats components as pure UI projections, uses TanStack Query for server state, and avoids effect-driven orchestration and speculative memoization.
---

# React

React components should be boring: they project state into UI.

```tsx
UI = f(state)
```

Feature components render, derive display values, and call event handlers. Data flow, subscriptions, request lifecycles, browser integration, and cross-component coordination belong in TanStack Query, owner components, adapter hooks, or reusable infrastructure.

This skill assumes a client-only React app. Do not suggest SSR, React Server Components, hydration-sensitive patterns, or `getServerSnapshot`.

## Core Rules

- Feature/application components must not call `useEffect`.
- Components must not hand-roll fetching, caching, retry, cancellation, refetching, or invalidation behavior.
- Store only source-of-truth UI state. Derive filtered, sorted, grouped, selected, counted, labeled, permissioned, and boolean values during render.
- User-caused behavior belongs in the event handler for the click, submit, drag, confirmation, selection, or input change that caused it.
- Do not create state whose only purpose is to trigger later behavior.
- Reset component state with ownership boundaries and `key`, not synchronization logic.
- Use refs or callback refs for imperative DOM access.
- External subscriptions must use `useSyncExternalStore` behind an adapter hook.
- Browser APIs that need setup or teardown belong in reusable adapter hooks. Feature components consume the hook.
- `useMemo` and `useCallback` are banned unless they fix a confirmed correctness bug and the adjacent comment names that bug. React Compiler is enabled; stable identity and speculative performance are not goals.

## Effect Alternatives

When an effect seems necessary, choose the matching ownership model instead.

| Need | Owner |
| --- | --- |
| Compute a value | Render derivation |
| Respond to a user action | Event handler |
| Read server state | TanStack Query `useQuery` |
| Write server state | TanStack Query `useMutation` from a handler |
| Reset local state | Component `key` |
| Keep duplicated values aligned | One source of truth |
| Subscribe to external state | Adapter hook using `useSyncExternalStore` |
| Imperatively touch the DOM | Ref or callback ref |
| Integrate browser APIs | Adapter hook |

If no row fits, question the component boundary before adding an escape hatch.

## State Standard

State is for values that cannot be derived from current props, existing state, or query results, such as text input, selected ids, dialog visibility, optimistic edits, and drag state.

Derived values stay in render:

```tsx
const visibleTodos = todos.filter((todo) => !todo.completed);
const selectedUser = users.find((user) => user.id === selectedUserId);
const itemCount = items.length;
```

If two values must be synchronized, remove the duplication, lift ownership, or pass callbacks so there is one owner.

## Server State Standard

TanStack Query owns server state. Components consume query results and invoke mutations; they do not implement request lifecycles.

Use `useQuery` for reads and `useMutation` for writes. Put network writes in event handlers, and put cache invalidation in mutation callbacks or shared mutation helpers.

```tsx
const user = useQuery({
  queryKey: ["user", id],
  queryFn: () => getUser(id),
});

const mutation = useMutation({
  mutationFn: updateUser,
  onSuccess() {
    queryClient.invalidateQueries({ queryKey: ["user", id] });
  },
});

function handleSubmit(values: FormValues) {
  mutation.mutate(values);
}
```

Do not use component state to trigger fetches, saves, invalidation, or refetching.

## Adapter Hooks

Wrap unavoidable React or browser integration once, then expose a domain-level hook to components.

Good component APIs:

```tsx
const online = useOnlineStatus();
const size = useElementSize(ref);
const visible = useIntersection(ref);
```

Adapter hooks may use the minimal React escape hatch internally when render derivation, handlers, refs, TanStack Query, `key`, or `useSyncExternalStore` cannot express the integration cleanly. Keep that complexity out of feature components.

For external subscriptions:

- Use `useSyncExternalStore(subscribe, getSnapshot)`.
- Do not subscribe from an effect.
- Do not pass `getServerSnapshot`.

## Manual Memoization

React Compiler is enabled. Prefer ordinary values and functions:

```tsx
const filtered = items.filter((item) => item.visible);

function handleClick() {
  onSelect(id);
}
```

Manual `useMemo` or `useCallback` requires a confirmed correctness bug, not a performance guess. The required adjacent comment must state the concrete failure:

```tsx
// Required: AG Grid treats a new columns array as a schema reset.
// Without this memoization, edited cells are discarded.
const columns = useMemo(() => buildColumns(schema), [schema]);
```

No bug comment means no memoization hook.

## Review Gate

Reject new code that introduces:

- `useEffect` in feature/application components.
- Component-level manual fetching or request lifecycle state.
- Derived or duplicated state.
- Effect-driven state machines.
- State flags that exist only to trigger behavior.
- `useMemo` or `useCallback` without a confirmed-bug comment.
- External subscriptions implemented with effects.
- SSR, RSC, hydration-specific code, or `getServerSnapshot`.

Prefer components shaped like this:

```tsx
function UserRow({ user, selectedUserId, onSelect }: Props) {
  const isSelected = user.id === selectedUserId;

  function handleClick() {
    onSelect(user.id);
  }

  return (
    <button aria-pressed={isSelected} onClick={handleClick}>
      {user.name}
    </button>
  );
}
```
