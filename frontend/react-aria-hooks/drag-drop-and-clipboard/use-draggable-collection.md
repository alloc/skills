# useDraggableCollection

Source: https://react-aria.adobe.com/useDraggableCollection.html

## Import

- Package: `react-aria`
- Import: `import {useDraggableCollection} from 'react-aria'`
- Install: `yarn add react-aria`
- Source version: 3.50.0

## Signature

```ts
useDraggableCollection(props: DraggableCollectionOptions, state: DraggableCollectionState, ref: RefObject<HTMLElement | null>): void
```

## Use For

Handles drag interactions for a collection component, with support for traditional mouse and touch based drag and drop, in addition to full parity for keyboard and screen reader users.

## Implementation Guidance

- Spread every returned `*Props` object onto the exact DOM slot it names; these props carry ARIA attributes, event handlers, ids, and keyboard behavior.
- Pass the ref for the rendered DOM element into the hook and attach that same ref to the element receiving the returned props.
- Create the matching `react-stately` state object once in the owning component and pass that same state to related item, cell, or trigger hooks.
- Preserve user-provided labels and descriptions; icon-only controls still need `aria-label` or `aria-labelledby`.

## Related Hooks From The Same Source Page

- [useDraggableCollectionState](./use-draggable-collection-state.md)
- [useDraggableItem](./use-draggable-item.md)

## Upstream Sections To Recheck

- Introduction
- Example
- Drag data
- Drag previews
- Drop operations
- Reordering
- Props
