# Overlay

Source: https://github.com/adobe/react-spectrum/blob/main/packages/react-aria/src/overlays/Overlay.tsx

## Import

- Import: `import {Overlay} from 'react-aria'`

## API Shape

```ts
interface OverlayProps {
  portalContainer?: Element;
  children: ReactNode;
  disableFocusManagement?: boolean;
  shouldContainFocus?: boolean;
  isExiting?: boolean;
}
```

## Use For

Use `Overlay` as the source-documented portal and focus-scope wrapper used by React Aria overlay examples. There does not appear to be a public docs page for it, but `usePopover`, `useModalOverlay`, `useMenu`, `useSelect`, `useComboBox`, and date picker examples render popup content through it.

## Implementation Guidance

- Use it for popup/modal content that should render in a portal and restore focus when it closes.
- Leave focus management enabled unless you are replacing focus containment and restoration yourself.
- Use `portalContainer` only when the app has a concrete portal root requirement; otherwise let it default to `document.body`.
- Do not introduce SSR handling around it; this skill excludes React Aria SSR utilities.
