# HiddenSelect

Source: https://github.com/adobe/react-spectrum/blob/main/packages/react-aria/src/select/HiddenSelect.tsx

## Import

- Import: `import {HiddenSelect} from 'react-aria'`

## API Shape

```ts
interface HiddenSelectProps<T, M extends SelectionMode = "single"> {
  state: SelectState<T, M>;
  triggerRef: RefObject<FocusableElement | null>;
  label?: ReactNode;
  name?: string;
  form?: string;
  isDisabled?: boolean;
}
```

## Use For

Use `HiddenSelect` with `useSelect` when the select must participate in browser autofill, mobile form navigation, native validation, FormData, or native HTML form submission.

## Implementation Guidance

- Pass the same `SelectState` and trigger ref used by `useSelect`.
- In SPA forms, add it for browser integration, not for server-post workflows by default.
- Keep `name`, `form`, `autoComplete`, disabled, required, and validation behavior aligned with the visible select control.
- For large collections, expect the implementation to fall back to hidden inputs rather than rendering every option in a hidden select.
