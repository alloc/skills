# useTooltipTriggerState

Source: https://react-aria.adobe.com/Tooltip/useTooltipTriggerState.html

## Import

- Package: `react-stately`
- Import: `import {useTooltipTriggerState} from 'react-stately'`
- Install: `yarn add react-stately`
- Source version: 3.48.0

## Signature

```ts
useTooltipTriggerState(props: TooltipTriggerProps): TooltipTriggerState
```

## Use For

Manages state for a tooltip trigger. Tracks whether the tooltip is open, and provides methods to toggle this state. Ensures only one tooltip is open at a time and controls the delay for showing a tooltip.

## Implementation Guidance

- Use this hook as the state owner for the matching React Aria behavior hook rather than recreating selection, open state, validation, or collection logic by hand.
- Keep keys stable across renders for collection items, especially when data can be inserted, removed, sorted, filtered, or loaded asynchronously.
- Use the hook result as the single source of truth for related child hooks and rendered collection items.
- Keep trigger, overlay, and dismissal props together so focus restoration, escape handling, and outside interaction semantics stay intact.

## Upstream Sections To Recheck

- Interface
- Example
