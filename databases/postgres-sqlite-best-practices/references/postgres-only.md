# Postgres-Specific Guidance

Use this reference when evaluating whether Postgres-specific behavior materially improves correctness, safety, or performance.

## Features Worth Specializing For

- Robust server-side concurrency with MVCC.
- Schemas, roles, privileges, and row-level security.
- Advanced indexing such as GIN, GiST, BRIN, expression, partial, and concurrent indexes.
- JSONB with operators and index support.
- Arrays, ranges, enums, domains, generated columns, and rich constraints.
- Extensions such as full-text search, PostGIS, trigram search, or UUID helpers when available.
- `RETURNING`, common table expressions, window functions, and advanced analytics.
- `LISTEN`/`NOTIFY`, advisory locks, and queue patterns where appropriate.

## Guardrails

- Verify extension availability before recommending extension-backed SQL.
- Do not use RLS casually. Policies need tests for allowed and denied access paths.
- Prefer `CREATE INDEX CONCURRENTLY` for large production tables when lock impact matters, but remember it cannot run inside a normal transaction block.
- Treat enum changes and type rewrites as migrations with rollout implications.
- Avoid overusing JSONB for relational data that needs constraints and joins.

## Common Patterns

Upsert:

```sql
INSERT INTO users (email, name)
VALUES ($1, $2)
ON CONFLICT (email)
DO UPDATE SET name = EXCLUDED.name
RETURNING id;
```

Partial unique index:

```sql
CREATE UNIQUE INDEX idx_users_active_email
ON users (lower(email))
WHERE deleted_at IS NULL;
```

Queue claim:

```sql
SELECT id
FROM jobs
WHERE status = 'queued'
ORDER BY created_at
FOR UPDATE SKIP LOCKED
LIMIT 1;
```

## Review Questions

- Is this feature available in the deployed Postgres version and extension set?
- Does the migration lock or rewrite a large table?
- Are privileges and ownership correct for runtime vs migration roles?
- Does this feature create a portability commitment the user accepts?
- Is there a simpler portable design that would be good enough?

## Primary Sources

- PostgreSQL feature documentation: https://www.postgresql.org/docs/current/
- PostgreSQL indexes: https://www.postgresql.org/docs/current/indexes.html
- PostgreSQL CREATE INDEX: https://www.postgresql.org/docs/current/sql-createindex.html
- PostgreSQL row security: https://www.postgresql.org/docs/current/ddl-rowsecurity.html
- PostgreSQL JSON types: https://www.postgresql.org/docs/current/datatype-json.html
