# Query Performance and Indexing

Use this reference for query rewrites, index recommendations, joins, pagination, aggregation, and read-path design.

## Start With Query Shape

Describe the query before choosing an index:

- Equality filters: `WHERE account_id = ?`
- Range filters: `WHERE created_at >= ?`
- Sort order: `ORDER BY created_at DESC`
- Join keys: `JOIN orders ON orders.customer_id = customers.id`
- Limit/window: `LIMIT 50`, cursor pagination, grouped aggregate
- Selectivity: how many rows the filter keeps

An index is useful when its leading columns match selective filters, join keys, or ordering the query can exploit.

## Composite Indexes

Put equality predicates first, then range/order columns:

```sql
CREATE INDEX idx_events_account_created
ON events (account_id, created_at DESC);
```

It serves queries like:
```sql
SELECT *
FROM events
WHERE account_id = ?
ORDER BY created_at DESC
LIMIT 50;
```

Avoid adding both `(account_id)` and `(account_id, created_at)` unless both are independently justified.

## Covering Indexes

Consider covering indexes for hot, narrow lookups where the engine can answer from the index alone. Balance this against write cost and index size.

```sql
CREATE INDEX idx_users_email_lookup
ON users (lower_email, id, status);
```

Do not add wide covering indexes by default.

## Partial and Expression Indexes

Use partial indexes for common filtered subsets:

```sql
CREATE INDEX idx_tasks_open_due
ON tasks (due_at)
WHERE completed_at IS NULL;
```

Use expression indexes for repeated computed lookups, but keep the query expression identical to what the engine expects.

## Pagination

Prefer keyset pagination for large or frequently changing result sets:

```sql
SELECT *
FROM events
WHERE account_id = ?
  AND (created_at, id) < (?, ?)
ORDER BY created_at DESC, id DESC
LIMIT 50;
```

`OFFSET` is acceptable for small admin lists, but it becomes slower and less stable as pages get deeper.

## Joins and Aggregates

- Index foreign-key columns used in joins.
- Aggregate after filtering whenever possible.
- Watch for accidental fanout when joining one-to-many tables before aggregating.
- Prefer `EXISTS` for existence checks instead of joining and deduplicating.

## Write Cost

Every index slows writes and consumes storage. Remove or avoid indexes that do not serve a real query, duplicate a prefix of another index without reason, or support a stale access pattern.

## Smells

- Index recommendation without naming the query it serves.
- Indexing every foreign key without checking write volume and access paths.
- Single-column indexes that cannot satisfy a composite filter plus sort.
- `LIKE '%term%'` expected to use a normal B-tree index.
- Deep `OFFSET` pagination on large tables.

## Primary Sources

- PostgreSQL indexes: https://www.postgresql.org/docs/current/indexes.html
- SQLite query planner: https://sqlite.org/queryplanner.html
- SQLite optimizer overview: https://sqlite.org/optoverview.html
