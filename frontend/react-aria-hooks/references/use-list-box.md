# useListBox

Source: https://react-aria.adobe.com/ListBox/useListBox.html

## Import

- Package: `react-aria`
- Import: `import {useListBox} from 'react-aria'`
- Install: `yarn add react-aria`
- Source version: 3.50.0

## Signature

```ts
useListBox<T>(props: AriaListBoxOptions<T>, state: ListState<T>, ref: RefObject<HTMLElement | null>): ListBoxAria
```

## Use For

Provides the behavior and accessibility implementation for a listbox component. A listbox displays a list of options and allows a user to select one or more of them.

## Source Highlights

- Exposed to assistive technology as a `listbox` using ARIA
- Support for single, multiple, or no selection
- Support for disabled items
- Support for sections
- Labeling support for accessibility
- Support for mouse, touch, and keyboard interactions
- Tab stop focus management
- Keyboard navigation support including arrow keys, home/end, page up/down, select all, and clear

## Implementation Guidance

- Spread every returned `*Props` object onto the exact DOM slot it names; these props carry ARIA attributes, event handlers, ids, and keyboard behavior.
- Pass the ref for the rendered DOM element into the hook and attach that same ref to the element receiving the returned props.
- Create the matching `react-stately` state object once in the owning component and pass that same state to related item, cell, or trigger hooks.
- Preserve user-provided labels and descriptions; icon-only controls still need `aria-label` or `aria-labelledby`.
- Do not replace React Aria collection or selection managers with ad hoc arrays of DOM handlers; render from the collection/state APIs.

## Related Hooks From The Same Source Page

- [useOption](./use-option.md)
- [useListBoxSection](./use-list-box-section.md)

## Upstream Sections To Recheck

- Features
- Anatomy
- State management
- Example
- Dynamic collections
- Selection
- Sections
- Complex options
- Asynchronous loading
- Links
- Disabled items
- Internationalization
