# Deployment and Migration

Use this reference for deployment, preset selection, provider-specific output, Nitro v2 migration, nightly channel, and compatibility dates. Do not copy deployment instructions into `SKILL.md`.

## Output and Presets

Nitro builds to `.output/`. Auto-detection can choose a provider preset, but explicit `NITRO_PRESET` or `preset` may be needed for CI, local previews, or non-detected targets.

Common runtime targets:

- Node.js
- Bun
- Deno
- Cloudflare Workers
- serverless functions
- edge platforms

Set compatibility dates when the target provider requires them, especially edge runtimes.

## Provider Notes

Check provider docs before editing deployment config. Nitro docs include provider sections for:

- AWS Lambda and AWS Amplify
- Azure
- Bun
- Cloudflare Workers and Pages
- Deno and Deno Deploy
- DigitalOcean
- Firebase
- GitHub Pages and GitLab Pages
- Heroku
- IIS
- Koyeb
- Netlify
- Platform.sh
- Render
- Vercel
- Zeabur
- Zephyr Cloud
- Zerops

Provider-specific concerns often include:

- start command
- build command
- output directory
- environment variables
- Node.js version
- static asset serving
- function streaming
- cron or scheduled task support
- queue support
- edge versus Node runtime behavior

## Cloudflare

Cloudflare Workers and Pages use specific presets and may require Wrangler config for local preview, bindings, environments, and deployment. Access bindings through the documented Nitro runtime path for Cloudflare rather than assuming Node globals.

## Vercel

Vercel-specific work may involve per-route function configuration, proxy route rules, scheduled tasks, queues, and ISR. Use route rules for ISR where possible and keep revalidation secrets in environment variables.

## Node.js

For Node output, confirm the start command points at the built server entry under `.output`. Cluster mode and advanced handlers have separate environment variable behavior.

## Migration from Nitro v2

Key Nitro v3 migration checks:

- Package rename: `nitropack` to `nitro`.
- Imports move from `nitropack/runtime/*` and deep paths to `nitro/*` subpaths.
- Handler API uses `defineHandler`.
- H3 v2 is web-standard first.
- Request body parsing uses native request methods such as `await event.req.json()`.
- Headers use `event.req.headers.get(...)`.
- Error utilities changed; check H3 v2 equivalents.
- Minimum Node.js version is 20.
- Some preset names changed or consolidated.
- App config support was removed.
- Type imports may need updates.
- Cloudflare bindings access changed.

When migrating, update imports and route behavior in small batches, then run type checks and route-level tests.

## Nightly Channel

Use the nightly channel only when the project intentionally tracks unreleased Nitro behavior. Document the reason in code comments or project docs if adopting nightly to work around a bug or use a required feature.
