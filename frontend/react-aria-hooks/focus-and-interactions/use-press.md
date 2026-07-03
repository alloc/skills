# usePress

Source: https://react-aria.adobe.com/usePress

## Import

- Import: `import {usePress} from 'react-aria/usePress'`

## Signature

```ts
usePress(props: PressHookProps): PressResult
```

## Use For

Use when a custom interactive element needs button-like press behavior across mouse, touch, keyboard, and screen readers.

## Implementation Guidance

- Use for low-level press interactions; prefer `useButton`, `useLink`, or other semantic hooks when the element has a known role.
- Use `continuePropagation` only when nested press handling intentionally needs parent handlers.

## Upstream Sections To Recheck

- Features
