# useBreadcrumbItem

Source: https://react-aria.adobe.com/Breadcrumbs/useBreadcrumbs.html

## Import

- Package: `react-aria`
- Import: `import {useBreadcrumbItem} from 'react-aria'`
- Install: `yarn add react-aria`
- Source version: 3.50.0
- Documented on upstream page: `useBreadcrumbs`

## Signature

```ts
useBreadcrumbItem(props: AriaBreadcrumbItemProps, ref: RefObject<FocusableElement | null>): BreadcrumbItemAria
```

## Use For

Use `useBreadcrumbItem` for the breadcrumb item part of the `useBreadcrumbs` pattern. The upstream page describes the broader pattern as: Provides the behavior and accessibility implementation for a breadcrumbs component. Breadcrumbs display a hierarchy of links to the current page or resource in an application.

## Source Highlights

- Support for mouse, touch, and keyboard interactions on breadcrumbs
- Support for navigation links via `<a>` elements or custom element types via ARIA
- Localized ARIA labeling support for landmark navigation region
- Support for disabled breadcrumbs

## Implementation Guidance

- Spread every returned `*Props` object onto the exact DOM slot it names; these props carry ARIA attributes, event handlers, ids, and keyboard behavior.
- Pass the ref for the rendered DOM element into the hook and attach that same ref to the element receiving the returned props.
- Preserve user-provided labels and descriptions; icon-only controls still need `aria-label` or `aria-labelledby`.
- Render item-level hooks inside the parent collection/control and pass the parent state or item data from the same render pass.

## Related Hooks From The Same Source Page

- [useBreadcrumbs](./use-breadcrumbs.md)

## Upstream Sections To Recheck

- Features
- Anatomy
- Example
- Navigation links
- Usage
