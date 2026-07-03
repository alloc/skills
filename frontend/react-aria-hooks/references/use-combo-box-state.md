# useComboBoxState

Source: https://react-aria.adobe.com/ComboBox/useComboBoxState.html

## Import

- Package: `react-stately`
- Import: `import {useComboBoxState} from 'react-stately'`
- Install: `yarn add react-stately`
- Source version: 3.48.0

## Signature

```ts
useComboBoxState<T, M extends SelectionMode = 'single'>(props: ComboBoxStateOptions<T, M>): ComboBoxState<T, M>
```

## Use For

Provides state management for a combo box component. Handles building a collection of items from props and manages the option selection state of the combo box. In addition, it tracks the input value, focus state, and other properties of the combo box.

## Implementation Guidance

- Use this hook as the state owner for the matching React Aria behavior hook rather than recreating selection, open state, validation, or collection logic by hand.
- Keep keys stable across renders for collection items, especially when data can be inserted, removed, sorted, filtered, or loaded asynchronously.
- Use the hook result as the single source of truth for related child hooks and rendered collection items.
- Do not replace React Aria collection or selection managers with ad hoc arrays of DOM handlers; render from the collection/state APIs.

## Upstream Sections To Recheck

- Interface
- Example
