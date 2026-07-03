# useRangeCalendar

Source: https://react-aria.adobe.com/RangeCalendar/useRangeCalendar.html

## Import

- Package: `react-aria`
- Import: `import {useRangeCalendar} from 'react-aria'`
- Install: `yarn add react-aria`
- Source version: 3.50.0

## Signature

```ts
useRangeCalendar<T extends DateValue>(props: AriaRangeCalendarProps<T>, state: RangeCalendarState, ref: RefObject<FocusableElement | null>): CalendarAria
```

## Use For

Provides the behavior and accessibility implementation for a range calendar component. A range calendar displays one or more date grids and allows users to select a contiguous range of dates.

## Source Highlights

- **Flexible** - Display one or more months at once, or a custom time range for use cases like a week view. Minimum and maximum values, unavailable dates, and non-contiguous selections are supported as well.
- **Touch friendly** - Date ranges can be selected by dragging over dates in the calendar using a touch screen, and all interactions are accessible using touch-based screen readers.
- **Customizable** - As with all of React Aria, the DOM structure and styling of all elements can be fully customized.

## Implementation Guidance

- Spread every returned `*Props` object onto the exact DOM slot it names; these props carry ARIA attributes, event handlers, ids, and keyboard behavior.
- Pass the ref for the rendered DOM element into the hook and attach that same ref to the element receiving the returned props.
- Create the matching `react-stately` state object once in the owning component and pass that same state to related item, cell, or trigger hooks.
- Preserve user-provided labels and descriptions; icon-only controls still need `aria-label` or `aria-labelledby`.

## Related Hooks From The Same Source Page

- [useCalendarGrid](./use-calendar-grid.md)
- [useCalendarCell](./use-calendar-cell.md)

## Upstream Sections To Recheck

- Features
- Anatomy
- Date and time values
- Example
- Styled examples
- Usage
- Advanced topics
