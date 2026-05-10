---
name: radix-primitives
description: Work on React UI using Radix Primitives, including primitive choice, part structure, accessibility, `asChild`, state, portals, focus, keyboard behavior, styling, SSR, RTL, and overlays.
---

# radix-primitives

Use Radix as headless accessibility and interaction logic. Keep the documented part structure intact, let Radix own focus and keyboard behavior, and supply the functional CSS and app-level state only where needed.

## Start Here

- Inspect which primitive family is already in use, or which built-in pattern should replace a custom widget.
- Read [choose-a-primitive.md](./references/choose-a-primitive.md) before swapping primitives or inventing a new interaction pattern.
- Read [composition-styling-and-runtime.md](./references/composition-styling-and-runtime.md) before using `asChild`, wrapping primitives in design-system components, styling state, adding animation libraries, or touching SSR and RTL behavior.
- Read [overlays-menus-and-positioning.md](./references/overlays-menus-and-positioning.md) before editing `Dialog`, `AlertDialog`, `Popover`, `HoverCard`, `Tooltip`, `DropdownMenu`, `ContextMenu`, `Menubar`, `Toast`, or overlay positioning.
- Read [forms-selection-and-inputs.md](./references/forms-selection-and-inputs.md) before editing `Form`, `Label`, `Checkbox`, `RadioGroup`, `Switch`, `Slider`, `Select`, `Toggle`, `ToggleGroup`, or specialized auth fields.
- Read [layout-navigation-and-utilities.md](./references/layout-navigation-and-utilities.md) before editing `Accordion`, `Collapsible`, `Tabs`, `NavigationMenu`, `Toolbar`, `AspectRatio`, `Avatar`, `ScrollArea`, `Separator`, `Progress`, `Portal`, `AccessibleIcon`, `VisuallyHidden`, or `Direction.Provider`.

## Workflow

- Prefer the smallest primitive that matches the interaction and WAI-ARIA pattern.
- Preserve the part tree that Radix expects. When abstracting parts behind your own components, keep required pieces such as `Title`, `Description`, `Viewport`, `ItemText`, `Thumb`, `Indicator`, or `Arrow`.
- Default to uncontrolled props such as `defaultOpen`, `defaultValue`, or `defaultChecked` when app logic does not need to own state. Move to controlled props only when app state must drive the primitive.
- Treat `asChild` as a contract. The child must spread props, forward refs, and render an element that stays focusable and semantically correct.
- Keep visible labels and accessible names explicit. Check what screen readers will announce for dialogs, selects, switches, icon-only buttons, and custom triggers.
- Preserve focus, dismissal, and portal behavior when nesting overlays. Radix does not style overlays or manage z-index for you.
- Prefer Radix `data-*` attributes and exposed CSS custom properties for stateful styling, sizing, collision-aware animation, and swipe gestures before introducing manual DOM bookkeeping.

## Decision Rules

- Read [choose-a-primitive.md](./references/choose-a-primitive.md) first when the real question is which primitive or pattern the UI should use.
- Read [composition-styling-and-runtime.md](./references/composition-styling-and-runtime.md) first when the task mentions `asChild`, wrapper components, refs, stateful styling, animation libraries, portal containers, RTL, or hydration.
- Read [overlays-menus-and-positioning.md](./references/overlays-menus-and-positioning.md) first when the task changes overlay structure, trigger behavior, dismissal rules, menu composition, or popper-style placement.
- Read [forms-selection-and-inputs.md](./references/forms-selection-and-inputs.md) first when the task changes labels, validation, form submission, checked state, numeric ranges, or selected values.
- Read [layout-navigation-and-utilities.md](./references/layout-navigation-and-utilities.md) first when the task changes disclosure, in-place panel switching, app navigation, non-interactive layout primitives, or accessibility helper utilities.
