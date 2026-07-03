# useModalOverlay

Source: https://react-aria.adobe.com/Modal/useModalOverlay.html

## Import

- Package: `react-aria`
- Import: `import {useModalOverlay} from 'react-aria'`
- Install: `yarn add react-aria`
- Source version: 3.50.0

## Signature

```ts
useModalOverlay(props: AriaModalOverlayProps, state: OverlayTriggerState, ref: RefObject<HTMLElement | null>): ModalOverlayAria
```

## Use For

Provides the behavior and accessibility implementation for a modal component. A modal is an overlay element which blocks interaction with elements outside it.

## Source Highlights

- **Accessible** - Content outside the modal is hidden from assistive technologies while it is open. The modal optionally closes when interacting outside, or pressing the Escape key.
- **Focus management** - Focus is moved into the modal on mount, and restored to the trigger element on unmount. While open, focus is contained within the modal, preventing the user from tabbing outside.
- **Scroll locking** - Scrolling the page behind the modal is prevented while it is open, including in mobile browsers.

## Implementation Guidance

- Spread every returned `*Props` object onto the exact DOM slot it names; these props carry ARIA attributes, event handlers, ids, and keyboard behavior.
- Pass the ref for the rendered DOM element into the hook and attach that same ref to the element receiving the returned props.
- Create the matching `react-stately` state object once in the owning component and pass that same state to related item, cell, or trigger hooks.
- Preserve user-provided labels and descriptions; icon-only controls still need `aria-label` or `aria-labelledby`.
- Keep trigger, overlay, and dismissal props together so focus restoration, escape handling, and outside interaction semantics stay intact.

## Upstream Sections To Recheck

- Features
- Anatomy
- Example
- Usage
