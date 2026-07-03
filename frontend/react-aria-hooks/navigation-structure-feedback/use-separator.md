# useSeparator

Source: https://react-aria.adobe.com/Separator/useSeparator.html

## Import

- Package: `react-aria`
- Import: `import {useSeparator} from 'react-aria'`
- Install: `yarn add react-aria`
- Source version: 3.50.0

## Signature

```ts
useSeparator(props: SeparatorProps): SeparatorAria
```

## Use For

Provides the accessibility implementation for a separator. A separator is a visual divider between two groups of content, e.g. groups of menu items or sections of a page.

## Source Highlights

- Support for horizontal and vertical orientation
- Support for HTML `<hr>` element or a custom element type

## Implementation Guidance

- Spread every returned `*Props` object onto the exact DOM slot it names; these props carry ARIA attributes, event handlers, ids, and keyboard behavior.
- Preserve user-provided labels and descriptions; icon-only controls still need `aria-label` or `aria-labelledby`.

## Upstream Sections To Recheck

- Features
- Anatomy
- Example
