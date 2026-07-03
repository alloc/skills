# useTreeState

Source: https://react-aria.adobe.com/Tree/useTreeState.html

## Import

- Package: `react-stately`
- Import: `import {useTreeState} from 'react-stately'`
- Install: `yarn add react-stately`
- Source version: 3.48.0

## Signature

```ts
useTreeState<T>(props: TreeProps<T>): TreeState<T>
```

## Use For

Provides state management for tree-like components. Handles building a collection of items from props, item expanded state, and manages multiple selection state.

## Implementation Guidance

- Use this hook as the state owner for the matching React Aria behavior hook rather than recreating selection, open state, validation, or collection logic by hand.
- Keep keys stable across renders for collection items, especially when data can be inserted, removed, sorted, filtered, or loaded asynchronously.
- Use the hook result as the single source of truth for related child hooks and rendered collection items.
- Do not replace React Aria collection or selection managers with ad hoc arrays of DOM handlers; render from the collection/state APIs.

## Upstream Sections To Recheck

- Interface
- Example
