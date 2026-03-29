# Downshift primitives and structure

## Choose the primitive first

- Use `useCombobox` for autocomplete or combobox flows with an input and filtered results.
- Use `useSelect` for custom select menus triggered by a button or toggle, without typed query input.
- Use `useTagGroup` for accessible tag or chip lists with left/right navigation and remove buttons.
- Treat `useMultipleSelection` as a legacy multi-select helper. The docs explicitly point tag-group-style multiple selection toward `useTagGroup`.
- Treat the render-prop `Downshift` component as a compatibility API. Prefer hooks for new work.

## Preserve the combobox DOM shape

- Keep the input inside the combobox wrapper.
- Render the menu element as a sibling of that wrapper.
- Do not collapse the input, toggle button, label, and menu into one container when you need wide screen-reader support.

## Legacy `Downshift` component rules

- Prefer `getRootProps` when maintaining the render-prop component. That is the path that preserves the recommended combobox structure.
- Avoid introducing new usages that omit `getRootProps`. Downshift still supports that older pattern, but the docs call out weaker screen-reader compatibility because all parts become children of the combobox element.
- Keep the getter-to-element mapping aligned:
  - `getLabelProps` -> label
  - `getToggleButtonProps` -> button
  - `getRootProps` -> wrapper around input and toggle button
  - `getInputProps` -> input
  - `getMenuProps` -> menu list
  - `getItemProps` -> each menu item

## Hook getter patterns

- `useCombobox` owns label, optional toggle button, input, menu, and items.
- `useSelect` owns label, toggle element, menu, and items.
- `useTagGroup` owns the tag container, individual tags, and remove buttons.
- Keep the corresponding state values (`isOpen`, `highlightedIndex`, `selectedItem`, `inputValue`, `activeIndex`) close to render logic instead of re-deriving them indirectly.

## General implementation rules

- Treat Downshift as state and accessibility logic, not a styled component system.
- Build UI with ordinary DOM nodes or UI-library primitives, then layer getter props onto those elements.
- In Preact codebases, import Downshift from `downshift/preact`. Treat that entrypoint as the preferred package path even though it is undocumented.
- Preserve item identity and display behavior explicitly when items are objects. Use `itemToString` instead of relying on implicit coercion.
