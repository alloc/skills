# Motion vanilla JavaScript quick start

Prefer `motion/react` in React components. Use vanilla Motion APIs when code needs to animate DOM outside React ownership, SVG attributes, WebGL/Three.js object properties, browser View Transitions, scroll-linked timelines, or shared Motion values without causing React renders.

Install the same package:

```sh
npm install motion
```

Import vanilla APIs from `motion`:

```js
import { animate, scroll } from "motion"

animate(".box", { rotate: 360 })
```

For small non-bundled pages, Motion can be loaded from an ESM CDN:

```html
<script type="module">
  import { animate } from "https://cdn.jsdelivr.net/npm/motion@latest/+esm"
  animate(".box", { opacity: 1 })
</script>
```

Pin the CDN version in production instead of using `latest`.

Vanilla targets can be CSS selectors, elements, element lists, Motion values, single values, and ordinary JavaScript objects depending on the API.
