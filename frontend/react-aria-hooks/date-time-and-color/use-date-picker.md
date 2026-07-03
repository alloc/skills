# useDatePicker

Source: https://react-aria.adobe.com/DatePicker/useDatePicker.html

## Import

- Package: `react-aria`
- Import: `import {useDatePicker} from 'react-aria'`
- Install: `yarn add react-aria`
- Source version: 3.50.0

## Signature

```ts
useDatePicker<T extends DateValue>(props: AriaDatePickerProps<T>, state: DatePickerState, ref: RefObject<Element | null>): DatePickerAria
```

## Use For

Provides the behavior and accessibility implementation for a date picker component. A date picker combines a DateField and a Calendar popover to allow users to enter or select a date and time value.

## Source Highlights

- **Dates and times** - Support for dates and times with configurable granularity.
- **Time zone aware** - Dates and times can optionally include a time zone. All modifications follow time zone rules such as daylight saving time.
- **Accessible** - Each date and time unit is displayed as an individually focusable and editable segment, which allows users an easy way to edit dates using the keyboard in supported date formats. Users can also open a calendar popover to select dates in a standard month grid. React Aria includes internal screen reader announcements for when the selection and visible date range change.
- **Touch friendly** - Date segments are editable using an easy to use numeric keypad, and all interactions are accessible using touch-based screen readers.
- **Customizable** - As with all of React Aria, the DOM structure and styling of all elements can be fully customized.

## Implementation Guidance

- Spread every returned `*Props` object onto the exact DOM slot it names; these props carry ARIA attributes, event handlers, ids, and keyboard behavior.
- Pass the ref for the rendered DOM element into the hook and attach that same ref to the element receiving the returned props.
- Create the matching `react-stately` state object once in the owning component and pass that same state to related item, cell, or trigger hooks.
- Preserve user-provided labels and descriptions; icon-only controls still need `aria-label` or `aria-labelledby`.

## Upstream Sections To Recheck

- Features
- Anatomy
- Date and time values
- Example
- Styled examples
- Usage
