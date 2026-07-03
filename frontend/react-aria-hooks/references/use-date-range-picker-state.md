# useDateRangePickerState

Source: https://react-aria.adobe.com/DateRangePicker/useDateRangePickerState.html

## Import

- Package: `react-stately`
- Import: `import {useDateRangePickerState} from 'react-stately'`
- Install: `yarn add react-stately`
- Source version: 3.48.0

## Signature

```ts
useDateRangePickerState<T extends DateValue = DateValue>(props: DateRangePickerStateOptions<T>): DateRangePickerState
```

## Use For

Provides state management for a date range picker component. A date range picker combines two DateFields and a RangeCalendar popover to allow users to enter or select a date and time range.

## Implementation Guidance

- Use this hook as the state owner for the matching React Aria behavior hook rather than recreating selection, open state, validation, or collection logic by hand.
- Keep keys stable across renders for collection items, especially when data can be inserted, removed, sorted, filtered, or loaded asynchronously.
- Use the hook result as the single source of truth for related child hooks and rendered collection items.

## Upstream Sections To Recheck

- Interface
- Example
