# useDateFieldState

Source: https://react-aria.adobe.com/DateField/useDateFieldState.html

## Import

- Package: `react-stately`
- Import: `import {useDateFieldState} from 'react-stately'`
- Install: `yarn add react-stately`
- Source version: 3.48.0

## Signature

```ts
useDateFieldState<T extends DateValue = DateValue>(props: DateFieldStateOptions<T>): DateFieldState
```

## Use For

Provides state management for a date field component. A date field allows users to enter and edit date and time values using a keyboard. Each part of a date value is displayed in an individually editable segment.

## Implementation Guidance

- Use this hook as the state owner for the matching React Aria behavior hook rather than recreating selection, open state, validation, or collection logic by hand.
- Keep keys stable across renders for collection items, especially when data can be inserted, removed, sorted, filtered, or loaded asynchronously.
- Use the hook result as the single source of truth for related child hooks and rendered collection items.
- Use `@internationalized/date` values and preserve locale, calendar, time zone, min/max, disabled, and unavailable-date constraints.

## Upstream Sections To Recheck

- Interface
- Example
