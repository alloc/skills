# Events, forms, and observers

## Native delegated events

Octane uses native, delegated DOM events (`onClick`, `onInput`, `onSubmit`) instead of a synthetic event layer — behavior matches the platform. There is no synthetic `onChange`.

### Text inputs: per-edit vs commit

Per-edit state uses the native `input` event:

```tsx
<input value={query} onInput={(event) => setQuery(event.currentTarget.value)} />
```

Native `change` fires when the browser commits an edit, usually on blur. An uncontrolled field that intentionally saves on commit keeps native `change` and marks that intent locally:

```tsx
<input
	defaultValue={savedDraft}
	onChange={(event) => save(event.currentTarget.value)}
	suppressNativeChangeWarning
/>
```

`suppressNativeChangeWarning` is a JS-only, non-serialized host hint that only silences `OCTANE_NATIVE_TEXT_ONCHANGE`; it does not alter event delivery. Never add it to hide a per-edit migration bug, and never add a noop `onInput` to silence the warning.

### The `OCTANE_NATIVE_TEXT_ONCHANGE` warning

A nonfatal authoring warning, not an event rewrite:

- The compiler reports direct `onChange`/`onChangeCapture` on a statically known text-entry `<input>` or `<textarea>` without a usable input handler.
- Development runtime checks cover unresolved spreads, dynamic types, and final props, reporting through `console.error` once per broken episode.
- Statically true `readOnly`/`disabled` controls are excluded.
- The fix for per-edit intent is the phase-preserving `onInput`/`onInputCapture` rename.
- Outside the warning, do not blanket-rename: selects, checkbox/radio/file and other non-text inputs, custom elements, and component/library callbacks named `onChange` are all out of scope.

## Controlled forms

`value`/`checked` on `<input>`/`<textarea>`/`<select>` follow React's controlled semantics exactly: the prop drives the DOM, rejected edits snap back, radio groups restore, `<select value>` selects the matching option. `defaultValue`/`defaultChecked` are the uncontrolled escape hatch. Handle per-edit text state with native `onInput`, not React's synthetic `onChange` convention.

### Checkbox and radio activation order

Activation follows the browser's native `click` → `input` → non-cancelable `change` order. Calling `preventDefault()` from native `onChange` cannot undo activation — cancel in `onClick` when rollback is intended. React's click-backed synthetic `onChange` can roll activation back; this cancellation timing is an intentional event-layer divergence even though controlled state restoration remains React-compatible.

## Observer callbacks

### ResizeObserver → `createResizeObserver`

Prefer `createResizeObserver(callback, realmCtor?)` from `octane` when resize callbacks set state, trigger layout updates, or write geometry. The callback receives native `ResizeObserverEntry` objects and the native observer in a separate task, coalescing to the latest entry per target, preserving ordinary automatic batching and synchronous initial measurements.

```ts
import { createResizeObserver, useLayoutEffect } from 'octane';

// Inside a component with a panelRef and setWidth state setter.
useLayoutEffect(() => {
	const element = panelRef.current;
	if (!element) return;
	const measure = () => setWidth(element.getBoundingClientRect().width);
	measure(); // required initial measurement stays synchronous
	const observer = createResizeObserver(measure);
	observer.observe(element);
	return () => observer.disconnect();
});
```

- Lifecycle ownership goes through the returned instance's `observe`, `unobserve`, `disconnect`. `unobserve(target)` removes that target's queued entries; `disconnect()` cancels queued delivery.
- The optional second argument is a `ResizeObserver` constructor from the observed element's realm, e.g. an iframe window.
- Nonconvergent size feedback still needs a bounded layout algorithm. Observers owned by a dependency need a library adapter that uses the helper; wrapping them yourself does not change their delivery.

### Other observers

`IntersectionObserver` already delivers callbacks in a separate task — leave it native. Preserve native `MutationObserver` microtask ordering: narrow its observed subtree and mutation types, and guard callbacks that mutate what they observe. Do not automatically wrap all observers.
