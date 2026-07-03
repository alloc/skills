# Motion React accessibility

Respect reduced-motion preferences. Use `useReducedMotion` to swap large movement for opacity/color changes, or configure globally:

```tsx
import { MotionConfig } from "motion/react"

<MotionConfig reducedMotion="user">{children}</MotionConfig>
```

Avoid essential information that is conveyed only through motion, keep focus states visible, and prefer transform/opacity animations that don't disrupt layout or reading position.
