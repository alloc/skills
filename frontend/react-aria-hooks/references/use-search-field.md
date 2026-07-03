# useSearchField

Source: https://react-aria.adobe.com/SearchField/useSearchField.html

## Import

- Package: `react-aria`
- Import: `import {useSearchField} from 'react-aria'`
- Install: `yarn add react-aria`
- Source version: 3.50.0

## Signature

```ts
useSearchField(props: AriaSearchFieldProps, state: SearchFieldState, inputRef: RefObject<HTMLInputElement | null>): SearchFieldAria
```

## Use For

Provides the behavior and accessibility implementation for a search field.

## Source Highlights

- Built with a native `<input type="search">` element
- Visual and ARIA labeling support
- Keyboard submit handling via the Enter key
- Keyboard support for clearing the search field with the Escape key
- Custom clear button support with an accessible label; provide custom clear-button copy from the application
- Support for native HTML constraint validation with customizable UI, custom validation functions, realtime validation, and server-side validation errors

## Implementation Guidance

- Spread every returned `*Props` object onto the exact DOM slot it names; these props carry ARIA attributes, event handlers, ids, and keyboard behavior.
- Create the matching `react-stately` state object once in the owning component and pass that same state to related item, cell, or trigger hooks.
- Preserve user-provided labels and descriptions; icon-only controls still need `aria-label` or `aria-labelledby`.

## Upstream Sections To Recheck

- Features
- Anatomy
- Example
- Styling
- Usage
