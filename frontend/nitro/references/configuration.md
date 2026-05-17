# Configuration

Use this reference before changing `nitro.config.ts`, directory options, build options, route rules, environment variables, or presets.

## Config File

```ts
import { defineConfig } from "nitro";

export default defineConfig({
  serverDir: "./server",
});
```

Configuration may also be affected by Vite plugin options, environment-specific config, extended configs, or `package.json`. Inspect existing sources before adding a new config file.

## Directory Options

Common directory options include:

- `workspaceDir`
- `rootDir`
- `serverDir`
- `scanDirs`
- `apiDir`
- `routesDir`
- `buildDir`
- `output`

Use these when adapting Nitro to an existing project layout. Do not move route files if a config option can preserve the app's structure.

## Runtime and Environment

Use `runtimeConfig` for runtime values and environment overrides. Confirm:

- local development values
- production environment variable names
- custom environment prefix behavior
- nested object mapping
- serialization constraints
- environment expansion behavior if enabled

Never place secrets in examples committed to the project.

## Route Rules Config

Use `routeRules` for URL-pattern behavior:

```ts
import { defineConfig } from "nitro";

export default defineConfig({
  routeRules: {
    "/api/**": { cors: true },
    "/old": { redirect: "/new" },
    "/blog/**": { swr: 300 },
  },
});
```

Review broad patterns such as `/**` and `/api/**` carefully before adding narrower rules.

## Feature Flags

Feature flags and experimental options control capabilities such as:

- runtime hooks
- WebSockets
- OpenAPI
- database
- tasks
- async context
- TypeScript bundler resolution
- environment expansion

Only enable experimental options for a concrete feature need.

## Build Options

Common build-related options include:

- builder selection
- Rollup or Rolldown config
- aliases
- externals and tracing
- sourcemaps
- minification
- dynamic import behavior
- export conditions
- Node.js behavior

Prefer existing project build patterns. Avoid broad `noExternals` or alias changes without checking bundle impact.

## Preset Options

The `preset` controls output for runtimes and providers. Auto-detection is often enough. Set `preset` explicitly when:

- local builds target a provider different from the current environment
- CI needs deterministic output
- provider docs require a specific preset
- testing a runtime-specific behavior

Read [deployment-and-migration.md](./deployment-and-migration.md) for provider-specific deployment details.
