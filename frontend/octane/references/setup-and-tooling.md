# Octane setup and tooling

## Scaffolding

```sh
npm create octane my-app -- --template spa        # client-only app
npm create octane my-app -- --template fullstack  # routing + SSR
```

`npm create octane` and `octane create` are the same command reached two ways; both scaffold into an empty directory. To add Octane to an existing project, use `octane init`.

## Build integrations

- **Vite (recommended):** install `octane` and `@octanejs/vite-plugin`, add `octane()` to `vite.config.ts`. Handles compilation by default, plus routing, streaming dev SSR, hydration wiring, and production client/server builds when configured.
- **Rspack:** install `octane`, `@rspack/core`, and `@octanejs/rspack-plugin`; add `new OctaneRspackPlugin()` to the plugins array. Covers client/server runtime selection, source maps, dependency watching, cache metadata, and Rspack HMR.
- **Rsbuild:** install `octane`, `@rsbuild/core`, and `@octanejs/rsbuild-plugin`; add `pluginOctane()` to `rsbuild.config.ts`. Add declarative `RenderRoute`/`ServerRoute` entries in `octane.config.ts` for routing, SSR, hydration, RPC, production builds, and preview.
- `octane/compiler/vite` is the low-level Vite adapter under `@octanejs/vite-plugin`; reserve it for unusual custom tooling.
- Deploy full-app production builds with `@octanejs/adapter-vercel` or `@octanejs/adapter-cloudflare` (Workers + Workers Static Assets).

### Mixed toolchains

By default Octane owns every project `.tsrx`/`.tsx` module. When another framework's toolchain also compiles `.tsx` (including `ReactCompat`/`OctaneCompat` projects), pass `requireDirective: true` to the Vite, Rspack, or Rsbuild integration:

- `.tsrx` is always Octane's — nothing else compiles the syntax.
- A project `.tsx`/`.ts`/`.js` is Octane's only when it opens with `/** @jsxImportSource octane */` (full compilation for `.tsx`; hook slotting for `.ts`/`.js`, used for custom Octane hooks shared across islands).
- A pragma naming a registered renderer's intrinsics module (e.g. `@octanejs/three/intrinsics`) claims the file the same way; a foreign source (`react`, `@emotion/react`) claims nothing. Unmarked project modules pass through to the host framework's pipeline, with a warning when they import from `octane` (usually a forgotten pragma).
- To route some `.tsrx` through another tsrx compiler (such as `@tsrx/react`), list those paths in the integration's `exclude` option. Installed packages keep their package-manifest decision, so bindings need no pragmas.

## The `octane` CLI

Every command emits `--json` output and uses fixed exit codes (`3` = doctor found problems).

| Command | Purpose |
| --- | --- |
| `create` | Scaffold a new app into an empty directory |
| `doctor` | Diagnose quiet misconfigurations: duplicated runtime, missing `jsxImportSource`, plain `tsc` over `.tsrx`, wildcard `declare module '*.tsrx'`. `--fix` repairs the mechanical ones |
| `analyze` | Compile every `.tsrx` through the project's own Octane and report compiler diagnostics |
| `init` | Wire Octane into an existing project |
| `add` | Install a binding by the React package it ports |
| `explain` | Decode a minified production error |
| `mcp add` | Register the MCP server with Claude Code, Codex, Cursor, or VS Code |

Run `octane doctor` first when an Octane project fails to compile or render without a clear error.

## Profiling

Pass `profile: true` to `octane()` (Vite), `new OctaneRspackPlugin()` (Rspack), or `pluginOctane()` (Rsbuild). With `@octanejs/mdx`, pass the same value to `octaneMdx()`. Profiling is client-only and independent of HMR/dev metadata.

Profile builds add bounded component events, schedule-to-render delay, and Chrome custom tracks; normal builds omit compiler metadata. In DevTools use `globalThis.__OCTANE_PROFILER__`, or import `profiler` from `octane/profiling` for summaries, recent render causes, raw events, and Chrome Trace Event export. An explicit `octane/profiling` import keeps the recorder in the build even when `profile` is false.

Octane's duration is component render plus synchronous DOM work; inclusive time contains descendants, self time subtracts nested component spans. Raw props/state/actions/DOM values and absolute paths are not retained by default.

## Publishing libraries

Ship the complete authored source graph — `.tsrx`, `.tsx`, `.ts`, `.js` — point package exports at that source, and let the consuming application compile it. Do not publish precompiled Octane output.

## Browser support

- Start with current evergreen browsers. The website playground uses Chrome/Edge 111, Firefox 114, Safari/iOS 16.4, matching Vite 8's default build target.
- The ordinary DOM runtime calls `Element.replaceChildren()` (Chrome/Edge 86, Firefox 78, Safari 14), `String.prototype.replaceAll()` (Chrome/Edge 85, Firefox 77, Safari 13.1), and `queueMicrotask()` directly — API lower bounds, not a guarantee that every feature works there.
- Releases 0.1.9–0.1.34 also used `Object.hasOwn()` in component capability checks; 0.1.35 removed it and added scheduling, observer, media-query, and mobile-input compatibility fixes. Check the installed version before applying current guidance to an older release.
- Form actions need `SubmitEvent.submitter` (Safari 15.4 for full support). Core `module server` RPC uses `fetch` and a serializer requiring `Object.hasOwn()` (Chrome/Edge 93, Firefox 92, Safari 15.4).
- Deferred hydration and behavior roots use `AbortController` and, for streamed-DOM observation, `MutationObserver`. Custom abort reasons need `AbortSignal.reason` (Chrome/Edge 98, Firefox 97, Safari 15.4).
- Feature-detected: view-transition animation and `Element.moveBefore()`; `idle()` falls back to a timer without `requestIdleCallback`; `visible()` activates immediately without `IntersectionObserver`; `media()` supports legacy media-query listeners. `ReadableStream`/`TextEncoder` are needed where `renderToReadableStream` executes — normally the server.
- The core package publishes modern ESM; browser syntax targets do not polyfill DOM or JS APIs. Load missing polyfills before the application.
