# useClipboard

Source: https://react-aria.adobe.com/useClipboard

## Import

- Import: `import {useClipboard} from 'react-aria/useClipboard'`

## Signature

```ts
useClipboard(options: ClipboardProps): ClipboardResult
```

## Use For

Handles clipboard interactions for a focusable element. Supports items of multiple data types, and integrates with the operating system native clipboard.

## Implementation Guidance

- Use for keyboard-accessible copy/paste on focusable custom elements; pair with app-owned selection state and Lingui-translated user-facing labels.
- Prefer native text selection behavior when copying plain editable text is enough.

## Upstream Sections To Recheck

- Introduction
- Example
- Copy data
- Paste data
- Disabling copy and paste
