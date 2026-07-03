# Focus and Interactions

Read when: native events are not enough for focus-visible styling, focus-within state, keyboard handling, press, hover, long press, move gestures, or programmatic focus movement.

Avoid when: Avoid these hooks when ordinary React event handlers and native focus behavior are sufficient and do not duplicate cross-input logic.

| API | Consider when |
| --- | --- |
| [FocusRing](./focus-ring.md) | Use when a wrapper component with focus CSS classes is simpler than manually wiring focus-visible state. |
| [useFocusManager](./use-focus-manager.md) | Use `useFocusManager` inside a `FocusScope` to move focus programmatically among focusable descendants, such as arrow-key navigation within a custom toolbar. |
| [useFocusRing](./use-focus-ring.md) | Determines whether a focus ring should be shown to indicate keyboard focus. |
| [useFocusVisible](./use-focus-visible.md) | Manages focus visible state for the page, and subscribes individual components for updates. |
| [useFocusWithin](./use-focus-within.md) | Use when a parent component needs focus enter/leave state for any descendant without duplicating child focus handlers. |
| [useFocus](./use-focus.md) | Use when a focusable element needs normalized focus and blur props that compose with React Aria event handling. |
| [useHover](./use-hover.md) | Use when hover behavior must ignore touch-emulated hover and compose pointer and mouse events consistently. |
| [useKeyboard](./use-keyboard.md) | Handles keyboard interactions for a focusable element. |
| [useLongPress](./use-long-press.md) | Use when an element needs an accessible long-press gesture across mouse, touch, keyboard, and screen readers. |
| [useMove](./use-move.md) | Use when a custom slider, color control, or draggable surface needs normalized move gestures across mouse, touch, and keyboard. |
| [usePress](./use-press.md) | Use when a custom interactive element needs button-like press behavior across mouse, touch, keyboard, and screen readers. |
