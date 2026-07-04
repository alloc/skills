# Performance and Limitations

Lisse cost depends mostly on effects. Bare clipping is path math plus `clip-path`; borders and shadows add SVG overlays, filters, DOM updates, and paint cost.

## Cost rules

- `autoEffects={false}` with no explicit effects is the cheapest mode.
- Auto-effects add a one-time `getComputedStyle` and stripping pass at mount.
- Borders and shadows dominate mount and resize cost because each instance needs SVG overlay work.
- Resize handling is shared through one `ResizeObserver` and batched with `requestAnimationFrame`, but each observed element still needs a sync.
- Above roughly 50 live instances, virtualize large lists or disable effects on low-priority rows.
- Keep `corners` referentially stable in hot lists to avoid avoidable stringify checks.

## Animation

Animating the radius or smoothing through React state is supported; the path is regenerated on updates.

Animating many clipped elements with SVG drop shadows can drop frames, especially in Safari/WebKit where `clip-path: path()` masks and SVG blur filters are more expensive during transform/opacity animation.

Prefer route or view-level View Transitions for large page changes:

```ts
function navigate(nextRoute: string) {
  if (!document.startViewTransition) {
    setRoute(nextRoute);
    return;
  }
  document.startViewTransition(() => setRoute(nextRoute));
}
```

For in-place animation, use smaller mitigations: `will-change: transform`, temporarily drop smooth corners during the transition if acceptable, or pre-render expensive shadows for the animated phase.

## Auto-effects limits

- Only the top border is extracted; per-side border values cannot map to one continuous path.
- CSS `border-image` and gradient borders are not extracted. Use explicit `GradientConfig`.
- `outline` is ignored and remains rectangular or clipped.
- Extraction happens once on mount. Dynamic stylesheet changes require explicit effect props.
- `!important` border or shadow rules can remain visible alongside the SVG replacement.
- CSS transitions on extracted `border` and `box-shadow` do not work after stripping.

## Clip-path gotchas

`clip-path` clips everything inside the element. This affects:

- Focus outlines on the clipped element.
- Pseudo-elements.
- Descendant popovers, dropdowns, tooltips, and hover lifts.
- Scrollbars inside clipped descendants.
- Raw CSS `box-shadow` when `autoEffects` is disabled.

Use portals or sibling DOM for overflowing UI, wrapper-level focus rings when possible, and explicit Lisse effects for shape-following borders and shadows.

## Wrapper impact

The `SmoothCorners` component always creates a wrapper. That can affect flex/grid layout, ordering, selectors, or table semantics. Use `useSmoothCorners` when the smoothed element must be the layout item.

## When not to use Lisse

Use native CSS when small circular corners are acceptable, radius animation must be fully CSS-native, concave/notched/beveled corners are required, or cross-browser Figma parity is not important.
