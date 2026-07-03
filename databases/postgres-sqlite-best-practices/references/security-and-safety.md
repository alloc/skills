# Security and Operational Safety

Use this reference for SQL injection, privileges, secrets, backups, destructive commands, tenant isolation, and safe database operations.

## SQL Injection

- Use parameterized queries for values.
- Use allowlists for identifiers such as column names, sort keys, and table names; parameters usually cannot bind identifiers.
- Avoid raw SQL escape helpers unless the driver documentation explicitly supports the use case.
- Treat search, sort, filter, and JSON path inputs as untrusted.

## Privileges

For Postgres, use least-privilege roles where the project has role management:

- Application roles should not own schema objects by default.
- Migration roles can have broader DDL permissions than runtime roles.
- Read-only jobs should not have write permissions.
- Row-level security can protect tenant data, but only when policies are tested and enabled deliberately.

SQLite has file-level access rather than server roles. Protect the database file, directory permissions, backups, and encryption approach where relevant.

## Secrets

- Keep connection strings and credentials out of source.
- Avoid logging full URLs, passwords, tokens, or SQL statements with sensitive bound values.
- Rotate credentials when exposure is plausible.
- Use environment or secret-management conventions already present in the project.

## Destructive Safeguards

Before `DROP`, `TRUNCATE`, bulk `DELETE`, bulk `UPDATE`, or table rebuilds:

- Confirm environment targeting.
- Confirm backup/restore path.
- Use transactions where the engine and operation support it.
- Add a `WHERE` clause or explicit justification when modifying a subset.
- For large changes, preview affected row counts.

```sql
SELECT count(*) FROM sessions WHERE expires_at < ?;
DELETE FROM sessions WHERE expires_at < ?;
```

## Tenant and Authorization Safety

- Include tenant/account predicates in every tenant-scoped query.
- Prefer composite uniqueness that includes tenant keys where names are tenant-local.
- Test authorization boundaries with rows from multiple tenants.
- Avoid relying only on UI filters for data separation.

## Backups and Recovery

- Mention backups when recommending destructive migrations or corruption repair.
- For SQLite, copy/backup using engine-safe mechanisms when the database may be live.
- For Postgres, ensure logical dumps, physical backups, or managed backup settings match the recovery need.
- A backup strategy is incomplete until restore has been tested.

## Smells

- Dynamic `ORDER BY ${request.query.sort}` without an allowlist.
- Runtime app user has schema-owner permissions without reason.
- Tenant-scoped table queried by primary key alone.
- Destructive migration without backup or environment guard.
- SQLite database file stored where unrelated processes or users can modify it.

## Primary Sources

- PostgreSQL privileges: https://www.postgresql.org/docs/current/ddl-priv.html
- PostgreSQL row security: https://www.postgresql.org/docs/current/ddl-rowsecurity.html
- SQLite backup API: https://sqlite.org/backup.html
