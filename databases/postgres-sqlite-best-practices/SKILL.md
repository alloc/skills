---
name: postgres-sqlite-best-practices
description: Best practices for designing, writing, reviewing, and optimizing PostgreSQL and SQLite databases. Use when Codex is creating schemas, queries, migrations, transactions, indexes, or data-access code for Postgres, SQLite, or SQL that should stay portable between them.
---

# Postgres and SQLite Best Practices

## Default Posture

Start portable, then specialize deliberately. Prefer SQL and schema patterns that work in both PostgreSQL and SQLite unless the user asks for a specific engine, the existing project clearly targets one engine, or an engine-specific feature materially improves correctness, safety, or performance.

Do not assume managed-platform behavior. Avoid vendor-specific connection pools, auth functions, roles, schemas, extensions, dashboards, or migration systems unless they appear in the project.

## First Steps

1. Identify the target engine: Postgres, SQLite, both, or unknown.
2. Inspect constraints that change database advice: expected data size, write concurrency, hosted vs embedded deployment, migration tooling, ORM/query builder, framework, required extensions, and test database setup.
3. Prefer portable recommendations when the engine is unclear. Label engine-specific SQL as `Postgres only` or `SQLite only`.
4. Separate correctness from performance. Constraints, transactions, and safe migrations come before speed tweaks.
5. Show concrete SQL or application-code examples when the recommendation is non-obvious.

## Reference Routing

Read only the reference files that match the task:

| Task | Read |
| --- | --- |
| Engine choice, portability, or Postgres-vs-SQLite tradeoffs | `references/compat-engine-selection.md` |
| Tables, columns, data types, constraints, keys, timestamps | `references/schema-types-constraints.md` |
| Query shape, indexes, pagination, aggregation, joins | `references/query-indexes.md` |
| `EXPLAIN`, plan inspection, or slow-query diagnosis | `references/query-explain.md` |
| Schema changes, backfills, rollback planning, destructive DDL | `references/migrations-safe-patterns.md` |
| Transactions, isolation, locking, retries, write contention | `references/transactions-concurrency.md` |
| Prepared statements, ORM boundaries, batching, N+1 issues | `references/data-access-patterns.md` |
| SQL injection, privileges, secrets, backups, destructive safeguards | `references/security-and-safety.md` |
| Vacuum/analyze, statistics, integrity checks, maintenance | `references/monitor-maintenance.md` |
| Deliberate Postgres-specific design | `references/postgres-only.md` |
| Deliberate SQLite-specific design | `references/sqlite-only.md` |

Use `postgres-only.md` or `sqlite-only.md` only when engine-specific behavior is intentional or already present.

## Always Check

Before finalizing database work, verify:

- Target engine assumptions are stated when they affect the answer.
- Destructive changes have a safer migration path or an explicit justification.
- Constraints enforce core data invariants instead of relying only on application code.
- Query examples use parameters, not string interpolation.
- Index recommendations name the query shape they serve.
- Transaction boundaries are explicit for multi-step writes.
- Foreign-key enforcement and cascade behavior are intentional.
- Portability risks are labeled when SQL differs between Postgres and SQLite.
- Operational follow-up is included when data volume, lock duration, or vacuum/analyze behavior matters.

## Output Style

When responding to users:

- State whether the answer is portable, Postgres-specific, or SQLite-specific.
- Use the placeholder style that matches the surrounding project or ecosystem.
- Prefer before/after SQL for reviews and migrations.
- Explain performance advice in terms of query shape, cardinality, and planner behavior.
- Keep source links to primary PostgreSQL or SQLite documentation when citing engine behavior.
