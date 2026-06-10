---
name: sem
description: Use sem for semantic, entity-level code diffs, impact analysis, blame, entity listing, history logs, and compact AI context generation.
---

# sem

Use `sem` when line diffs are too noisy and you need entity-level information about code changes, dependencies, affected tests, blame, history, or concise context for an AI agent.

## Semantic diffs

`sem diff` reports additions, modifications, deletions, renames, and moves at the entity level, such as functions, classes, properties, config keys, Markdown sections, and data rows.

```bash
# Working tree changes.
sem diff

# Staged changes only.
sem diff --staged

# One commit.
sem diff --commit <sha>

# Commit range.
sem diff --from <ref> --to <ref>

# Restrict by extension.
sem diff --file-exts .ts .tsx

# Include inline before/after content when useful.
sem diff --staged --verbose
```

`sem diff --stdin` can analyze supplied file-change input without requiring a git repository.

## Impact analysis

Use impact analysis before changing or reviewing an entity to find directly related code.

```bash
sem impact <entity>
sem impact <entity> --file path/to/file.ts
sem impact <entity> --deps
sem impact <entity> --dependents
sem impact <entity> --tests
sem impact <entity> --file-exts .ts .tsx
```

Use `--file` when multiple entities share the same name.

## Blame and history

Use blame for file-level authorship/change information, and log for entity history across recent commits.

```bash
sem blame path/to/file.ts
sem log <entity>
sem log <entity> --file path/to/file.ts --limit 100
sem log <entity> --file path/to/file.ts --verbose
```

## Entity listing

Use `sem entities` to list entities under a file or directory path.

```bash
sem entities
sem entities path/to/file.ts
sem entities path/to/directory
```

## AI context

Use context generation to gather a bounded, entity-centered context bundle before asking an AI agent to implement or review a change.

```bash
sem context <entity>
sem context <entity> --file path/to/file.ts --budget 12000
sem context <entity> --file-exts .ts .tsx
```

## Supported content

`sem` parses source code and structured files. Common supported families include TypeScript/JavaScript, Python, Go, Rust, Java, C/C++, C#, Ruby, PHP, Swift, Elixir, Bash, HCL/Terraform, Kotlin, Fortran, Vue, XML, ERB, Svelte, JSON, YAML, TOML, CSV/TSV, and Markdown.
