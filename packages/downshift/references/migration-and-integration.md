# Migration and integration notes

## Version checkpoints

- Downshift hook behavior changed in v7 to align `useCombobox` and `useSelect` with the ARIA 1.2 combobox pattern.
- v8 and v9 introduced additional breaking changes, including TypeScript changes.
- Before editing version-sensitive code, confirm the installed Downshift major version and compare it against any assumptions in the codebase.

## Migration posture

- Avoid mixing guidance from different major versions without checking the current package version.
- Expect older code to use the render-prop `Downshift` component or pre-v7 structure. Preserve behavior intentionally if you are fixing a bug rather than rewriting the surface.
- When the task is a migration, keep API choice and DOM structure changes separate from business-logic changes so regressions stay attributable.

## Material UI and similar libraries

- Spread getter props onto components that forward refs directly.
- When the real DOM node uses a custom ref prop, pass the correct `refKey` into the getter. The documented example is `getInputProps({ refKey: 'inputRef' })` for Material UI `Input`.
- Preserve focusable DOM nodes. Broken refs usually manifest as failed scrolling, focus jumps, or menus that stop tracking the active item.

## Alternate window contexts

- Pass the hook a custom `window` when the widget lives inside an iframe or another non-default browsing context.
- Do not rely on the global browser `window` in embedded contexts. Downshift uses the provided window for DOM-related behavior.

## Platform notes

- In Preact codebases, prefer the undocumented `downshift/preact` entrypoint.
- React Native keeps the same hook logic and interaction model, with native element replacements.
- Downshift supplies behavior and accessibility wiring, so visual rendering can change across platforms as long as the element mapping and focus behavior stay intact.
