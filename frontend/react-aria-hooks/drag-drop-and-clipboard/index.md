# Drag, Drop, and Clipboard

Read when: building keyboard-accessible drag/drop, collection drag/drop, drop indicators, or copy/paste behavior for focusable custom elements.

Avoid when: Avoid these hooks when browser-native text selection, simple file inputs, or non-interactive data movement already satisfy the workflow.

| API | Consider when |
| --- | --- |
| [useClipboard](./use-clipboard.md) | Handles clipboard interactions for a focusable element. |
| [useDrag](./use-drag.md) | Handles drag interactions for an element, with support for traditional mouse and touch based drag and drop, in addition to full parity for keyboard and screen reader users. |
| [useDraggableCollectionState](./use-draggable-collection-state.md) | Manages state for a draggable collection. |
| [useDraggableCollection](./use-draggable-collection.md) | Handles drag interactions for a collection component, with support for traditional mouse and touch based drag and drop, in addition to full parity for keyboard and screen reader users. |
| [useDraggableItem](./use-draggable-item.md) | Use `useDraggableItem` for the draggable item part of the `useDraggableCollection` pattern. |
| [useDropIndicator](./use-drop-indicator.md) | Use `useDropIndicator` for the drop indicator part of the `useDroppableCollection` pattern. |
| [useDrop](./use-drop.md) | Handles drop interactions for an element, with support for traditional mouse and touch based drag and drop, in addition to full parity for keyboard and screen reader users. |
| [useDroppableCollectionState](./use-droppable-collection-state.md) | Manages state for a droppable collection. |
| [useDroppableCollection](./use-droppable-collection.md) | Handles drop interactions for a collection component, with support for traditional mouse and touch based drag and drop, in addition to full parity for keyboard and screen reader users. |
| [useDroppableItem](./use-droppable-item.md) | Use `useDroppableItem` for the droppable item part of the `useDroppableCollection` pattern. |
