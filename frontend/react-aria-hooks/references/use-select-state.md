# useSelectState

Source: https://react-aria.adobe.com/Select/useSelectState.html

## Import

- Package: `react-stately`
- Import: `import {useSelectState} from 'react-stately'`
- Install: `yarn add react-stately`
- Source version: 3.48.0

## Signature

```ts
useSelectState<T, M extends SelectionMode = 'single'>(props: SelectStateOptions<T, M>): SelectState<T, M>
```

## Use For

Provides state management for a select component. Handles building a collection of items from props, handles the open state for the popup menu, and manages multiple selection state.

## Implementation Guidance

- Use this hook as the state owner for the matching React Aria behavior hook rather than recreating selection, open state, validation, or collection logic by hand.
- Keep keys stable across renders for collection items, especially when data can be inserted, removed, sorted, filtered, or loaded asynchronously.
- Use the hook result as the single source of truth for related child hooks and rendered collection items.
- Do not replace React Aria collection or selection managers with ad hoc arrays of DOM handlers; render from the collection/state APIs.

## Upstream Sections To Recheck

- Interface
- Example
