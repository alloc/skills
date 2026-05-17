# Runtime Primitives

Use this reference for Nitro storage, server assets, cache, database, runtime config, plugins, lifecycle hooks, tasks, WebSockets, SSE, and OpenAPI.

## Runtime Config

Use runtime config for values that differ by environment, especially secrets and external service URLs. Keep secrets out of source files and client-visible payloads.

Runtime config values must be serializable. Prefer nested objects for grouped settings and confirm environment variable prefix behavior before renaming keys.

## Storage

Nitro storage is a runtime-agnostic key-value layer backed by unstorage.

```ts
import { useStorage } from "nitro/storage";

const storage = useStorage();
await storage.setItem("user:1", { name: "Nitro" });
const user = await storage.getItem("user:1");
```

Use storage for portable key-value state, cache backing stores, and server asset access. Configure mount points when different namespaces need different drivers.

## Server Assets

Use server assets for files that server code reads at runtime but clients should not fetch directly. Public assets are served to clients; server assets are bundled or exposed to server runtime code.

## Cache

Use cached handlers for route responses:

```ts
import { defineCachedHandler } from "nitro/cache";

export default defineCachedHandler(
  () => "cached",
  { maxAge: 60 * 60 },
);
```

Use cached functions for reusable expensive operations:

```ts
import { defineCachedFunction } from "nitro/cache";

export const getUser = defineCachedFunction(
  async (id: string) => fetchUser(id),
  {
    maxAge: 300,
    getKey: (id) => id,
  },
);
```

Cache checklist:

- Include all response-affecting inputs in the cache key.
- Avoid caching unsafe methods unless the behavior is intentional.
- Use SWR only when stale data is acceptable.
- Consider invalidation paths before adding long-lived cache entries.
- Confirm cache storage when deploying to serverless or edge targets.

## Database

Nitro database provides a SQL layer that defaults to SQLite for development and can connect to other databases through connectors.

```ts
import { useDatabase } from "nitro/database";

const db = useDatabase();
const rows = await db.sql`SELECT * FROM users`;
```

Use `db.sql` for parameterized SQL templates, `db.exec` for direct statements where safe, and prepared statements for repeated queries. Keep migrations deterministic; tasks can be a good fit for explicit migration commands.

## Plugins and Hooks

Use plugins for runtime setup and app-level integration. Plugins can register runtime hooks and access the Nitro app context.

Common hooks:

- request lifecycle observation
- response header mutation
- error capture
- graceful shutdown

Keep plugin side effects explicit and avoid doing request-specific work at module load time.

## Tasks

Tasks are experimental. Use them for named server-side jobs, scheduled work on supported platforms, migration helpers, and explicit admin operations.

Check platform support before relying on scheduled tasks. For work triggered from a request, use `waitUntil` when background completion should outlive the response.

## WebSockets and SSE

Enable WebSockets in config before adding handlers. Use `defineWebSocketHandler` for lifecycle hooks:

- `open`
- `message`
- `close`
- `error`
- `upgrade`

Peers can send messages, subscribe to topics, publish to topics, close, or terminate. Use namespaces for pub/sub separation when multiple real-time channels coexist.

Use SSE for one-way server-to-client event streams when full duplex WebSockets are unnecessary.

## OpenAPI

Enable OpenAPI when the API surface should be discoverable or documented. Route metadata can describe parameters, response schemas, tags, and global components. Keep metadata close to handlers so changes stay synchronized.
