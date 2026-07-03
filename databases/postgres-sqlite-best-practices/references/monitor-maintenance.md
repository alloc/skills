# Monitoring and Maintenance

Use this reference for routine maintenance, statistics, vacuum/analyze behavior, integrity checks, and operational diagnosis.

## Maintenance Mindset

Database performance and safety depend on statistics, storage health, and routine checks. Recommend maintenance only in terms of the target engine and deployment model; do not invent dashboards or managed-service features unless the project uses them.

## Postgres

Postgres maintenance commonly involves:

- Autovacuum health.
- Table and index bloat signals.
- Stale planner statistics.
- Slow query logs or query-stat extensions when available.
- Lock waits and long-running transactions.
- Connection saturation.
- Replication lag when replicas exist.

Long-running transactions can prevent cleanup and make vacuum less effective. Large updates/deletes may require follow-up vacuum/analyze planning.

## SQLite

SQLite maintenance commonly involves:

- `PRAGMA integrity_check` or `quick_check` when corruption is suspected.
- `PRAGMA foreign_key_check` after migrations or imports.
- WAL checkpoint behavior for WAL-mode databases.
- `VACUUM` or incremental vacuum where file size reclamation matters.
- `ANALYZE` or `PRAGMA optimize` for planner statistics.
- Safe backups for live database files.

Do not treat SQLite database files as ordinary text files for live copying or concurrent writes.

## Slow Query Diagnosis

1. Capture the SQL and bound-parameter shape.
2. Check data volume and selectivity.
3. Inspect the query plan.
4. Check whether relevant statistics exist.
5. Add or adjust indexes only for confirmed access paths.
6. Re-check write overhead and migration cost.

## Operational Review Questions

- What table is expected to grow fastest?
- Which queries are latency-sensitive?
- Which writes happen most frequently?
- What maintenance tasks are automatic in this deployment?
- What happens when a migration fails halfway?
- How are backups created and restored?

## Smells

- Performance advice ignores table size and data distribution.
- Postgres table has heavy churn but no mention of vacuum/autovacuum.
- SQLite WAL file growth is treated as corruption without checking checkpoint behavior.
- Integrity checks are skipped after a risky SQLite rebuild.
- Monitoring advice assumes a cloud provider not present in the project.

## Primary Sources

- PostgreSQL routine vacuuming: https://www.postgresql.org/docs/current/routine-vacuuming.html
- PostgreSQL monitoring: https://www.postgresql.org/docs/current/monitoring.html
- SQLite PRAGMA statements: https://sqlite.org/pragma.html
- SQLite VACUUM: https://sqlite.org/lang_vacuum.html
- SQLite ANALYZE and PRAGMA optimize: https://sqlite.org/lang_analyze.html
