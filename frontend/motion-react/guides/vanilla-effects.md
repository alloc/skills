# Vanilla Motion value effects

Use effect helpers when Motion values should render directly to DOM, SVG, or object state without React renders.

```js
import {
  attrEffect,
  motionValue,
  propEffect,
  styleEffect,
  svgEffect,
  transformValue,
} from "motion"
```

`styleEffect(target, values)` applies Motion values to HTML styles once per animation frame. It supports independent transforms, default unit conversion, and CSS properties.

```js
const x = motionValue(0)
const opacity = motionValue(1)
const cancel = styleEffect(".item", { x, opacity })
```

`attrEffect(target, values)` applies Motion values to element attributes. It handles `aria` and `data` casing, and uses JavaScript setters when available.

```js
const progress = motionValue(0)
attrEffect("#meter", { ariaValuenow: progress, dataProgress: progress })
```

`svgEffect(target, values)` applies Motion values to SVG styles and attributes. Use `attr` prefixes when a value should be written as an attribute, and use `pathLength`, `pathSpacing`, and `pathOffset` for draw effects.

```js
const pathLength = motionValue(0)
svgEffect("path", { pathLength })
```

`propEffect(object, values)` writes Motion values to ordinary object properties. Use it for objects owned by graphics libraries such as Three.js.

```js
const x = motionValue(0)
propEffect(mesh.position, { x })
```

Each helper returns a cleanup function. Store and call it when the target lifecycle ends.
