# useCalendar

Source: https://react-aria.adobe.com/Calendar/useCalendar.html

## Import

- Package: `react-aria`
- Import: `import {useCalendar} from 'react-aria'`
- Install: `yarn add react-aria`
- Source version: 3.50.0

## Signature

```ts
useCalendar<T extends DateValue, M extends CalendarSelectionMode = 'single'>(props: AriaCalendarProps<T, M>, state: CalendarState<M>): CalendarAria
```

## Use For

Provides the behavior and accessibility implementation for a calendar component. A calendar displays one or more date grids and allows users to select a single date.

## Source Highlights

- **Flexible** - Display one or more months at once, or a custom time range for use cases like a week view. Minimum and maximum values, unavailable dates, and non-contiguous selections are supported as well.
- **International** - Support for 13 calendar systems used around the world, including Gregorian, Buddhist, Islamic, Persian, and more. Locale-specific formatting, number systems, and right-to-left support are available as well.
- **Accessible** - Calendar cells can be navigated and selected using the keyboard, and localized screen reader messages are included to announce when the selection and visible date range change.
- **Customizable** - As with all of React Aria, the DOM structure and styling of all elements can be fully customized.

## Implementation Guidance

- Spread every returned `*Props` object onto the exact DOM slot it names; these props carry ARIA attributes, event handlers, ids, and keyboard behavior.
- Create the matching `react-stately` state object once in the owning component and pass that same state to related item, cell, or trigger hooks.
- Preserve user-provided labels and descriptions; icon-only controls still need `aria-label` or `aria-labelledby`.
- Use `@internationalized/date` values and preserve locale, calendar, time zone, min/max, disabled, and unavailable-date constraints.

## Related Hooks From The Same Source Page

- [useCalendarGrid](./use-calendar-grid.md)
- [useCalendarCell](./use-calendar-cell.md)

## Upstream Sections To Recheck

- Features
- Anatomy
- Date and time values
- Example
- Styled Examples
- Usage
- Advanced topics
