# useMenuTriggerState

Source: https://react-aria.adobe.com/Menu/useMenuTriggerState.html

## Import

- Package: `react-stately`
- Import: `import {useMenuTriggerState} from 'react-stately'`
- Install: `yarn add react-stately`
- Source version: 3.48.0

## Signature

```ts
useMenuTriggerState(props: MenuTriggerProps): RootMenuTriggerState
```

## Use For

Manages state for a menu trigger. Tracks whether the menu is currently open, and controls which item will receive focus when it opens. Also tracks the open submenus within the menu tree via their trigger keys.

## Implementation Guidance

- Use this hook as the state owner for the matching React Aria behavior hook rather than recreating selection, open state, validation, or collection logic by hand.
- Keep keys stable across renders for collection items, especially when data can be inserted, removed, sorted, filtered, or loaded asynchronously.
- Use the hook result as the single source of truth for related child hooks and rendered collection items.
- Keep trigger, overlay, and dismissal props together so focus restoration, escape handling, and outside interaction semantics stay intact.
- Do not replace React Aria collection or selection managers with ad hoc arrays of DOM handlers; render from the collection/state APIs.

## Upstream Sections To Recheck

- Interface
- Example
