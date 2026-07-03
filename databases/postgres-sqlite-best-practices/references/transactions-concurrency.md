# Transactions and Concurrency

Use this reference for transaction boundaries, isolation, locking, retries, write conflicts, and contention.

## Transaction Boundaries

Use a transaction when multiple statements must commit or fail together:

```sql
BEGIN;
UPDATE accounts SET balance_cents = balance_cents - ? WHERE id = ?;
UPDATE accounts SET balance_cents = balance_cents + ? WHERE id = ?;
INSERT INTO ledger_entries (...);
COMMIT;
```

Keep transactions short. Do not hold a transaction open while waiting on network calls, user input, long file work, or unrelated computation.

## Correctness Patterns

- Use constraints for invariants that must survive concurrency.
- Use conditional updates for compare-and-set flows.
- Re-read or lock rows when decisions depend on current state.
- Add idempotency keys for retried external operations.
- Retry serialization failures, deadlocks, and SQLite busy/write conflicts only when the operation is safe to retry.

## Postgres Concurrency

Postgres supports many concurrent readers and writers with MVCC, but locks still matter for row updates, DDL, foreign keys, and unique checks.

Use row locks deliberately:

```sql
SELECT *
FROM jobs
WHERE status = 'queued'
ORDER BY created_at
FOR UPDATE SKIP LOCKED
LIMIT 1;
```

This is Postgres-specific and useful for worker queues. State the tradeoff: skipped rows may be processed later, and starvation must be considered.

## SQLite Concurrency

Classic SQLite is excellent for embedded workloads, but writes are serialized. WAL mode improves reader/writer coexistence, not multi-writer throughput.

Some SQLite-compatible providers or alternate engines relax the single-writer model. For example, Turso supports MVCC-based concurrent writes when `PRAGMA journal_mode = 'mvcc'` is enabled and transactions use `BEGIN CONCURRENT`; conflicting transactions must roll back and retry. Treat this as provider-specific behavior, not portable SQLite.

For SQLite applications:

- Keep write transactions short.
- Configure busy timeouts through the driver or connection settings.
- Use WAL for persistent databases when appropriate.
- Avoid using a classic single-writer SQLite database as a high-write shared server database.
- Be careful on network filesystems and environments with unreliable file locking.

## Isolation

Do not assume the same anomalies or lock behavior across engines. If a workflow depends on exact isolation semantics, read the engine-specific documentation and write a concurrency test that runs against the target engine.

## Smells

- Multi-step write sequence without a transaction.
- Long transaction wraps API calls or expensive computation.
- Check-then-insert race without a unique constraint or upsert.
- Retry loop around non-idempotent side effects.
- SQLite used for high-concurrency server writes without distinguishing classic single-writer behavior from provider-specific concurrent-write support and retry requirements.

## Primary Sources

- PostgreSQL transactions: https://www.postgresql.org/docs/current/tutorial-transactions.html
- PostgreSQL explicit locking: https://www.postgresql.org/docs/current/explicit-locking.html
- PostgreSQL transaction isolation: https://www.postgresql.org/docs/current/transaction-iso.html
- SQLite isolation: https://sqlite.org/isolation.html
- SQLite WAL: https://sqlite.org/wal.html
- Turso concurrent writes: https://docs.turso.tech/tursodb/concurrent-writes
