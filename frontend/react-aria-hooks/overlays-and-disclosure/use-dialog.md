# useDialog

Source: https://react-aria.adobe.com/Modal/useDialog.html

## Import

- Package: `react-aria`
- Import: `import {useDialog} from 'react-aria'`
- Install: `yarn add react-aria`
- Source version: 3.50.0

## Signature

```ts
useDialog(props: AriaDialogProps, ref: RefObject<FocusableElement | null>): DialogAria
```

## Use For

Provides the behavior and accessibility implementation for a dialog component. A dialog is an overlay shown above other content in an application.

## Source Highlights

- **Flexible** - Dialogs can be used within a [modal](https://react-aria.adobe.com/Modal/useModalOverlay.html) or [popover](https://react-aria.adobe.com/Popover/usePopover.html) to create many types of overlay elements.
- **Accessible** - Exposed to assistive technology as a `dialog` or `alertdialog` with ARIA. The dialog is labeled by its title element, and content outside the dialog is hidden from assistive technologies while it is open.
- **Focus management** - Focus is moved into the dialog on mount, and restored to the trigger element on unmount. While open, focus is contained within the dialog, preventing the user from tabbing outside.

## Implementation Guidance

- Spread every returned `*Props` object onto the exact DOM slot it names; these props carry ARIA attributes, event handlers, ids, and keyboard behavior.
- Pass the ref for the rendered DOM element into the hook and attach that same ref to the element receiving the returned props.
- Preserve user-provided labels and descriptions; icon-only controls still need `aria-label` or `aria-labelledby`.
- Keep trigger, overlay, and dismissal props together so focus restoration, escape handling, and outside interaction semantics stay intact.

## Upstream Sections To Recheck

- Features
- Anatomy
- Example
- Styled examples
