# Setting up TSRX for a Preact project

Use this guide when the user says something like "install TSRX", "use TSRX", "set up TSRX", or asks whether a Preact project needs TSRX packages.

## First check the project

1. Read `package.json` and identify the bundler, formatter, linter, editor tooling, and runtime package manager.
2. Check existing config files such as `vite.config.*`, `rspack.config.*`, `rollup.config.*`, `eslint.config.*`, `.prettierrc*`, `tsconfig.json`, and editor workspace settings.
3. Install only the TSRX packages that match tools the project actually uses.
4. Prefer the Preact-specific integration package when one exists.

## TSRX packages relevant to Preact users

These package names are from `packages/*/package.json` in `Ripple-TS/ripple`. Packages with the `@ripple-ts` scope and React/Solid/Vue/Ripple-specific packages are intentionally excluded.

| Package | Use when | How to verify whether it is needed |
| --- | --- | --- |
| `@tsrx/core` | The project needs the core TSRX compiler/runtime package directly. | Check whether another installed TSRX integration already depends on it. Add it directly only if project scripts, custom build steps, or docs import/use the core package explicitly. |
| `@tsrx/preact` | The project authors Preact components in `.tsrx` files. | Check for Preact in dependencies and planned or existing `.tsrx` Preact components. This is the main Preact TSRX package. |
| `@tsrx/vite-plugin-preact` | The Preact project is built with Vite. | Check for `vite`, `@preact/preset-vite`, or `vite.config.*`. Use this rather than generic or non-Preact plugins. |
| `@tsrx/rspack-plugin-preact` | The Preact project is built with Rspack. | Check for `@rspack/*`, `rspack`, or `rspack.config.*`. Use only for Rspack-based builds. |
| `@tsrx/bun-plugin-preact` | The project uses Bun as the build/transpile pipeline for Preact. | Check for `bun.lock`, Bun build scripts, or direct Bun plugin configuration. Do not add only because Bun is used as a package manager. |
| `@tsrx/typescript-plugin` | The project needs TypeScript editor/language-service support for `.tsrx`. | Check `tsconfig.json` for `compilerOptions.plugins`, editor errors in `.tsrx` files, or a request for IDE type support. |
| `@tsrx/prettier-plugin` | The project formats `.tsrx` files with Prettier. | Check for Prettier config or formatting scripts. Add only if Prettier is the formatter. |
| `@tsrx/eslint-parser` | ESLint must parse `.tsrx` files. | Check for ESLint config and lint scripts that should include `.tsrx`. Usually used with `@tsrx/eslint-plugin`. |
| `@tsrx/eslint-plugin` | ESLint should apply TSRX-specific linting. | Check for ESLint config and whether `.tsrx` files are linted. Pair with the parser when configuring ESLint for TSRX. |
| `@tsrx/mcp` | The user explicitly wants TSRX MCP/tooling integration. | Check for existing MCP configuration or an explicit request. Most Preact apps do not need this for build setup. |

## Minimal setup shape

For a typical Vite + Preact app, expect to add:

- `@tsrx/preact`
- `@tsrx/vite-plugin-preact`
- optional `@tsrx/typescript-plugin` for editor support
- optional `@tsrx/prettier-plugin` and `@tsrx/eslint-*` packages if the project already uses those tools

For other bundlers, swap the Vite plugin for the matching Preact integration (`@tsrx/rspack-plugin-preact` or `@tsrx/bun-plugin-preact`).
