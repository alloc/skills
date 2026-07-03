# useToolbar

Source: https://react-aria.adobe.com/Toolbar/useToolbar.html

## Import

- Package: `@react-aria/toolbar`
- Import: `import {useToolbar} from '@react-aria/toolbar'`
- Install: `yarn add @react-aria/toolbar`
- Source version: 3.0.0-beta.26

## Signature

```ts
useToolbar(props: AriaToolbarProps, ref: RefObject<HTMLElement | null>): ToolbarAria
```

## Use For

Provides the behavior and accessibility implementation for a toolbar. A toolbar is a container for a set of interactive controls with arrow key navigation.

## Source Highlights

- Exposed to assistive technology as a `toolbar` element via ARIA
- Support for arrow key navigation
- Support for both horizontal and vertical orientations
- Support for interactive children including button, toggle button, menu, checkbox, and link
- Automatic scrolling support during keyboard navigation

## Implementation Guidance

- Spread every returned `*Props` object onto the exact DOM slot it names; these props carry ARIA attributes, event handlers, ids, and keyboard behavior.
- Pass the ref for the rendered DOM element into the hook and attach that same ref to the element receiving the returned props.
- Preserve user-provided labels and descriptions; icon-only controls still need `aria-label` or `aria-labelledby`.

## Upstream Sections To Recheck

- Features
- Anatomy
- Example
- Internationalization
