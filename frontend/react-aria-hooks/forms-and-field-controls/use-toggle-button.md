# useToggleButton

Source: https://react-aria.adobe.com/ToggleButton/useToggleButton.html

## Import

- Package: `react-aria`
- Import: `import {useToggleButton} from 'react-aria'`
- Install: `yarn add react-aria`
- Source version: 3.50.0

## Signature

```ts
useToggleButton(props: AriaToggleButtonOptions<ElementType>, state: ToggleState, ref: RefObject<any>): ToggleButtonAria<HTMLAttributes<any>>
```

## Use For

Provides the behavior and accessibility implementation for a toggle button component. ToggleButtons allow users to toggle a selection on or off, for example switching between two states or modes.

## Source Highlights

- Native HTML `<button>`, `<a>`, and custom element type support
- Exposed as a toggle button via ARIA
- Mouse and touch event handling, and press state management
- Keyboard focus management and cross browser normalization
- Keyboard event support for Space and Enter keys

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
