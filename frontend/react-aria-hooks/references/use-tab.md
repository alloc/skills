# useTab

Source: https://react-aria.adobe.com/Tabs/useTabList.html

## Import

- Package: `react-aria`
- Import: `import {useTab} from 'react-aria'`
- Install: `yarn add react-aria`
- Source version: 3.50.0
- Documented on upstream page: `useTabList`

## Signature

```ts
useTab<T>(props: AriaTabProps, state: TabListState<T>, ref: RefObject<FocusableElement | null>): TabAria
```

## Use For

Use `useTab` for the tab part of the `useTabList` pattern. The upstream page describes the broader pattern as: Provides the behavior and accessibility implementation for a tab list. Tabs organize content into multiple sections and allow users to navigate between them.

## Source Highlights

- Support for mouse, touch, and keyboard interactions on tabs
- Support for LTR and RTL keyboard navigation
- Support for disabled tabs
- Follows the tabs ARIA pattern, semantically linking tabs and their associated tab panels
- Focus management for tab panels without any focusable children

## Implementation Guidance

- Spread every returned `*Props` object onto the exact DOM slot it names; these props carry ARIA attributes, event handlers, ids, and keyboard behavior.
- Pass the ref for the rendered DOM element into the hook and attach that same ref to the element receiving the returned props.
- Create the matching `react-stately` state object once in the owning component and pass that same state to related item, cell, or trigger hooks.
- Preserve user-provided labels and descriptions; icon-only controls still need `aria-label` or `aria-labelledby`.
- Render item-level hooks inside the parent collection/control and pass the parent state or item data from the same render pass.

## Related Hooks From The Same Source Page

- [useTabList](./use-tab-list.md)
- [useTabPanel](./use-tab-panel.md)

## Upstream Sections To Recheck

- Features
- Anatomy
- Example
- Styled examples
- Usage
