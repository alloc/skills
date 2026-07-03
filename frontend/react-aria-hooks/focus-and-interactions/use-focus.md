# useFocus

Source: https://react-aria.adobe.com/useFocus

## Import

- Import: `import {useFocus} from 'react-aria/useFocus'`

## Signature

```ts
useFocus<Target extends FocusableElement = FocusableElement>(props: FocusProps<Target>): FocusResult<Target>
```

## Use For

Use when a focusable element needs normalized focus and blur props that compose with React Aria event handling.

## Implementation Guidance

- Use for focus and blur events on a single element; use `useFocusWithin` for descendants and `useFocusRing` for visual focus indicators.

## Upstream Sections To Recheck

- Features
