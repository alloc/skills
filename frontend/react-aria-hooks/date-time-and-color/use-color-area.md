# useColorArea

Source: https://react-aria.adobe.com/ColorArea/useColorArea.html

## Import

- Package: `react-aria`
- Import: `import {useColorArea} from 'react-aria'`
- Install: `yarn add react-aria`
- Source version: 3.50.0

## Signature

```ts
useColorArea(props: AriaColorAreaOptions, state: ColorAreaState): ColorAreaAria
```

## Use For

Provides the behavior and accessibility implementation for a color area component. Color area allows users to adjust two channels of an RGB, HSL or HSB color value against a two-dimensional gradient background.

## Source Highlights

- Support for adjusting two-channel values of an HSL, HSB or RGB color value
- Support for mouse, touch, and keyboard via the [useMove](https://react-aria.adobe.com/useMove) hook
- Multi-touch support
- Pressing on the color area background moves the thumb to that position
- Supports using the arrow keys, for changing value by step, as well as shift + arrow key, page up/down, home, and end keys, for changing the value by page step.
- Support for disabling the color area
- Prevents text selection while dragging
- Exposed to assistive technology as a `2D slider` element via ARIA

## Implementation Guidance

- Spread every returned `*Props` object onto the exact DOM slot it names; these props carry ARIA attributes, event handlers, ids, and keyboard behavior.
- Create the matching `react-stately` state object once in the owning component and pass that same state to related item, cell, or trigger hooks.
- Preserve user-provided labels and descriptions; icon-only controls still need `aria-label` or `aria-labelledby`.

## Upstream Sections To Recheck

- Features
- Anatomy
- Example
- Usage
