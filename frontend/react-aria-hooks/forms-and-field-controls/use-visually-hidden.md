# useVisuallyHidden

Source: https://react-aria.adobe.com/VisuallyHidden

## Import

- Import: `import {useVisuallyHidden} from 'react-aria/VisuallyHidden'`

## Signature

```ts
useVisuallyHidden(props: VisuallyHiddenProps): VisuallyHiddenAria
```

## Use For

VisuallyHidden hides its children visually, while keeping content visible to screen readers. ``` import {VisuallyHidden} from 'react-aria/VisuallyHidden'; <VisuallyHidden>I am hidden</VisuallyHidden> ``` ### Positioning VisuallyHidden is positioned absolutely, so it must have a `position: relative` or `position: absolute` ancestor. Otherwise, undesired scrollbars may appear.

## Implementation Guidance

- Use when the element must be rendered directly rather than wrapped by `VisuallyHidden`.
- Spread `visuallyHiddenProps` onto the element that should remain screen-reader accessible but visually clipped.

## Upstream Sections To Recheck

- Example
