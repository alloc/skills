---
name: postgres-sqlite-best-practices
description: Best practices for designing, writing, reviewing, and optimizing PostgreSQL and SQLite databases. Use when Codex is creating schemas, queries, migrations, transactions, indexes, or data-access code for Postgres, SQLite, or SQL that should stay portable between them.
---

# Postgres and SQLite Best Practices

## Default Posture

Start portable, then specialize deliberately. Prefer SQL and schema patterns that work in both PostgreSQL and SQLite unless the user asks for a specific engine, the existing project clearly targets one engine, or an engine-specific feature materially improves correctness, safety, or performance.

Do not assume managed-platform behavior. Avoid vendor-specific connection pools, auth functions, roles, schemas, extensions, dashboards, or migration systems unless they appear in the project.

## Core Rules

- State whether guidance is portable, Postgres-specific, SQLite-specific, or based on an unknown engine.
- Treat constraints, transaction safety, and migration reversibility as correctness concerns; handle them before performance tuning.
- Tie index and query-performance advice to the query shape, data distribution, and planner behavior it serves.
- Use concrete SQL or application-code examples when the recommendation changes behavior or risk.
- Cite primary PostgreSQL or SQLite documentation when relying on detailed engine behavior.

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
