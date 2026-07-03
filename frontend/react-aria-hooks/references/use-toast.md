# useToast

Source: https://react-aria.adobe.com/Toast/useToast.html

## Import

- Package: `react-aria`
- Import: `import {useToast} from 'react-aria'`
- Install: `yarn add react-aria`
- Source version: 3.50.0

## Signature

```ts
useToast<T>(props: AriaToastProps<T>, state: ToastState<T>, ref: RefObject<FocusableElement | null>): ToastAria
```

## Use For

Provides the behavior and accessibility implementation for a toast component. Toasts display brief, temporary notifications of actions, errors, or other events in an application.

## Source Highlights

- **Accessible** - Toasts follow the [ARIA alertdialog pattern](https://www.w3.org/WAI/ARIA/apg/patterns/alertdialog/). They are rendered in a [landmark region](https://www.w3.org/WAI/ARIA/apg/practices/landmark-regions/), which keyboard and screen reader users can easily jump to when an alert is announced.
- **Focus management** - When a toast unmounts, focus is moved to the next toast if any. Otherwise, focus is restored to where it was before navigating to the toast region. Tabbing through the Toast region will move from newest to oldest.

## Implementation Guidance

- Spread every returned `*Props` object onto the exact DOM slot it names; these props carry ARIA attributes, event handlers, ids, and keyboard behavior.
- Pass the ref for the rendered DOM element into the hook and attach that same ref to the element receiving the returned props.
- Create the matching `react-stately` state object once in the owning component and pass that same state to related item, cell, or trigger hooks.
- Preserve user-provided labels and descriptions; icon-only controls still need `aria-label` or `aria-labelledby`.

## Related Hooks From The Same Source Page

- [useToastRegion](./use-toast-region.md)

## Upstream Sections To Recheck

- Features
- Anatomy
- Example
- Usage
- Advanced topics
