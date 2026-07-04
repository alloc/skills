# Migrations

## From `figma-squircle`

Use `@lisse/core` when replacing raw path generation:

```ts
import { generatePath, generateClipPath } from "@lisse/core";

const d = generatePath(width, height, {
  radius: cornerRadius,
  smoothing: cornerSmoothing,
});

const clipPath = generateClipPath(width, height, {
  radius: cornerRadius,
  smoothing: cornerSmoothing,
});
```

Key mapping:

| `figma-squircle` | Lisse |
|---|---|
| `getSvgPath({ width, height, cornerRadius, cornerSmoothing })` | `generatePath(width, height, { radius, smoothing })` |
| manual `path("...")` wrapping | `generateClipPath(width, height, options)` |
| `topLeftCornerRadius` | `topLeft` |
| `topRightCornerRadius` | `topRight` |
| `bottomRightCornerRadius` | `bottomRight` |
| `bottomLeftCornerRadius` | `bottomLeft` |

Important behavior difference: `figma-squircle` defaults `preserveSmoothing` to `false`; Lisse defaults it to `true`. Pass `preserveSmoothing: false` if matching existing shapes matters.

If a React component hand-wires `ResizeObserver` and `clipPath`, prefer `SmoothCorners` or `useSmoothCorners`:

```tsx
import { SmoothCorners } from "@lisse/react";

<SmoothCorners corners={{ radius: 24, smoothing: 0.6 }} className="bg-white p-6">
  Content
</SmoothCorners>
```

Use `@lisse/core/path` for SSR-safe path generation.

## From `corner-smoothing`

Map flattened props into the `corners` object:

| `corner-smoothing` | Lisse |
|---|---|
| `cornerRadius={20}` | `corners={{ radius: 20 }}` |
| `cornerSmoothing={0.6}` | `corners={{ radius: 20, smoothing: 0.6 }}` |
| `preserveSmoothing={true}` | `corners={{ radius: 20, preserveSmoothing: true }}` |
| `topLeftCornerRadius={40}` | `corners={{ topLeft: 40 }}` |
| `as="a"` | `as="a"` |

`corner-smoothing` defaults to maximum smoothing; Lisse defaults to `0.6`. Pass `smoothing: 1` to match that default.

Move border styling from wrapper/background tricks into explicit effects or let auto-effects extract plain CSS borders:

```tsx
<SmoothCorners
  corners={{ radius: 20, smoothing: 0.6 }}
  innerBorder={{ width: 1, color: "#e5e7eb", opacity: 1 }}
  className="bg-white p-6"
>
  Content
</SmoothCorners>
```

Watch for behavioral changes:

- Lisse injects SVG overlays for borders and shadows.
- Auto-effects are on by default and strip CSS `border` and `box-shadow` on mount.
- Lisse supports per-corner smoothing and layered shadows; existing CSS selectors may need checking if they assumed a different DOM shape.
