# Vanilla animate

Use `animate()` when an imperative animation is more direct than React props: one-off DOM effects, SVG path drawing, object/WebGL values, timelines, or playback controls.

```js
import { animate } from "motion"

const controls = animate(".item", { opacity: 1, y: 0 }, { duration: 0.3 })
controls.pause()
controls.play()
```

Import from `motion` for the hybrid API. Import from `motion/mini` for the smaller HTML/SVG style animator when independent transforms, CSS variables, SVG paths, objects, values, and sequences are not needed.

```js
import { animate } from "motion/mini"

animate(element, { opacity: 0.5 }, { duration: 0.2 })
```

The hybrid API can animate:

- HTML/SVG styles via selectors, elements, or element lists.
- Independent transforms like `x`, `y`, `scale`, `rotate`, and `skewX`.
- CSS variables and complex strings when the value shapes match.
- SVG draw properties: `pathLength`, `pathSpacing`, and `pathOffset`.
- Single values through `onUpdate`.
- Motion values and plain object properties, including Three.js object state.
- Timeline sequences.

```js
const sequence = [
  ["ul", { opacity: 1 }],
  ["li", { x: [-100, 0], opacity: [0, 1] }, { at: "-0.1" }],
]

animate(sequence, {
  defaultTransition: { duration: 0.25, ease: "easeOut" },
})
```

Use transition options like `duration`, `delay`, `ease`, `type`, `repeat`, `repeatType`, and per-value overrides. Sequence timing can use absolute seconds, labels, `"<"` for the previous segment start, and `"+0.2"` or `"-0.2"` offsets.

Controls expose `duration`, `time`, `speed`, `then`, `pause()`, `play()`, `complete()`, `cancel()`, and `stop()`. Prefer `stop()` when the final visual state should remain committed to the element.
