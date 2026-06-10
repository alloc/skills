---
name: sem
description: Use sem for semantic, entity-level code diffs, impact analysis, blame, history tracing, and compact AI context generation; prefer JSON output for automation and agent workflows.
---

# sem

Use `sem` when line diffs are too noisy and you need entity-level information about code changes, dependencies, affected tests, blame, or concise context for an AI agent.

## Prefer JSON

Prefer machine-readable output whenever the result will be parsed, piped, attached to a bug report, used in CI, or consumed by another agent:

```bash
sem diff --format json | jq
sem impact MyEntity --json | jq
sem blame path/to/file.ts --json | jq
sem trace MyEntity --json | jq
sem context MyEntity --json | jq
```

Use terminal/plain/markdown output only when a human will read the result directly.

## Semantic diffs

`sem diff` reports additions, modifications, deletions, renames, and moves at the entity level, such as functions, classes, properties, config keys, Markdown sections, and data rows.

```bash
# Working tree changes.
sem diff --format json

# Staged changes only.
sem diff --staged --format json

# One commit.
sem diff --commit <sha> --format json

# Commit range.
sem diff --from <ref> --to <ref> --format json

# Restrict by extension.
sem diff --file-exts .ts .tsx --format json

# Include inline before/after content when useful.
sem diff --staged --verbose --format json
```

`sem diff --stdin --format json` can analyze supplied file-change input without requiring a git repository.

## Impact analysis

Use impact analysis before changing or reviewing an entity to find directly related code.

```bash
sem impact <entity> --json
sem impact <entity> --file path/to/file.ts --json
sem impact <entity> --deps --json
sem impact <entity> --dependents --json
sem impact <entity> --tests --json
sem impact <entity> --file-exts .ts .tsx --json
```

Use `--file` when multiple entities share the same name.

## Blame and trace

Use blame for file-level authorship/change information, and trace for entity history across recent commits.

```bash
sem blame path/to/file.ts --json
sem trace <entity> --json
sem trace <entity> --file path/to/file.ts --limit 100 --json
sem trace <entity> --file path/to/file.ts --verbose --json
```

## AI context

Use context generation to gather a bounded, entity-centered context bundle before asking an AI agent to implement or review a change.

```bash
sem context <entity> --json
sem context <entity> --file path/to/file.ts --budget 12000 --json
sem context <entity> --file-exts .ts .tsx --json
```

## Supported content

`sem` parses source code and structured files. Common supported families include TypeScript/JavaScript, Python, Go, Rust, Java, C/C++, C#, Ruby, PHP, Swift, Elixir, Bash, HCL/Terraform, Kotlin, Fortran, Vue, XML, ERB, Svelte, JSON, YAML, TOML, CSV/TSV, and Markdown.
