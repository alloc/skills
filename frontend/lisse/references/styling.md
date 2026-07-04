# Styling and Data Hooks

`SmoothCorners` forwards `className`, style, events, and normal element props to the clipped inner element. The wrapper created by the component is positional and should not be treated as the styled surface.

## Classes and styles

Classes and inline styles work normally because Lisse reads computed styles and applies the clip path inline.

```tsx
<SmoothCorners
  corners={{ radius: 20, smoothing: 0.7 }}
  className="cardSurface"
>
  Content
</SmoothCorners>
```

By default, CSS `box-shadow` and `border` are auto-extracted into SVG effects. Color values that resolve to standard `rgb()` or `rgba()` are parsed.

Drop `border-radius` from the clipped element unless it is needed as a fallback. Lisse's `clip-path` defines the visible geometry, so `border-radius` is redundant once the path is ready.

Drop `overflow: hidden` when it only exists to clip the same element. `clip-path` already clips descendants. Keep overflow rules only when a surrounding layout needs them independently.

## `asChild` class merging

Use `asChild` when styling must remain on an existing child:

```tsx
<SmoothCorners asChild corners={{ radius: 12 }}>
  <button className="primaryButton">
    Save
  </button>
</SmoothCorners>
```

Child classes win after merge. Preserve a single child and make sure custom components forward refs and props to a real DOM element.

## Data attributes

Lisse sets:

- `data-slot="smooth-corners"` on managed elements.
- `data-state="pending"` until a non-zero-size element has received its first clip path, then `data-state="ready"`.

Use these for first-paint masking or scoped styling:

```css
[data-slot="smooth-corners"][data-state="pending"] {
  opacity: 0;
}

[data-slot="smooth-corners"][data-state="ready"] {
  opacity: 1;
  transition: opacity 100ms;
}
```

If the element mounts as `display: none` or zero-sized, it remains `pending` until ResizeObserver reports real dimensions.

## Focus and overflow styling

`clip-path` crops the element's own outline and descendants. For focus rings, prefer an outer wrapper ring, an `outline-offset` large enough to clear the clip, or a Lisse border driven by focus state.

Render tooltips, menus, and other overflowing UI outside the clipped element, usually through a React portal. A clipped ancestor will crop descendants regardless of z-index.
