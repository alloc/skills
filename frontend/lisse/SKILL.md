---
name: lisse
description: Use when building greenfield React SPA UI with Lisse (`@lisse/react` or `@lisse/core`) for Figma-style smooth/squircle corners, choosing `SmoothCorners` vs `useSmoothCorners`, configuring corner smoothing, borders, gradient borders, shadows, styling hooks, auto-effects, client-side path generation, performance, or limitations.
---

# Lisse

Use Lisse for React smooth corners that need to match Figma-style corner smoothing across browsers.

## Start Here

- Read [setup-and-api-choice.md](./references/setup-and-api-choice.md) before installing Lisse, choosing `SmoothCorners` vs `useSmoothCorners`, using `as` or `asChild`, or avoiding the component wrapper.
- Read [corners-and-core.md](./references/corners-and-core.md) before changing `radius`, `smoothing`, `preserveSmoothing`, per-corner options, or low-level path generation.
- Read [effects.md](./references/effects.md) before configuring borders, gradient borders, shadows, multiple shadows, auto-effects, or animated effect values.
- Read [styling.md](./references/styling.md) before styling with classes, `data-slot`, `data-state`, `border-radius`, `overflow-hidden`, or focus-ring CSS.
- Read [performance-and-limitations.md](./references/performance-and-limitations.md) before using many instances, animating smooth-cornered elements, debugging Safari animation cost, or working around clipping, outlines, overflow, scrollbars, and dynamic CSS effects.
- Read [recipes.md](./references/recipes.md) for compact React patterns for buttons, cards, and dialogs.

## Core Rules

- Prefer `@lisse/react` APIs in React component trees; use `@lisse/core` only for direct path generation or custom client-side DOM wiring.
- Use `SmoothCorners` for the normal case where an extra wrapper is acceptable and effects should work automatically.
- Use `useSmoothCorners` when the clipped element must keep exact DOM position, be a direct flex/grid child, or attach SVG effects to a specific ancestor.
- Treat `autoEffects` as mount-time extraction of CSS `border` and `box-shadow`, not as a reactive bridge for changing stylesheet values.
- Validate visual behavior when changing layout wrappers, effects, focus indicators, overflow, dimensions, or animation patterns.
