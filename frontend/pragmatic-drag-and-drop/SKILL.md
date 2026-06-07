---
name: pragmatic-drag-and-drop
description: Build and debug Atlassian Pragmatic drag and drop core package experiences, including element, external, and text-selection adapters, draggables, drop targets, monitors, events, cleanup, React integration, and reorder utilities.
---

# Pragmatic Drag And Drop

Use this skill when a web codebase uses, adds, or debugs `@atlaskit/pragmatic-drag-and-drop`.

Pragmatic drag and drop is a vanilla TypeScript library. It provides adapter entry points for different drag entities, and the application owns rendering, state updates, styling, accessibility affordances, and framework lifecycle.

## Core Mental Model

A typical experience has these pieces:

1. An adapter import for the entity being dragged.
2. A `draggable()` registration for element drags, when the app creates draggable DOM elements.
3. One or more adapter-specific drop targets attached to DOM elements.
4. Optional monitors for global drag lifecycle handling.
5. Cleanup functions wired into the framework lifecycle.
6. App state updates in `onDrop`, often using `reorder()` for list movement.

Adapters are scoped by drag entity type:

- Element drags: `@atlaskit/pragmatic-drag-and-drop/element/adapter`
- External drags, such as files or text from outside the window: `@atlaskit/pragmatic-drag-and-drop/external/adapter`
- Text selection drags: `@atlaskit/pragmatic-drag-and-drop/text-selection/adapter`

Start with [references/core-api.md](references/core-api.md) for imports, event ordering, drop target rules, monitor behavior, and utilities.

## Default Implementation Guidance

- Import only the adapter and utility entry points you use; the package is split into optional entry points.
- Treat every `draggable`, `dropTargetFor*`, and `monitorFor*` return value as a required cleanup function.
- In React, register inside `useEffect` after confirming `ref.current` exists, and return the cleanup function from the effect.
- Use `combine()` when a component registers multiple draggables, drop targets, or monitors.
- Put stable application data in `getInitialData()` on draggables and `getData()` on drop targets; keep these functions pure and cheap.
- Use `once()` or precomputed data if `getData()` is expensive, because it can be called repeatedly while dragging.
- Make `canDrop()` explicit for permission, type, or state checks. Returning `false` removes only that target from consideration; parents or children may still accept the drop.
- Use `getIsSticky()` for list gaps or other cases where a previous drop target should remain active while the pointer is not directly over it.
- Read `location.current.dropTargets` in bubble order, with the innermost target first.
- In nested targets, check whether `location.current.dropTargets[0]?.element === self.element` when the parent needs to know whether it was the innermost accepted drop target.

## Minimal React Pattern

```tsx
import { useEffect, useRef } from 'react';
import { combine } from '@atlaskit/pragmatic-drag-and-drop/combine';
import {
  draggable,
  dropTargetForElements,
} from '@atlaskit/pragmatic-drag-and-drop/element/adapter';

export function Card({ id }: { id: string }) {
  const ref = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    const element = ref.current;
    if (!element) {
      return;
    }

    return combine(
      draggable({
        element,
        getInitialData: () => ({ type: 'card', id }),
      }),
      dropTargetForElements({
        element,
        canDrop: ({ source }) => source.data.type === 'card',
        getData: () => ({ type: 'card', id }),
      }),
    );
  }, [id]);

  return <div ref={ref}>{id}</div>;
}
```

## Events

Use events according to when DOM or state should change:

- `onGenerateDragPreview`: make DOM changes that must appear in the native drag preview.
- `onDragStart`: mark dragging state after the preview is captured.
- `onDropTargetChange`: respond to hierarchy changes; `onDragEnter` and `onDragLeave` are derived from this for drop targets.
- `onDrag`: handle high-fidelity pointer updates; it is throttled with `requestAnimationFrame`.
- `onDrop`: finalize state changes. It fires when the operation ends, including cancel/error recovery cases.

Event order is always drag source, then drop targets from innermost to outermost, then monitors in creation order.

## Troubleshooting Shortcuts

- Duplicate warnings: ensure a DOM element is not registered twice as the same entity type of draggable or drop target.
- Drop handler fires on both child and parent: nested targets bubble by design; inspect `location.current.dropTargets[0]` to detect the innermost target.
- A monitor fires too often: add `canMonitor()` to opt in only once per matching drag operation.
- A newly created monitor misses the current event: monitors added during an event start on subsequent events.
- Drop target data is stale while sticky: sticky targets preserve the last computed data and drop effect until they are actively dragged over again.
- React remounts during drag: reconciliation treats a removed and re-added registration on the same element as the same piece during the active operation, but prefer stable effects and functional state updates where possible.
- File drops open the browser: use `preventUnhandled.start()` from a relevant external monitor for each drag operation that should block unhandled native drop behavior.

## Decision Rules

- Read [references/core-api.md](references/core-api.md) before changing adapter imports, draggable/drop target setup, monitors, event handlers, sticky behavior, or utilities.
- Prefer core package APIs before optional Pragmatic drag and drop packages unless the project already uses an optional package for hitboxes, indicators, accessibility, or auto-scroll.
- Keep framework wrappers thin. The core package works on DOM elements and cleanup functions; avoid hiding adapter semantics behind abstractions unless the codebase already has that pattern.
