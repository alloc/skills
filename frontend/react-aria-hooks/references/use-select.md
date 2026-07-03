# useSelect

Source: https://react-aria.adobe.com/Select/useSelect.html

## Import

- Package: `react-aria`
- Import: `import {useSelect} from 'react-aria'`
- Install: `yarn add react-aria`
- Source version: 3.50.0

## Signature

```ts
useSelect<T, M extends SelectionMode = 'single'>(props: AriaSelectOptions<T, M>, state: SelectState<T, M>, ref: RefObject<HTMLElement | null>): SelectAria<T, M>
```

## Use For

Provides the behavior and accessibility implementation for a select component. A select displays a collapsible list of options and allows a user to select one of them.

## Source Highlights

- Exposed to assistive technology as a button with a `listbox` popup using ARIA (combined with [useListBox](https://react-aria.adobe.com/ListBox/useListBox.html))
- Support for selecting a single option
- Support for disabled options
- Support for sections
- Labeling support for accessibility
- Support for native HTML constraint validation with customizable UI, custom validation functions, realtime validation, and server-side validation errors
- Support for mouse, touch, and keyboard interactions
- Tab stop focus management

## Implementation Guidance

- Spread every returned `*Props` object onto the exact DOM slot it names; these props carry ARIA attributes, event handlers, ids, and keyboard behavior.
- Pass the ref for the rendered DOM element into the hook and attach that same ref to the element receiving the returned props.
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
- Internationalization
