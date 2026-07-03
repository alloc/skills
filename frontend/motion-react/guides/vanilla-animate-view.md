# Vanilla animateView

Use `animateView()` for DOM or page transitions that benefit from the browser View Transition API: full-page wipes, shared-element morphs across different DOM, and transitions outside React layout animation.

```js
import { animateView } from "motion"

function update() {
  container.classList.toggle("expanded")
}

animateView(update)
  .add(".card")
  .old({ opacity: 0 })
  .new({ opacity: 1 })
```

`animateView(update, options)` runs a synchronous or async DOM update function, then returns a chainable builder. In unsupported browsers, the DOM update still runs and the animation is skipped.

Common methods:

- `.add(target, newTarget?)`: opt elements into layout/shared-element animation. Targets can be selectors or elements.
- `.new(keyframes, options?)` and `.old(keyframes, options?)`: animate incoming and outgoing snapshots.
- `.enter(keyframes, options?)` and `.exit(keyframes, options?)`: animate appearing and leaving layers.
- `.layout(options?)`: override the targeted element's layout transition.
- `.crop(enabled?)`: control aspect-ratio cropping during morphs.
- `.group(enabled?)`: control whether layers nest under DOM ancestor layers.
- `.class(name)`: add a `view-transition-class` for CSS targeting.

```js
animateView(update, { duration: 0.5 })
  .add(".dialog")
  .exit({ clipPath: "inset(50%)" })
  .enter({ clipPath: "inset(0%)" })
```

`animateView` can animate CSS-animatable values on View Transition pseudo-elements. For custom properties or values like mask gradients, register CSS properties before animating them.

The builder is awaitable for controls:

```js
const animation = await animateView(update).add(".card")
animation.pause()
await animation.finished
```

View transitions are snapshot-based and generally one-at-a-time. Use React layout animation for interruptible component-level layout changes; use `animateView()` for page transitions, cross-DOM morphs, or filesize-constrained vanilla flows.
