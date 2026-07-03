# useColorWheelState

Source: https://react-aria.adobe.com/ColorWheel/useColorWheelState.html

## Import

- Package: `react-stately`
- Import: `import {useColorWheelState} from 'react-stately'`
- Install: `yarn add react-stately`
- Source version: 3.48.0

## Signature

```ts
useColorWheelState(props: ColorWheelProps): ColorWheelState
```

## Use For

Provides state management for a color wheel component. Color wheels allow users to adjust the hue of an HSL or HSB color value on a circular track.

## Implementation Guidance

- Use this hook as the state owner for the matching React Aria behavior hook rather than recreating selection, open state, validation, or collection logic by hand.
- Keep keys stable across renders for collection items, especially when data can be inserted, removed, sorted, filtered, or loaded asynchronously.
- Use the hook result as the single source of truth for related child hooks and rendered collection items.

## Upstream Sections To Recheck

- Interface
- Example
