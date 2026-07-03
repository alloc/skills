# Decision and Composition

Read when: deciding whether React Aria is justified, or when composing returned props, refs, ids, hidden content, or low-level utility behavior.

Avoid when: Avoid React Aria when native HTML or existing app components already cover the behavior without custom ARIA, focus, keyboard, collection, overlay, form, or cross-input logic.

| API | Consider when |
| --- | --- |
| [mergeProps](./merge-props.md) | Use when combining React Aria props with app props so event handlers, ids, class names, and refs compose instead of replacing each other. |
| [useId](./use-id.md) | Use `useId` to create a stable id for ARIA relationships when callers have not provided one. |
| [useObjectRef](./use-object-ref.md) | Offers an object ref for a given callback ref or an object ref. |
