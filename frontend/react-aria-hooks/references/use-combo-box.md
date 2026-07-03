# useComboBox

Source: https://react-aria.adobe.com/ComboBox/useComboBox.html

## Import

- Package: `react-aria`
- Import: `import {useComboBox} from 'react-aria'`
- Install: `yarn add react-aria`
- Source version: 3.50.0

## Signature

```ts
useComboBox<T, M extends SelectionMode = 'single'>(props: AriaComboBoxOptions<T, M>, state: ComboBoxState<T, M>): ComboBoxAria<T>
```

## Use For

Provides the behavior and accessibility implementation for a combo box component. A combo box combines a text input with a listbox, allowing users to filter a list of options to items matching a query.

## Source Highlights

- Support for filtering a list of options by typing
- Support for selecting a single option
- Support for disabled options
- Support for groups of items in sections
- Support for custom user input values
- Support for controlled and uncontrolled options, selection, input value, and open state
- Support for custom filter functions
- Async loading and infinite scrolling support

## Implementation Guidance

- Spread every returned `*Props` object onto the exact DOM slot it names; these props carry ARIA attributes, event handlers, ids, and keyboard behavior.
- Create the matching `react-stately` state object once in the owning component and pass that same state to related item, cell, or trigger hooks.
- Preserve user-provided labels and descriptions; icon-only controls still need `aria-label` or `aria-labelledby`.
- Do not replace React Aria collection or selection managers with ad hoc arrays of DOM handlers; render from the collection/state APIs.

## Upstream Sections To Recheck

- Features
- Anatomy
- State management
- Example
- Styled examples
- Usage
