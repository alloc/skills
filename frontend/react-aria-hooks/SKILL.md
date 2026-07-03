---
name: react-aria-hooks
description: Use React Aria and React Stately hooks to build accessible custom React components, including choosing the right hook, wiring refs/state/props, preserving ARIA and keyboard behavior, excluding React Aria i18n and SSR utilities, and checking hook-specific guidance in bundled category docs.
---

# React Aria Hooks

Use React Aria hooks as the owner of accessibility semantics, keyboard behavior, focus management, collection navigation, overlays, drag and drop, and date, time, and color interactions. Use React Stately hooks as the owner of state machines, collection state, selection, validation, queues, and async list data.

## Excluded React Aria Features

- Do not include React Aria SSR utilities such as `SSRProvider`, `useIsSSR`, or SSR-specific id wiring.
- Do not include React Aria i18n utilities such as `I18nProvider`, `useLocale`, `useDateFormatter`, `useNumberFormatter`, `useCollator`, or `useFilter`.
- Pass application-prepared labels, descriptions, validation text, and formatted values into React Aria props when user-facing copy is needed.
- React Aria internal accessibility strings for generic hidden controls are acceptable; do not add React Aria i18n providers or formatting hooks.

## Use React Aria Only When It Pays For It

Start with native HTML, existing app components, and ordinary React state. Reach for React Aria hooks only when they clearly remove or centralize nontrivial accessibility or interaction logic.

Treat the benefit as measurable: the hook should delete custom code, prevent duplicated behavior, or replace a fragile interaction contract with a maintained React Aria contract.

Use a React Aria API when it owns at least one behavior that would otherwise be easy to get wrong:

- ARIA relationships, labels, descriptions, or invalid state across multiple elements.
- Keyboard navigation beyond native browser behavior.
- Focus containment, restoration, roving focus, or focus-visible behavior.
- Collection semantics, item keys, selection managers, disabled items, or virtualized collection integration.
- Overlay dismissal, portal focus behavior, hidden dismiss controls, or outside interaction handling.
- Cross-input press, drag, drop, long-press, move, hover, or clipboard behavior.
- Hidden native form integration, browser autofill, native validation, or FormData support.

Do not add React Aria when it only wraps behavior the platform already handles well, such as a plain `<button>`, `<a>`, `<input>`, `<textarea>`, or `<select>` with no custom interaction model.

Before adding a hook, name the behavior it will own and the custom code it replaces. If that list is empty or vague, do not use the hook.

## Workflow

1. Identify the component pattern and read the matching category selector before implementing or changing behavior.
2. Use the hook pair the docs expect: behavior hooks from `react-aria`, state hooks from `react-stately`, and date values from `@internationalized/date` where date and time hooks require them.
3. Read helper references before using low-level utilities: `mergeProps`, focus helpers, `VisuallyHidden`, `Overlay`, `DismissButton`, and `HiddenSelect`.
4. Spread every returned props object onto the named DOM slot, attach the same ref passed into the hook, and merge props with existing app handlers instead of overwriting them.
5. Keep labels, descriptions, validation state, disabled state, ids, and relationships wired through the hook props. Do not hand-roll ARIA attributes when the hook returns them.
6. For collections, render from the React Stately collection/state APIs and pass the same state to parent and item hooks. Keep item keys stable.
7. For overlays and triggers, keep trigger props, overlay props, dismissal behavior, focus restoration, and portal placement together.
8. Validate with keyboard, pointer, touch where relevant, screen-reader naming, focus order, disabled/invalid states, and controlled/uncontrolled state behavior.

## Reference Navigation

Use these selector pages first. Each page lists the APIs in that category with a short "consider when" summary so you can choose without opening every detailed API file.

- [Decision and composition](./decision-and-composition/index.md): read before adding React Aria, or when composing returned props, refs, ids, hidden content, or low-level utility behavior.
- [Forms and field controls](./forms-and-field-controls/index.md): read when building custom buttons, inputs, labels, validation, descriptions, hidden native form integration, sliders, toggles, checkboxes, radios, or switches.
- [Collections and selection](./collections-and-selection/index.md): read when rendering item collections, option lists, menus, selects, comboboxes, tables, grids, trees, tags, async data, disabled keys, keyboard collection navigation, or selection state.
- [Overlays and disclosure](./overlays-and-disclosure/index.md): read when implementing popovers, modal overlays, dialogs, tooltips, disclosures, outside dismissal, focus restoration, portal behavior, or hidden dismiss controls.
- [Focus and interactions](./focus-and-interactions/index.md): read when native events are not enough for focus-visible styling, focus-within state, keyboard handling, press, hover, long press, move gestures, or programmatic focus movement.
- [Drag, drop, and clipboard](./drag-drop-and-clipboard/index.md): read when building keyboard-accessible drag/drop, collection drag/drop, drop indicators, or copy/paste behavior for focusable custom elements.
- [Date, time, and color](./date-time-and-color/index.md): read when building date fields, calendars, time fields, date pickers, range calendars, color fields, color sliders, color wheels, color swatches, or color areas.
- [Navigation, structure, and feedback](./navigation-structure-feedback/index.md): read when adding breadcrumbs, links, tabs, toolbars, landmarks, separators, progress, meters, toast regions, or structural feedback widgets.

## Review Gate

- Do not remove returned props, refs, ids, or event handlers unless the replacement preserves the same accessibility contract.
- Do not split parent and item hooks across unrelated state owners.
- Do not replace React Aria collection, overlay, date, color, or drag-and-drop behavior with custom DOM event code unless the hook cannot model the product requirement.
- Reject React Aria usage that does not clearly replace custom ARIA, focus, keyboard, collection, overlay, form, or cross-input interaction logic.
- Do not use React Aria i18n or SSR utilities in this skill.
- Do not omit `Overlay`, `DismissButton`, `HiddenSelect`, `FocusScope`, or `VisuallyHidden` when the hook pattern needs the accessibility behavior those helpers provide.
- Recheck the hook reference before changing controlled props, selection behavior, validation, date value handling, virtualization, drag payloads, or overlay dismissal.
