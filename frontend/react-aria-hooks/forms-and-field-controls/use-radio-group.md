# useRadioGroup

Source: https://react-aria.adobe.com/RadioGroup/useRadioGroup.html

## Import

- Package: `react-aria`
- Import: `import {useRadioGroup} from 'react-aria'`
- Install: `yarn add react-aria`
- Source version: 3.50.0

## Signature

```ts
useRadioGroup(props: AriaRadioGroupProps, state: RadioGroupState): RadioGroupAria
```

## Use For

Provides the behavior and accessibility implementation for a radio group component. Radio groups allow users to select a single item from a list of mutually exclusive options.

## Source Highlights

- Radio groups are exposed to assistive technology via ARIA
- Each radio is built with a native HTML `<input>` element, which can be optionally visually hidden to allow custom styling
- Full support for browser features like form autofill and validation
- Keyboard focus management and cross browser normalization
- Group and radio labeling support for assistive technology

## Implementation Guidance

- Spread every returned `*Props` object onto the exact DOM slot it names; these props carry ARIA attributes, event handlers, ids, and keyboard behavior.
- Create the matching `react-stately` state object once in the owning component and pass that same state to related item, cell, or trigger hooks.
- Preserve user-provided labels and descriptions; icon-only controls still need `aria-label` or `aria-labelledby`.
- Render item-level hooks inside the parent collection/control and pass the parent state or item data from the same render pass.

## Related Hooks From The Same Source Page

- [useRadio](./use-radio.md)

## Upstream Sections To Recheck

- Features
- Anatomy
- Example
- Styling
- Styled examples
- Usage
