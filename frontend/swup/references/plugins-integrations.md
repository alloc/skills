# Plugins And Integrations

Source pages: https://swup.js.org/plugins/, plugin pages under https://swup.js.org/plugins/, and integration pages under https://swup.js.org/integrations/

## Contents

- Plugin Install Pattern
- Official Plugins
- Accessibility Plugin
- Head Plugin
- Forms Plugin
- Fragment Plugin
- Preload Plugin
- Scroll Plugin
- Debug, Body, Scripts, Progress
- Integrations

## Plugin Install Pattern

```sh
npm install @swup/scroll-plugin
```

```js
import Swup from 'swup';
import SwupScrollPlugin from '@swup/scroll-plugin';

const swup = new Swup({
  plugins: [new SwupScrollPlugin()]
});
```

Plugins can also be added later:

```js
swup.use(new SwupScrollPlugin());
swup.unuse('SwupScrollPlugin');
const plugin = swup.findPlugin('SwupScrollPlugin');
```

## Official Plugins

| Plugin | Package | Use When |
| --- | --- | --- |
| Accessibility Plugin | `@swup/a11y-plugin` | Announce page visits, restore focus, respect reduced motion. |
| Body Class Plugin | `@swup/body-class-plugin` | Update body classes or attributes from the next page. |
| Debug Plugin | `@swup/debug-plugin` | Log hooks, expose common mistakes, make `swup.log` visible. |
| Forms Plugin | `@swup/forms-plugin` | Submit simple forms with animated page transitions. |
| Fragment Plugin | `@swup/fragment-plugin` | Replace only selected page fragments for filters, tabs, modals. |
| Head Plugin | `@swup/head-plugin` | Update head tags, stylesheets, metadata, `lang`, and `dir`. |
| JS Plugin | `@swup/js-plugin` | Manage route-matched JavaScript animations. |
| Parallel Plugin | `@swup/parallel-plugin` | Animate previous and next containers at the same time. |
| Preload Plugin | `@swup/preload-plugin` | Preload likely next pages. |
| Progress Bar Plugin | `@swup/progress-plugin` | Show a delayed loading bar for slow requests. |
| Route Name Plugin | `@swup/route-name-plugin` | Add route-based classes and route info to visits. |
| Scripts Plugin | `@swup/scripts-plugin` | Re-evaluate script tags as a last resort. |
| Scroll Plugin | `@swup/scroll-plugin` | Smooth scroll, offsets, and nested scroll containers. |

## Accessibility Plugin

```js
import SwupA11yPlugin from '@swup/a11y-plugin';

new Swup({
  plugins: [
    new SwupA11yPlugin({
      headingSelector: ['main h1', 'h1'],
      respectReducedMotion: true,
      autofocus: false,
      announcements: {
        visit: 'Navigated to: {title}',
        url: 'New page at {url}'
      }
    })
  ]
});
```

Use semantic page headings. The plugin announces, in order, an `h1` `aria-label`, heading text, document title, or URL. It extends the visit object with `visit.a11y.announce` and `visit.a11y.focus`.

## Head Plugin

Use when next pages need different metadata, stylesheets, scripts in head, or `html` attributes.

```js
import SwupHeadPlugin from '@swup/head-plugin';

new Swup({
  plugins: [
    new SwupHeadPlugin({
      persistAssets: false,
      awaitAssets: true
    })
  ]
});
```

Options to remember:

- `persistAssets: true`: keep orphaned `link`, `style`, and `script[src]` tags.
- `persistTags`: selector for tags to keep.
- `awaitAssets: true`: wait for new stylesheets before animating in.
- `attributes`: update selected `html` attributes.

## Forms Plugin

Use for simple form submissions. The server response must be a valid full page with the required swup containers.

```js
import SwupFormsPlugin from '@swup/forms-plugin';

new Swup({
  plugins: [new SwupFormsPlugin()]
});
```

```html
<form action="/search" data-swup-form data-swup-animation="fade">
  ...
</form>
```

Inline forms update only themselves:

```html
<form id="filters" class="transition-form" data-swup-form data-swup-inline-form>
  ...
</form>
```

```css
.transition-form.is-changing { transition: opacity 200ms; }
.transition-form.is-animating { opacity: 0; }
```

Options:

- `formSelector`: default `form[data-swup-form]`.
- `inlineFormSelector`: default `form[data-swup-inline-form]`.
- `stripEmptyParams`: remove empty GET params.

Hooks: `form:submit`, `form:submit:newtab`.

## Fragment Plugin

Use when only a list, tab panel, modal, or other fragment should be replaced.

```js
import SwupFragmentPlugin from '@swup/fragment-plugin';

new Swup({
  plugins: [
    new SwupFragmentPlugin({
      rules: [
        {
          from: '/users/:filter?',
          to: '/users/:filter?',
          containers: ['#users'],
          name: 'users-filter'
        }
      ]
    })
  ]
});
```

Rules use `path-to-regexp` style paths or regexes. The first matching rule wins. Fragment `containers` must be IDs, not classes or nested selectors, and must exist in both current and incoming documents. Fragment elements must match or descend from a swup container.

Optional rule fields:

- `name`: adds a scoped `to-{name}` class.
- `scroll`: `true`, selector, boolean, or callback.
- `focus`: boolean or selector for Accessibility Plugin focus.
- `if`: predicate receiving the visit.

Advanced modal support:

- `data-swup-fragment-url="/users/"`: identify the URL represented by a fragment.
- `data-swup-link-to-fragment="#list"`: keep a close/back link synced to a tracked fragment URL.
- Use `<template id="modal"></template>` as an empty fragment placeholder to skip animations when every fragment is a template.

## Preload Plugin

```js
import SwupPreloadPlugin from '@swup/preload-plugin';

new Swup({
  plugins: [
    new SwupPreloadPlugin({
      throttle: 5,
      preloadHoveredLinks: true,
      preloadVisibleLinks: false,
      preloadInitialPage: true
    })
  ]
});
```

Markup:

```html
<a href="/about" data-swup-preload>About</a>

<nav data-swup-preload-all>
  <a href="/about">About</a>
  <a href="/contact">Contact</a>
</nav>
```

Methods and hooks:

```js
await swup.preload('/path');
await swup.preload(['/a', '/b']);
swup.preloadLinks();

swup.hooks.on('page:preload', (_visit, { page }) => console.log(page));
swup.hooks.on('link:hover', (_visit, { el }) => console.log(el));
```

## Scroll Plugin

Swup 4 already resets scroll and handles same-page anchors. Add Scroll Plugin for smooth scrolling, fixed-header offsets, custom scroll containers, and custom scroll functions.

```js
import SwupScrollPlugin from '@swup/scroll-plugin';

new Swup({
  plugins: [
    new SwupScrollPlugin({
      animateScroll: {
        betweenPages: true,
        samePageWithHash: true,
        samePage: true
      },
      offset: () => document.querySelector('#header')?.offsetHeight ?? 0,
      scrollContainers: '[data-swup-scroll-container]'
    })
  ]
});
```

Respect reduced motion when enabling animated scroll:

```js
const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

new SwupScrollPlugin({
  animateScroll: reduceMotion ? false : {
    betweenPages: true,
    samePageWithHash: true,
    samePage: true
  }
});
```

## Debug, Body, Scripts, Progress

Debug Plugin:

```js
import SwupDebugPlugin from '@swup/debug-plugin';

new Swup({
  plugins: [new SwupDebugPlugin({ globalInstance: true })]
});
```

Body Class Plugin:

```js
import SwupBodyClassPlugin from '@swup/body-class-plugin';

new Swup({
  plugins: [
    new SwupBodyClassPlugin({
      prefix: 'page-',
      attributes: ['lang', 'dir', /^data-/]
    })
  ]
});
```

Scripts Plugin:

```js
import SwupScriptsPlugin from '@swup/scripts-plugin';

new Swup({
  plugins: [
    new SwupScriptsPlugin({
      head: true,
      body: true,
      optin: false
    })
  ]
});
```

If `optin` is true, only scripts marked with `data-swup-reload-script` are reloaded. Mark the script that initializes swup with `data-swup-ignore-script` to avoid creating multiple instances.

Progress Bar Plugin:

```js
import SwupProgressPlugin from '@swup/progress-plugin';

new Swup({
  plugins: [
    new SwupProgressPlugin({
      className: 'swup-progress-bar',
      transition: 300,
      delay: 300,
      initialValue: 0.25,
      finishAnimation: true
    })
  ]
});
```

## Integrations

Astro:

```sh
npm install @swup/astro
```

```js
// astro.config.mjs
import { defineConfig } from 'astro/config';
import swup from '@swup/astro';

export default defineConfig({
  integrations: [swup()]
});
```

Alpine:

```js
import Swup from 'swup';
import Alpine from 'alpinejs';

const swup = new Swup();
Alpine.start();
```

```html
<div x-data x-on:swup:page:view.document="console.log($event.detail.visit.to.url)">
  ...
</div>
```

Analytics integrations:

- GA Plugin: `@swup/ga-plugin`, pass `gaMeasurementId` for `gtag.js`.
- GTM Plugin: `@swup/gtm-plugin`, pushes `VirtualPageview`.
- Matomo Plugin: `@swup/matomo-plugin`, updates title and URL then tracks page view.

Component integrations:

- Gia Plugin: `@swup/gia-plugin`, pass component map and optional `firstLoad`.
- Livewire Plugin: `@swup/livewire-plugin`, reinitializes Laravel Livewire components after page changes.
