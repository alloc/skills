# useSelect

## Core shape

- Use `useSelect` for custom select menus that behave like a native select but are rendered with custom markup.
- Wire the returned getters to label, toggle element, menu, and items.
- Keep `isOpen`, `highlightedIndex`, and `selectedItem` near the render path because they drive visibility and item styling.

## Common patterns

- Use `itemToString` when items are objects or when typeahead and announcements need an explicit display string.
- Control `selectedItem` when multiple widgets or app state need to stay synchronized.
- Use `stateReducer` for select-specific keyboard overrides. The docs show keeping the menu closed while `ArrowUp` and `ArrowDown` change `selectedItem` on Windows-style behavior.
- Use action props such as `openMenu` and `selectItem` for imperative UX like hover-to-open or clear-selection buttons.

## UI-library integration

- Spread getter props onto the actual rendered DOM nodes or onto components that forward refs correctly.
- Expect focus and scroll behavior to depend on valid refs.
- Treat object-item selects the same way as comboboxes: define `itemToString` so highlighting by character keys and selection announcements stay correct.

## Special cases

- Pass a custom `window` option when the select renders inside an iframe or other alternate-window context.
- In React Native, keep the same hook contract and translate markup to native components.

## Multiple selection with selects

- For checkbox-style multi-select menus, control `selectedItem` to `null` and keep `selectedItems` in app state.
- Use `onSelectedItemChange` to add or remove items from that array.
- Use `stateReducer` to keep the menu open after Enter or click selection when repeated selection is expected.
- Prefer `useTagGroup` when the selected values are shown as removable tags outside the menu.
