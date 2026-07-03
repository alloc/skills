# useTooltip

Source: https://react-aria.adobe.com/Tooltip/useTooltipTrigger.html

## Import

- Package: `react-aria`
- Import: `import {useTooltip} from 'react-aria'`
- Install: `yarn add react-aria`
- Source version: 3.50.0
- Documented on upstream page: `useTooltipTrigger`

## Signature

```ts
useTooltip(props: AriaTooltipProps, state?: TooltipTriggerState): TooltipAria
```

## Use For

Use `useTooltip` for the tooltip part of the `useTooltipTrigger` pattern. The upstream page describes the broader pattern as: Provides the behavior and accessibility implementation for a tooltip trigger, e.g. a button that shows a description when focused or hovered.

## Source Highlights

- Keyboard focus management and cross browser normalization
- Hover management and cross browser normalization
- Labeling support for screen readers (aria-describedby)
- Exposed as a tooltip to assistive technology via ARIA
- Matches native tooltip behavior with delay on hover of first tooltip and no delay on subsequent tooltips.

## Implementation Guidance

- Spread every returned `*Props` object onto the exact DOM slot it names; these props carry ARIA attributes, event handlers, ids, and keyboard behavior.
- Preserve user-provided labels and descriptions; icon-only controls still need `aria-label` or `aria-labelledby`.
- Keep trigger, overlay, and dismissal props together so focus restoration, escape handling, and outside interaction semantics stay intact.

## Related Hooks From The Same Source Page

- [useTooltipTrigger](./use-tooltip-trigger.md)

## Upstream Sections To Recheck

- Features
- Anatomy
- Example
- Usage
- Internationalization
