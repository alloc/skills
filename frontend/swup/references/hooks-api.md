# Hooks, Visit Object, And API

Source pages: https://swup.js.org/hooks/, https://swup.js.org/visit/, https://swup.js.org/api/methods/, https://swup.js.org/api/cache/, https://swup.js.org/api/helpers/

## Contents

- Registering Hooks
- Common Hooks
- Visit Object
- Methods And Properties
- Cache API
- Helpers

## Registering Hooks

```js
swup.hooks.on('page:view', (visit) => {
  console.log('New page loaded:', visit.to.url);
});
```

Handlers can be async; swup awaits returned Promises.

```js
swup.hooks.on('visit:start', async () => {
  await prepareTransition();
});
```

Options and shortcuts:

```js
swup.hooks.on('page:view', handler, { once: true });
swup.hooks.once('page:view', handler);

swup.hooks.on('content:replace', handler, { before: true });
swup.hooks.before('content:replace', handler);

swup.hooks.on('visit:start', handler, { priority: -100 });
swup.hooks.off('page:view', handler);
```

Register handlers at initialization:

```js
const swup = new Swup({
  hooks: {
    'visit:start': () => console.log('starting visit'),
    'content:replace.before': () => console.log('before replacement'),
    'fetch:error.once': () => console.log('first fetch error')
  }
});
```

## Common Hooks

- `visit:start`: transition begins.
- `link:click`: link is clicked.
- `page:load`: page loaded from fetch or cache.
- `content:replace`: old content is replaced by new content.
- `page:view`: new content is visible.
- `visit:end`: visit completes.
- `visit:abort`: visit is aborted by a newer visit.
- `fetch:error`: request rejected because of a server error.
- `fetch:timeout`: request timed out.
- `animation:out:start`, `animation:out:await`, `animation:out:end`: leave phase.
- `animation:in:start`, `animation:in:await`, `animation:in:end`: enter phase.
- `animation:skip`: visit skips animation.
- `cache:set`, `cache:clear`: cache lifecycle.
- `scroll:top`, `scroll:anchor`: core scroll behavior.

All hooks are also emitted on `document` with a `swup:` prefix:

```js
document.addEventListener('swup:page:view', ({ detail: { visit } }) => {
  console.log('Going to', visit.to.url);
});
```

## Visit Object

Every hook receives the current visit object. Useful fields:

```js
{
  id,
  from: { url, hash },
  to: { url, hash, html, document },
  containers: ['#swup'],
  animation: { animate: true, name: 'fade' },
  trigger: { el, event },
  cache: { read: true, write: true },
  history: { action: 'push', popstate: false, direction: undefined },
  scroll: { reset: true, target: '#anchor' },
  meta: {}
}
```

Modify the visit in `visit:start` before requests and animations begin:

```js
swup.hooks.on('visit:start', (visit) => {
  if (visit.trigger.el?.matches('[data-instant]')) {
    visit.animation.animate = false;
  }

  if (visit.to.url.startsWith('/filter/')) {
    visit.history.action = 'replace';
    visit.scroll.reset = false;
    visit.cache.read = false;
  }
});
```

Access the incoming document during replacement:

```js
swup.hooks.on('content:replace', (visit) => {
  const lang = visit.to.document?.documentElement.getAttribute('lang');
  if (lang) document.documentElement.setAttribute('lang', lang);
});
```

Pass custom metadata from navigation:

```js
swup.navigate('/search', { meta: { source: 'keyboard' } });

swup.hooks.on('page:view', (visit) => {
  console.log(visit.meta.source);
});
```

## Methods And Properties

Navigate programmatically:

```js
swup.navigate('/about');
swup.navigate('/about', { animate: false });
swup.navigate('/about', { animation: 'slide' });
swup.navigate('/about', { history: 'replace' });
swup.navigate('/search', { method: 'POST', data: new FormData(form) });
swup.navigate('/dynamic', { cache: { read: false, write: true } });
```

Manage the instance:

```js
swup.destroy();
swup.use(new SwupScrollPlugin());
swup.unuse('SwupScrollPlugin');
swup.findPlugin('SwupScrollPlugin');
swup.log('Message visible with Debug Plugin', { detail: true });
```

Useful properties:

- `swup.options`: merged default and user options.
- `swup.plugins`: enabled plugin instances.
- `swup.location`: current URL object with `.url`, `.pathname`, `.search`, and `.hash`.
- `swup.currentPageUrl`: URL last navigated to after redirects.

## Cache API

Disable cache for dynamic sites:

```js
const swup = new Swup({ cache: false });
```

Direct cache methods:

```js
swup.cache.size;
swup.cache.set('/about', { url: '/about', html: '<html>...</html>' });
swup.cache.get('/about');
swup.cache.has('/about');
swup.cache.update('/about', { created: Date.now(), ttl: 300_000 });
swup.cache.delete('/about');
swup.cache.clear();
swup.cache.prune((url, page) => shouldDelete(url, page));
```

TTL pruning:

```js
const ttl = 5 * 60_000;

swup.hooks.on('cache:set', (visit, { page }) => {
  swup.cache.update(page.url, { created: Date.now(), ttl });
});

swup.hooks.before('page:load', () => {
  swup.cache.prune((url, { created, ttl }) => Date.now() > created + ttl);
});
```

## Helpers

Advanced plugin/theme work can import helpers from `swup`:

```js
import {
  Location,
  classify,
  createHistoryRecord,
  updateHistoryRecord,
  delegateEvent,
  getCurrentUrl
} from 'swup';
```

Common uses:

- `Location.fromUrl(href)` and `Location.fromElement(link)` parse path/hash data.
- `classify('Lorem ipsum')` creates safe class/slug text.
- `createHistoryRecord(url, data)` and `updateHistoryRecord(url, data)` create history entries swup recognizes.
- `delegateEvent(selector, event, handler)` creates a delegated listener with `.destroy()`.
