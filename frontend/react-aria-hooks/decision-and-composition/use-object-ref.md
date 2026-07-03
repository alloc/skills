# useObjectRef

Source: https://react-aria.adobe.com/useObjectRef

## Import

- Import: `import {useObjectRef} from 'react-aria/useObjectRef'`

## Signature

```ts
useObjectRef<T>(ref?: (instance: T | null) => () => void | void | MutableRefObject<T | null> | null): MutableRefObject<T | null>
```

## Use For

Offers an object ref for a given callback ref or an object ref. Especially helfpul when passing forwarded refs (created using `React.forwardRef`) to React Aria hooks.

## Implementation Guidance

- Use when a hook needs an object ref but component callers may pass callback refs.
- Prefer existing repo ref-forwarding patterns.

## Upstream Sections To Recheck

- Introduction
- Example
