# useToastState

Source: https://react-aria.adobe.com/Toast/useToastState.html

## Import

- Package: `react-stately`
- Import: `import {useToastState} from 'react-stately'`
- Install: `yarn add react-stately`
- Source version: 3.48.0

## Signature

```ts
useToastState<T>(props: ToastStateProps): ToastState<T>
```

## Use For

Provides state management for a toast queue. Toasts display brief, temporary notifications of actions, errors, or other events in an application.

## Implementation Guidance

- Use this hook as the state owner for the matching React Aria behavior hook rather than recreating selection, open state, validation, or collection logic by hand.
- Keep keys stable across renders for collection items, especially when data can be inserted, removed, sorted, filtered, or loaded asynchronously.
- Use the hook result as the single source of truth for related child hooks and rendered collection items.

## Upstream Sections To Recheck

- Interface
- ToastQueue
- Example
