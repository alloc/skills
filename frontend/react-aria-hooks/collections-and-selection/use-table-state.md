# useTableState

Source: https://react-aria.adobe.com/Table/useTableState.html

## Import

- Package: `react-stately`
- Import: `import {useTableState} from 'react-stately'`
- Install: `yarn add react-stately`
- Source version: 3.48.0

## Signature

```ts
useTableState<T extends object>(props: TableStateProps<T>): TableState<T>
```

## Use For

Provides state management for a table component. Handles building a collection of columns and rows from props. In addition, it tracks row selection and manages sort order changes.

## Implementation Guidance

- Use this hook as the state owner for the matching React Aria behavior hook rather than recreating selection, open state, validation, or collection logic by hand.
- Keep keys stable across renders for collection items, especially when data can be inserted, removed, sorted, filtered, or loaded asynchronously.
- Use the hook result as the single source of truth for related child hooks and rendered collection items.
- Do not replace React Aria collection or selection managers with ad hoc arrays of DOM handlers; render from the collection/state APIs.

## Related Hooks From The Same Source Page

- [useTableColumnResizeState](./use-table-column-resize-state.md)

## Upstream Sections To Recheck

- Interface
- Example
