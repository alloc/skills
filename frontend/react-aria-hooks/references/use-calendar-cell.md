# useCalendarCell

Source: https://react-aria.adobe.com/Calendar/useCalendar.html

## Import

- Package: `react-aria`
- Import: `import {useCalendarCell} from 'react-aria'`
- Install: `yarn add react-aria`
- Source version: 3.50.0
- Documented on upstream page: `useCalendar`

## Signature

```ts
useCalendarCell(props: AriaCalendarCellProps, state: CalendarState<CalendarSelectionMode> | RangeCalendarState, ref: RefObject<HTMLElement | null>): CalendarCellAria
```

## Use For

Use `useCalendarCell` for the calendar cell part of the `useCalendar` pattern. The upstream page describes the broader pattern as: Provides the behavior and accessibility implementation for a calendar component. A calendar displays one or more date grids and allows users to select a single date.

## Source Highlights

- **Flexible** - Display one or more months at once, or a custom time range for use cases like a week view. Minimum and maximum values, unavailable dates, and non-contiguous selections are supported as well.
- **Customizable** - As with all of React Aria, the DOM structure and styling of all elements can be fully customized.

## Implementation Guidance

- Spread every returned `*Props` object onto the exact DOM slot it names; these props carry ARIA attributes, event handlers, ids, and keyboard behavior.
- Pass the ref for the rendered DOM element into the hook and attach that same ref to the element receiving the returned props.
- Create the matching `react-stately` state object once in the owning component and pass that same state to related item, cell, or trigger hooks.
- Preserve user-provided labels and descriptions; icon-only controls still need `aria-label` or `aria-labelledby`.
- Render item-level hooks inside the parent collection/control and pass the parent state or item data from the same render pass.

## Related Hooks From The Same Source Page

- [useCalendar](./use-calendar.md)
- [useCalendarGrid](./use-calendar-grid.md)

## Upstream Sections To Recheck

- Features
- Anatomy
- Date and time values
- Example
- Styled Examples
- Usage
- Advanced topics
