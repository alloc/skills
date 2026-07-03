---
name: react-aria-hooks
description: Use React Aria and React Stately hooks to build accessible custom React components, including choosing the right hook, wiring refs/state/props, preserving ARIA and keyboard behavior, excluding React Aria i18n and SSR utilities, and checking hook-specific guidance in bundled references.
---

# React Aria Hooks

Use React Aria hooks as the owner of accessibility semantics, keyboard behavior, focus management, collection navigation, overlays, drag and drop, and date, time, and color interactions. Use React Stately hooks as the owner of state machines, collection state, selection, validation, queues, and async list data.

## Excluded React Aria Features

- Do not include React Aria SSR utilities such as `SSRProvider`, `useIsSSR`, or SSR-specific id wiring.
- Do not include React Aria i18n utilities such as `I18nProvider`, `useLocale`, `useDateFormatter`, `useNumberFormatter`, `useCollator`, or `useFilter`.
- Pass application-prepared labels, descriptions, validation text, and formatted values into React Aria props when user-facing copy is needed.
- React Aria internal accessibility strings for generic hidden controls are acceptable; do not add React Aria i18n providers or formatting hooks.

## Use React Aria Only When It Pays For It

Start with native HTML, existing app components, and ordinary React state. Reach for React Aria hooks only when they clearly remove or centralize nontrivial accessibility or interaction logic.

Treat the benefit as measurable: the hook should delete custom code, prevent duplicated behavior, or replace a fragile interaction contract with a maintained React Aria contract.

Use a React Aria API when it owns at least one behavior that would otherwise be easy to get wrong:

- ARIA relationships, labels, descriptions, or invalid state across multiple elements.
- Keyboard navigation beyond native browser behavior.
- Focus containment, restoration, roving focus, or focus-visible behavior.
- Collection semantics, item keys, selection managers, disabled items, or virtualized collection integration.
- Overlay dismissal, portal focus behavior, hidden dismiss controls, or outside interaction handling.
- Cross-input press, drag, drop, long-press, move, hover, or clipboard behavior.
- Hidden native form integration, browser autofill, native validation, or FormData support.

Do not add React Aria when it only wraps behavior the platform already handles well, such as a plain `<button>`, `<a>`, `<input>`, `<textarea>`, or `<select>` with no custom interaction model.

Before adding a hook, name the behavior it will own and the custom code it replaces. If that list is empty or vague, do not use the hook.

## Workflow

1. Identify the component pattern and read the matching hook reference in `references/` before implementing or changing behavior.
2. Use the hook pair the docs expect: behavior hooks from `react-aria`, state hooks from `react-stately`, and date values from `@internationalized/date` where date and time hooks require them.
3. Read helper references before using low-level utilities: `mergeProps`, focus helpers, `VisuallyHidden`, `Overlay`, `DismissButton`, and `HiddenSelect`.
4. Spread every returned props object onto the named DOM slot, attach the same ref passed into the hook, and merge props with existing app handlers instead of overwriting them.
5. Keep labels, descriptions, validation state, disabled state, ids, and relationships wired through the hook props. Do not hand-roll ARIA attributes when the hook returns them.
6. For collections, render from the React Stately collection/state APIs and pass the same state to parent and item hooks. Keep item keys stable.
7. For overlays and triggers, keep trigger props, overlay props, dismissal behavior, focus restoration, and portal placement together.
8. Validate with keyboard, pointer, touch where relevant, screen-reader naming, focus order, disabled/invalid states, and controlled/uncontrolled state behavior.

## Reference Navigation

Each hook has its own document under `references/`. Search by hook name or use these groups:

### Collections And Selection

- [useAsyncList](./references/use-async-list.md)
- [useAutocomplete](./references/use-autocomplete.md)
- [useAutocompleteState](./references/use-autocomplete-state.md)
- [useComboBox](./references/use-combo-box.md)
- [useComboBoxState](./references/use-combo-box-state.md)
- [useGridList](./references/use-grid-list.md)
- [useGridListItem](./references/use-grid-list-item.md)
- [useGridListSelectionCheckbox](./references/use-grid-list-selection-checkbox.md)
- [useListBox](./references/use-list-box.md)
- [useListBoxSection](./references/use-list-box-section.md)
- [useListData](./references/use-list-data.md)
- [useListState](./references/use-list-state.md)
- [useMenu](./references/use-menu.md)
- [useMenuItem](./references/use-menu-item.md)
- [useMenuSection](./references/use-menu-section.md)
- [useMenuTrigger](./references/use-menu-trigger.md)
- [useMenuTriggerState](./references/use-menu-trigger-state.md)
- [useMultipleSelectionState](./references/use-multiple-selection-state.md)
- [useOption](./references/use-option.md)
- [useSelect](./references/use-select.md)
- [useSelectState](./references/use-select-state.md)
- [useSingleSelectListState](./references/use-single-select-list-state.md)
- [useTable](./references/use-table.md)
- [useTableCell](./references/use-table-cell.md)
- [useTableColumnHeader](./references/use-table-column-header.md)
- [useTableColumnResize](./references/use-table-column-resize.md)
- [useTableColumnResizeState](./references/use-table-column-resize-state.md)
- [useTableHeaderRow](./references/use-table-header-row.md)
- [useTableRow](./references/use-table-row.md)
- [useTableRowGroup](./references/use-table-row-group.md)
- [useTableSelectAllCheckbox](./references/use-table-select-all-checkbox.md)
- [useTableSelectionCheckbox](./references/use-table-selection-checkbox.md)
- [useTableState](./references/use-table-state.md)
- [useTabList](./references/use-tab-list.md)
- [useTabListState](./references/use-tab-list-state.md)
- [useTag](./references/use-tag.md)
- [useTagGroup](./references/use-tag-group.md)
- [useTreeData](./references/use-tree-data.md)
- [useTreeState](./references/use-tree-state.md)

### Color

- [useColorArea](./references/use-color-area.md)
- [useColorAreaState](./references/use-color-area-state.md)
- [useColorField](./references/use-color-field.md)
- [useColorFieldState](./references/use-color-field-state.md)
- [useColorSlider](./references/use-color-slider.md)
- [useColorSliderState](./references/use-color-slider-state.md)
- [useColorSwatch](./references/use-color-swatch.md)
- [useColorWheel](./references/use-color-wheel.md)
- [useColorWheelState](./references/use-color-wheel-state.md)

### Date And Time

- [useCalendar](./references/use-calendar.md)
- [useCalendarCell](./references/use-calendar-cell.md)
- [useCalendarGrid](./references/use-calendar-grid.md)
- [useCalendarState](./references/use-calendar-state.md)
- [useDateField](./references/use-date-field.md)
- [useDateFieldState](./references/use-date-field-state.md)
- [useDatePicker](./references/use-date-picker.md)
- [useDatePickerState](./references/use-date-picker-state.md)
- [useDateRangePicker](./references/use-date-range-picker.md)
- [useDateRangePickerState](./references/use-date-range-picker-state.md)
- [useDateSegment](./references/use-date-segment.md)
- [useRangeCalendar](./references/use-range-calendar.md)
- [useRangeCalendarState](./references/use-range-calendar-state.md)
- [useTimeField](./references/use-time-field.md)
- [useTimeFieldState](./references/use-time-field-state.md)

### Drag And Drop

- [useDrag](./references/use-drag.md)
- [useDrop](./references/use-drop.md)
- [useDraggableCollection](./references/use-draggable-collection.md)
- [useDraggableCollectionState](./references/use-draggable-collection-state.md)
- [useDraggableItem](./references/use-draggable-item.md)
- [useDropIndicator](./references/use-drop-indicator.md)
- [useDroppableCollection](./references/use-droppable-collection.md)
- [useDroppableCollectionState](./references/use-droppable-collection-state.md)
- [useDroppableItem](./references/use-droppable-item.md)

### Event And Focus Hooks

- [useClipboard](./references/use-clipboard.md)
- [useFocus](./references/use-focus.md)
- [useFocusManager](./references/use-focus-manager.md)
- [useFocusRing](./references/use-focus-ring.md)
- [useFocusVisible](./references/use-focus-visible.md)
- [useFocusWithin](./references/use-focus-within.md)
- [useHover](./references/use-hover.md)
- [useKeyboard](./references/use-keyboard.md)
- [useLongPress](./references/use-long-press.md)
- [useMove](./references/use-move.md)
- [usePress](./references/use-press.md)

### Feedback And Structure

- [useMeter](./references/use-meter.md)
- [useProgressBar](./references/use-progress-bar.md)
- [useSeparator](./references/use-separator.md)
- [useToast](./references/use-toast.md)
- [useToastRegion](./references/use-toast-region.md)
- [useToastState](./references/use-toast-state.md)

### Inputs

- [useButton](./references/use-button.md)
- [useCheckbox](./references/use-checkbox.md)
- [useCheckboxGroup](./references/use-checkbox-group.md)
- [useCheckboxGroupItem](./references/use-checkbox-group-item.md)
- [useCheckboxGroupState](./references/use-checkbox-group-state.md)
- [useNumberField](./references/use-number-field.md)
- [useNumberFieldState](./references/use-number-field-state.md)
- [useRadio](./references/use-radio.md)
- [useRadioGroup](./references/use-radio-group.md)
- [useRadioGroupState](./references/use-radio-group-state.md)
- [useSearchField](./references/use-search-field.md)
- [useSearchFieldState](./references/use-search-field-state.md)
- [useSlider](./references/use-slider.md)
- [useSliderState](./references/use-slider-state.md)
- [useSliderThumb](./references/use-slider-thumb.md)
- [useSwitch](./references/use-switch.md)
- [useTextField](./references/use-text-field.md)
- [useToggleButton](./references/use-toggle-button.md)
- [useToggleButtonGroup](./references/use-toggle-button-group.md)
- [useToggleButtonGroupItem](./references/use-toggle-button-group-item.md)
- [useToggleState](./references/use-toggle-state.md)

### Navigation

- [useBreadcrumbItem](./references/use-breadcrumb-item.md)
- [useBreadcrumbs](./references/use-breadcrumbs.md)
- [useLink](./references/use-link.md)
- [useTab](./references/use-tab.md)
- [useTabPanel](./references/use-tab-panel.md)
- [useToolbar](./references/use-toolbar.md)

### Overlays And Disclosure

- [useDialog](./references/use-dialog.md)
- [useDisclosure](./references/use-disclosure.md)
- [useDisclosureGroupState](./references/use-disclosure-group-state.md)
- [useDisclosureState](./references/use-disclosure-state.md)
- [useModalOverlay](./references/use-modal-overlay.md)
- [useOverlayTriggerState](./references/use-overlay-trigger-state.md)
- [usePopover](./references/use-popover.md)
- [useTooltip](./references/use-tooltip.md)
- [useTooltipTrigger](./references/use-tooltip-trigger.md)
- [useTooltipTriggerState](./references/use-tooltip-trigger-state.md)

### Utility Hooks And Helpers

- [DismissButton](./references/dismiss-button.md)
- [FocusRing](./references/focus-ring.md)
- [FocusScope](./references/focus-scope.md)
- [HiddenSelect](./references/hidden-select.md)
- [Overlay](./references/overlay.md)
- [VisuallyHidden](./references/visually-hidden.md)
- [mergeProps](./references/merge-props.md)
- [useField](./references/use-field.md)
- [useId](./references/use-id.md)
- [useLabel](./references/use-label.md)
- [useLandmark](./references/use-landmark.md)
- [useObjectRef](./references/use-object-ref.md)
- [useVisuallyHidden](./references/use-visually-hidden.md)

## Review Gate

- Do not remove returned props, refs, ids, or event handlers unless the replacement preserves the same accessibility contract.
- Do not split parent and item hooks across unrelated state owners.
- Do not replace React Aria collection, overlay, date, color, or drag-and-drop behavior with custom DOM event code unless the hook cannot model the product requirement.
- Reject React Aria usage that does not clearly replace custom ARIA, focus, keyboard, collection, overlay, form, or cross-input interaction logic.
- Do not use React Aria i18n or SSR utilities in this skill.
- Do not omit `Overlay`, `DismissButton`, `HiddenSelect`, `FocusScope`, or `VisuallyHidden` when the hook pattern needs the accessibility behavior those helpers provide.
- Recheck the hook reference before changing controlled props, selection behavior, validation, date value handling, virtualization, drag payloads, or overlay dismissal.
