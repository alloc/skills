# useTooltipTrigger

Source: https://react-aria.adobe.com/Tooltip/useTooltipTrigger.html

## Import

- Package: `react-aria`
- Import: `import {useTooltipTrigger} from 'react-aria'`
- Install: `yarn add react-aria`
- Source version: 3.50.0

## Signature

```ts
useTooltipTrigger(props: TooltipTriggerProps, state: TooltipTriggerState, ref: RefObject<FocusableElement | null>): TooltipTriggerAria
```

## Use For

Provides the behavior and accessibility implementation for a tooltip trigger, e.g. a button that shows a description when focused or hovered.

## Source Highlights

- Keyboard focus management and cross browser normalization
- Hover management and cross browser normalization
- Labeling support for screen readers (aria-describedby)
- Exposed as a tooltip to assistive technology via ARIA
- Matches native tooltip behavior with delay on hover of first tooltip and no delay on subsequent tooltips.

## Implementation Guidance

- Spread every returned `*Props` object onto the exact DOM slot it names; these props carry ARIA attributes, event handlers, ids, and keyboard behavior.
- Pass the ref for the rendered DOM element into the hook and attach that same ref to the element receiving the returned props.
- Create the matching `react-stately` state object once in the owning component and pass that same state to related item, cell, or trigger hooks.
- Preserve user-provided labels and descriptions; icon-only controls still need `aria-label` or `aria-labelledby`.
- Keep trigger, overlay, and dismissal props together so focus restoration, escape handling, and outside interaction semantics stay intact.

## Related Hooks From The Same Source Page

- [useTooltip](./use-tooltip.md)

## Upstream Sections To Recheck

- Features
- Anatomy
- Example
- Usage
