# useButton

Source: https://react-aria.adobe.com/Button/useButton.html

## Import

- Package: `react-aria`
- Import: `import {useButton} from 'react-aria'`
- Install: `yarn add react-aria`
- Source version: 3.50.0

## Signature

```ts
useButton(props: AriaButtonOptions<ElementType>, ref: RefObject<any>): ButtonAria<HTMLAttributes<any>>
```

## Use For

Provides the behavior and accessibility implementation for a button component. Handles mouse, keyboard, and touch interactions, focus behavior, and ARIA props for both native button elements and custom element types.

## Source Highlights

- Native HTML `<button>` support
- `<a>` and custom element type support via ARIA
- Mouse and touch event handling, and press state management
- Keyboard focus management and cross browser normalization
- Keyboard event support for Space and Enter keys

## Implementation Guidance

- Spread every returned `*Props` object onto the exact DOM slot it names; these props carry ARIA attributes, event handlers, ids, and keyboard behavior.
- Pass the ref for the rendered DOM element into the hook and attach that same ref to the element receiving the returned props.
- Preserve user-provided labels and descriptions; icon-only controls still need `aria-label` or `aria-labelledby`.

## Upstream Sections To Recheck

- Features
- Anatomy
- Example
- Custom element type
- Usage
