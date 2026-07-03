# useCheckbox

Source: https://react-aria.adobe.com/Checkbox/useCheckbox.html

## Import

- Package: `react-aria`
- Import: `import {useCheckbox} from 'react-aria'`
- Install: `yarn add react-aria`
- Source version: 3.50.0

## Signature

```ts
useCheckbox(props: AriaCheckboxProps, state: ToggleState, inputRef: RefObject<HTMLInputElement | null>): CheckboxAria
```

## Use For

Provides the behavior and accessibility implementation for a checkbox component. Checkboxes allow users to select multiple items from a list of individual items, or to mark one individual item as selected.

## Source Highlights

- Built with a native HTML `<input>` element, which can be optionally visually hidden to allow custom styling
- Full support for browser features like form autofill
- Keyboard focus management and cross browser normalization
- Labeling support for assistive technology
- Indeterminate state support

## Implementation Guidance

- Spread every returned `*Props` object onto the exact DOM slot it names; these props carry ARIA attributes, event handlers, ids, and keyboard behavior.
- Create the matching `react-stately` state object once in the owning component and pass that same state to related item, cell, or trigger hooks.
- Preserve user-provided labels and descriptions; icon-only controls still need `aria-label` or `aria-labelledby`.

## Upstream Sections To Recheck

- Features
- Anatomy
- Example
- Styling
- Styled examples
- Usage
