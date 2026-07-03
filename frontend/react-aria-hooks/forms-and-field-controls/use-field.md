# useField

Source: https://react-aria.adobe.com/useField

## Import

- Import: `import {useField} from 'react-aria/useField'`

## Signature

```ts
useField(props: AriaFieldProps): FieldAria
```

## Use For

Provides the accessibility implementation for input fields. Fields accept user input, gain context from their label, and may display a description or error message.

## Implementation Guidance

- Use for custom form controls that are not already covered by `useTextField`, `useSelect`, `useComboBox`, or another field hook.
- Prepare label, description, and error-message copy before passing it into React Aria props.

## Upstream Sections To Recheck

- Introduction
- Example
