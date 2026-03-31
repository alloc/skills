---
name: readme-docs
description: Refresh README-style documentation, llms.txt, and best-practices docs from the current API declaration file or primary public API source.
---

# README Docs

Use this skill when updating public documentation such as `README`, `llms.txt`, best-practices docs, or docs-derived `skills/` content from an API declaration file or other primary public API source.

## Source of Truth

- Read the current declaration file or primary public API documentation first. Treat it as canonical for exported surface and documented behavior unless the task says otherwise.
- Re-read the existing `README`, `llms.txt`, any existing best-practices or conventions document, and the `skills/` directory if one exists before editing.
- If older prose conflicts with the source, repair the prose. Do not preserve stale wording for continuity.

## Workflow

1. Inventory which public docs exist and decide what each one should own before editing.
2. Update only the docs affected by the change. Keep diffs scoped; do not rewrite stable sections for style alone.
3. When public capabilities, signatures, overloads, defaults, tracked behavior, reactive getter behavior, constructor rules, composition rules, lazy initialization behavior, deprecations, or guidance-worthy usage patterns change, update every affected public doc.
4. When other public documentation is updated, update the `skills/` directory too if one exists and any skill content depends on those docs.
5. Keep examples source-accurate. When examples depend on signatures, inference, or cleanup behavior, make them match the source exactly.
6. When an API returns an unsubscribe, cleanup, or dispose handle, show that return value unless the example is explicitly about ignoring it.
7. After editing, reread the updated docs against the source and verify that terminology, examples, links, and ownership boundaries still agree.

## Document Contracts

### `README`

- Optimize for first-use success: quick mental model, install/import or setup, smallest useful example, then the most common tasks or patterns.
- Document public behavior, defaults, and constraints that affect adoption or daily use.
- Keep it usage-first rather than exhaustive. Link out instead of turning it into a full API reference or conventions dump.
- Include migration or deprecation callouts when a returning user would otherwise do the wrong thing.

### Best-practices or conventions doc

- Own prescriptive guidance: naming, inference, structure, composition, performance, cleanup, and "prefer X over Y" rules.
- Explain anti-patterns and edge cases that are easy to miss from the API surface alone.
- Do not duplicate onboarding material or exhaustive API listings from the `README` or source.

### `llms.txt`

- Be machine-friendly and exhaustive about public terminology, concepts, supported features, invariants, and best practices.
- Start with a glossary for repo-specific terms.
- Capture decision rules, caveats, and unsupported or non-idiomatic patterns when they matter for correct use.
- Keep it aligned with the current public surface and any guidance that materially affects correct generation.

### `skills/` docs

- Update only when a skill derives behavior, workflow, or constraints from the public docs.
- Keep skill instructions procedural and compact. Point to canonical docs or references instead of duplicating them.
- Treat skills as downstream guidance, not an alternate source of truth.

## Writing Guidance

- Do not invent behavior, guarantees, rationale, or compatibility claims that are not supported by the source.
- Use one canonical term for each concept across all docs.
- Prefer links and clear ownership boundaries over repeated prose.
- Focus on what users need to choose, do, or avoid; skip incidental implementation detail and private types unless they are part of the intended public experience.
- Prefer small, runnable examples over long narrative code dumps.
