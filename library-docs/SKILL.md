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
- Treat emitted declaration files in `dist/` as generated output, not an editing surface.
- Keep `README.md` thin and routing-oriented.

## Start Here

- Inventory `README.md`, `docs/`, `examples/`, public entrypoints, and exported symbols before editing.
- Determine whether the task is to define the system, migrate an existing repo toward it, or update docs after an API change.
- Read [documentation-system.md](./references/documentation-system.md) before changing document ownership, section schemas, or declaration-output rules.

## Workflow

1. Inventory the current documentation surfaces.
   - Identify where API facts, concepts, examples, and top-level routing currently live.
   - Flag duplicated explanations, stale guides, and hand-maintained API-prose content.
2. Assign each kind of information to one owner.
   - Move factual API behavior into public TSDoc.
   - Move usage patterns into runnable `examples/*.ts`.
   - Keep non-local conceptual material in `docs/context.md`.
   - Keep `README.md` focused on purpose, installation, one minimal example, and links.
   - Use emitted `dist/**/*.d.ts` or `dist/**/*.d.mts` files for exact signature lookup.
3. Rewrite the docs to match those boundaries.
   - Remove duplicated API detail from `README.md` and conceptual prose from surfaces that should only route or summarize.
   - Normalize terminology across TSDoc, examples, and prose.
   - Preserve only the prose that cannot be derived from code or examples.
4. Tighten drift control.
   - Define or update build or type commands that emit declaration files into `dist/`.
   - Keep declaration output aligned with the library's public entrypoints and published surface.
5. Re-read the edited docs against the source.
   - Verify that every public export is documented somewhere appropriate.
   - Verify that examples use real imports, valid options, and preferred defaults.
   - Verify that conceptual docs still match the library's abstractions, invariants, and lifecycle.

## Decision Rules

- Update `docs/context.md` only when abstractions, lifecycle, invariants, terminology, or API-selection guidance changes.
- Update `README.md` only when the user-facing entry path, install path, or documentation routing changes.
- Add or update `examples/*.ts` whenever a user-facing task, workflow, or composition pattern changes.
- Use emitted `dist/**/*.d.ts` or `dist/**/*.d.mts` files as the exact exported-signature surface instead of hand-maintaining reference prose.
- Add migration or decision documents only when breaking changes or recurring architectural constraints justify them.

## Output Rules

- Produce concrete document edits, not commentary alone.
- Keep ownership boundaries explicit so future changes have one obvious place to land.
- Prefer deleting redundant prose over polishing duplicate explanations.
- Keep examples executable and small.
- When the repo does not yet emit declarations into `dist/`, add that as part of the migration instead of creating a manual `reference.md`.
