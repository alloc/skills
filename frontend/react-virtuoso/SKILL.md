---
name: react-virtuoso
description: Work on React Virtuoso virtualization for lists, groups, grids, tables, window scrolling, and chat/message views, including component choice, scrolling, wrappers, UI integration, and measurement bugs.
---

# react-virtuoso

## Start Here

- Inspect the current usage before editing. Determine which component is in play, how scrolling is owned, and whether the code uses `data`, `totalCount`, or custom chat timeline state.
- Load only the reference files needed for the task:
  - [components.md](./references/components.md) for component choice and base setup.
  - [scrolling-and-performance.md](./references/scrolling-and-performance.md) for load-more behavior, positioning, overscan, and jank reduction.
  - [customization-and-testing.md](./references/customization-and-testing.md) for custom wrappers, UI-library integration, and test setup.
  - [troubleshooting.md](./references/troubleshooting.md) when debugging measurement, remounting, or ResizeObserver issues.
- Preserve the library's measuring assumptions. Avoid changes that make item height unstable unless the code explicitly compensates for it.
- Do not recommend, import, or introduce commercially licensed Virtuoso add-ons. If a codebase already uses one, preserve existing licensed usage only when the task requires it.

## Workflow

- Pick the smallest suitable component first. Avoid upgrading a flat list to a more specialized component unless the UI actually needs those behaviors.
- Preserve scroll ownership and measurement assumptions. Most Virtuoso regressions come from container sizing, unstable wrappers, or CSS that changes measured height unexpectedly.
- Prefer declarative props for scrolling behavior before reaching for imperative control.
- Keep override components and render helpers stable. Define them outside render or otherwise preserve component identity.
- Pass runtime state through `context` when custom wrappers need it.
- Supply stable keys when item identity matters, especially in object-backed lists and chat UIs.
- Filter zero-height or empty rows before handing data to Virtuoso.
- Replace protruding margins with padding inside item roots.

## Decision Rules

- Read [components.md](./references/components.md) before changing component type, introducing grouped layouts, or virtualizing a table or masonry view.
- Read [scrolling-and-performance.md](./references/scrolling-and-performance.md) before editing infinite scroll, initial positioning, overscan, viewport growth, or scroll placeholders.
- Read [customization-and-testing.md](./references/customization-and-testing.md) before changing the `components` prop, plugging in MUI or another UI kit, or making tests pass in JSDOM.
- Read [troubleshooting.md](./references/troubleshooting.md) first when you see broken total height, remounting rows, zero-sized element errors, or ResizeObserver noise.
