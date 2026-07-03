# useColorWheel

Source: https://react-aria.adobe.com/ColorWheel/useColorWheel.html

## Import

- Package: `react-aria`
- Import: `import {useColorWheel} from 'react-aria'`
- Install: `yarn add react-aria`
- Source version: 3.50.0

## Signature

```ts
useColorWheel(props: AriaColorWheelOptions, state: ColorWheelState, inputRef: RefObject<HTMLInputElement | null>): ColorWheelAria
```

## Use For

Provides the behavior and accessibility implementation for a color wheel component. Color wheels allow users to adjust the hue of an HSL or HSB color value on a circular track.

## Source Highlights

- Support for adjusting the hue of an HSL or HSB color value
- Support for mouse, touch, and keyboard via the [useMove](https://react-aria.adobe.com/useMove) hook
- Multi-touch support
- Pressing on the track moves the thumb to that position
- Supports using the arrow keys, as well as page up/down, home, and end keys
- Support for disabling the color wheel
- Prevents text selection while dragging
- Exposed to assistive technology as a `slider` element via ARIA

## Implementation Guidance

- Spread every returned `*Props` object onto the exact DOM slot it names; these props carry ARIA attributes, event handlers, ids, and keyboard behavior.
- Create the matching `react-stately` state object once in the owning component and pass that same state to related item, cell, or trigger hooks.
- Preserve user-provided labels and descriptions; icon-only controls still need `aria-label` or `aria-labelledby`.

## Upstream Sections To Recheck

- Features
- Anatomy
- Example
- Usage
- Internationalization
