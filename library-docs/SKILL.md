---
name: library-docs
description: Design, audit, and update low-maintenance documentation systems for TypeScript libraries where factual API behavior lives in source TSDoc, usage lives in runnable `examples/*.ts`, concepts live in `docs/context.md`, and exact exported signatures live in emitted declaration files such as `dist/**/*.d.ts` or `dist/**/*.d.mts`. Use when Codex needs to create or revise library documentation structure, tighten ownership boundaries between `README.md`, source comments, examples, and docs, or reduce documentation drift in a library repository.
---

# Library Docs

Use this skill to build or repair a compact documentation system for a TypeScript library without letting prose drift away from the source.

## Default Stance

- Keep canonical facts adjacent to code.
- Prefer runnable examples over narrative guides.
- Keep one prose owner for each concept.
- Keep stable prescriptive guidance centralized in `docs/context.md`, not scattered across guides.
- Treat emitted declaration files in `dist/` as generated output, not an editing surface.
- Keep `README.md` thin and routing-oriented.
- Treat `CHANGELOG.md` as optional release notes, not a canonical API surface.

## Start Here

- Inventory `README.md`, `CHANGELOG.md` if present, `docs/`, `examples/`, public entrypoints, and exported symbols before editing.
- Determine whether the task is to define the system, migrate an existing repo toward it, or update docs after an API change.
- Read [documentation-system.md](./references/documentation-system.md) before changing document ownership, section schemas, or declaration-output rules.

## Workflow

1. Inventory the current documentation surfaces.
   - Identify where API facts, concepts, examples, top-level routing, and release notes currently live.
   - Flag duplicated explanations, stale guides, and hand-maintained API-prose content.
   - Note whether `CHANGELOG.md` exists and whether the repo expects manual release-note maintenance.
2. Assign each kind of information to one owner.
   - Move factual API behavior into public TSDoc.
   - Use runnable `examples/*.ts` only for canonical or materially different usage patterns.
   - Keep non-local conceptual material and stable best-practice guidance in `docs/context.md`.
   - Keep `README.md` focused on purpose, installation, one minimal example, and links.
   - Keep `CHANGELOG.md` limited to summary-level release notes for shipped user-visible changes.
   - Use emitted `dist/**/*.d.ts` or `dist/**/*.d.mts` files for exact signature lookup.
3. Rewrite the docs to match those boundaries.
   - Remove duplicated API detail from `README.md` and conceptual prose from surfaces that should only route or summarize.
   - Remove API facts from `CHANGELOG.md` when they belong in TSDoc, examples, or conceptual docs instead.
   - Normalize terminology across TSDoc, examples, and prose.
   - Preserve only the prose that cannot be derived from code or examples.
4. Tighten drift control.
   - Define or update build or type commands that emit declaration files into `dist/`.
   - Keep declaration output aligned with the library's public entrypoints and published surface.
5. Re-read the edited docs against the source.
   - Verify that every public export is documented somewhere appropriate.
   - Verify that each example earns its existence by covering a materially different pattern, and that it uses real imports, valid options, and preferred defaults.
   - Verify that conceptual docs still match the library's abstractions, invariants, and lifecycle.

## Decision Rules

- Update `docs/context.md` only when abstractions, lifecycle, invariants, terminology, API-selection guidance, or stable recommended patterns change.
- Update `README.md` only when the user-facing entry path, install path, or documentation routing changes.
- Update `CHANGELOG.md` only when the repo already maintains one or the task explicitly includes release-note work; keep entries concise and consumer-facing.
- Add or update `examples/*.ts` only when a change introduces a materially different user-facing task, workflow, or composition pattern.
- Use emitted `dist/**/*.d.ts` or `dist/**/*.d.mts` files as the exact exported-signature surface instead of hand-maintaining reference prose.
- Add migration or decision documents only when breaking changes or recurring architectural constraints justify them.

## Output Rules

- Produce concrete document edits, not commentary alone.
- Keep ownership boundaries explicit so future changes have one obvious place to land.
- Prefer deleting redundant prose over polishing duplicate explanations.
- Keep examples executable and small.
- When the repo does not yet emit declarations into `dist/`, add that as part of the migration instead of creating a manual `reference.md`.
