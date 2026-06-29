---
name: zod-v4
description: Use when writing, reviewing, or explaining Zod v4 schemas and APIs, especially when choosing v4-native features such as Zod Mini, metadata registries, JSON Schema conversion, recursive object getters, file schemas, locales, pretty errors, top-level string formats, template literals, number formats, stringbool, unified error customization, upgraded discriminated unions, multi-value literals, refinements inside schemas, overwrite transforms, or zod/v4/core. This is a Zod v4 differences and feature-orientation skill, not a v3-to-v4 migration playbook.
---

# Zod v4

## Operating Stance

Treat Zod v4 as a redesigned schema platform, not just a faster Zod 3. Prefer v4-native APIs when they clarify intent, reduce bundle size, improve TypeScript performance, or preserve runtime introspection.

Do not turn this skill into migration guidance. If the user asks for migration steps or breaking-change audits, use the official migration guide instead of inferring from this skill.

## Before Answering

1. Identify the task shape: schema design, API review, bundle-size advice, JSON Schema generation, error customization, recursive types, library integration, or explanation.
2. Read [references/v4-differences.md](references/v4-differences.md) when the answer depends on a specific Zod v4 feature, API name, or behavior.
3. Prefer examples that demonstrate the v4 capability directly. Avoid `zod@3` comparison code unless the user explicitly asks why an old pattern is no longer needed.
4. Preserve the distinction between regular `zod`, `zod/mini`, and `zod/v4/core`.

## Defaults

- Use regular `zod` for most application code.
- Use `zod/mini` only when strict bundle-size constraints justify its functional API.
- Use top-level string formats such as `z.email()` and `z.uuidv7()` instead of deprecated method forms like `z.string().email()` in new examples.
- Use `.meta()` or registries for schema metadata; keep metadata outside schema definitions unless the global registry is the right target.
- Use `z.toJSONSchema()` for first-party JSON Schema conversion and remember that global registry metadata is included.
- Use getter properties for recursive object fields; do not reach for `z.lazy()` patterns unless the surrounding code still requires them.
- Use `.overwrite()` when a transform preserves the inferred type and must remain introspectable; use `.transform()` when output type can truly change.
- Use unified `error` callbacks or strings for new error customization examples.

## Review Checklist

When reviewing Zod v4 code, check for:

- v4 APIs hidden behind older patterns that are now noisier or less introspectable.
- method-style string formats in new code where a top-level format would be clearer.
- transforms that should be `.overwrite()` because they preserve the output type.
- hand-rolled JSON Schema export paths that can be replaced by `z.toJSONSchema()`.
- recursive object code using casts where getter-based recursion would infer cleanly.
- discriminated unions that could now compose instead of flattening branches manually.
- bundle-sensitive code importing regular `zod` when `zod/mini` was explicitly required.
- library code depending on the full public API when `zod/v4/core` is the intended substrate.

## Source

This skill is based on the Zod v4 release notes fetched from `https://zod.dev/v4` with `sitefetch https://zod.dev/v4 --limit 0`.
