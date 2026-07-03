# useId

Source: https://react-aria.adobe.com/useId

## Import

- Import: `import {useId} from 'react-aria/useId'`

## Signature

```ts
useId(defaultId?: string): string
```

## Use For

Use `useId` to create a stable id for ARIA relationships when callers have not provided one.

## Implementation Guidance

- Use for stable ARIA relationships in SPA components when no app-provided id exists.
- Do not add SSRProvider; this skill assumes SPA-only apps.

## Upstream Sections To Recheck

- Introduction
- Example
