# useTableRowGroup

Source: https://react-aria.adobe.com/Table/useTable.html

## Import

- Package: `react-aria`
- Import: `import {useTableRowGroup} from 'react-aria'`
- Install: `yarn add react-aria`
- Source version: 3.50.0
- Documented on upstream page: `useTable`

## Signature

```ts
useTableRowGroup(): GridRowGroupAria
```

## Use For

Use `useTableRowGroup` for the table row group part of the `useTable` pattern. The upstream page describes the broader pattern as: Provides the behavior and accessibility implementation for a table component. A table displays data in rows and columns and enables a user to navigate its contents via directional navigation keys, and optionally supports row selection and sorting.

## Source Highlights

- Exposed to assistive technology as a `grid` using ARIA
- Keyboard navigation between columns, rows, cells, and in-cell focusable elements via the arrow keys
- Single, multiple, or no row selection via mouse, touch, or keyboard interactions
- Support for disabled rows, which cannot be selected
- Optional support for checkboxes in each row for selection, as well as in the header to select all rows
- Support for both `toggle` and `replace` selection behaviors
- Support for row actions via double click, Enter key, or tapping
- Long press to enter selection mode on touch when there is both selection and row actions

## Implementation Guidance

- Spread every returned `*Props` object onto the exact DOM slot it names; these props carry ARIA attributes, event handlers, ids, and keyboard behavior.
- Preserve user-provided labels and descriptions; icon-only controls still need `aria-label` or `aria-labelledby`.
- Render item-level hooks inside the parent collection/control and pass the parent state or item data from the same render pass.
- Do not replace React Aria collection or selection managers with ad hoc arrays of DOM handlers; render from the collection/state APIs.

## Related Hooks From The Same Source Page

- [useTable](./use-table.md)
- [useTableHeaderRow](./use-table-header-row.md)
- [useTableColumnHeader](./use-table-column-header.md)
- [useTableRow](./use-table-row.md)
- [useTableCell](./use-table-cell.md)
- [useTableSelectionCheckbox](./use-table-selection-checkbox.md)
- [useTableSelectAllCheckbox](./use-table-select-all-checkbox.md)
- [useTableColumnResize](./use-table-column-resize.md)

## Upstream Sections To Recheck

- Features
- Anatomy
- State management
- Example
- Usage
- Resizable Columns
