# Vanilla press

Use `press()` for accessible press gestures outside React event props. It filters secondary pointer events and makes pressed elements keyboard accessible with focus and Enter.

```js
import { animate, press } from "motion"

const cancelPress = press("button", (element, startEvent) => {
  animate(element, { scale: 0.96 })

  return (endEvent, info) => {
    animate(element, { scale: 1 })
    if (info.success) submit()
  }
})
```

Targets can be a selector, element, or element array. The start callback receives the pressed element and the triggering `PointerEvent`. If it returns a function, the returned function runs when the gesture ends and receives `{ success }`.

`success` is `true` when the press completes like a click, and `false` when it is cancelled by ending outside the element or by keyboard blur.

Options:

- `passive`: defaults to `true`; set `false` only when calling `preventDefault()`.
- `once`: fire only once per matched element.

Call the returned cleanup function when the gesture should be removed.
