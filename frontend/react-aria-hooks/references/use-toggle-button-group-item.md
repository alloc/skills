# useToggleButtonGroupItem

Source: https://react-aria.adobe.com/ToggleButtonGroup/useToggleButtonGroup.html

## Import

- Package: `react-aria`
- Import: `import {useToggleButtonGroupItem} from 'react-aria'`
- Install: `yarn add react-aria`
- Source version: 3.50.0
- Documented on upstream page: `useToggleButtonGroup`

## Signature

```ts
useToggleButtonGroupItem(props: AriaToggleButtonGroupItemOptions<ElementType>, state: ToggleGroupState, ref: RefObject<any>): ToggleButtonAria<HTMLAttributes<any>>
```

## Use For

Use `useToggleButtonGroupItem` for the toggle button group item part of the `useToggleButtonGroup` pattern.

## Source Highlights

- **Accessible** - Represented as an ARIA [radiogroup](https://www.w3.org/WAI/ARIA/apg/patterns/radio/) when using single selection, or a [toolbar](https://www.w3.org/WAI/ARIA/apg/patterns/toolbar/) when using multiple selection.
- **Keyboard navigation** - Users can navigate between buttons with the arrow keys. Selection can be toggled using the Enter or Space keys.
- **Styleable** - Hover, press, keyboard focus, and selection states are provided for easy styling.

## Implementation Guidance

- Spread every returned `*Props` object onto the exact DOM slot it names; these props carry ARIA attributes, event handlers, ids, and keyboard behavior.
- Pass the ref for the rendered DOM element into the hook and attach that same ref to the element receiving the returned props.
- Create the matching `react-stately` state object once in the owning component and pass that same state to related item, cell, or trigger hooks.
- Preserve user-provided labels and descriptions; icon-only controls still need `aria-label` or `aria-labelledby`.
- Render item-level hooks inside the parent collection/control and pass the parent state or item data from the same render pass.

## Related Hooks From The Same Source Page

- [useToggleButtonGroup](./use-toggle-button-group.md)

## Upstream Sections To Recheck

- Features
- Anatomy
- Example
- Selection
- Disabled
- Orientation
- Accessibility
