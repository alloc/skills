# Animations

Source pages: https://swup.js.org/getting-started/animations/, https://swup.js.org/plugins/js-plugin/, https://swup.js.org/plugins/parallel-plugin/, https://swup.js.org/plugins/route-name-plugin/

## Contents

- CSS Animations
- Native View Transitions
- JS Animation Hooks
- Parallel Animations
- Route-Based CSS Animations

## CSS Animations

Swup's default mode waits for CSS transitions or keyframe animations on elements matched by `animationSelector`, defaulting to class names containing `transition-`.

```css
html.is-changing .transition-fade {
  transition: opacity 0.25s;
  opacity: 1;
}

html.is-animating .transition-fade {
  opacity: 0;
}
```

Classes added to `html` by default:

- `is-changing`: added before animation, removed after the visit finishes.
- `is-animating`: added before animation, removed after content replacement.
- `is-leaving`: identifies the leave phase.
- `is-rendering`: identifies the enter phase.
- `to-{animation-name}`: set from `data-swup-animation`.

Set `animationScope: 'containers'` when phase classes should live on each container instead of `html`.

## Native View Transitions

Enable browser View Transitions API mode:

```js
const swup = new Swup({ native: true });
```

```css
html.is-changing .transition-fade {
  view-transition-name: main;
}

::view-transition-old(main) {
  animation: fade 0.5s ease-in-out both;
}

::view-transition-new(main) {
  animation: fade 0.5s ease-in-out both reverse;
}

@keyframes fade {
  from { opacity: 1; }
  to { opacity: 0; }
}
```

Unsupported browsers update without native animation. Add fallback CSS by targeting the absence of `swup-native`.

```css
html.is-changing:not(.swup-native) .transition-fade {
  transition: opacity 0.25s;
}

html.is-animating:not(.swup-native) .transition-fade {
  opacity: 0;
}
```

## JS Animation Hooks

For a one-off JS animation, replace the default animation await hooks:

```js
swup.hooks.replace('animation:out:await', async () => {
  await gsap.to('.transition-fade', { opacity: 0, duration: 0.25 });
});

swup.hooks.replace('animation:in:await', async () => {
  await gsap.fromTo('.transition-fade', { opacity: 0 }, { opacity: 1, duration: 0.25 });
});
```

Use JS Plugin when route-matched JS animations are an ongoing pattern:

```sh
npm install @swup/js-plugin
```

```js
import SwupJsPlugin from '@swup/js-plugin';

const swup = new Swup({
  plugins: [
    new SwupJsPlugin({
      animations: [
        {
          from: '(.*)',
          to: '(.*)',
          out: async () => {
            await document.querySelector('#swup')
              .animate([{ opacity: 1 }, { opacity: 0 }], 250)
              .finished;
          },
          in: async () => {
            await document.querySelector('#swup')
              .animate([{ opacity: 0 }, { opacity: 1 }], 250)
              .finished;
          }
        }
      ]
    })
  ]
});
```

JS Plugin animation matching can use exact routes, regular expressions, `path-to-regexp` route patterns, or custom names from `data-swup-animation`. Put more specific animations before generic fallbacks.

## Parallel Animations

Use Parallel Plugin for crossfades, overlays, slideshows, or any transition where previous and next containers must overlap.

```sh
npm install @swup/parallel-plugin
```

```js
import SwupParallelPlugin from '@swup/parallel-plugin';

const swup = new Swup({
  plugins: [new SwupParallelPlugin()]
});
```

The plugin skips the out phase, inserts the next container, animates old and new containers together during the in phase, then removes the previous container. The next container is inserted before the previous one; the previous one receives `aria-hidden="true"`.

Use grid layering for simple overlap:

```css
section {
  display: grid;
  overflow: hidden;
  grid-template-areas:
    "header"
    "main";
}

section > header { grid-area: header; }
section > main { grid-area: main; }

.is-changing .transition-slide {
  transition: transform 0.3s ease-in-out, opacity 0.3s ease-in-out;
}

.transition-slide.is-previous-container {
  transform: translateX(-100%);
  opacity: 0;
}

.transition-slide.is-next-container {
  transform: translateX(100%);
  opacity: 0;
}
```

Options:

```js
new SwupParallelPlugin({
  containers: ['main'],
  keep: 0
});
```

Disable parallel behavior for one visit:

```js
swup.hooks.on('visit:start', (visit) => {
  if (someCondition) visit.animation.parallel = false;
});
```

## Route-Based CSS Animations

Route Name Plugin adds `from-route-*`, `to-route-*`, and `to-same-route` classes.

```sh
npm install @swup/route-name-plugin
```

```js
import SwupRouteNamePlugin from '@swup/route-name-plugin';

const swup = new Swup({
  plugins: [
    new SwupRouteNamePlugin({
      routes: [
        { name: 'home', path: '/:lang?' },
        { name: 'projects', path: '/:lang/projects' },
        { name: 'project', path: '/:lang/project/:slug' },
        { name: 'any', path: '(.*)' }
      ]
    })
  ]
});
```

```css
html.is-animating.from-route-home .transition-default {
  opacity: 1;
  transform: translateX(100%);
}
```

For simple per-link animation choices, prefer `data-swup-animation` before adding Route Name Plugin.
