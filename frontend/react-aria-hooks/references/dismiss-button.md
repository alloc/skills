# DismissButton

Source: https://github.com/adobe/react-spectrum/blob/main/packages/react-aria/src/overlays/DismissButton.tsx

## Import

- Import: `import {DismissButton} from 'react-aria'`

## API Shape

```ts
interface DismissButtonProps {
  onDismiss?: () => void;
  // also accepts ARIA labeling and DOM id props
}
```

## Use For

Use `DismissButton` as a visually hidden dismiss affordance for modals and popups that otherwise have no visible close control for screen-reader users.

## Implementation Guidance

- Place dismiss buttons at the start and end of popover/dialog content when following React Aria popover examples.
- Wire `onDismiss` to the same state close function used by the overlay trigger state.
- Use Lingui for custom `aria-label` or `aria-labelledby` values when the default hidden label is not appropriate.
