---
name: react
description: Build and review client-only React code with pure component projection, TanStack Query for server state, no application `useEffect`, and React Compiler-aware avoidance of `useMemo` and `useCallback`.
---

# react

React components should be boring: a component projects state into UI.

```tsx
UI = f(state)
```

Do not use React components to orchestrate data flow, synchronize unrelated state, manage request lifecycles, or imperatively coordinate the application. Put those responsibilities in event handlers, TanStack Query, adapter hooks, reusable infrastructure, or the owner of the state.

This guidance assumes a client-only React application:

- No SSR.
- No React Server Components.
- No hydration-sensitive rendering.
- Do not suggest SSR-specific patterns.

## Hard Rules

- Never call `useEffect` in application code.
- Never fetch from a component with `fetch`, Axios, or a hand-rolled request lifecycle.
- Never store derived state.
- Never duplicate state that can be derived from existing values.
- Never use state variables whose only purpose is to trigger later behavior.
- Never add `useMemo` unless it fixes a confirmed correctness bug and has a comment explaining that bug.
- Never add `useCallback` unless it fixes a confirmed correctness bug and has a comment explaining that bug.
- Never pass `getServerSnapshot` to `useSyncExternalStore`; this app is client-only.

## Effect Replacements

When you think you need an effect, classify the actual problem first:

| Problem | Use instead |
| --- | --- |
| Compute a value | Derive it during render |
| React to a click, submit, drag, confirmation, selection, or typing | Event handler |
| Fetch data | TanStack Query `useQuery` |
| Submit or write data | TanStack Query `useMutation` |
| Reset state | React `key` |
| Synchronize duplicated state | Remove the duplication |
| Subscribe to external state | `useSyncExternalStore` |
| Access the DOM | `useRef` or a callback ref |
| Integrate browser APIs | Adapter hook |

If none of these categories fit, question the design before adding an escape hatch.

## Derive During Render

If a value can be computed from current props, state, or query data, compute it while rendering.

Bad:

```tsx
const [fullName, setFullName] = useState("");

useEffect(() => {
  setFullName(`${first} ${last}`);
}, [first, last]);
```

Good:

```tsx
const fullName = `${first} ${last}`;
```

Derive filtered lists, sorted lists, grouped data, selected objects, booleans, labels, permissions, counts, and totals.

```tsx
const visibleTodos = todos.filter((todo) => !todo.completed);

const selectedUser = users.find((user) => user.id === selectedUserId);

const hasErrors = errors.length > 0;

const itemCount = items.length;
```

State is only for source-of-truth values that cannot be derived, such as text input, selected ids, dialog visibility, optimistic edits, and drag state.

## Put User Actions In Handlers

If behavior happens because the user clicked, typed, submitted, dragged, confirmed, or selected something, run the logic in that handler.

Bad:

```tsx
const [shouldSave, setShouldSave] = useState(false);

useEffect(() => {
  if (shouldSave) {
    saveDraft();
  }
}, [shouldSave]);
```

Good:

```tsx
async function handleSave() {
  await saveDraft();
}
```

Do not build effect-driven state machines.

## Use TanStack Query For Server State

Components consume server state. TanStack Query owns server state.

Never manually manage loading, error, retry, cancellation, deduplication, cache invalidation, or refetching from a component.

Bad:

```tsx
useEffect(() => {
  fetch(url).then(handleResponse);
}, [url]);
```

Good:

```tsx
const user = useQuery({
  queryKey: ["user", id],
  queryFn: () => getUser(id),
});
```

Network writes belong in event handlers using mutations.

```tsx
const queryClient = useQueryClient();

const mutation = useMutation({
  mutationFn: updateUser,
  onSuccess() {
    queryClient.invalidateQueries({
      queryKey: ["user", id],
    });
  },
});

function handleSubmit(values: FormValues) {
  mutation.mutate(values);
}
```

## Reset With Keys

Do not synchronize reset behavior with effects.

Bad:

```tsx
useEffect(() => {
  setComment("");
}, [postId]);
```

Good:

```tsx
<CommentEditor key={postId} postId={postId} />
```

## Use Refs For DOM Work

Use refs for imperative DOM work.

```tsx
const inputRef = useRef<HTMLInputElement>(null);

function focusInput() {
  inputRef.current?.focus();
}
```

For setup that occurs when a node appears or disappears, use a callback ref.

```tsx
function inputRef(node: HTMLInputElement | null) {
  if (node) {
    node.focus();
  }
}

return <input ref={inputRef} />;
```

Do not introduce `useCallback` for callback refs unless a confirmed correctness bug requires stable identity.

## Use External Store Subscriptions

Never subscribe inside an effect.

Bad:

```tsx
useEffect(() => {
  return store.subscribe(handleChange);
}, []);
```

Good:

```tsx
const value = useSyncExternalStore(store.subscribe, store.getSnapshot);
```

Wrap browser APIs once in adapter hooks. Components should consume the adapter hook, not implement subscriptions themselves.

```tsx
function subscribe(callback: () => void) {
  window.addEventListener("online", callback);
  window.addEventListener("offline", callback);

  return () => {
    window.removeEventListener("online", callback);
    window.removeEventListener("offline", callback);
  };
}

function getSnapshot() {
  return navigator.onLine;
}

export function useOnlineStatus() {
  return useSyncExternalStore(subscribe, getSnapshot);
}
```

## Avoid Manual Memoization

React Compiler is enabled. Do not stabilize references or memoize values speculatively.

Bad:

```tsx
const filtered = useMemo(() => items.filter((item) => item.visible), [items]);
```

Good:

```tsx
const filtered = items.filter((item) => item.visible);
```

Manual memoization is allowed only when it fixes a confirmed correctness bug. Every `useMemo` must include a comment explaining the bug.

```tsx
// Required: AG Grid treats a new columns array as a schema reset.
// Without this memoization, edited cells are discarded.
const columns = useMemo(() => buildColumns(schema), [schema]);
```

The same rule applies to `useCallback`.

Bad:

```tsx
const handleClick = useCallback(() => {
  onSelect(id);
}, [id, onSelect]);
```

Good:

```tsx
function handleClick() {
  onSelect(id);
}
```

Stable callback identity is not a goal. Measure first, fix real bugs, and trust React Compiler.

## Hide React Complexity Behind Adapter Hooks

Some APIs genuinely require React hooks or lifecycle-style integration:

- `useSyncExternalStore`
- ResizeObserver
- IntersectionObserver
- Media queries
- BroadcastChannel
- WebSocket
- Browser events

Wrap them once in infrastructure hooks.

```tsx
const online = useOnlineStatus();
const size = useElementSize(ref);
const visible = useIntersection(ref);
```

Infrastructure hooks may use React escape hatches internally when no better API exists. Feature components should not.

## Prefer Ownership Over Synchronization

If two pieces of state need to stay synchronized, they are probably the same piece of state. Remove duplicated state, lift ownership, pass callbacks, or use composition so one owner controls the value.

## Escape Hatch Checklist

Before adding `useEffect`, `useMemo`, or `useCallback`, ask:

1. Can I derive this during render?
2. Can this happen inside an event handler?
3. Should this be a TanStack Query?
4. Should this be a mutation?
5. Should this be a ref?
6. Should this be a `key`?
7. Should this be `useSyncExternalStore`?
8. Should this be an adapter hook?

If any answer is yes, do that instead.

## Code Review Checklist

Reject new application code that contains:

- `useEffect(...)`.
- `useMemo(...)` without a comment documenting the confirmed bug it fixes.
- `useCallback(...)` without a comment documenting the confirmed bug it fixes.
- Manual fetches from components.
- Duplicated state.
- Effects that synchronize state.
- Effects that respond to user actions.
- SSR-specific React patterns.

Prefer React code shaped like this:

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

The ideal React component is a pure projection from state to UI. Everything else belongs in event handlers, TanStack Query, adapter hooks, or reusable infrastructure.
