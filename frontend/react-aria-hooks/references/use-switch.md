# useSwitch

Source: https://react-aria.adobe.com/Switch/useSwitch.html

## Import

- Package: `react-aria`
- Import: `import {useSwitch} from 'react-aria'`
- Install: `yarn add react-aria`
- Source version: 3.50.0

## Signature

```ts
useSwitch(props: AriaSwitchProps, state: ToggleState, ref: RefObject<HTMLInputElement | null>): SwitchAria
```

## Use For

Provides the behavior and accessibility implementation for a switch component. A switch is similar to a checkbox, but represents on/off values as opposed to selection.

## Source Highlights

- Built with a native HTML `<input>` element, which can be optionally visually hidden to allow custom styling
- Full support for browser features like form autofill
- Keyboard focus management and cross browser normalization
- Labeling support for screen readers
- Exposed as a switch to assistive technology via ARIA

## Implementation Guidance

- Spread every returned `*Props` object onto the exact DOM slot it names; these props carry ARIA attributes, event handlers, ids, and keyboard behavior.
- Pass the ref for the rendered DOM element into the hook and attach that same ref to the element receiving the returned props.
- Create the matching `react-stately` state object once in the owning component and pass that same state to related item, cell, or trigger hooks.
- Preserve user-provided labels and descriptions; icon-only controls still need `aria-label` or `aria-labelledby`.

## Upstream Sections To Recheck

- Features
- Anatomy
- Example
- Usage
- Internationalization
