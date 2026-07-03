# useMeter

Source: https://react-aria.adobe.com/Meter/useMeter.html

## Import

- Package: `react-aria`
- Import: `import {useMeter} from 'react-aria'`
- Install: `yarn add react-aria`
- Source version: 3.50.0

## Signature

```ts
useMeter(props: AriaMeterProps): MeterAria
```

## Use For

Provides the accessibility implementation for a meter component. Meters represent a quantity within a known range, or a fractional value.

## Source Highlights

- Exposed to assistive technology as a `meter` via ARIA, with fallback to `progressbar` where unsupported
- Labeling support for accessibility
- Internationalized number formatting as a percentage or value

## Implementation Guidance

- Spread every returned `*Props` object onto the exact DOM slot it names; these props carry ARIA attributes, event handlers, ids, and keyboard behavior.
- Preserve user-provided labels and descriptions; icon-only controls still need `aria-label` or `aria-labelledby`.

## Upstream Sections To Recheck

- Features
- Anatomy
- Example
- Styled examples
- Usage
- Internationalization
