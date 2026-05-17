# Routing and Handlers

Use this reference for Nitro v3 routes, middleware, route rules, errors, server entry, and framework adapters.

## Filesystem Routing

- Nitro scans route files from the configured server directory. Common defaults are `routes/` and `routes/api/`.
- A route file exports one fetch-compatible handler.
- `routes/api/test.ts` maps to `/api/test`.
- Nested folders become nested route segments.
- Dynamic params use `[name]`; catch-all params use `[...name]`.
- One dynamic param per file or folder segment. Use nested folders for multiple params.
- Method-specific files append the HTTP method before `.ts`, such as `hello.get.ts`, `hello.post.ts`, `hello.put.ts`, or `hello.delete.ts`.
- Parenthesized folders are route groups and do not affect URL paths.
- Ignored files can be controlled through config when generated or helper files sit near routes.

## Handler APIs

```ts
import { defineHandler } from "nitro";

export default defineHandler((event) => {
  const url = new URL(event.req.url);
  return { path: url.pathname };
});
```

Use web-standard request APIs:

- `event.req.headers.get("name")`
- `await event.req.json()`
- `await event.req.formData()`
- `await event.req.text()`
- `new URL(event.req.url)`

Return values can be plain text, JSON-serializable values, `Response` objects, or streams.

## Programmatic Routes

Use `routes` or `handlers` config when route files are not the right fit, such as generated routes or framework integration. Prefer filesystem routes for ordinary API endpoints because they preserve code splitting and simple route discovery.

## Middleware

Use middleware for cross-cutting request work:

- authentication context
- request logging
- URL normalization
- shared validation context
- per-request setup used by multiple routes

Keep middleware narrow. Use route-scoped middleware or filtering when only specific paths need the behavior.

## Route Rules

Route rules declaratively configure behavior for URL patterns:

- `headers`
- `cors`
- `redirect`
- `proxy`
- `basicAuth`
- `cache`, `swr`, and static caching
- `prerender`
- provider-specific features such as Vercel ISR

Check overlapping rules carefully. More specific path behavior should not be hidden by broad catch-all rules.

## Error Handling

Use Nitro/H3 v2 error utilities for intentional HTTP errors. For app-wide behavior, configure an error handler or runtime hooks. Preserve existing error response shape when modifying APIs consumed by clients.

## Server Entry

Use `server.ts` when the project brings its own HTTP framework or wants full control over routing. Nitro can detect a server entry automatically or use a configured custom entry file.

Compatible server entry styles include:

- web-compatible frameworks such as Hono, Elysia, and H3
- fetch-compatible handlers
- Node.js framework adapters when the target runtime supports them

Example:

```ts
import { Hono } from "hono";

const app = new Hono();

app.get("/", (c) => c.text("Hello"));

export default app;
```

When a server entry is present, confirm whether filesystem routes still participate in the app. Do not mix routing models casually.
