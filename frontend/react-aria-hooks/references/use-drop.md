# useDrop

Source: https://react-aria.adobe.com/useDrop

## Import

- Import: `import {useDrop} from 'react-aria/useDrop'`

## Signature

```ts
useDrop(options: DropOptions): DropResult
```

## Use For

Handles drop interactions for an element, with support for traditional mouse and touch based drag and drop, in addition to full parity for keyboard and screen reader users.

## Implementation Guidance

- Use for standalone drop targets; use collection drop hooks for list/table/grid collections.
- Validate accepted item kinds and render clear focused/hovered drop affordances.

## Upstream Sections To Recheck

- Introduction
- Example
- Drop data
- Drop operations
- Events
- Disabling dropping
