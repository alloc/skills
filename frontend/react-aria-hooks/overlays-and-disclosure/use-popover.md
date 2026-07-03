# usePopover

Source: https://react-aria.adobe.com/Popover/usePopover.html

## Import

- Package: `react-aria`
- Import: `import {usePopover} from 'react-aria'`
- Install: `yarn add react-aria`
- Source version: 3.50.0

## Signature

```ts
usePopover(props: AriaPopoverProps, state: OverlayTriggerState): PopoverAria
```

## Use For

Provides the behavior and accessibility implementation for a popover component. A popover is an overlay element positioned relative to a trigger.

## Source Highlights

- **Accessible** - The trigger and popover are automatically associated semantically via ARIA. Content outside the popover is hidden from assistive technologies while it is open. The popover closes when interacting outside, or pressing the Escape key.
- **Focus management** - Focus is moved into the popover on mount, and restored to the trigger element on unmount.
- **Positioning** - The popover is positioned relative to the trigger element, and automatically flips and adjusts to avoid overlapping with the edge of the browser window. Scrolling is prevented outside the popover to avoid unintentionally repositioning or closing it.

## Implementation Guidance

- Spread every returned `*Props` object onto the exact DOM slot it names; these props carry ARIA attributes, event handlers, ids, and keyboard behavior.
- Create the matching `react-stately` state object once in the owning component and pass that same state to related item, cell, or trigger hooks.
- Preserve user-provided labels and descriptions; icon-only controls still need `aria-label` or `aria-labelledby`.
- Keep trigger, overlay, and dismissal props together so focus restoration, escape handling, and outside interaction semantics stay intact.

## Upstream Sections To Recheck

- Features
- Anatomy
- Example
- Usage
