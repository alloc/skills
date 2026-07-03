# useAutocompleteState

Source: https://react-aria.adobe.com/Autocomplete/useAutocompleteState.html

## Import

- Package: `@react-stately/autocomplete`
- Import: `import {useAutocompleteState} from '@react-stately/autocomplete'`
- Install: `yarn add @react-stately/autocomplete`
- Source version: 3.0.0-beta.6

## Signature

```ts
useAutocompleteState(props: AutocompleteStateOptions): AutocompleteState
```

## Use For

beta # useAutocompleteState Provides state management for an autocomplete component.

## Implementation Guidance

- Use this hook as the state owner for the matching React Aria behavior hook rather than recreating selection, open state, validation, or collection logic by hand.
- Keep keys stable across renders for collection items, especially when data can be inserted, removed, sorted, filtered, or loaded asynchronously.
- Use the hook result as the single source of truth for related child hooks and rendered collection items.
- Do not replace React Aria collection or selection managers with ad hoc arrays of DOM handlers; render from the collection/state APIs.

## Upstream Sections To Recheck

- Interface
