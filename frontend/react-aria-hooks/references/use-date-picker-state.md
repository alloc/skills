# useDatePickerState

Source: https://react-aria.adobe.com/DatePicker/useDatePickerState.html

## Import

- Package: `react-stately`
- Import: `import {useDatePickerState} from 'react-stately'`
- Install: `yarn add react-stately`
- Source version: 3.48.0

## Signature

```ts
useDatePickerState<T extends DateValue = DateValue>(props: DatePickerStateOptions<T>): DatePickerState
```

## Use For

Provides state management for a date picker component. A date picker combines a DateField and a Calendar popover to allow users to enter or select a date and time value.

## Implementation Guidance

- Use this hook as the state owner for the matching React Aria behavior hook rather than recreating selection, open state, validation, or collection logic by hand.
- Keep keys stable across renders for collection items, especially when data can be inserted, removed, sorted, filtered, or loaded asynchronously.
- Use the hook result as the single source of truth for related child hooks and rendered collection items.
- Use `@internationalized/date` values and preserve locale, calendar, time zone, min/max, disabled, and unavailable-date constraints.

## Upstream Sections To Recheck

- Interface
- Example
