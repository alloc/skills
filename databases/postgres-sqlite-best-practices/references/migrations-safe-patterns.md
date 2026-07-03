# Safe Migrations

Use this reference for schema changes, data migrations, backfills, rollback planning, and destructive DDL.

## Migration Principles

- Prefer additive, backward-compatible changes.
- Separate schema changes from large data backfills.
- Make deployments tolerate old and new schema versions during rollout.
- Avoid long locks on large production tables.
- Make destructive changes the final step, after code no longer depends on old data.
- Keep rollback realistic: some data migrations need a forward fix, not a clean reversal.

## Expand and Contract

For risky changes, use this sequence:

1. Add the new nullable column/table/index.
2. Deploy code that writes both old and new representations when needed.
3. Backfill in bounded batches.
4. Validate counts and constraints.
5. Switch reads to the new representation.
6. Enforce `NOT NULL`, uniqueness, or foreign keys.
7. Remove old columns/tables after a soak period.

## Adding Constraints

- Backfill and deduplicate data before adding uniqueness or foreign keys.
- Add `NOT NULL` only after all existing rows have valid values.
- In Postgres, consider validation strategy and lock behavior for large tables.
- In SQLite, many constraint changes require table rebuild patterns.

## Backfills

- Batch by primary key or another stable cursor.
- Keep transactions short enough for the workload.
- Make the backfill idempotent.
- Record progress if the job may be interrupted.
- Throttle if it competes with production traffic.
- Verify row counts and edge cases after completion.

## Destructive Changes

Avoid one-step drops or rewrites when data matters:

```sql
-- Risky
ALTER TABLE users DROP COLUMN name;
```

Prefer a staged removal with code first, then DDL after verification. If a destructive migration is unavoidable, state backup, restore, and downtime assumptions explicitly.

## SQLite Table Rebuilds

For SQLite changes that require a table rebuild, the usual shape is:

1. Disable or account for foreign-key constraints during the controlled rebuild.
2. Create a new table with the desired schema.
3. Copy data explicitly by column.
4. Recreate indexes, triggers, and constraints.
5. Swap table names in a transaction.
6. Run integrity and foreign-key checks.

Do not hand-wave this step; missing indexes or triggers after rebuilds are common migration bugs.

## Smells

- Migration mixes DDL, a huge backfill, and code assumptions in one step.
- `DROP`, `TRUNCATE`, or type rewrite appears without backup or rollout context.
- New required column has no default/backfill path.
- Unique constraint is added before duplicate cleanup.
- SQLite migration ignores indexes/triggers during table rebuild.

## Primary Sources

- PostgreSQL ALTER TABLE: https://www.postgresql.org/docs/current/sql-altertable.html
- PostgreSQL CREATE INDEX: https://www.postgresql.org/docs/current/sql-createindex.html
- SQLite ALTER TABLE: https://sqlite.org/lang_altertable.html
- SQLite foreign-key checks: https://sqlite.org/pragma.html#pragma_foreign_key_check
