# useLink

Source: https://react-aria.adobe.com/Link/useLink.html

## Import

- Package: `react-aria`
- Import: `import {useLink} from 'react-aria'`
- Install: `yarn add react-aria`
- Source version: 3.50.0

## Signature

```ts
useLink(props: AriaLinkOptions, ref: RefObject<FocusableElement | null>): LinkAria
```

## Use For

Provides the behavior and accessibility implementation for a link component. A link allows a user to navigate to another page or resource within a web page or application.

## Source Highlights

- Support for mouse, touch, and keyboard interactions
- Support for navigation links via `<a>` elements or custom element types via ARIA
- Support for disabled links

## Implementation Guidance

- Spread every returned `*Props` object onto the exact DOM slot it names; these props carry ARIA attributes, event handlers, ids, and keyboard behavior.
- Pass the ref for the rendered DOM element into the hook and attach that same ref to the element receiving the returned props.
- Preserve user-provided labels and descriptions; icon-only controls still need `aria-label` or `aria-labelledby`.

## Upstream Sections To Recheck

- Features
- Anatomy
- Example
- Client handled links
- Disabled links
