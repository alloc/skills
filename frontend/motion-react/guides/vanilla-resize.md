# Vanilla resize

Use `resize()` to react to viewport or element size changes outside React measurement hooks. It uses shared `ResizeObserver` handling for element listeners.

```js
import { frame, resize } from "motion"

const stop = resize(".drawer", (element, { width, height }) => {
  frame.render(() => {
    element.style.setProperty("--drawer-height", `${height}px`)
  })
})
```

Pass only a callback to track viewport changes:

```js
resize(({ width, height }) => {
  console.log(width, height)
})
```

Pass an element or selector to track specific elements. The reported `width` and `height` are border-box dimensions.

Batch DOM writes with `frame.render()` when responding to measurements. Call the returned function to remove listeners; Motion stops observing elements when no listeners remain.
