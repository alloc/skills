# useDraggableItem

Source: https://react-aria.adobe.com/useDraggableCollection.html

## Import

- Package: `react-aria`
- Import: `import {useDraggableItem} from 'react-aria'`
- Install: `yarn add react-aria`
- Source version: 3.50.0
- Documented on upstream page: `useDraggableCollection`

## Signature

```ts
useDraggableItem(props: DraggableItemProps, state: DraggableCollectionState): DraggableItemResult
```

## Use For

Use `useDraggableItem` for the draggable item part of the `useDraggableCollection` pattern. The upstream page describes the broader pattern as: Handles drag interactions for a collection component, with support for traditional mouse and touch based drag and drop, in addition to full parity for keyboard and screen reader users.

## Implementation Guidance

- Spread every returned `*Props` object onto the exact DOM slot it names; these props carry ARIA attributes, event handlers, ids, and keyboard behavior.
- Create the matching `react-stately` state object once in the owning component and pass that same state to related item, cell, or trigger hooks.
- Preserve user-provided labels and descriptions; icon-only controls still need `aria-label` or `aria-labelledby`.
- Render item-level hooks inside the parent collection/control and pass the parent state or item data from the same render pass.

## Related Hooks From The Same Source Page

- [useDraggableCollectionState](./use-draggable-collection-state.md)
- [useDraggableCollection](./use-draggable-collection.md)

## Upstream Sections To Recheck

- Introduction
- Example
- Drag data
- Drag previews
- Drop operations
- Reordering
- Props
