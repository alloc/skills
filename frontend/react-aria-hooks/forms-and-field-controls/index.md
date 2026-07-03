# Forms and Field Controls

Read when: building custom buttons, inputs, labels, validation, descriptions, hidden native form integration, sliders, toggles, checkboxes, radios, or switches.

Avoid when: Avoid these hooks for plain native form controls whose built-in label, validation, keyboard, and submission behavior already satisfy the requirement.

| API | Consider when |
| --- | --- |
| [HiddenSelect](./hidden-select.md) | Use with `useSelect` when a custom select needs browser autofill, mobile form navigation, native validation, FormData, or native form submission. |
| [useButton](./use-button.md) | Provides the behavior and accessibility implementation for a button component. |
| [useCheckboxGroupItem](./use-checkbox-group-item.md) | Use `useCheckboxGroupItem` for the checkbox group item part of the `useCheckboxGroup` pattern. |
| [useCheckboxGroupState](./use-checkbox-group-state.md) | Provides state management for a checkbox group component. |
| [useCheckboxGroup](./use-checkbox-group.md) | Provides the behavior and accessibility implementation for a checkbox group component. |
| [useCheckbox](./use-checkbox.md) | Provides the behavior and accessibility implementation for a checkbox component. |
| [useField](./use-field.md) | Provides the accessibility implementation for input fields. |
| [useLabel](./use-label.md) | Provides the accessibility implementation for labels and their associated elements. |
| [useNumberFieldState](./use-number-field-state.md) | Provides state management for a number field component. |
| [useNumberField](./use-number-field.md) | Provides the behavior and accessibility implementation for a number field component. |
| [useRadioGroupState](./use-radio-group-state.md) | Provides state management for a radio group component. |
| [useRadioGroup](./use-radio-group.md) | Provides the behavior and accessibility implementation for a radio group component. |
| [useRadio](./use-radio.md) | Use `useRadio` for the radio part of the `useRadioGroup` pattern. |
| [useSearchFieldState](./use-search-field-state.md) | Provides state management for a search field. |
| [useSearchField](./use-search-field.md) | Provides the behavior and accessibility implementation for a search field. |
| [useSliderState](./use-slider-state.md) | Provides state management for a slider component. |
| [useSliderThumb](./use-slider-thumb.md) | Use `useSliderThumb` for the slider thumb part of the `useSlider` pattern. |
| [useSlider](./use-slider.md) | Provides the behavior and accessibility implementation for a slider component representing one or more values. |
| [useSwitch](./use-switch.md) | Provides the behavior and accessibility implementation for a switch component. |
| [useTextField](./use-text-field.md) | Provides the behavior and accessibility implementation for a text field. |
| [useToggleButtonGroupItem](./use-toggle-button-group-item.md) | Use `useToggleButtonGroupItem` for the toggle button group item part of the `useToggleButtonGroup` pattern. |
| [useToggleButtonGroup](./use-toggle-button-group.md) | Use `useToggleButtonGroup` for the pattern documented in the upstream source page. |
| [useToggleButton](./use-toggle-button.md) | Provides the behavior and accessibility implementation for a toggle button component. |
| [useToggleState](./use-toggle-state.md) | Provides state management for toggle components like checkboxes and switches. |
| [useVisuallyHidden](./use-visually-hidden.md) | Use when an element must be visually hidden directly rather than wrapped by `VisuallyHidden`. |
| [VisuallyHidden](./visually-hidden.md) | Use when content must be visually hidden while remaining available to assistive technology. |
