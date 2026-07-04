# Corners and Core Path Generation

Lisse implements Figma-style smooth corners: cubic Bezier shoulders around a small circular arc, not CSS `corner-shape: squircle`'s superellipse family.

## Corner options

Uniform corners:

```tsx
<SmoothCorners corners={{ radius: 20, smoothing: 0.6 }}>
  Content
</SmoothCorners>
```

`smoothing` ranges from `0` to `1`:

- `0`: equivalent to circular `border-radius`.
- `0.6`: default, Figma-like and close to iOS continuous corners.
- `1`: maximum smoothing, with no circular arc segment left.

`preserveSmoothing` defaults to `true`. When a radius is too large for the element, `true` keeps the requested smoothing and reduces effective radius; `false` keeps more of the requested radius and reduces smoothing.

## Per-corner options

Each corner can be a radius number or a full config:

```tsx
<SmoothCorners
  corners={{
    topLeft: { radius: 40, smoothing: 1 },
    topRight: 16,
    bottomRight: { radius: 20, preserveSmoothing: false },
    bottomLeft: 0,
  }}
>
  Content
</SmoothCorners>
```

Omitted corners in a per-corner object are sharp. Adjacent oversized corners share edge space; larger radii receive priority before smaller adjacent corners.

## How Lisse draws the shape

The path depends on the element's measured width and height. Lisse applies:

```ts
el.style.clipPath = generateClipPath(width, height, options);
```

`clip-path` clips backgrounds, images, videos, text, canvas, pseudo-elements, and descendants. Borders and shadows need Lisse's SVG effect system because raw CSS borders and shadows are clipped or rectangular.

## Core APIs

Use `generatePath` for SVG `d` attributes and `generateClipPath` for CSS `clip-path` values:

```ts
import { generatePath, generateClipPath } from "@lisse/core";

const d = generatePath(200, 120, { radius: 24, smoothing: 0.6 });
const clipPath = generateClipPath(200, 120, { radius: 24, smoothing: 0.6 });
```

Use `observeResize` only for custom DOM wiring outside React. In React code, prefer `SmoothCorners` or `useSmoothCorners` so cleanup, resize batching, effects, and style restoration stay owned by the adapter.

## When native CSS is enough

Use CSS `border-radius` when circular arcs are acceptable, the radius is small, or native border/shadow/outline composition and CSS transitions matter more than Figma parity.

CSS `corner-shape` is useful for progressive enhancement or concave/beveled/notched corners, but it is Chromium-only in the source docs and does not match Figma's smoothing family.
