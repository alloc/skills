# SQLite-Specific Guidance

Use this reference only when the project targets SQLite or SQLite-specific deployment behavior matters.

## Strengths

- Embedded database with minimal operations burden.
- Excellent local development, test fixtures, local-first apps, edge/client storage, and single-user tools.
- Durable single-file database when used on appropriate storage.
- Good read performance and simple deployment.
- WAL mode for better reader/writer coexistence.

## Guardrails

- SQLite serializes writes. It is not a high-write-concurrency server database.
- Enable and verify foreign-key enforcement through the driver or connection settings.
- Use `STRICT` tables when available and type enforcement matters.
- Be cautious on network filesystems or environments with unreliable file locking.
- Treat live database copying carefully; use SQLite backup mechanisms where possible.
- Remember that many schema changes require table rebuilds.

## Pragmas

Use pragmas deliberately and document why:

- `PRAGMA foreign_keys = ON`
- `PRAGMA journal_mode = WAL`
- `PRAGMA busy_timeout = ...`
- `PRAGMA optimize`
- `PRAGMA integrity_check`
- `PRAGMA foreign_key_check`

Connection-level pragmas may need to be set for every new connection, depending on driver behavior.

## Schema Notes

- Consider `INTEGER PRIMARY KEY` for rowid-backed primary keys when suitable.
- Use `CHECK` constraints to enforce booleans, enums, and numeric bounds.
- Use `STRICT` tables for stronger type checks when the target SQLite version supports them.
- Avoid assuming declared column types behave like Postgres types.

## Migration Notes

SQLite supports a subset of direct `ALTER TABLE` operations. For unsupported changes, rebuild the table and preserve indexes, triggers, foreign keys, and data explicitly.

After risky migrations or imports, run:

```sql
PRAGMA foreign_key_check;
PRAGMA integrity_check;
```

## Review Questions

- Is SQLite appropriate for the expected write concurrency?
- Are connection pragmas applied consistently?
- Does the app use transactions for multi-statement writes?
- Are database files stored on safe local storage?
- Does backup or sync logic avoid corrupting live files?

## Primary Sources

- SQLite documentation: https://sqlite.org/docs.html
- SQLite WAL: https://sqlite.org/wal.html
- SQLite isolation: https://sqlite.org/isolation.html
- SQLite PRAGMA statements: https://sqlite.org/pragma.html
- SQLite ALTER TABLE: https://sqlite.org/lang_altertable.html
