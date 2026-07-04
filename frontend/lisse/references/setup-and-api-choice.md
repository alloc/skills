# Setup and API Choice

Source wiki pages: `Getting-Started.md`, `Which-API-Should-I-Use.md`, `FAQ.md`.

## Install

Use `@lisse/react` in React 18 or later:

```sh
pnpm add @lisse/react
```

The React package depends on `@lisse/core`; install `@lisse/core` separately only when direct path generation is the actual dependency surface.

## `SmoothCorners`

Use the component for the common case. It creates a wrapper `<div>` with `position: relative`, clips the inner element, and anchors SVG effects for borders and shadows.

```tsx
import { SmoothCorners } from "@lisse/react";

export function Card() {
  return (
    <SmoothCorners
      as="section"
      corners={{ radius: 24, smoothing: 0.6 }}
      className="bg-white p-6 shadow-md"
    >
      <h2>Hello, squircle</h2>
    </SmoothCorners>
  );
}
```

Use `as` to choose the inner element tag. Standard element props are forwarded to that element.

## `asChild`

Use `asChild` when the existing child must own the rendered element, such as a design-system button or link. Pass exactly one child. The child receives Lisse's props/ref; child class names win after merge, and child event handlers run before parent handlers.

```tsx
<SmoothCorners asChild corners={{ radius: 12 }}>
  <a href="/signup" className="bg-neutral-900 px-5 py-2.5 text-white">
    Sign up
  </a>
</SmoothCorners>
```

When `asChild` is true, `as` is ignored.

## `useSmoothCorners`

Use the hook for strict DOM control or when the clipped element must remain a direct layout child. Without effects, pass the target ref and corner options:

```tsx
import { useRef } from "react";
import { useSmoothCorners } from "@lisse/react";

function Card() {
  const ref = useRef<HTMLDivElement>(null);
  useSmoothCorners(ref, { radius: 20, smoothing: 0.6 });
  return <div ref={ref} className="bg-white p-6">Content</div>;
}
```

For borders or shadows with the hook, provide an ancestor `wrapperRef` with non-static positioning. Lisse mounts SVG overlays there.

```tsx
const ref = useRef<HTMLDivElement>(null);
const wrapperRef = useRef<HTMLDivElement>(null);

useSmoothCorners(ref, { radius: 24 }, {
  wrapperRef,
  effects: {
    innerBorder: { width: 1, color: "#ffffff", opacity: 0.2 },
    shadow: { offsetX: 0, offsetY: 8, blur: 24, spread: 0, color: "#000000", opacity: 0.15 },
  },
});

return (
  <div ref={wrapperRef} style={{ position: "relative" }}>
    <div ref={ref}>Content</div>
  </div>
);
```

## Dynamic updates

Drive radius, smoothing, and explicit effects through React state or another state manager. Lisse re-applies the clip path on render and on resize. Memoize hot `corners` objects in large lists to avoid avoidable stringify work.
