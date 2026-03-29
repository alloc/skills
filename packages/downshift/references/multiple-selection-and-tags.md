# Multiple selection and tags

## Prefer `useTagGroup` for tag UIs

- Use `useTagGroup` when the selected state is rendered as chips or tags with remove buttons.
- Wire `getTagGroupProps` to the container, `getTagProps` to each tag, and `getTagRemoveProps` to each remove button.
- Use `items` and `activeIndex` to render and style the active tag.
- Use `addItem` to append a selection when another hook or menu chooses an item.

## Treat `useMultipleSelection` as legacy

- The docs mark `useMultipleSelection` as deprecated for tag-group-style dropdowns and point new tag flows to `useTagGroup`.
- Keep `useMultipleSelection` in mind when maintaining existing code that already depends on its API or when the UI is not being migrated yet.
- Its primary getters and actions are:
  - `getDropdownProps` for the input or button that owns focus
  - `getSelectedItemProps` for rendered selected items
  - `addSelectedItem` and `removeSelectedItem` for imperative updates

## Coordinate hooks deliberately

- When combining `useCombobox` or `useSelect` with multi-select state, keep the single-select hook from owning final selection.
- Control `selectedItem` to `null` and store `selectedItems` in app state.
- Use `onSelectedItemChange` or `onStateChange` to add the chosen item to the selected array.
- Use `removeSelectedItem` or tag remove handlers to delete selections.

## Keyboard and focus rules

- Use `getDropdownProps({ preventKeyAction: isOpen })` when Backspace deletion or left/right navigation should be disabled while the menu is open.
- Keep removal and tag navigation accessible from the keyboard instead of moving that behavior into mouse-only affordances.
- Preserve the live-region announcements and focus behavior supplied by the hook rather than recreating them manually.

## Implementation patterns

- Render selected items with simple spans or UI-library primitives. Downshift only requires the correct prop wiring, not a specific visual structure.
- Keep the menu open after a selection when repeated picking is the goal.
- For combobox-plus-tags flows, also control `inputValue` so filtering excludes or accounts for already selected items.
- In React Native, keep the same hook responsibilities and map elements to native equivalents.
