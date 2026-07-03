# useDateField

Source: https://react-aria.adobe.com/DateField/useDateField.html

## Import

- Package: `react-aria`
- Import: `import {useDateField} from 'react-aria'`
- Install: `yarn add react-aria`
- Source version: 3.50.0

## Signature

```ts
useDateField<T extends DateValue>(props: AriaDateFieldOptions<T>, state: DateFieldState, ref: RefObject<Element | null>): DateFieldAria
```

## Use For

Provides the behavior and accessibility implementation for a date field component. A date field allows users to enter and edit date and time values using a keyboard. Each part of a date value is displayed in an individually editable segment.

## Source Highlights

- **Dates and times** - Support for dates and times with configurable granularity.
- **Time zone aware** - Dates and times can optionally include a time zone. All modifications follow time zone rules such as daylight saving time.
- **Accessible** - Each date and time unit is displayed as an individually focusable and editable segment, which allows users an easy way to edit dates using the keyboard in supported date formats.
- **Touch friendly** - Date segments are editable using an easy to use numeric keypad, and all interactions are accessible using touch-based screen readers.
- **Customizable** - As with all of React Aria, the DOM structure and styling of all elements can be fully customized.

## Implementation Guidance

- Spread every returned `*Props` object onto the exact DOM slot it names; these props carry ARIA attributes, event handlers, ids, and keyboard behavior.
- Pass the ref for the rendered DOM element into the hook and attach that same ref to the element receiving the returned props.
- Create the matching `react-stately` state object once in the owning component and pass that same state to related item, cell, or trigger hooks.
- Preserve user-provided labels and descriptions; icon-only controls still need `aria-label` or `aria-labelledby`.

## Related Hooks From The Same Source Page

- [useDateSegment](./use-date-segment.md)

## Upstream Sections To Recheck

- Features
- Anatomy
- Date and time values
- Example
- Styled examples
- Usage
- Advanced topics
