---
name: fallow-verification
description: Use Fallow as scoped TypeScript/JavaScript codebase evidence after nontrivial JS/TS edits, before deleting exports/files/dependencies, or when considering Fallow cleanup fixes. Run audit and dead-code trace commands, read JSON output, and act only on findings introduced by or clearly related to the current task.
---

# Fallow Verification

Use Fallow as a verification oracle for JavaScript and TypeScript work. Treat its output as structured evidence to narrow risk after an edit or before a deletion, not as permission to perform broad cleanup.

## Post-Edit Audit

After any nontrivial JavaScript or TypeScript code change, run:

```bash
pnpx fallow audit --format json --quiet
```

Read the JSON result before deciding what to do next. Use the overall status and findings to identify changed-code risk, dead code, health issues, duplication, complexity, or dependency signals connected to the current work.

Fix only findings that the current change introduced, exposed in touched code, or made clearly relevant to the task. Leave unrelated repo-wide cleanup alone unless the user explicitly asked for it.

If Fallow is unavailable, blocked by package-manager policy, or not configured for the repository, report that limitation and continue with the repository's normal verification commands.

## Deletion Evidence

Do not delete an export, source file, or dependency based only on search results, naming, or intuition. Get Fallow trace evidence first.

For an export:

```bash
pnpx fallow dead-code --trace <file>:<export> --format json
```

For a file:

```bash
pnpx fallow dead-code --trace-file <path> --format json
```

For a dependency:

```bash
pnpx fallow dead-code --trace-dependency <package> --format json
```

Read the trace output and combine it with the repository's tests, build, and any known dynamic usage. Static analysis can miss runtime imports, external package entrypoints, plugin registration, generated code, and reflection-style access.

## Auto-Fix Gate

Never start with a write-mode Fallow fix. Preview first:

```bash
pnpx fallow fix --dry-run --format json
```

Apply a suggested fix only when the preview is small, obviously safe, and directly related to the current task. After applying it, run the project's relevant build and tests.

## Boundaries

Use Fallow only for TypeScript and JavaScript codebase evidence. Avoid using it for full-repo cleanup, CI design, runtime coverage decisions, sweeping refactors, or unrelated modernization unless the user specifically asks for that scope.
