# useSliderState

Source: https://react-aria.adobe.com/Slider/useSliderState.html

## Import

- Package: `react-stately`
- Import: `import {useSliderState} from 'react-stately'`
- Install: `yarn add react-stately`
- Source version: 3.48.0

## Signature

```ts
useSliderState<T extends number | number[]>(props: SliderStateOptions<T>): SliderState
```

## Use For

Provides state management for a slider component. Stores values for all thumbs, formats values for localization, and provides methods to update the position of any thumbs.

## Implementation Guidance

- Use this hook as the state owner for the matching React Aria behavior hook rather than recreating selection, open state, validation, or collection logic by hand.
- Keep keys stable across renders for collection items, especially when data can be inserted, removed, sorted, filtered, or loaded asynchronously.
- Use the hook result as the single source of truth for related child hooks and rendered collection items.

## Upstream Sections To Recheck

- Interface
- Example
