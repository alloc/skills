---
name: library-docs
description: Create, audit, rewrite, or repair downstream-user documentation for TypeScript libraries, including README routing, public TSDoc, examples, docs/context.md, declaration emit, and API docs drift.
---

# Library Docs

Use this skill when a user asks to document a TypeScript package, rewrite a library README, document public exports, add or fix examples, sync docs after an API change, reduce docs drift, or design a compact downstream-user documentation system.

## Mission

Build documentation that helps downstream users discover, choose, and correctly use the published API while keeping maintenance cost low.

Default to this source-of-truth model:

- Public TSDoc owns factual API behavior.
- Runnable examples own usage and composition patterns.
- `docs/context.md` owns concepts, lifecycle, invariants, terminology, and stable API-selection guidance.
- `README.md` owns entry, install, one minimal example, and routing.
- Generated declarations own exact signatures and module shape.
- `CHANGELOG.md` is optional release notes, not an API reference.

Keep contributor setup, maintainer playbooks, release process, local development notes, and internal architecture out of consumer docs unless the user explicitly asks for those surfaces.

## Before Editing

1. Find the package boundary.
   - In monorepos, identify the relevant package root before changing files.
   - Inspect `package.json`, workspace config, export maps, source entrypoints, and package manager conventions.
2. Classify the request.
   - Narrow update: fix the requested surface and nearby source-of-truth gaps.
   - API-change follow-up: update TSDoc, affected examples, declarations, and only the concept docs that actually changed.
   - README rewrite: keep it short and route to deeper surfaces.
   - Full migration: redesign ownership across README, TSDoc, examples, context docs, and declaration emit.
3. For full migrations, new documentation systems, section schemas, or ownership disputes, read [documentation-system.md](./references/documentation-system.md). For small edits, keep this file in context and open the reference only if needed.

## Workflow

1. Inventory the published surface.
   - List public entrypoints and exported symbols from package metadata, source, and declarations if present.
   - Inspect `README.md`, `docs/`, `examples/`, `CHANGELOG.md` if present, public TSDoc, generated declarations, and docs-related scripts.
   - Note accidental exports, undocumented exports, stale declarations, non-runnable examples, and manual API-reference prose.
2. Diagnose drift.
   - Mark each important fact by its proper owner: TSDoc, example, context doc, README, declarations, or changelog.
   - Flag duplicated explanations, version-sensitive prose outside source, outdated examples, and consumer docs polluted with maintainer material.
   - Check whether examples and declaration emit are covered by existing scripts or CI.
3. Edit the owners, not every surface.
   - Move API facts into public TSDoc.
   - Replace long prose guides with small runnable examples when usage is the point.
   - Centralize non-local conceptual material in `docs/context.md`.
   - Collapse README content into purpose, installation, quick example, and documentation map.
   - Keep changelog entries concise and consumer-visible when a changelog already exists or the user asks for release notes.
4. Avoid unnecessary new surfaces.
   - Do not add `CHANGELOG.md`, migration docs, contributor docs, or broad guide trees by default.
   - Do not create hand-maintained API reference pages when generated declarations can provide exact signatures.
   - Do not add examples that duplicate an existing task or cannot reasonably be executed.
   - Do not add `docs/context.md` for a tiny package unless concepts, lifecycle, invariants, or API-selection guidance justify it.
5. Verify the edited system.
   - Re-read changed docs against public entrypoints and source.
   - Confirm examples import the real package path or intended local source path, use valid options, and show preferred defaults.
   - Confirm generated declarations align with the intended public entrypoints when declarations are part of the task.
   - Confirm consumer docs no longer contain contributor, release-process, or internal-only guidance.

## Verification

Discover existing commands before inventing new ones. Prefer the narrowest relevant checks:

- package typecheck or build
- declaration emit
- docs generation if present
- example tests or direct example execution
- lint or formatting only when the repo normally requires it for touched files

For a full migration, fix missing declaration emit when the package lacks a generated public signature surface. For a narrow docs-only request, report the declaration gap instead of silently expanding the change.

If examples cannot be executed locally, validate imports and option shapes against source and explain the skipped execution.

## Output

Produce concrete edits. In the final response, report:

- documentation surfaces changed
- source-of-truth ownership decisions that matter for future updates
- validation commands run and skipped
- remaining public API coverage gaps, stale declarations, or unexecuted examples
