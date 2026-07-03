# useProgressBar

Source: https://react-aria.adobe.com/ProgressBar/useProgressBar.html

## Import

- Package: `react-aria`
- Import: `import {useProgressBar} from 'react-aria'`
- Install: `yarn add react-aria`
- Source version: 3.50.0

## Signature

```ts
useProgressBar(props: AriaProgressBarProps): ProgressBarAria
```

## Use For

Provides the accessibility implementation for a progress bar component. Progress bars show either determinate or indeterminate progress of an operation over time.

## Source Highlights

- Exposed to assistive technology as a progress bar via ARIA
- Labeling support for accessibility
- Internationalized number formatting as a percentage or value
- Determinate and indeterminate progress support

## Implementation Guidance

- Spread every returned `*Props` object onto the exact DOM slot it names; these props carry ARIA attributes, event handlers, ids, and keyboard behavior.
- Preserve user-provided labels and descriptions; icon-only controls still need `aria-label` or `aria-labelledby`.

## Upstream Sections To Recheck

- Features
- Anatomy
- Example
- Circular example
- Usage
- Internationalization
