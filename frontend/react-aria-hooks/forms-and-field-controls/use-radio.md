# useRadio

Source: https://react-aria.adobe.com/RadioGroup/useRadioGroup.html

## Import

- Package: `react-aria`
- Import: `import {useRadio} from 'react-aria'`
- Install: `yarn add react-aria`
- Source version: 3.50.0
- Documented on upstream page: `useRadioGroup`

## Signature

```ts
useRadio(props: AriaRadioProps, state: RadioGroupState, ref: RefObject<HTMLInputElement | null>): RadioAria
```

## Use For

Use `useRadio` for the radio part of the `useRadioGroup` pattern. The upstream page describes the broader pattern as: Provides the behavior and accessibility implementation for a radio group component. Radio groups allow users to select a single item from a list of mutually exclusive options.

## Source Highlights

- Radio groups are exposed to assistive technology via ARIA
- Each radio is built with a native HTML `<input>` element, which can be optionally visually hidden to allow custom styling
- Full support for browser features like form autofill and validation
- Keyboard focus management and cross browser normalization
- Group and radio labeling support for assistive technology

## Implementation Guidance

- Spread every returned `*Props` object onto the exact DOM slot it names; these props carry ARIA attributes, event handlers, ids, and keyboard behavior.
- Pass the ref for the rendered DOM element into the hook and attach that same ref to the element receiving the returned props.
- Create the matching `react-stately` state object once in the owning component and pass that same state to related item, cell, or trigger hooks.
- Preserve user-provided labels and descriptions; icon-only controls still need `aria-label` or `aria-labelledby`.
- Render item-level hooks inside the parent collection/control and pass the parent state or item data from the same render pass.

## Related Hooks From The Same Source Page

- [useRadioGroup](./use-radio-group.md)

## Upstream Sections To Recheck

- Features
- Anatomy
- Example
- Styling
- Styled examples
- Usage
