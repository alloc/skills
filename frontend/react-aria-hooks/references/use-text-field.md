# useTextField

Source: https://react-aria.adobe.com/TextField/useTextField.html

## Import

- Package: `react-aria`
- Import: `import {useTextField} from 'react-aria'`
- Install: `yarn add react-aria`
- Source version: 3.50.0

## Signature

```ts
useTextField<T extends TextFieldIntrinsicElements = DefaultElementType>(props: AriaTextFieldOptions<T>, ref: TextFieldRefObject<T>): TextFieldAria<T>
```

## Use For

Provides the behavior and accessibility implementation for a text field.

## Source Highlights

- Built with a native `<input>` or `<textarea>` element
- Visual and ARIA labeling support
- Change, clipboard, composition, selection, and input event support
- Support for native HTML constraint validation with customizable UI, custom validation functions, realtime validation, and server-side validation errors
- Support for description and error message help text linked to the input via ARIA

## Implementation Guidance

- Spread every returned `*Props` object onto the exact DOM slot it names; these props carry ARIA attributes, event handlers, ids, and keyboard behavior.
- Pass the ref for the rendered DOM element into the hook and attach that same ref to the element receiving the returned props.
- Preserve user-provided labels and descriptions; icon-only controls still need `aria-label` or `aria-labelledby`.

## Upstream Sections To Recheck

- Features
- Anatomy
- Example
- Usage
