# Renderer, Vite, and SSR

Use this reference for Nitro renderer behavior, Vite integration, HTML templates, SPA fallback, SSR outlets, and framework SSR examples.

## Renderer

The renderer catches routes that do not match a specific API or route handler. It is useful for:

- single-page app fallback
- server-side rendering
- custom HTML responses
- universal frontend rendering

Renderer priority is lowest:

1. Specific API routes
2. Specific server routes
3. Renderer fallback

Avoid catch-all route conflicts. Nitro warns when catch-all routes can be overridden by renderer behavior.

## Renderer Config

```ts
import { defineConfig } from "nitro";

export default defineConfig({
  renderer: {
    template: "./index.html",
    handler: "./renderer.ts",
    static: false,
  },
});
```

- `template`: HTML file used as renderer template.
- `handler`: custom renderer module.
- `static`: force static HTML handling.
- `renderer: false`: disable renderer auto-detection.

If `handler` is set, it owns rendering and `template` is ignored.

## HTML Templates

Nitro can auto-detect `index.html` in the project source directory and use it as a renderer template. Static templates can be served directly. Dynamic templates may use rendu syntax.

Common template concerns:

- Use `<!--ssr-outlet-->` for Vite SSR output insertion.
- Keep API route paths out of SPA fallback expectations.
- Ensure production build transforms the final template through Vite when using the Nitro Vite plugin.

## Vite Plugin

Use `nitro()` in `vite.config.ts` when the app builds frontend and backend together:

```ts
import { defineConfig } from "vite";
import { nitro } from "nitro/vite";

export default defineConfig({
  plugins: [nitro()],
});
```

With Vite integration, one Vite build can produce an optimized `.output/` folder containing both frontend and backend output.

## SSR Patterns

Load [example-vite-ssr.md](./example-vite-ssr.md) for framework-specific SSR examples.

General checks:

- Server entry renders the initial HTML or stream.
- Client entry hydrates or mounts the same app shape.
- Template contains the expected outlet.
- Route data fetching works on the server without browser globals.
- Response headers and status codes are preserved during SSR.

## Rendu Template Notes

Use dynamic template syntax only when the app already uses Nitro templates or a small server-rendered page is simpler than a full renderer handler.

- `{{ expression }}` escapes output.
- `{{{ expression }}}` and `<?= expression ?>` output raw HTML.
- `<? ... ?>` runs JavaScript control flow.
- `<script server>` runs server-side JavaScript.
- `echo()` can stream strings, promises, responses, or readable streams.

Avoid raw output unless the value is trusted or explicitly sanitized.
