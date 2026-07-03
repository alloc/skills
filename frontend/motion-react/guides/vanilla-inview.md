# Vanilla inView

Use `inView()` for scroll-triggered work outside React hooks: enter animations, lazy loading, pausing offscreen animations, or starting/stopping videos.

```js
import { animate, inView } from "motion"

const stop = inView(".card", (element, entry) => {
  const animation = animate(element, { opacity: 1, y: 0 })

  return () => animation.stop()
})
```

Targets can be a selector, element, or element array. By default, the callback fires once when an element first enters the viewport. Returning a function makes detection continue and runs that function when the element leaves.

Options:

- `root`: scrollable parent element to use instead of the browser window.
- `margin`: viewport margin such as `"0px 100px 0px 0px"`.
- `amount`: `"some"`, `"all"`, or a number between `0` and `1`.

```js
const carousel = document.querySelector("#carousel")

inView("#carousel li", callback, {
  root: carousel,
  amount: 0.5,
})
```

Call the returned function to stop observation.
