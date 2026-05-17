---
name: nitro
description: Build, modify, and review Nitro v3 servers and Vite-integrated Nitro apps. Use when working with `nitro`, `nitro.config.ts`, `server.ts`, `routes/`, `middleware/`, Nitro route rules, handlers, renderer/SSR, storage, cache, database, tasks, WebSockets, OpenAPI, or migration from `nitropack` to `nitro`.
---

# nitro

Use this skill for Nitro v3 server work. Prefer Nitro's web-standard APIs and local project conventions before adding framework-specific abstractions.

## Start Here

- Inspect `package.json`, `nitro.config.ts`, `vite.config.ts`, `server.ts`, `routes/`, `api/`, `middleware/`, `plugins/`, `tasks/`, and existing imports before editing.
- Use `nitro` package imports for v3 work: `defineHandler` from `nitro`, `useStorage` from `nitro/storage`, `useDatabase` from `nitro/database`, and cache helpers from `nitro/cache`.
- Treat request and response handling as Web API first: `event.req`, `Request`, `Response`, `Headers`, `URL`, `await event.req.json()`, and native streams.
- Keep common route and runtime tasks in this file. Load references only for task-specific details.

## References

- Read [routing-and-handlers.md](./references/routing-and-handlers.md) before changing filesystem routes, dynamic params, method-specific routes, middleware, route rules, errors, server entry, or framework adapters.
- Read [renderer-vite-and-ssr.md](./references/renderer-vite-and-ssr.md) before changing Nitro renderer behavior, Vite integration, HTML templates, SPA fallback, SSR outlets, or framework SSR examples.
- Read [runtime-primitives.md](./references/runtime-primitives.md) before changing storage, server assets, cache, database, runtime config, plugins, lifecycle hooks, tasks, WebSockets, SSE, or OpenAPI.
- Read [configuration.md](./references/configuration.md) before changing `nitro.config.ts`, directory options, build options, route rules config, environment variables, or presets.
- Read [deployment-and-migration.md](./references/deployment-and-migration.md) only when the task involves deployment, preset selection, provider-specific output, Nitro v2 migration, nightly channel, or compatibility dates.
- Read [example-framework-server-entry.md](./references/example-framework-server-entry.md) only when adapting Hono, Elysia, H3, Express, Fastify, or another framework through `server.ts`.
- Read [example-vite-ssr.md](./references/example-vite-ssr.md) only when implementing or repairing Vite SSR with React, Preact, Solid, Vue Router, TanStack Router, TanStack Start, RSC, or HTML streaming.
- Read [example-trpc.md](./references/example-trpc.md) only when routing tRPC through Nitro in a Vite app.
- Read [example-websocket.md](./references/example-websocket.md) only when a WebSocket example would reduce risk beyond the lifecycle notes in the runtime reference.

## Common Workflow

1. Classify the change.
   - Route/API behavior: use filesystem route patterns or `server.ts` if the project already owns the server entry.
   - Cross-cutting request behavior: use middleware, plugins, route rules, or hooks depending on scope.
   - Data persistence: choose Nitro database for SQL and Nitro storage for key-value or asset-like data.
   - Expensive or repeated work: use cached handlers, cached functions, or route rule caching.
   - UI rendering: use the renderer or Vite SSR path already present in the app.
2. Preserve the app's current mode.
   - If it uses Vite plugin config, keep server changes compatible with `vite build`.
   - If it uses a `server.ts` entry, avoid adding filesystem routes unless that pattern already exists.
   - If it uses filesystem routing, place handlers under the configured `serverDir`, `routesDir`, or `apiDir`.
3. Implement the smallest Nitro-native change.
   - Export one handler per route file.
   - Use method suffixes such as `.get.ts` or `.post.ts` for method-specific handlers.
   - Use route rules for declarative headers, redirects, proxying, CORS, SWR/static caching, prerendering, ISR, or auth where appropriate.
   - Use runtime config for environment-dependent values; never hard-code secrets.
4. Validate with the repo's existing scripts first. If none are present, run the narrowest relevant Nitro, Vite, TypeScript, or package-manager command available.

## Route Handler Patterns

Basic handler:

```ts
import { defineHandler } from "nitro";

export default defineHandler(() => {
  return { ok: true };
});
```

Read params and body with Nitro v3 web-standard APIs:

```ts
import { defineHandler } from "nitro";

export default defineHandler(async (event) => {
  const id = event.context.params.id;
  const body = await event.req.json();

  return { id, body };
});
```

Return a custom response when status, headers, streaming, or raw output matters:

```ts
import { defineHandler } from "nitro";

export default defineHandler(() => {
  return new Response("created", {
    status: 201,
    headers: { "content-type": "text/plain; charset=utf-8" },
  });
});
```

## File Routing Reminders

- `routes/api/test.ts` maps to `/api/test`.
- `routes/hello.get.ts` maps to `GET /hello`.
- `routes/hello.post.ts` maps to `POST /hello`.
- `routes/users/[id].ts` exposes `event.context.params.id`.
- `routes/files/[...path].ts` captures the remaining path.
- Parenthesized route groups organize files without changing URL paths.
- Renderer fallback has lower priority than specific API and route handlers.

## Review Checklist

- Confirm imports match Nitro v3 and avoid legacy `nitropack/runtime/*` paths.
- Confirm handlers use native request APIs for headers, body, and URLs.
- Confirm route file names match the intended URL and HTTP method.
- Confirm middleware and plugins do not accidentally run broader than intended.
- Confirm route rules are ordered and specific enough for overlapping paths.
- Confirm cache keys vary by every request input that changes the response.
- Confirm secrets come from runtime config or environment variables.
- Confirm preset or migration changes are backed by the relevant reference, not memory.
