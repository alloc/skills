# useMenuSection

Source: https://react-aria.adobe.com/Menu/useMenu.html

## Import

- Package: `react-aria`
- Import: `import {useMenuSection} from 'react-aria'`
- Install: `yarn add react-aria`
- Source version: 3.50.0
- Documented on upstream page: `useMenu`

## Signature

```ts
useMenuSection(props: AriaMenuSectionProps): MenuSectionAria
```

## Use For

Use `useMenuSection` for the menu section part of the `useMenu` pattern. The upstream page describes the broader pattern as: Provides the behavior and accessibility implementation for a menu component. A menu displays a list of actions or options that a user can choose.

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
- Preserve user-provided labels and descriptions; icon-only controls still need `aria-label` or `aria-labelledby`.
- Do not replace React Aria collection or selection managers with ad hoc arrays of DOM handlers; render from the collection/state APIs.

## Related Hooks From The Same Source Page

- [useMenuTrigger](./use-menu-trigger.md)
- [useMenu](./use-menu.md)
- [useMenuItem](./use-menu-item.md)

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
