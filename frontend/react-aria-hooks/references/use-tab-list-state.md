# useTabListState

Source: https://react-aria.adobe.com/Tabs/useTabListState.html

## Import

- Package: `react-stately`
- Import: `import {useTabListState} from 'react-stately'`
- Install: `yarn add react-stately`
- Source version: 3.48.0

## Signature

```ts
useTabListState<T extends object>(props: TabListStateOptions<T>): TabListState<T>
```

## Use For

Provides state management for a Tabs component. Tabs include a TabList which tracks which tab is currently selected and displays the content associated with that Tab in a TabPanel.

## Implementation Guidance

- Use this hook as the state owner for the matching React Aria behavior hook rather than recreating selection, open state, validation, or collection logic by hand.
- Keep keys stable across renders for collection items, especially when data can be inserted, removed, sorted, filtered, or loaded asynchronously.
- Use the hook result as the single source of truth for related child hooks and rendered collection items.
- Do not replace React Aria collection or selection managers with ad hoc arrays of DOM handlers; render from the collection/state APIs.

## Upstream Sections To Recheck

- Interface
- Example
