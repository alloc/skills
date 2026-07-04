# Borders, Shadows, Gradients, and Auto-Effects

Source wiki pages: `Auto-Effects.md`, `Border-Effects.md`, `Gradient-Borders.md`, `Shadow-Effects.md`, `Multiple-Shadows.md`, `Limitations.md`.

Lisse renders borders and shadows as SVG paths so they follow the smooth-corner outline instead of the rectangular box.

## Auto-effects

`autoEffects` defaults to `true`. On mount, Lisse reads computed CSS `border` and `box-shadow`, converts them into effect configs, strips the inline CSS values, and restores original inline styles on cleanup.

```tsx
<SmoothCorners corners={{ radius: 20 }} className="border shadow-lg">
  Content
</SmoothCorners>
```

Auto-effects are one-time extraction, not reactive CSS observation. If classes, media queries, or CSS variables later change border or shadow values, drive explicit effect props instead.

Disable extraction when the element has no CSS border/shadow, when raw CSS effects should remain, or when CSS transitions on those properties must keep working:

```tsx
<SmoothCorners corners={{ radius: 20 }} autoEffects={false} />
```

Explicit props override auto-extracted effects by key.

## Border positions

```tsx
<SmoothCorners
  corners={{ radius: 20 }}
  innerBorder={{ width: 1, color: "#ffffff", opacity: 0.4 }}
  middleBorder={{ width: 1, color: "#888888", opacity: 0.5 }}
  outerBorder={{ width: 2, color: "#000000", opacity: 0.15 }}
>
  Content
</SmoothCorners>
```

- `innerBorder`: contained inside the shape; this is what auto-extracted CSS borders become.
- `outerBorder`: outside the shape, like an outline.
- `middleBorder`: centered on the path and cheaper than inner/outer masking.

Supported styles: `solid`, `dashed`, `dotted`, `double`, `groove`, `ridge`. `double` needs `width >= 3`; `inset` and `outset` have no squircle equivalent and fall back to solid when extracted.

## Gradient borders

Gradient borders are API-only. CSS `border-image` is not auto-extracted.

```tsx
<SmoothCorners
  corners={{ radius: 20 }}
  innerBorder={{
    width: 2,
    opacity: 1,
    color: {
      type: "linear",
      angle: 90,
      stops: [
        { offset: 0, color: "#ff0000" },
        { offset: 1, color: "#0000ff" },
      ],
    },
  }}
/>
```

Linear gradients use CSS-angle convention. Radial gradients use `cx`, `cy`, and `r` from `0` to `1` relative to the element.

## Shadows

`shadow` renders behind the element. `innerShadow` renders inside the shape. Both accept a single config or an array; arrays preserve CSS order, with the first shadow visually closest to the element.

```tsx
<SmoothCorners
  corners={{ radius: 24 }}
  shadow={[
    { offsetX: 0, offsetY: 1, blur: 3, spread: 0, color: "#000000", opacity: 0.12 },
    { offsetX: 0, offsetY: 8, blur: 24, spread: 0, color: "#000000", opacity: 0.08 },
  ]}
  innerShadow={{ offsetX: 0, offsetY: 1, blur: 2, spread: 0, color: "#ffffff", opacity: 0.15 }}
/>
```

Keep layered shadows modest. Two or three layers usually balance depth and paint cost; more than four or five layers can become expensive during animation.

## Animate effects through React

CSS transitions on extracted `border` or `box-shadow` do not animate after auto-effects strips them. Use React state to update explicit effect props:

```tsx
<SmoothCorners
  corners={{ radius }}
  autoEffects={false}
  innerBorder={{ width: focused ? 2 : 0, color: "#3b82f6", opacity: focused ? 1 : 0 }}
/>
```
