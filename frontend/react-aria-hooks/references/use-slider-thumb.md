# useSliderThumb

Source: https://react-aria.adobe.com/Slider/useSlider.html

## Import

- Package: `react-aria`
- Import: `import {useSliderThumb} from 'react-aria'`
- Install: `yarn add react-aria`
- Source version: 3.50.0
- Documented on upstream page: `useSlider`

## Signature

```ts
useSliderThumb(opts: AriaSliderThumbOptions, state: SliderState): SliderThumbAria
```

## Use For

Use `useSliderThumb` for the slider thumb part of the `useSlider` pattern. The upstream page describes the broader pattern as: Provides the behavior and accessibility implementation for a slider component representing one or more values.

## Source Highlights

- Support for one or multiple thumbs
- Support for mouse, touch, and keyboard via the [useMove](https://react-aria.adobe.com/useMove) hook
- Multi-touch support for dragging multiple thumbs or multiple sliders at once
- Pressing on the track moves the nearest thumb to that position
- Supports using the arrow keys, as well as page up/down, home, and end keys
- Support for both horizontal and vertical orientations
- Support for custom min, max, and step values with handling for rounding errors
- Support for disabling the whole slider or individual thumbs

## Implementation Guidance

- Spread every returned `*Props` object onto the exact DOM slot it names; these props carry ARIA attributes, event handlers, ids, and keyboard behavior.
- Create the matching `react-stately` state object once in the owning component and pass that same state to related item, cell, or trigger hooks.
- Preserve user-provided labels and descriptions; icon-only controls still need `aria-label` or `aria-labelledby`.
- Render item-level hooks inside the parent collection/control and pass the parent state or item data from the same render pass.

## Related Hooks From The Same Source Page

- [useSlider](./use-slider.md)

## Upstream Sections To Recheck

- Features
- Anatomy
- Examples
- Usage
- Internationalization
