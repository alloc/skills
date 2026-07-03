# useTag

Source: https://react-aria.adobe.com/TagGroup/useTagGroup.html

## Import

- Package: `react-aria`
- Import: `import {useTag} from 'react-aria'`
- Install: `yarn add react-aria`
- Source version: 3.50.0
- Documented on upstream page: `useTagGroup`

## Signature

```ts
useTag<T>(props: AriaTagProps<T>, state: ListState<T>, ref: RefObject<FocusableElement | null>): TagAria
```

## Use For

Use `useTag` for the tag part of the `useTagGroup` pattern. The upstream page describes the broader pattern as: Provides the behavior and accessibility implementation for a tag group component. A tag group is a focusable list of labels, categories, keywords, filters, or other items, with support for keyboard navigation, selection, and removal.

## Source Highlights

- Exposed to assistive technology as a grid using ARIA
- Keyboard navigation support including arrow keys, home/end, page up/down, and delete
- Keyboard focus management and cross browser normalization
- Labeling support for accessibility
- Support for mouse, touch, and keyboard interactions

## Implementation Guidance

- Spread every returned `*Props` object onto the exact DOM slot it names; these props carry ARIA attributes, event handlers, ids, and keyboard behavior.
- Pass the ref for the rendered DOM element into the hook and attach that same ref to the element receiving the returned props.
- Create the matching `react-stately` state object once in the owning component and pass that same state to related item, cell, or trigger hooks.
- Preserve user-provided labels and descriptions; icon-only controls still need `aria-label` or `aria-labelledby`.
- Render item-level hooks inside the parent collection/control and pass the parent state or item data from the same render pass.

## Related Hooks From The Same Source Page

- [useTagGroup](./use-tag-group.md)

## Upstream Sections To Recheck

- Features
- Anatomy
- Example
- Styled examples
- Usage
