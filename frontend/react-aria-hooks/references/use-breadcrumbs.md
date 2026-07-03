# useBreadcrumbs

Source: https://react-aria.adobe.com/Breadcrumbs/useBreadcrumbs.html

## Import

- Package: `react-aria`
- Import: `import {useBreadcrumbs} from 'react-aria'`
- Install: `yarn add react-aria`
- Source version: 3.50.0

## Signature

```ts
useBreadcrumbs(props: AriaBreadcrumbsProps): BreadcrumbsAria
```

## Use For

Provides the behavior and accessibility implementation for a breadcrumbs component. Breadcrumbs display a hierarchy of links to the current page or resource in an application.

## Source Highlights

- Support for mouse, touch, and keyboard interactions on breadcrumbs
- Support for navigation links via `<a>` elements or custom element types via ARIA
- Localized ARIA labeling support for landmark navigation region
- Support for disabled breadcrumbs

## Implementation Guidance

- Spread every returned `*Props` object onto the exact DOM slot it names; these props carry ARIA attributes, event handlers, ids, and keyboard behavior.
- Preserve user-provided labels and descriptions; icon-only controls still need `aria-label` or `aria-labelledby`.

## Related Hooks From The Same Source Page

- [useBreadcrumbItem](./use-breadcrumb-item.md)

## Upstream Sections To Recheck

- Features
- Anatomy
- Example
- Navigation links
- Usage
