# Troubleshooting And Upgrading

Source pages: https://swup.js.org/getting-started/common-issues/, https://swup.js.org/getting-started/reloading-javascript/, https://swup.js.org/getting-started/upgrading/

## Contents

- Debug Checklist
- Scripts Do Not Run On Next Page
- Stylesheets Or Head Tags Are Missing
- Current And Next Pages Need To Overlap
- Screen Readers Are Not Announced
- Anchors Are Hidden Behind Fixed Headers
- History Navigation Is Ignored
- Transition Classes Cause Timing Bugs
- Overflowing Containers Reset
- Swup 3 To 4 Migration

## Debug Checklist

Install Debug Plugin during development and preserve console logs across navigation. When a transition fails, verify:

1. Every selector in `containers` exists in the current and incoming page.
2. Each container selector matches exactly one intended element.
3. The clicked link matches `linkSelector`.
4. No clicked link or parent has `data-no-swup`.
5. `ignoreVisit` is not excluding the URL.
6. No click handler calls `stopPropagation()` before swup sees the event.
7. The server returns a full HTML page, not a partial payload.

## Scripts Do Not Run On Next Page

Swup keeps the current JS session alive and replaces containers. `DOMContentLoaded` runs only once.

Preferred pattern:

```js
function init() {
  if (document.querySelector('#carousel')) {
    // initialize carousel
  }
}

const swup = new Swup();

if (document.readyState === 'complete') {
  init();
} else {
  document.addEventListener('DOMContentLoaded', init, { once: true });
}

swup.hooks.on('page:view', init);
```

Clean up state before content replacement:

```js
function unload() {
  if (document.querySelector('#carousel')) {
    // carousel.destroy()
  }
}

swup.hooks.before('content:replace', unload);
```

Use Scripts Plugin only when script tags cannot be converted into explicit init/cleanup code.

## Stylesheets Or Head Tags Are Missing

Swup core updates content containers and document title, not the full `head`. Prefer one shared stylesheet for the whole site. If pages need unique metadata or assets, use Head Plugin. Set `awaitAssets: true` when the transition should wait for new stylesheets.

Watch for invalid `<noscript>` contents inside `head`; browsers can implicitly close the head if a `noscript` contains body-only markup.

## Current And Next Pages Need To Overlap

Core swup hides the old page, replaces content, then shows the new page. Use Parallel Plugin for crossfades, overlays, slideshows, or 3D effects that require old and new containers to exist at the same time.

## Screen Readers Are Not Announced

Use Accessibility Plugin. It announces the next page and restores focus. Ensure each page has a meaningful `h1`; use `aria-label` on the `h1` when the announced title should differ from visible text.

## Anchors Are Hidden Behind Fixed Headers

Prefer CSS for normal anchor offset:

```css
[id] {
  scroll-margin-top: var(--header-height, 100px);
}
```

Use Scroll Plugin `offset` for dynamic or nested scroll behavior.

## History Navigation Is Ignored

Swup only handles history entries it created. If other code creates history entries that swup should handle:

- Use swup helpers such as `createHistoryRecord` or `updateHistoryRecord`.
- Or customize `skipPopStateHandling`.

Also check whether some links bypass swup due to `linkSelector`, `ignoreVisit`, or propagation handling.

## Transition Classes Cause Timing Bugs

Swup waits for every element matching `animationSelector`. If another library uses `transition-*`, make the selector stricter:

```js
const swup = new Swup({
  animationSelector: '[class*="swup-transition-"]'
});
```

```html
<main id="swup" class="swup-transition-fade"></main>
```

Avoid putting `transition-*` on every animated child. Usually only one timing element needs that class; other child animations can run with matching durations but without matching `animationSelector`.

## Overflowing Containers Reset

Replacing a container resets its scroll position. For nested scroll restoration, use Scroll Plugin and mark containers with `data-swup-scroll-container` or configure `scrollContainers`. For morphing content without replacing the element, consider a morphing approach outside core swup.

## Swup 3 To 4 Migration

Install latest:

```sh
npm install swup@latest
```

Update CDN URLs from `swup@3` to `swup@4`, and repeat for plugins.

Key changes:

- Scroll reset and same-page anchors are built into core. Keep Scroll Plugin only for animated scroll, offsets, and advanced customization.
- Events moved to hooks on `swup.hooks`.
- The visit object replaces the old transition object.
- `swup.loadPage({ url })` became `swup.navigate(url)`.
- `data-swup-transition` became `data-swup-animation`.
- Container selectors should be unique; swup 4 matches one element per selector.
- `[data-swup]` attributes are no longer added to containers.
- Custom payloads are no longer supported; return full HTML pages.
- Vendor-prefixed CSS transition/animation support was removed.

Event to hook examples:

```js
swup.on('pageView', handler);
swup.hooks.on('page:view', handler);

swup.on('clickLink', handler);
swup.hooks.on('link:click', handler);

swup.on('contentReplaced', handler);
swup.hooks.on('content:replace', handler);

swup.on('transitionStart', handler);
swup.hooks.on('visit:start', handler);

swup.on('transitionEnd', handler);
swup.hooks.on('visit:end', handler);
```

Before/after replacement:

```js
swup.hooks.before('content:replace', beforeReplacement);
swup.hooks.on('content:replace', afterReplacement);
```

Cache API changed from storing title/container/body-class data to storing URL and HTML:

```js
swup.cache.set('/about', { url: '/about', html: '<html>...</html>' });
```

Plugin authors should replace internal method overwrites with replaceable hooks:

```js
this.swup.hooks.replace('content:replace', (visit, args, defaultHandler) => {
  if (someCondition) return customReplacement(visit, args);
  return defaultHandler(visit, args);
});
```
