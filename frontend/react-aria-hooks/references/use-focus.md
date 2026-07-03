# useFocus

Source: https://react-aria.adobe.com/useFocus

## Import

- Import: `import {useFocus} from 'react-aria/useFocus'`

## Signature

```ts
useFocus<Target extends FocusableElement = FocusableElement>(props: FocusProps<Target>): FocusResult<Target>
```

## Use For

Use `useFocus` for the React Aria behavior documented by the source page.

## Implementation Guidance

- Use for focus and blur events on a single element; use `useFocusWithin` for descendants and `useFocusRing` for visual focus indicators.

## Upstream Sections To Recheck

- Features
