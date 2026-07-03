# useAutocomplete

Source: https://react-aria.adobe.com/Autocomplete/useAutocomplete.html

## Import

- Package: `@react-aria/autocomplete`
- Import: `import {useAutocomplete} from '@react-aria/autocomplete'`
- Install: `yarn add @react-aria/autocomplete`
- Source version: 3.0.0-rc.8

## Signature

```ts
useAutocomplete<T>(props: AriaAutocompleteOptions<T>, state: AutocompleteState): AutocompleteAria<T>
```

## Use For

beta # useAutocomplete Provides the behavior and accessibility implementation for an autocomplete component. An autocomplete combines a text input with a collection, allowing users to filter the collection's contents match a query.

## Implementation Guidance

- Spread every returned `*Props` object onto the exact DOM slot it names; these props carry ARIA attributes, event handlers, ids, and keyboard behavior.
- Create the matching `react-stately` state object once in the owning component and pass that same state to related item, cell, or trigger hooks.
- Preserve user-provided labels and descriptions; icon-only controls still need `aria-label` or `aria-labelledby`.
- Do not replace React Aria collection or selection managers with ad hoc arrays of DOM handlers; render from the collection/state APIs.

## Upstream Sections To Recheck

- Features
- Anatomy
- Internationalization
