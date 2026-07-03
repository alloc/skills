# useNumberField

Source: https://react-aria.adobe.com/NumberField/useNumberField.html

## Import

- Package: `react-aria`
- Import: `import {useNumberField} from 'react-aria'`
- Install: `yarn add react-aria`
- Source version: 3.50.0

## Signature

```ts
useNumberField(props: AriaNumberFieldProps, state: NumberFieldState, inputRef: RefObject<HTMLInputElement | null>): NumberFieldAria
```

## Use For

Provides the behavior and accessibility implementation for a number field component. Number fields allow users to enter a number, and increment or decrement the value using stepper buttons.

## Source Highlights

- Support for internationalized number formatting and parsing including decimals, percentages, currency values, and units
- Support for the Latin, Arabic, and Han positional decimal numbering systems in [over 30 locales](https://react-aria.adobe.com/quality#supported-locales)
- Automatically detects the numbering system used and supports parsing numbers not in the default numbering system for the locale
- Support for multiple currency formats including symbol, code, and name in standard or accounting notation
- Validates keyboard entry as the user types so that only valid numeric input according to the locale and numbering system is accepted
- Handles composed input from input method editors, e.g. Pinyin
- Automatically selects an appropriate software keyboard for mobile according to the current platform and allowed values
- Supports rounding to a configurable number of fraction digits

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
