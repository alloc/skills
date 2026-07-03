# Vanilla hover

Use `hover()` for pointer hover behavior outside React event props. It filters emulated hover events from touch devices and automatically manages listeners.

```js
import { animate, hover } from "motion"

const cancelHover = hover(".button", (element, startEvent) => {
  const animation = animate(element, { scale: 1.05 })

  return (endEvent) => {
    animation.stop()
    animate(element, { scale: 1 })
  }
})
```

Targets can be a CSS selector, an element, or an element array. The start callback receives the hovered element and the triggering `PointerEvent`. If the callback returns a function, that function runs on hover end and receives the ending `PointerEvent`.

`hover()` returns a cleanup function. Call it when the owning view or integration unmounts.

```js
cancelHover()
```

Set `{ passive: false }` only when the callback must call `event.preventDefault()`.
