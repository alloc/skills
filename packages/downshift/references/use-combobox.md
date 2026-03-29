# useCombobox

## Core shape

- Use `useCombobox` for autocomplete or combobox interactions with typed input.
- Wire the returned getters to label, optional toggle button, input, menu, and items.
- Use `onInputValueChange` to drive filtering from the current query.
- Keep `isOpen`, `highlightedIndex`, `selectedItem`, and `inputValue` in render scope because they drive menu visibility, styling, and filtered data.

## Preserve accessibility structure

- Keep the input and optional toggle button inside the combobox wrapper.
- Keep the menu list adjacent to that wrapper, not nested under the same interactive element.
- Preserve the getter-prop wiring on the real input and menu nodes even when wrapping them in other components.

## Common patterns

- Use `itemToString` when items are objects. The docs use `item.title` as the display string in object-item examples.
- Control `selectedItem`, `highlightedIndex`, or `inputValue` when app state must stay authoritative.
- Use `stateReducer` for narrow behavioral overrides, such as transforming `inputValue` on `InputChange` while leaving other transitions unchanged.
- Use action props such as `selectItem` for imperative flows like custom clear buttons.

## UI-library integration

- Pass getter props straight through when the library forwards refs normally.
- When a component exposes the real input node under a custom prop, pass `refKey` to `getInputProps`. The docs show Material UI `Input` using `getInputProps({ refKey: 'inputRef' })`.
- Keep the DOM node reachable because Downshift performs focus and scroll work internally.

## Special cases

- Pass a custom `window` option when the combobox lives inside an iframe or another non-default window context.
- For large menus, keep Downshift's state logic and swap the scrolling implementation to a virtualization library. The docs call out `react-virtual` for this pattern.
- In React Native, keep the same interaction model and swap HTML elements for native equivalents.

## Multiple selection with comboboxes

- For a simple checked-list combobox, keep `selectedItems` outside the hook, control `selectedItem` to `null`, and update the array from `onSelectedItemChange`.
- Keep the menu open after selection when the UX requires repeated picks by intercepting the relevant transitions in `stateReducer`.
- Prefer `useTagGroup` when the selected items are rendered as removable chips or tags next to the combobox.
