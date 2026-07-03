# useRangeCalendarState

Source: https://react-aria.adobe.com/RangeCalendar/useRangeCalendarState.html

## Import

- Package: `react-stately`
- Import: `import {useRangeCalendarState} from 'react-stately'`
- Install: `yarn add react-stately`
- Source version: 3.48.0

## Signature

```ts
useRangeCalendarState<T extends DateValue = DateValue>(props: RangeCalendarStateOptions<T>): RangeCalendarState<T>
```

## Use For

Provides state management for a range calendar component. A range calendar displays one or more date grids and allows users to select a contiguous range of dates.

## Implementation Guidance

- Use this hook as the state owner for the matching React Aria behavior hook rather than recreating selection, open state, validation, or collection logic by hand.
- Keep keys stable across renders for collection items, especially when data can be inserted, removed, sorted, filtered, or loaded asynchronously.
- Use the hook result as the single source of truth for related child hooks and rendered collection items.

## Upstream Sections To Recheck

- Interface
- Example
