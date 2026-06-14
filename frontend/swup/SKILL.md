---
name: swup
description: Build, debug, and customize swup page transitions for server-rendered websites. Use when Codex needs to install swup, add page transition markup/CSS/JavaScript, configure swup options, reinitialize JavaScript after swup navigations, choose swup plugins or integrations, migrate swup versions, or troubleshoot hard page loads, scripts, styles, scroll, cache, hooks, and animations.
---

# Swup

Prefer swup's core behavior first; add plugins only for a specific missing capability. The goal is a multi-page/server-rendered site that feels like an SPA without becoming one.

## Common Workflow

1. Confirm the site renders complete HTML pages for each URL. Swup fetches the next page and replaces shared containers; it is not a client router.
2. Add one stable content container that exists on every swup-managed page, usually `<main id="swup" class="transition-fade">`.
3. Initialize one swup instance from the site's main client entry.
4. Define transition timing on the animation selector. By default, swup waits for elements with class names containing `transition-`.
5. Move page-specific JavaScript initialization out of `DOMContentLoaded`-only code and run it on `page:view` as well.
6. Test normal links, back/forward navigation, hash links, reduced-motion behavior, and at least one page whose layout differs from the current page.

Minimal setup:

```html
<main id="swup" class="transition-fade">
  ...
</main>
```

```css
html.is-changing .transition-fade {
  transition: opacity 0.25s;
  opacity: 1;
}

html.is-animating .transition-fade {
  opacity: 0;
}
```

```js
import Swup from 'swup';

const swup = new Swup();
```

For CDN/native ESM setup and core options, read [references/setup.md](references/setup.md).

## Common Tasks

### Reinitialize Components

Do not rely on `DOMContentLoaded` after the first load. Put page behavior in an idempotent `init()` function and call it on initial load and after swup page views.

```js
const swup = new Swup();

function init() {
  document.querySelectorAll('[data-carousel]').forEach((el) => {
    if (el.dataset.initialized) return;
    el.dataset.initialized = 'true';
    // initialize component
  });
}

if (document.readyState === 'complete') {
  init();
} else {
  document.addEventListener('DOMContentLoaded', init, { once: true });
}

swup.hooks.on('page:view', init);
```

If components attach global listeners, timers, observers, media players, or third-party instances, also add a cleanup step before `content:replace`. See [references/troubleshooting-upgrading.md](references/troubleshooting-upgrading.md).

### Choose Animation Strategy

- Use CSS transitions for ordinary fades, slides, and route-specific classes.
- Use `native: true` when the project wants the browser View Transitions API and can accept no animation in unsupported browsers unless CSS fallback is added.
- Use JS hooks for one-off custom animation control.
- Use JS Plugin only when route-matched JS animations are a recurring pattern.
- Use Parallel Plugin when the old and new containers must be visible at the same time.

For animation classes, native transitions, JS hooks, Parallel Plugin timing, and route-specific animation patterns, read [references/animations.md](references/animations.md).

### Add Behavior With Hooks

Most custom behavior starts with these hooks:

- `visit:start`: inspect or modify the upcoming visit before requests or animations.
- `content:replace.before`: clean up old page code before DOM replacement.
- `content:replace`: inspect the incoming document or adjust global attributes.
- `page:view`: initialize components, analytics, and post-navigation UI.
- `visit:end`: final work after animations and replacement finish.

For the complete hook list, visit object fields, cache, methods, and DOM events, read [references/hooks-api.md](references/hooks-api.md).

### Pick Plugins

Use plugins when core swup does not cover a need:

- Accessibility Plugin: announce new pages, restore focus, respect reduced motion.
- Head Plugin: update head tags, metadata, page-specific stylesheets, `lang`, and `dir`.
- Preload Plugin: preload likely next pages.
- Forms Plugin: animate simple form submissions.
- Fragment Plugin: replace only filtered lists, tabs, modal fragments, or other page subsections.
- Scroll Plugin: smooth scrolling, offsets for fixed headers, nested scroll containers.
- Debug Plugin: development warnings and hook logging.
- Scripts Plugin: last-resort script tag re-evaluation when code cannot be moved to hooks.

For install/import snippets and less common plugins/integrations, read [references/plugins-integrations.md](references/plugins-integrations.md).

### Debug First

When swup unexpectedly performs a hard page visit or skips an expected behavior:

1. Add Debug Plugin in development.
2. Preserve the browser console log across navigations.
3. Verify every replaced container selector exists exactly once in the current and next document.
4. Check `ignoreVisit`, `data-no-swup`, custom `linkSelector`, and click handlers that stop propagation.
5. Check whether missing head updates, script lifecycle, or overbroad `transition-*` selectors are the real issue.

For issue-specific fixes and migration notes, read [references/troubleshooting-upgrading.md](references/troubleshooting-upgrading.md).
