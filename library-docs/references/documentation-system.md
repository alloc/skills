# Documentation System

## Contents

- [Objective](#objective)
- [File Layout](#file-layout)
- [Source-of-Truth Model](#source-of-truth-model)
- [Document Responsibilities](#document-responsibilities)
- [Fixed Section Schemas](#fixed-section-schemas)
- [Public API Coverage Rules](#public-api-coverage-rules)
- [Example Design Rules](#example-design-rules)
- [Generation Pipeline](#generation-pipeline)
- [Drift-Control Policy](#drift-control-policy)
- [Maintenance Workflow](#maintenance-workflow)
- [Retrieval Model for AI Consumers](#retrieval-model-for-ai-consumers)
- [Non-Goals](#non-goals)
- [Optional Extensions](#optional-extensions)
- [Recommended Default System](#recommended-default-system)

## Objective

Design a minimal documentation system for TypeScript libraries that:

- keeps canonical facts adjacent to source code
- minimizes hand-maintained prose
- reduces documentation drift
- optimizes retrieval and interpretation by AI systems
- keeps maintenance cost low for low-traffic libraries

## File Layout

```text
README.md
docs/
  context.md
dist/
  **/*.d.ts             # generated declaration surface; never edited by hand
  **/*.d.mts            # generated declaration surface for ESM entrypoints
examples/
  *.ts
src/
  **/*.ts               # canonical TSDoc source
```

## Source-of-Truth Model

### Canonical sources

1. `src/**/*.ts` TSDoc
   Canonical source for factual API behavior.
2. `examples/*.ts`
   Canonical source for usage patterns and API composition.
3. `docs/context.md`
   Canonical source for concepts not cleanly expressible in code.

### Derived surfaces

4. `dist/**/*.d.ts` or `dist/**/*.d.mts`
   Generated declaration files used for exact signature and module-shape lookup.
5. `README.md`
   Thin entry document; may be partially generated or manually maintained, but should not duplicate exact API detail.

## Document Responsibilities

### `README.md`

Purpose: entry point and router.

Should contain:

- library purpose
- install
- one minimal happy-path example
- links to `docs/context.md`, relevant declaration files in `dist/`, and `examples/`

Should not contain:

- exhaustive API reference
- duplicated conceptual explanations
- task-specific guides
- version-sensitive details better owned by source comments or examples

### `src/**/*.ts` TSDoc

Purpose: factual reference for public API.

Should contain:

- summary of exported symbol behavior
- parameter and return semantics
- constraints and invariants
- side effects
- error behavior
- deprecation status
- related APIs
- short focused examples where useful

Should not contain:

- broad conceptual essays
- duplicate tutorial material
- unstable implementation notes unless externally relevant

### `examples/*.ts`

Purpose: executable documentation for canonical use.

Should contain:

- realistic end-to-end usage
- correct import paths
- valid option shapes
- common composition patterns
- minimal setup required to run

Should be:

- runnable
- small and focused
- named by task or workflow

### `docs/context.md`

Purpose: single conceptual document for non-local knowledge.

Should contain:

- mental model
- core abstractions
- lifecycle / data flow
- invariants
- tradeoffs
- terminology
- non-goals
- task-to-API mapping

Should remain:

- short
- stable
- library-specific
- intentionally non-redundant with TSDoc

### `dist/**/*.d.ts` and `dist/**/*.d.mts`

Purpose: exact exported signatures and module layout for readers who need the built public surface.

Should be:

- generated from source
- emitted from public entrypoints
- treated as disposable build output
- excluded from manual editorial ownership

Should not:

- become the primary authoring surface for API behavior
- expose internal-only symbols unintentionally

## Fixed Section Schemas

### `docs/context.md` schema

```md
# Overview

# When to Use

# When Not to Use

# Core Abstractions

# Data Flow / Lifecycle

# Common Tasks -> Recommended APIs

# Invariants and Constraints

# Error Model

# Terminology

# Non-Goals
```

Reuse this schema across libraries for consistent AI retrieval.

### `README.md` schema

```md
# <Library Name>

## Purpose

## Installation

## Quick Example

## Documentation Map
```

### TSDoc minimum schema for exported symbols

For each public export, include as applicable:

- summary line
- `@param`
- `@returns`
- `@throws`
- `@example`
- `@remarks`
- `@deprecated`
- `@see`

Not every tag is mandatory for every symbol, but every exported symbol should have at least a useful summary.

## Public API Coverage Rules

Treat **public exports** as the documentation surface.

Coverage rules:

- every public export must have TSDoc
- internal symbols should not be documented unless intentionally exposed
- declaration emit should only include symbols reachable from public entrypoints

Recommended interpretation of "public":

- anything exported from package entrypoints
- anything included in generated type declarations intended for consumers

## Example Design Rules

Use examples to replace most narrative guides.

Requirements:

- one example per task or usage pattern
- executable in CI
- no pseudo-code
- minimal fixture setup
- stable output or assertions where practical

Suggested naming:

```text
examples/basic-usage.ts
examples/configuration.ts
examples/error-handling.ts
examples/framework-integration.ts
```

Examples should demonstrate:

- canonical call order
- preferred defaults
- edge-safe usage
- realistic object shapes

## Generation Pipeline

### Inputs

- public entrypoints
- exported symbols
- TypeScript source
- declaration emit configuration

### Outputs

- `dist/**/*.d.ts` or `dist/**/*.d.mts`
- optionally README API link sections or symbol indices

### Pipeline steps

1. discover public entrypoints
2. resolve exported symbols
3. emit declaration files from the build
4. compare emitted output against published or checked-in artifacts when applicable
5. fail CI if declaration artifacts are stale or missing

### Constraints

- emitted declaration files must never be the primary authoring surface
- source comments must remain the editable truth
- declaration emit must be deterministic

## Drift-Control Policy

The system reduces drift by enforcing these rules:

- facts belong in TSDoc, not prose
- usage belongs in runnable examples, not guides
- concepts belong in exactly one prose file
- exact signatures belong in emitted declaration files, not hand-maintained reference pages
- README is routing-only
- no parallel explanations of the same API behavior

Practical rule:

> If a statement can be derived from source, declaration output, or examples, it should not be hand-maintained elsewhere.

## Maintenance Workflow

### When adding a new API

Update:

- source TSDoc
- one or more examples if user-facing
- declaration output

Do not update:

- `docs/context.md` unless the conceptual model changed
- `README.md` unless the primary entry path changed

### When changing API behavior

Update:

- TSDoc
- affected examples
- declaration output

Also update `docs/context.md` only if:

- abstractions changed
- invariants changed
- lifecycle changed
- recommended API selection changed

### When making breaking changes

Update:

- TSDoc
- examples
- declaration output
- `docs/context.md` if conceptual behavior changed

Add migration material only if the change is significant enough to justify it.

## Retrieval Model for AI Consumers

Support this predictable retrieval path:

1. `README.md` for top-level routing
2. `docs/context.md` for concepts and task selection
3. `dist/**/*.d.ts` or `dist/**/*.d.mts` for exact signatures and module layout
4. source TSDoc for factual behavior lookup
5. `examples/*.ts` for concrete usage and composition

This structure is optimized for AI because:

- exact exports live in emitted declaration files
- facts are local to source
- concepts are centralized
- examples are executable

## Non-Goals

Do not optimize the system for:

- a large tutorial tree
- a course-based learning path
- manually maintained guides for every use case
- duplicate reference content in prose form
- human-first editorial polish across many pages

Exclude these on purpose to keep the documentation set small, stable, and low-maintenance.

## Optional Extensions

### `docs/decisions.md`

Use only if architectural decisions or policy constraints recur often enough to warrant preservation.

### `docs/migrations/*.md`

Use only for major or externally disruptive upgrades.

Do not create either by default.

## Recommended Default System

For most libraries, the default implementation is:

- `README.md`
- `docs/context.md`
- `src/**/*.ts` with strong TSDoc coverage
- `examples/*.ts`
- emitted `dist/**/*.d.ts` or `dist/**/*.d.mts`
