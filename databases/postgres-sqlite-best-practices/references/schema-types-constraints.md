# Schema, Types, and Constraints

Use this reference for table design, column choices, keys, nullability, checks, generated columns, timestamps, and relationship modeling.

## Design Order

1. Name the domain invariant.
2. Represent it with columns and relationships.
3. Enforce it with constraints where the engine can do so.
4. Add indexes for lookup paths after constraints are clear.
5. Keep application validation for user experience, not as the only data-protection layer.

## Keys and Identity

- Prefer stable surrogate primary keys when rows are referenced broadly or natural keys can change.
- Keep natural-key uniqueness with `UNIQUE` constraints when the domain requires it.
- Use composite primary keys only when the relationship itself is the entity, such as join tables.
- Avoid exposing rowid-like implementation details across service boundaries.

## Nullability

- Default to `NOT NULL` for required values.
- Use nullable columns only when `unknown`, `not applicable`, or `not yet provided` are valid states.
- Avoid sentinel values such as empty string, `0`, or epoch timestamps for missing data.
- In unique constraints, remember that `NULL` semantics can differ from user expectations. Add partial indexes or checks when needed.

## Foreign Keys

- Declare foreign keys for real relationships.
- Choose `ON DELETE` behavior deliberately: `RESTRICT`/`NO ACTION` for protected parents, `CASCADE` for ownership, `SET NULL` for optional references.
- In SQLite, ensure foreign-key enforcement is enabled by the connection or framework.
- Index child foreign-key columns when they are used for joins, deletes, or cascades.

## Checks and Domain Constraints

Use `CHECK` constraints for bounded values, state machines, positive quantities, date ordering, and mutually exclusive columns.

```sql
CHECK (amount_cents >= 0)
CHECK (starts_at < ends_at)
CHECK (status IN ('draft', 'published', 'archived'))
```

For complex state transitions, combine database constraints for impossible states with transactional application logic for allowed transitions.

## Types

- Use integer cents or fixed-precision numeric types for money. Avoid floating point for monetary amounts.
- Store timestamps consistently. Prefer UTC instants for cross-timezone event times.
- Use text for identifiers that originate outside the database.
- Be careful with JSON columns. Add generated columns, expression indexes, or checks for fields that become query-critical.
- In SQLite, consider `STRICT` tables when type enforcement matters and the deployment supports them.

## Timestamps

- Use `created_at` for insertion time when it matters.
- Use `updated_at` only if the project has a reliable update mechanism.
- Do not rely on app servers in different time zones to produce comparable local timestamps.
- For audit needs, prefer append-only event/history tables over repeatedly overwriting a row.

## Normalization

- Normalize data that has independent identity, lifecycle, or permissions.
- Denormalize only for a measured read path or a deliberate cache.
- When denormalizing, document the owner of the derived value and how it is repaired.

## Smells

- Missing foreign keys for application-enforced relationships.
- Nullable columns with no domain meaning.
- Status stored as free-form text without a check or enum-like constraint.
- Timestamps stored in mixed time zones or mixed formats.
- JSON blobs used to avoid schema design for core queryable data.

## Primary Sources

- PostgreSQL constraints: https://www.postgresql.org/docs/current/ddl-constraints.html
- PostgreSQL data types: https://www.postgresql.org/docs/current/datatype.html
- SQLite datatypes: https://sqlite.org/datatype3.html
- SQLite foreign keys: https://sqlite.org/foreignkeys.html
