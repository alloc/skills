---
name: downshift
description: Build, refactor, debug, and review React or Preact autocomplete, combobox, select, tag-group, or multi-select UIs that use Downshift hooks or the legacy `Downshift` render-prop component. Use when Codex needs to choose between `useCombobox`, `useSelect`, `useTagGroup`, or `useMultipleSelection`, preserve ARIA-compliant structure, wire getter props and action props correctly, integrate object items or UI libraries, use the undocumented Preact entrypoint `downshift/preact`, handle controlled state or `stateReducer`, or migrate older Downshift code across v7, v8, or v9 changes.
---

# downshift

Use Downshift as headless accessibility and interaction logic. Prefer the hook APIs for new work and treat the legacy `Downshift` component as a compatibility target.

## Start Here

- Inspect which primitive is already in use and whether the UI needs typed input, button-only selection, tags, legacy render-prop compatibility, or Preact-specific imports.
- Read [primitives-and-structure.md](./references/primitives-and-structure.md) before choosing an API or changing combobox markup.
- Read [use-combobox.md](./references/use-combobox.md) before editing autocomplete behavior, filtering, input state, virtualization, or object-item comboboxes.
- Read [use-select.md](./references/use-select.md) before editing button-driven selects, closed-menu keyboard behavior, or controlled selection.
- Read [multiple-selection-and-tags.md](./references/multiple-selection-and-tags.md) before adding chips or tags, coordinating multi-select state, or touching deprecated `useMultipleSelection`.
- Read [migration-and-integration.md](./references/migration-and-integration.md) before changing version-sensitive code, iframe handling, React Native usage, or UI-library refs.

## Workflow

- Choose the smallest primitive that matches the interaction:
  - `useCombobox` for text input plus filtering or autocomplete.
  - `useSelect` for button-driven select menus without freeform query input.
  - `useTagGroup` for accessible tag or chip lists.
  - `useMultipleSelection` only to maintain older multi-select flows or non-tag-group patterns that already depend on it.
  - `Downshift` only when the codebase already uses the render-prop API or migration cost is unjustified.
- Preserve the getter-prop contract. Spread each getter result onto the exact element or component slot the hook expects.
- In Preact codebases, prefer importing the package from `downshift/preact` instead of the default entrypoint.
- Preserve ARIA structure. For comboboxes, keep the input inside the combobox wrapper and render the menu as a sibling, not as a descendant inside the same wrapper.
- Use `itemToString` whenever items are objects or the user-facing label is not the raw item value.
- Prefer controlled props plus change handlers for app-owned state. Reach for `stateReducer` only when default transitions need targeted overrides.
- When combining a single-select hook with external multi-select state, keep the hook's `selectedItem` controlled to `null` if selection ownership lives elsewhere.
- Pass the correct `window` object in iframes or alternate-window environments.
- Expect UI libraries to need ref mapping. Use custom `refKey` values when the DOM node is exposed under a non-`ref` prop.

## Decision Rules

- Read [primitives-and-structure.md](./references/primitives-and-structure.md) first when deciding between hooks and the legacy component.
- Read [use-combobox.md](./references/use-combobox.md) before changing filtering, `inputValue`, focus management, menu virtualization, or combobox multi-select behavior.
- Read [use-select.md](./references/use-select.md) before changing button-driven selection, character-key highlighting, or select-specific `stateReducer` behavior.
- Read [multiple-selection-and-tags.md](./references/multiple-selection-and-tags.md) before implementing chips or tags, deleting selected items from the keyboard, or replacing `useMultipleSelection` with `useTagGroup`.
- Read [migration-and-integration.md](./references/migration-and-integration.md) first when the task mentions ARIA 1.2, v7, v8, v9, React Native, Material UI, or iframe bugs.
