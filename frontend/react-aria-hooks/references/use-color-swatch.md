# useColorSwatch

Source: https://react-aria.adobe.com/ColorSwatch/useColorSwatch.html

## Import

- Package: `react-aria`
- Import: `import {useColorSwatch} from 'react-aria'`
- Install: `yarn add react-aria`
- Source version: 3.50.0

## Signature

```ts
useColorSwatch(props: AriaColorSwatchProps): ColorSwatchAria
```

## Use For

Provides the accessibility implementation for a color swatch component. A color swatch displays a preview of a selected color.

## Source Highlights

- **Accessible** - Includes a localized color description for screen reader users (e.g. "dark vibrant blue"). Uses the [img](https://w3c.github.io/aria/#img) role with a custom `aria-roledescription` of "color swatch".
- **International** - Accessible color description and role description are translated into over 30 languages.

## Implementation Guidance

- Spread every returned `*Props` object onto the exact DOM slot it names; these props carry ARIA attributes, event handlers, ids, and keyboard behavior.
- Preserve user-provided labels and descriptions; icon-only controls still need `aria-label` or `aria-labelledby`.

## Upstream Sections To Recheck

- Features
- Anatomy
- Example
- Usage
