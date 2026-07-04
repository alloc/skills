# SSR and Core API

Source wiki pages: `SSR-Support.md`, `API-Reference.md`, `Type-Reference.md`, `Getting-Started.md`.

Use `@lisse/core/path` when code must run without DOM APIs.

```ts
import { generatePath, generateClipPath } from "@lisse/core/path";
```

The `/path` subpath includes pure path generation, constants, and types. It excludes DOM helpers such as `createSvgEffects`, `createDropShadow`, `observeResize`, `extractAndStripEffects`, `restoreStyles`, and position-management helpers.

## Next.js and React SSR

The React package is client-only. Use `SmoothCorners` and `useSmoothCorners` in Client Components.

For static server-rendered paths, dimensions must be known ahead of time:

```tsx
// Server Component
import { generateClipPath } from "@lisse/core/path";

export default function Page() {
  const clipPath = generateClipPath(200, 100, { radius: 20, smoothing: 0.6 });

  return (
    <div style={{ width: 200, height: 100, clipPath }}>
      Server-rendered smooth corners
    </div>
  );
}
```

Server-generated clip paths are static. Responsive elements still need client-side measurement through `SmoothCorners`, `useSmoothCorners`, or custom `observeResize` wiring.

## Direct core APIs

Use `@lisse/core` in browser-only custom code:

```ts
import { generateClipPath, observeResize } from "@lisse/core";

const options = { radius: 24, smoothing: 0.6 };
const unobserve = observeResize(element, () => {
  const { width, height } = element.getBoundingClientRect();
  element.style.clipPath = generateClipPath(width, height, options);
});
```

Use `@lisse/core/path` in Node, edge runtimes, tests without DOM, or code that should avoid pulling DOM helpers into the bundle.

## Useful exported types

```ts
import type {
  SmoothCornerOptions,
  CornerConfig,
  PerCornerConfig,
  BorderConfig,
  ShadowConfig,
  EffectsConfig,
  GradientConfig,
} from "@lisse/react";
```

`@lisse/react` re-exports core types for React code. Import from `@lisse/core` or `@lisse/core/path` when a package should not depend on React.
