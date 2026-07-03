# Motion React upgrade guide

When migrating, update imports to the current package entrypoints:

```tsx
import { motion, AnimatePresence } from "motion/react"
```

Check changed APIs around package names, feature bundles, and removed/deprecated props. Run typecheck after migration and update tests for timing-sensitive animations.
