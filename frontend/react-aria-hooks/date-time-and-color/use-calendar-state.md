# useCalendarState

Source: https://react-aria.adobe.com/Calendar/useCalendarState.html

## Import

- Package: `react-stately`
- Import: `import {useCalendarState} from 'react-stately'`
- Install: `yarn add react-stately`
- Source version: 3.48.0

## Signature

```ts
useCalendarState<T extends DateValue = DateValue, M extends CalendarSelectionMode = 'single'>(props: CalendarStateOptions<T, M>): CalendarState<M>
```

## Use For

Provides state management for a calendar component. A calendar displays one or more date grids and allows users to select a single date.

## Implementation Guidance

- Use this hook as the state owner for the matching React Aria behavior hook rather than recreating selection, open state, validation, or collection logic by hand.
- Keep keys stable across renders for collection items, especially when data can be inserted, removed, sorted, filtered, or loaded asynchronously.
- Use the hook result as the single source of truth for related child hooks and rendered collection items.

## Upstream Sections To Recheck

- Interface
- Example
