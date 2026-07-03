# Vanilla scroll

Use `scroll()` for scroll-linked animations where progress should track scroll position directly. Use `inView()` for scroll-triggered enter/leave behavior.

```js
import { animate, scroll } from "motion"

const animation = animate(
  ".progress",
  { scaleX: [0, 1] },
  { ease: "linear" }
)

const cancel = scroll(animation)
```

`scroll()` can also receive a callback:

```js
scroll((progress, info) => {
  console.log(progress, info.y.velocity)
})
```

Key options:

- `container`: scroll container, defaulting to `window`.
- `axis`: `"y"` by default, or `"x"` for horizontal scroll.
- `target`: element whose progress is measured through the container.
- `offset`: intersections such as `["start end", "end start"]`, numbers, names, pixels, percentages, `vh`, or `vw`.
- `trackContentSize`: set `true` when changing content size should update scroll measurements before the next scroll event.

```js
scroll(animation, {
  container: document.querySelector(".carousel"),
  target: document.querySelector(".panel"),
  axis: "x",
  offset: ["start end", "end start"],
})
```

Use `position: sticky` for pinning effects so the browser handles the pinning path. Call the function returned by `scroll()` to stop tracking.
