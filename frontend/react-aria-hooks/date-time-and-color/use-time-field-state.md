# useTimeFieldState

Source: https://react-aria.adobe.com/TimeField/useTimeFieldState.html

## Import

- Package: `react-stately`
- Import: `import {useTimeFieldState} from 'react-stately'`
- Install: `yarn add react-stately`
- Source version: 3.48.0

## Signature

```ts
useTimeFieldState<T extends TimeValue = TimeValue>(props: TimeFieldStateOptions<T>): TimeFieldState
```

## Use For

Provides state management for a time field component. A time field allows users to enter and edit time values using a keyboard. Each part of a time value is displayed in an individually editable segment.

## Implementation Guidance

- Use this hook as the state owner for the matching React Aria behavior hook rather than recreating selection, open state, validation, or collection logic by hand.
- Keep keys stable across renders for collection items, especially when data can be inserted, removed, sorted, filtered, or loaded asynchronously.
- Use the hook result as the single source of truth for related child hooks and rendered collection items.

## Upstream Sections To Recheck

- Interface
- Example
