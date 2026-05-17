# Example: Framework Server Entry

Use this example only when adapting a web framework through Nitro's `server.ts` entry. For ordinary API routes, prefer filesystem handlers.

## When to Use

- The project already has `server.ts`.
- The user asks to use Hono, Elysia, H3, Express, Fastify, or another HTTP framework.
- Routing is primarily framework-owned rather than Nitro filesystem-owned.
- Middleware or adapters are easier to express through the framework.

## Web-Compatible Entry

Hono-style entry:

```ts
import { Hono } from "hono";

const app = new Hono();

app.get("/", (c) => c.text("Hello from Hono"));
app.get("/api/health", (c) => c.json({ ok: true }));

export default app;
```

Use the same principle for web-compatible frameworks: export the app or fetch-compatible handler that Nitro can serve.

## Node Framework Caveats

Express and Fastify can require Node-compatible output or adapters. Before using them:

- confirm the deployment target supports Node APIs
- check whether the project already has a Nitro preset
- avoid edge presets unless the framework adapter is edge-compatible
- validate production build, not just dev server behavior

## Review Checks

- Confirm whether filesystem routes still participate when `server.ts` exists.
- Keep framework routes and Nitro routes from defining the same path.
- Keep request body parsing owned by one layer.
- Preserve Web API response behavior when crossing adapter boundaries.
