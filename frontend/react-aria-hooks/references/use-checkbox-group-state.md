# useCheckboxGroupState

Source: https://react-aria.adobe.com/CheckboxGroup/useCheckboxGroupState.html

## Import

- Package: `react-stately`
- Import: `import {useCheckboxGroupState} from 'react-stately'`
- Install: `yarn add react-stately`
- Source version: 3.48.0

## Signature

```ts
useCheckboxGroupState(props: CheckboxGroupProps): CheckboxGroupState
```

## Use For

Provides state management for a checkbox group component. Provides a name for the group, and manages selection and focus state.

## Implementation Guidance

- Use this hook as the state owner for the matching React Aria behavior hook rather than recreating selection, open state, validation, or collection logic by hand.
- Keep keys stable across renders for collection items, especially when data can be inserted, removed, sorted, filtered, or loaded asynchronously.
- Use the hook result as the single source of truth for related child hooks and rendered collection items.

## Upstream Sections To Recheck

- Interface
