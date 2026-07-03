# useDrag

Source: https://react-aria.adobe.com/useDrag

## Import

- Import: `import {useDrag} from 'react-aria/useDrag'`

## Signature

```ts
useDrag(options: DragOptions): DragResult
```

## Use For

Handles drag interactions for an element, with support for traditional mouse and touch based drag and drop, in addition to full parity for keyboard and screen reader users.

## Implementation Guidance

- Use for standalone draggable elements; use collection drag hooks for list/table/grid collections.
- Provide keyboard-accessible alternatives where drag is not the only way to complete the task.

## Upstream Sections To Recheck

- Introduction
- Example
- Drag data
- Drag previews
- Drop operations
- Drag button
- Disabling dragging
