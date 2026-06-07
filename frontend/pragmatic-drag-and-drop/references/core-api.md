# Pragmatic Drag And Drop Core API

Source material: Atlassian Design docs for Pragmatic drag and drop core package pages matching `**/core-package/**`.

## Installation And Entry Points

Install the core package:

```sh
yarn add @atlaskit/pragmatic-drag-and-drop
```

The package is split into entry points. Import the specific pieces the experience uses:

```ts
import {
  draggable,
  dropTargetForElements,
  monitorForElements,
} from '@atlaskit/pragmatic-drag-and-drop/element/adapter';

import {
  dropTargetForExternal,
  monitorForExternal,
} from '@atlaskit/pragmatic-drag-and-drop/external/adapter';

import {
  dropTargetForTextSelection,
  monitorForTextSelection,
} from '@atlaskit/pragmatic-drag-and-drop/text-selection/adapter';
```

Useful utility entry points:

```ts
import { combine } from '@atlaskit/pragmatic-drag-and-drop/combine';
import { once } from '@atlaskit/pragmatic-drag-and-drop/once';
import { reorder } from '@atlaskit/pragmatic-drag-and-drop/reorder';
import { preventUnhandled } from '@atlaskit/pragmatic-drag-and-drop/prevent-unhandled';
import type { CleanupFn } from '@atlaskit/pragmatic-drag-and-drop/types';
```

## Adapters

An adapter teaches the library how to handle a drag entity type:

- Element adapter: dragging app-owned DOM elements.
- External adapter: drag operations that start outside the current `window`, such as files or text from another application.
- Text selection adapter: dragging selected text in the document.

Adapters expose drop target registration and monitor creation. The element adapter also exposes `draggable()` to register a DOM element as a drag source.

## Draggables

`draggable({ element })` registers one `HTMLElement` as draggable and returns a cleanup function.

Rules:

- The key for a draggable is the DOM element.
- An element can only have one active draggable registration.
- Removing and re-adding a draggable on the same element during a drag is reconciled as the same draggable for that active operation.
- Prefer stable effect dependencies and functional state updates so React does not remount draggables unnecessarily.

Use `getInitialData()` to attach source data that downstream drop targets and monitors can inspect.

## Drop Targets

`dropTargetForElements`, `dropTargetForExternal`, and `dropTargetForTextSelection` attach adapter-specific drop behavior to an element and return cleanup functions.

Rules:

- Drop targets are scoped to entity type.
- One element can be a drop target for multiple entity types.
- One element cannot have two drop targets for the same entity type.
- Drop targets can be nested.
- During a drag, targets may be added, removed, remounted, or resized.

Important arguments:

- `element`: required DOM element.
- `getData(args)`: returns target data. It is called repeatedly while dragging over a target, so keep it pure and cheap.
- `canDrop(args)`: returns whether this target accepts the current drag. Returning `false` ignores this target only.
- `getDropEffect(args)`: controls the cursor/drop effect. With nesting, the innermost accepted target's drop effect wins.
- `getIsSticky(args)`: allows a previous target to remain active when the pointer is no longer directly over it.
- Event callbacks: `onGenerateDragPreview`, `onDragStart`, `onDrag`, `onDropTargetChange`, `onDrop`, plus derived `onDragEnter` and `onDragLeave` on drop targets.

Nested drop targets are ordered from innermost to outermost in `location.current.dropTargets`. For parent targets that need to know whether they were directly dropped on:

```ts
dropTargetForElements({
  element: parent,
  onDrop({ location, self }) {
    if (location.current.dropTargets[0]?.element === self.element) {
      handleDirectDrop();
      return;
    }

    handleNestedDrop();
  },
});
```

## Sticky Targets

Use `getIsSticky()` when a previous drop target should remain selected through pointer gaps.

Stickiness is preserved only when:

- The target is still mounted.
- `canDrop()` returns `true`.
- `getIsSticky()` returns `true`.
- The parent target is unchanged.

Sticky targets preserve the last computed `data` and `dropEffect`; these are not recomputed until the target is actively dragged over again.

## Monitors

Monitors listen to drag operation events anywhere and are not tied to an element.

```ts
const cleanup = monitorForElements({
  canMonitor: ({ source }) => source.data.type === 'card',
  onDragStart: ({ source }) => {
    console.log(source.data);
  },
});
```

Rules:

- Every monitor call creates a new independent monitor.
- Monitors fire after the drag source and drop targets.
- Monitors fire in creation order.
- `canMonitor()` is called once as a drag operation starts and opts the monitor into or out of that operation.
- A monitor added during an event is not called for the current event, but can receive later events.

## Events And Payloads

Available events:

- `onGenerateDragPreview`: before drag starts; DOM changes can be captured in the drag preview.
- `onDragStart`: drag has started; DOM changes are not captured in the preview.
- `onDropTargetChange`: active drop target hierarchy changed.
- `onDrag`: throttled high-fidelity drag updates.
- `onDrop`: drag operation ended.

Drop targets also expose derived `onDragEnter` and `onDragLeave` callbacks from `onDropTargetChange`.

Event order:

1. Drag source, when relevant.
2. Drop targets from innermost to outermost.
3. Monitors in creation order.

Shared payloads include:

- `location.initial`: drag start location.
- `location.current`: current input and bubble-ordered drop targets.
- `location.previous`: prior drop target state.
- `source`: adapter-specific source payload.
- `self`: drop-target convenience record with the target element, target data, and drop effect.

`onDrop` fires when the operation ends. The platform does not reliably distinguish a normal drop, cancel, drop on no target, or error recovery; inspect `location.current.dropTargets` for the final accepted targets.

## Utilities

`combine()` merges cleanup functions:

```ts
return combine(
  draggable({ element }),
  dropTargetForElements({ element }),
  monitorForElements({ onDrop: handleDrop }),
);
```

`once()` memoizes work that should only happen once:

```ts
const getDataOnce = once(getExpensiveData);

dropTargetForExternal({
  element,
  getData: () => getDataOnce(),
});
```

`reorder()` returns a new reordered array without mutating the original:

```ts
const next = reorder({
  list: items,
  startIndex,
  finishIndex,
});
```

`preventUnhandled.start()` blocks unhandled native drop behavior for the current drag operation. Call it for every drag operation where the behavior is needed, commonly from `monitorForExternal({ onDragStart })`. Use `preventUnhandled.stop()` to stop blocking during the active drag.

## TypeScript Types

The shared type entry point exports:

- `DropTargetRecord`
- `Position`
- `Input`
- `DragLocation`
- `DragLocationHistory`
- `CleanupFn`
- `AllDragTypes`
- `MonitorArgs`
- `BaseEventPayload`

Adapters also expose adapter-specific payload and argument types. Prefer inference for local handlers, and use explicit types only when sharing helpers across files.
