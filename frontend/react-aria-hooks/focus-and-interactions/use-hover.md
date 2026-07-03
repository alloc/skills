# useHover

Source: https://react-aria.adobe.com/useHover

## Import

- Import: `import {useHover} from 'react-aria/useHover'`

## Signature

```ts
useHover(props: HoverProps): HoverResult
```

## Use For

Use when hover behavior must ignore touch-emulated hover and compose pointer and mouse events consistently.

## Implementation Guidance

- Use for hover state only when hover changes behavior or styling; keep touch and keyboard behavior independent.

## Upstream Sections To Recheck

- Features
