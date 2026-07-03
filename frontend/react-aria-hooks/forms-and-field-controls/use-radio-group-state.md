# useRadioGroupState

Source: https://react-aria.adobe.com/RadioGroup/useRadioGroupState.html

## Import

- Package: `react-stately`
- Import: `import {useRadioGroupState} from 'react-stately'`
- Install: `yarn add react-stately`
- Source version: 3.48.0

## Signature

```ts
useRadioGroupState(props: RadioGroupProps): RadioGroupState
```

## Use For

Provides state management for a radio group component. Provides a name for the group, and manages selection and focus state.

## Implementation Guidance

- Use this hook as the state owner for the matching React Aria behavior hook rather than recreating selection, open state, validation, or collection logic by hand.
- Keep keys stable across renders for collection items, especially when data can be inserted, removed, sorted, filtered, or loaded asynchronously.
- Use the hook result as the single source of truth for related child hooks and rendered collection items.
- Render item-level hooks inside the parent collection/control and pass the parent state or item data from the same render pass.

## Upstream Sections To Recheck

- Interface
- Example
