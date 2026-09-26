# Bindings: `@octanejs/*` ecosystem

Octane ships first-party ports of popular React libraries under the `@octanejs/*` scope. **When asked for the Octane equivalent of a well-known React library, point to the matching binding first.** To keep an existing component on real React — or use a library with no port — use `ReactCompat` with its real React dependencies (see [react-interop.md](./react-interop.md)).

In many cases the main application change is the import path (`@tanstack/react-query` → `@octanejs/tanstack-query`), but maturity, supported surface, known divergences, and SSR/hydration coverage vary by package. Check the generated bindings status table (`docs/bindings-status.md` in the octane repo) before relying on a specific native API. `octane add` installs a binding by the React package it ports.

## Core packages

| Package | Role |
| --- | --- |
| `octane` | Runtime and `.tsrx`/`.tsx` compiler — the only package every app needs |
| `octane/react` | `ReactCompat`, `OctaneCompat`, `bridgeReactContext`; server impls in `octane/react/server` |
| `octane/compiler/vite` | Low-level Vite compiler adapter under `@octanejs/vite-plugin`; for unusual custom tooling |
| `@octanejs/rspack-plugin` | Rspack 2.x compiler integration: client/server runtime selection, source maps, dependency watching, cache metadata, Rspack HMR |
| `@octanejs/app-core` | Bundler-neutral config, routing, SSR/hydration codegen, production request-handler core |
| `@octanejs/vite-plugin` | Recommended Vite integration for SPAs and full apps |
| `@octanejs/rsbuild-plugin` | Full app integration for Rsbuild 2.x, built on the Rspack plugin |
| `@octanejs/adapter-vercel` | Deploy a full-app production build to Vercel |
| `@octanejs/adapter-cloudflare` | Deploy a full-app production build to Cloudflare Workers with Workers Static Assets |

## Bindings by domain

All names below are npm packages under the `@octanejs/` scope (e.g. `wagmi` → `@octanejs/wagmi`).

- **Shared state** — `alien-signals`, `zustand`, `valtio`, `jotai`, `mobx`, `rxjs`, `redux`, `redux-toolkit`, `tanstack-store`, `xstate`, `xstate-store`
- **AI, data, and routing** — `tanstack-ai`, `apollo-client`, `livestore`, `dexie`, `swr`, `tanstack-query`, `tanstack-db`, `tanstack-router`, `tanstack-router-ssr-query`, `remix-router`, `inertia`, `nuqs`, `better-auth`, `wouter`
- **Web3** — `wagmi`, `rainbowkit`, `solana-kit`
- **UI and interaction** — `radix`, `zag`, `vaul`, `base-ui`, `base-ui-utils`, `aria`, `mantine-hooks`, `embla-carousel`, `floating-ui`, `animejs`, `gsap`, `popper`, `motion`, `spring`, `dnd-kit`, `sonner`, `draggable`, `resizable-panels`, `select`, `react-error-boundary`, `transition-group`, `day-picker`, `textarea-autosize`, `colorful`, `cmdk`, `shadcn`, `lucide`, `phosphor-icons`, `usehooks-ts`, `intersection-observer`, `tanstack-hotkeys`, `tanstack-pacer`, `stick-to-bottom`, `image-crop`, `content-loader`, `to-print`, `calendar`, `auto-animate`, `thinking-orbs`, `waypoint`, `xyflow`
- **Forms and content** — `formisch`, `hook-form`, `input-otp`, `dropzone`, `tanstack-form`, `email`, `email-cli`, `lexical`, `tiptap`, `blocknote`, `markdown`, `streamdown`, `pdf`, `monaco-editor`, `syntax-highlighter`, `mdx`, `i18next`, `html-react-parser`
- **Sanity content** — `portabletext`, `sanity-loader`, `sanity-icons`, `sanity-logos`
- **Data-heavy screens** — `tanstack-table`, `tanstack-virtual`, `window`, `recharts`, `visx`, `react-map-gl`
- **Web 3D** — `three`, `drei`
- **Terminal UI** — `ink`, `opentui`
- **Desktop** — `tauri`, `electron`
- **Styling, tests, devtools** — `stylex`, `styled-components`, `testing-library`, `octane-is`, `tanstack-devtools`, `devtools`

## Porting standard

Ports are held to a pinned-release standard rather than written from upstream documentation:

- A binding targets one immutable upstream release and keeps that release's React-facing source beside the Octane implementation, so the two read together and the next upgrade is a reviewable diff.
- Every upstream export is accounted for as ported, reused verbatim from a framework-neutral core, a divergence, or an explicit gap.
- The binding runs that release's own test suite where it ships one — framework-neutral suites unmodified, React-binding suites ported case by case — not only tests written around the port. Whatever parity cannot reach is recorded as a divergence with a behavioral test.
- Older bindings are being brought up to that bar package by package; the generated status table records evidence and remaining gaps per package. Some bindings additionally use differential fixtures that drive Octane and React implementations through the same interactions and compare output.
- Creating a native binding for a package that has none follows the same porting workflow.
