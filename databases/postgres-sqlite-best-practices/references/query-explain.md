# Query Plans and EXPLAIN

Use this reference when reviewing slow queries, validating index usefulness, or explaining why a query plan changed.

## Plan Workflow

1. Capture the exact SQL after ORM/query-builder expansion.
2. Use representative parameter values when possible.
3. Inspect the plan before and after query/index changes.
4. Compare estimated rows with actual rows when the engine can report them.
5. Confirm the chosen index serves the intended filter, join, or order.
6. Check whether statistics are stale before assuming the planner is wrong.

## Postgres

Use `EXPLAIN` for estimated plans and `EXPLAIN ANALYZE` when it is safe to execute the query. For write queries, remember that `EXPLAIN ANALYZE` actually runs the statement.

Common useful options:

```sql
EXPLAIN (ANALYZE, BUFFERS)
SELECT ...
```

Look for:

- Sequential scans over large tables where a selective index should exist.
- Nested loops that multiply into many repeated lookups.
- Sort nodes that could be avoided by an index.
- Hash or merge joins chosen because they fit the data shape.
- Row-estimate errors that suggest stale stats or correlated predicates.
- High buffer reads that indicate disk-heavy work.

## SQLite

Use:

```sql
EXPLAIN QUERY PLAN
SELECT ...;
```

Look for whether SQLite searches using an index, scans a table, creates temporary B-trees for sorting/grouping, or misses an expression/partial index because the query text does not match.

Run `ANALYZE` or `PRAGMA optimize` as appropriate for persistent databases with meaningful data distribution.

## Interpreting Plans

- A sequential scan is not automatically bad. It can be right for small tables or unselective filters.
- An index scan is not automatically good. It can be slower when it visits many rows randomly.
- Planner estimates depend on statistics and data distribution.
- Test data can mislead. Small fixtures rarely reveal production join order, cardinality, or sort costs.
- Query plans are evidence, not decoration. Tie recommendations to the plan line that changes.

## Review Pattern

When proposing a plan-based fix, include:

- the problematic query shape
- the observed plan smell
- the schema/index change or query rewrite
- the expected plan improvement
- any write-cost or migration tradeoff

## Primary Sources

- PostgreSQL EXPLAIN: https://www.postgresql.org/docs/current/using-explain.html
- PostgreSQL planner statistics: https://www.postgresql.org/docs/current/planner-stats.html
- SQLite EXPLAIN QUERY PLAN: https://sqlite.org/eqp.html
- SQLite ANALYZE: https://sqlite.org/lang_analyze.html
