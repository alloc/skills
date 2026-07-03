# useAsyncList

Source: https://react-aria.adobe.com/useAsyncList.html

## Import

- Package: `react-stately`
- Import: `import {useAsyncList} from 'react-stately'`
- Install: `yarn add react-stately`
- Source version: 3.48.0

## Signature

```ts
useAsyncList<T, C = string>(options: AsyncListOptions<T, C>): AsyncListData<T>
```

## Use For

Manages state for an immutable async loaded list data structure, and provides convenience methods to update the data over time. Manages loading and error states, pagination, and sorting.

## Implementation Guidance

- Use this hook as the state owner for the matching React Aria behavior hook rather than recreating selection, open state, validation, or collection logic by hand.
- Keep keys stable across renders for collection items, especially when data can be inserted, removed, sorted, filtered, or loaded asynchronously.
- Use the hook result as the single source of truth for related child hooks and rendered collection items.
- Do not replace React Aria collection or selection managers with ad hoc arrays of DOM handlers; render from the collection/state APIs.

## Upstream Sections To Recheck

- Introduction
- Options
- Interface
- Example
- Sorting
- Filtering
- Pre-selecting items
- Client side updates
