# Reduce Motion React bundle size

Prefer importing only what you use from `motion/react`. For advanced bundle control, use `LazyMotion` with a feature bundle and `m` components.

```tsx
import { LazyMotion, domAnimation, m } from "motion/react"

<LazyMotion features={domAnimation}>
  <m.div animate={{ opacity: 1 }} />
</LazyMotion>
```

Use the smallest feature bundle that supports required animations and gestures. Keep `LazyMotion` near the app root when many children share it.
