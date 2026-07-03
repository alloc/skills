# useGridListSelectionCheckbox

Source: https://react-aria.adobe.com/GridList/useGridList.html

## Import

- Package: `react-aria`
- Import: `import {useGridListSelectionCheckbox} from 'react-aria'`
- Install: `yarn add react-aria`
- Source version: 3.50.0
- Documented on upstream page: `useGridList`

## Signature

```ts
useGridListSelectionCheckbox<T>(props: AriaGridSelectionCheckboxProps, state: ListState<T>): GridSelectionCheckboxAria
```

## Use For

Use `useGridListSelectionCheckbox` for the grid list selection checkbox part of the `useGridList` pattern. The upstream page describes the broader pattern as: Provides the behavior and accessibility implementation for a list component with interactive children. A grid list displays data in a single column and enables a user to navigate its contents via directional navigation keys.

## Source Highlights

- **Item selection** - Single or multiple selection, with optional checkboxes, disabled rows, and both `toggle` and `replace` selection behaviors.
- **Interactive children** - List items may include interactive elements such as buttons, checkboxes, menus, etc.
- **Actions** - Items support optional row actions such as navigation via click, tap, double click, or Enter key.
- **Async loading** - Support for loading items asynchronously, with infinite and virtualized scrolling.
- **Keyboard navigation** - List items and focusable children can be navigated using the arrow keys, along with page up/down, home/end, etc. Typeahead, auto scrolling, and selection modifier keys are supported as well.
- **Touch friendly** - Selection and actions adapt their behavior depending on the device. For example, selection is activated via long press on touch when item actions are present.
- **Accessible** - Follows the [ARIA grid pattern](https://www.w3.org/WAI/ARIA/apg/patterns/grid/), with additional selection announcements via an ARIA live region. Extensively tested across many devices and [assistive technologies](https://react-aria.adobe.com/quality#supported-screen-readers) to ensure announcements and behaviors are consistent.

## Implementation Guidance

- Spread every returned `*Props` object onto the exact DOM slot it names; these props carry ARIA attributes, event handlers, ids, and keyboard behavior.
- Create the matching `react-stately` state object once in the owning component and pass that same state to related item, cell, or trigger hooks.
- Preserve user-provided labels and descriptions; icon-only controls still need `aria-label` or `aria-labelledby`.
- Do not replace React Aria collection or selection managers with ad hoc arrays of DOM handlers; render from the collection/state APIs.

## Related Hooks From The Same Source Page

- [useGridList](./use-grid-list.md)
- [useGridListItem](./use-grid-list-item.md)

## Upstream Sections To Recheck

- Features
- Anatomy
- State management
- Example
- Usage
