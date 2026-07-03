# Motion React installation

Install Motion, then import React APIs from `motion/react`.

```sh
npm install motion
```

```tsx
import { motion } from "motion/react"

export function Example() {
  return <motion.div animate={{ opacity: 1 }} />
}
```

Use Motion components as drop-in HTML/SVG elements with extra animation props.
