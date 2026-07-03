# useTimeField

Source: https://react-aria.adobe.com/TimeField/useTimeField.html

## Import

- Package: `react-aria`
- Import: `import {useTimeField} from 'react-aria'`
- Install: `yarn add react-aria`
- Source version: 3.50.0

## Signature

```ts
useTimeField<T extends TimeValue>(props: AriaTimeFieldOptions<T>, state: TimeFieldState, ref: RefObject<Element | null>): DateFieldAria
```

## Use For

Provides the behavior and accessibility implementation for a time field component. A time field allows users to enter and edit time values using a keyboard. Each part of a time value is displayed in an individually editable segment.

## Source Highlights

- **International** - Support for locale-specific formatting, number systems, hour cycles, and right-to-left layout.
- **Time zone aware** - Times can optionally include a time zone. All modifications follow time zone rules such as daylight saving time.
- **Accessible** - Each time unit is displayed as an individually focusable and editable segment, which allows users an easy way to edit times using the keyboard, in any format and locale.
- **Touch friendly** - Time segments are editable using an easy to use numeric keypad, and all interactions are accessible using touch-based screen readers.
- **Customizable** - As with all of React Aria, the DOM structure and styling of all elements can be fully customized.

## Implementation Guidance

- Spread every returned `*Props` object onto the exact DOM slot it names; these props carry ARIA attributes, event handlers, ids, and keyboard behavior.
- Pass the ref for the rendered DOM element into the hook and attach that same ref to the element receiving the returned props.
- Create the matching `react-stately` state object once in the owning component and pass that same state to related item, cell, or trigger hooks.
- Preserve user-provided labels and descriptions; icon-only controls still need `aria-label` or `aria-labelledby`.
- Use `@internationalized/date` values and preserve locale, calendar, time zone, min/max, disabled, and unavailable-date constraints.

## Related Hooks From The Same Source Page

- [useDateSegment](./use-date-segment.md)

## Upstream Sections To Recheck

- Features
- Anatomy
- Time values
- Example
- Styled examples
- Usage
