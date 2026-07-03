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

- Use for stable ARIA relationships when no app-provided id exists.
- Do not add `SSRProvider`; this skill excludes React Aria SSR utilities.

## Upstream Sections To Recheck

- Introduction
- Example
