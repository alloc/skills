# useColorSlider

Source: https://react-aria.adobe.com/ColorSlider/useColorSlider.html

## Import

- Package: `react-aria`
- Import: `import {useColorSlider} from 'react-aria'`
- Install: `yarn add react-aria`
- Source version: 3.50.0

## Signature

```ts
useColorSlider(props: AriaColorSliderOptions, state: ColorSliderState): ColorSliderAria
```

## Use For

Provides the behavior and accessibility implementation for a color slider component. Color sliders allow users to adjust an individual channel of a color value.

## Source Highlights

- Support for adjusting a single channel of RGBA, HSLA, and HSBA colors
- Support for mouse, touch, and keyboard via the [useMove](https://react-aria.adobe.com/useMove) hook
- Multi-touch support for dragging multiple sliders at once
- Pressing on the track moves the thumb to that position
- Supports using the arrow keys, as well as page up/down, home, and end keys
- Support for both horizontal and vertical orientations
- Support for disabling the color slider
- Prevents text selection while dragging

## Implementation Guidance

- Spread every returned `*Props` object onto the exact DOM slot it names; these props carry ARIA attributes, event handlers, ids, and keyboard behavior.
- Create the matching `react-stately` state object once in the owning component and pass that same state to related item, cell, or trigger hooks.
- Preserve user-provided labels and descriptions; icon-only controls still need `aria-label` or `aria-labelledby`.

## Upstream Sections To Recheck

- Features
- Anatomy
- Example
- Usage
