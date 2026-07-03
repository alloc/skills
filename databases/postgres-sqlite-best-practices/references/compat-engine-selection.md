# Engine Selection and Portability

Use this reference when the target engine is unclear, the user asks whether to use Postgres or SQLite, or SQL must work across both.

## Selection Guide

Choose Postgres when the application needs high write concurrency, multi-user server access, robust roles and privileges, row-level security, advanced query planning, large datasets, complex analytics, extensions, online operations, or operational observability.

Choose SQLite when the application needs embedded or local storage, simple deployment, low operational overhead, single-user or low-write-concurrency workloads, local-first sync, test fixtures, edge/client storage, or a durable database file managed by the application.

Use portable SQL when the project is early, tests run on SQLite while production runs on Postgres, the same library supports both engines, or the cost of engine lock-in is not yet justified.

## Portability Rules

- Use standard table, column, constraint, join, and aggregate patterns when practical.
- Keep engine-specific SQL behind adapters, migrations branches, or clearly named helpers.
- Label code samples `Postgres only`, `SQLite only`, or `Portable`.
- Do not rely on identical type enforcement. Postgres enforces declared types strictly; SQLite has dynamic typing unless using `STRICT` tables.
- Do not assume identical DDL support. SQLite supports fewer direct `ALTER TABLE` operations than Postgres.
- Do not assume identical concurrency behavior. Postgres uses MVCC for many concurrent server workloads; SQLite allows many readers but serializes writers.
- Do not assume identical placeholder syntax. Match the project driver or ORM.

## Common Portability Friction

- Auto-increment identity syntax differs.
- Boolean storage differs, though many drivers abstract it.
- Timestamp defaults and timezone handling differ.
- JSON support differs in type, indexing, operators, and constraints.
- Case-insensitive matching differs.
- Full-text search differs.
- Upsert syntax overlaps but details and constraint targets can differ.
- Partial indexes exist in both engines, but supported expressions and planner behavior differ.
- Enum, array, range, exclusion constraint, RLS, and many extension-backed features are Postgres-specific.

## Adapter Pattern

Prefer a small engine boundary over scattered conditional SQL:

```ts
interface UserQueries {
  findActivePage(limit: number, cursor?: string): Promise<User[]>;
  markDeleted(id: string): Promise<void>;
}
```

Keep table semantics shared, and let the adapter own placeholder style, returning clauses, engine-specific pagination helpers, or specialized indexes.

## Test Matrix

For portable code, run database tests against both engines when feasible. If production uses Postgres and unit tests use SQLite, add at least one Postgres integration check for migrations, constraints, transaction behavior, and query syntax.

## Primary Sources

- PostgreSQL documentation: https://www.postgresql.org/docs/current/
- SQLite documentation: https://sqlite.org/docs.html
- SQLite foreign keys: https://sqlite.org/foreignkeys.html
- SQLite isolation: https://sqlite.org/isolation.html
