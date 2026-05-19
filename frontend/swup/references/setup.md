# Setup And Core Options

Source pages: https://swup.js.org/getting-started/installation/, https://swup.js.org/getting-started/example/, https://swup.js.org/options/, https://swup.js.org/api/markup/

## Contents

- Installation
- Required Page Shape
- Default Options
- Markup Attributes

## Installation

Bundler:

```sh
npm install swup
```

```js
import Swup from 'swup';

const swup = new Swup();
```

CDN global:

```html
<script src="https://unpkg.com/swup@4"></script>
<script>
  const swup = new Swup();
</script>
```

Browser ESM:

```html
<script type="module">
  import Swup from 'https://unpkg.com/swup@4?module';
  const swup = new Swup();
</script>
```

## Required Page Shape

Each swup-managed page must return a full HTML document and include matching container selectors. The default container is `#swup`.

```html
<main id="swup" class="transition-fade">
  <h1>Page title</h1>
</main>
```

Use unique selectors for containers, preferably IDs. Swup 4 replaces one element per container selector.

## Default Options

```js
const swup = new Swup({
  animateHistoryBrowsing: false,
  animationSelector: '[class*="transition-"]',
  animationScope: 'html',
  cache: true,
  containers: ['#swup'],
  hooks: {},
  ignoreVisit: (url, { el } = {}) => el?.closest('[data-no-swup]'),
  linkSelector: 'a[href]',
  linkToSelf: 'scroll',
  native: false,
  plugins: [],
  resolveUrl: (url) => url,
  requestHeaders: {
    'X-Requested-With': 'swup',
    'Accept': 'text/html, application/xhtml+xml'
  },
  skipPopStateHandling: (event) => event.state?.source !== 'swup',
  timeout: 0
});
```

Common adjustments:

- `containers`: replace multiple stable elements, such as `['#nav', '#swup']`.
- `animationSelector`: make stricter when other libraries use `transition-*` classes.
- `animationScope: 'containers'`: add phase classes to containers instead of `html`.
- `cache: false`: use for highly dynamic pages that must always refetch.
- `ignoreVisit`: exclude specific URLs or link contexts.
- `linkSelector`: include SVG links, map areas, or narrower link sets.
- `native: true`: enable View Transitions API mode.
- `timeout`: fall back to a normal page load after slow fetches.

## Markup Attributes

Ignore a link or a whole section:

```html
<a href="/admin" data-no-swup>Admin</a>

<section data-no-swup>
  <a href="/legacy">Legacy flow</a>
</section>
```

Choose an animation for a link or section:

```html
<a href="/case-study" data-swup-animation="slide">Case study</a>

<section data-swup-animation="overlay">
  <a href="/modal">Overlay</a>
</section>
```

Swup adds `to-{name}` to the animation scope during that visit:

```css
html.is-changing .transition-page {
  transition: opacity 250ms;
}

html.is-changing.to-slide .transition-page {
  transition: transform 250ms;
}
```

Persist an element inside replaced containers by matching `data-swup-persist` values between pages:

```html
<video src="/intro.mp4" autoplay data-swup-persist="hero-video"></video>
```

Replace the current history entry:

```html
<a href="/filtered" data-swup-history="replace">Filter</a>
```
