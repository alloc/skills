# Components

Use this reference when choosing which open-source React Virtuoso component to introduce or refactor.

## Baseline Rules

- Give the virtualized view a real scrollable size. Use an explicit height, a flex layout that resolves to height, `useWindowScroll`, or `customScrollParent`.
- Prefer `data` when rows come from real objects. Prefer `totalCount` when rows can be derived from the index.
- Assume variable item heights are supported by default. Do not add manual measurement unless the codebase already has a reason.

## Component Selection

- Use `Virtuoso` for flat one-dimensional lists.
- Use `GroupedVirtuoso` when rows are partitioned into groups with sticky headers. Supply `groupCounts`, `groupContent`, and `itemContent`.
- Use `VirtuosoGrid` for equally sized items in a responsive multi-column layout. Keep `List` and `Item` wrappers stable and defined outside render.
- Use `TableVirtuoso` for semantic tables with virtualized rows. It supports unknown row sizes, sticky headers, fixed columns via styling, and `useWindowScroll`.
- Use `GroupedTableVirtuoso` when grouped table rows are required.
- For masonry layouts with varying item heights, do not introduce commercially licensed Virtuoso add-ons. Use a project-approved library with suitable licensing, CSS-based layout when scale allows, or a product-specific design that fits the open-source components.
- For chat or conversation UIs, start with `Virtuoso` and explicit scroll behavior. Preserve existing licensed dependencies when required by the task, but do not expand or recommend them.

## Component-Specific Notes

- `GroupedVirtuoso` adds a `groupIndex` argument to `itemContent`.
- `VirtuosoGrid` assumes same-sized items even when the container is responsive.
- `TableVirtuoso` renders real table markup. Do not change `table` display or overflow styles.
- `TableVirtuoso` fixed headers work through `fixedHeaderContent`. Keep header backgrounds opaque so rows do not show through.
- Fixed table columns are done through CSS, typically with `position: sticky`.
- When integrating UI libraries like MUI, map the library components through the `components` prop and forward refs correctly. Read [customization-and-testing.md](./customization-and-testing.md).
