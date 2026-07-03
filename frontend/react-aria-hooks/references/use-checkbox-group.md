# useCheckboxGroup

Source: https://react-aria.adobe.com/CheckboxGroup/useCheckboxGroup.html

## Import

- Package: `react-aria`
- Import: `import {useCheckboxGroup} from 'react-aria'`
- Install: `yarn add react-aria`
- Source version: 3.50.0

## Signature

```ts
useCheckboxGroup(props: AriaCheckboxGroupProps, state: CheckboxGroupState): CheckboxGroupAria
```

## Use For

Provides the behavior and accessibility implementation for a checkbox group component. Checkbox groups allow users to select multiple items from a list of options.

## Source Highlights

- Checkbox groups are exposed to assistive technology via ARIA
- Each checkbox is built with a native HTML `<input>` element, which can be optionally visually hidden to allow custom styling
- Full support for browser features like form autofill and validation
- Keyboard focus management and cross browser normalization
- Group and checkbox labeling support for assistive technology

## Implementation Guidance

- Spread every returned `*Props` object onto the exact DOM slot it names; these props carry ARIA attributes, event handlers, ids, and keyboard behavior.
- Create the matching `react-stately` state object once in the owning component and pass that same state to related item, cell, or trigger hooks.
- Preserve user-provided labels and descriptions; icon-only controls still need `aria-label` or `aria-labelledby`.

## Related Hooks From The Same Source Page

- [useCheckboxGroupItem](./use-checkbox-group-item.md)

## Upstream Sections To Recheck

- Features
- Anatomy
- Example
- Styling
- Styled examples
- Usage
