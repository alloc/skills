# Vanilla Motion values

Use vanilla Motion values for high-frequency animated state outside React hooks. They track state, velocity, subscriptions, and active animations without causing React renders.

```js
import {
  animate,
  mapValue,
  motionValue,
  springValue,
  styleEffect,
  transformValue,
} from "motion"

const x = motionValue(0)
const opacity = mapValue(x, [-100, 0, 100], [0, 1, 0])

styleEffect(".item", { x, opacity })
animate(x, 100)
```

Core `motionValue` methods:

- `get()`: read the latest state.
- `getVelocity()`: read velocity for number-like values.
- `set(value)`: update state and preserve continuity.
- `jump(value)`: update state, reset velocity, and stop active animations.
- `isAnimating()`: check active animation state.
- `stop()`: stop the active animation.
- `on(event, callback)`: subscribe to `change`, `animationStart`, `animationCancel`, or `animationComplete`.
- `destroy()`: clean up subscribers.

`mapValue(input, inputRange, outputRange, options?)` creates a read-only value mapped from a numerical Motion value. Input and output ranges must have matching lengths; output can be numbers, colors, or complex strings with matching shapes. Use `{ clamp: false }` for unclamped interpolation.

`springValue(valueOrMotionValue, options?)` creates a Motion value that follows updates with a physics spring. Prefer `stiffness`, `damping`, and `mass` for responsive values because they incorporate velocity.

`transformValue(() => output)` computes a read-only Motion value from any Motion values read with `.get()` inside the callback.

```js
const blur = motionValue(0)
const filter = transformValue(() => `blur(${blur.get()}px)`)

styleEffect("img", { filter })
```
