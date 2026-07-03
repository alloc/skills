# useMenuItem

Source: https://react-aria.adobe.com/Menu/useMenu.html

## Import

- Package: `react-aria`
- Import: `import {useMenuItem} from 'react-aria'`
- Install: `yarn add react-aria`
- Source version: 3.50.0
- Documented on upstream page: `useMenu`

## Signature

```ts
useMenuItem<T>(props: AriaMenuItemProps, state: TreeState<T>, ref: RefObject<FocusableElement | null>): MenuItemAria
```

## Use For

Use `useMenuItem` for the menu item part of the `useMenu` pattern. The upstream page describes the broader pattern as: Provides the behavior and accessibility implementation for a menu component. A menu displays a list of actions or options that a user can choose.

## Source Highlights

- Exposed to assistive technology as a button with a `menu` using ARIA
- Support for single, multiple, or no selection
- Support for disabled items
- Support for sections
- Complex item labeling support for accessibility
- Keyboard navigation support including arrow keys, home/end, page up/down
- Automatic scrolling support during keyboard navigation
- Keyboard support for opening the menu using the arrow keys, including automatically focusing the first or last item accordingly

## Implementation Guidance

- Spread every returned `*Props` object onto the exact DOM slot it names; these props carry ARIA attributes, event handlers, ids, and keyboard behavior.
- Pass the ref for the rendered DOM element into the hook and attach that same ref to the element receiving the returned props.
- Create the matching `react-stately` state object once in the owning component and pass that same state to related item, cell, or trigger hooks.
- Preserve user-provided labels and descriptions; icon-only controls still need `aria-label` or `aria-labelledby`.
- Render item-level hooks inside the parent collection/control and pass the parent state or item data from the same render pass.
- Do not replace React Aria collection or selection managers with ad hoc arrays of DOM handlers; render from the collection/state APIs.

## Related Hooks From The Same Source Page

- [useMenuTrigger](./use-menu-trigger.md)
- [useMenu](./use-menu.md)
- [useMenuSection](./use-menu-section.md)

## Upstream Sections To Recheck

- Features
- Anatomy
- Example
- Styled examples
- Dynamic collections
- Selection
- Sections
- Complex menu items
- Disabled items
- Links
- Controlled open state
- Internationalization
