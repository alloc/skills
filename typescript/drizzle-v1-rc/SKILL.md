---
name: drizzle-v1-rc
description: Explain, use, or review Drizzle ORM v1 RC behavior when model knowledge may be stale, especially differences from Drizzle v0 around Relational Queries v2, defineRelations, object filters, drizzle-kit migrations, casing, validators, RLS, arrays, generated columns, and kit push/pull defaults.
---

# Drizzle v1 RC

Treat this as a compact correction layer for Drizzle knowledge that may not be in model training data. Prefer these v1 RC facts over older Drizzle v0 patterns when answering questions, writing examples, or reviewing code.

## Mental Model

- Drizzle v1 RC is not just a version bump; several public APIs and defaults changed.
- Relational Queries v1 was removed. Relational Queries v2 is centered on `defineRelations()`.
- `drizzle-kit` was substantially rewritten, with a new migration folder format and different push/pull defaults.
- Prefer v1 RC API names in examples. Mention v0 names only when explaining a difference.

## Relations V2

Relations now live in one `defineRelations(schema, ...)` declaration instead of per-table `relations(table, ...)` declarations.

```ts
import { defineRelations } from "drizzle-orm";
import * as schema from "./schema";

export const relations = defineRelations(schema, (r) => ({
  users: {
    posts: r.many.posts(),
  },
  posts: {
    author: r.one.users({
      from: r.posts.authorId,
      to: r.users.id,
    }),
  },
}));
```

Pass the relation object to `drizzle()` when using relational queries:

```ts
import { relations } from "./relations";

export const db = drizzle(process.env.DATABASE_URL, { relations });
```

Important differences from v0:

- `relations` from `drizzle-orm/_relations` is gone; use `defineRelations` from `drizzle-orm`.
- `fields` became `from`; `references` became `to`.
- `from` and `to` accept a single column or an array.
- `relationName` became `alias`.
- `optional: false` makes a related object required at the type level when that entity is guaranteed to exist.
- MySQL RQB setup no longer needs `mode: "planetscale"` or `mode: "default"`.
- `defineRelationsPart(schema, ...)` exists for splitting relation declarations, then spreading parts into one relations object.

## Many-To-Many

RQB v2 can hide junction tables behind `through`, so examples should query the target relation directly instead of returning junction rows and post-processing them.

```ts
export const relations = defineRelations(schema, (r) => ({
  users: {
    groups: r.many.groups({
      from: r.users.id.through(r.usersToGroups.userId),
      to: r.groups.id.through(r.usersToGroups.groupId),
    }),
  },
  groups: {
    participants: r.many.users(),
  },
}));

const users = await db.query.users.findMany({
  with: {
    groups: true,
  },
});
```

Relations can also define reusable filters:

```ts
export const relations = defineRelations(schema, (r) => ({
  groups: {
    verifiedUsers: r.many.users({
      from: r.groups.id.through(r.usersToGroups.groupId),
      to: r.users.id.through(r.usersToGroups.userId),
      where: { verified: true },
    }),
  },
}));
```

## Relational Query Shape

Use `db.query`, not `db._query`. Filters and ordering are object-based:

```ts
await db.query.users.findMany({
  where: {
    OR: [{ id: { gt: 10 } }, { name: { like: "John%" } }],
  },
  orderBy: { id: "asc" },
});
```

Object filters support `AND`, `OR`, `NOT`, relation filters, and `RAW`. Use `RAW: (table) => sql\`...\`` for JSON, array, function, range, or other SQL predicates that object operators cannot express.

Nested relations support `offset`:

```ts
await db.query.posts.findMany({
  limit: 5,
  offset: 2,
  with: {
    comments: {
      offset: 3,
      limit: 3,
    },
  },
});
```

## Schema API Differences

- Global `drizzle({ casing: "camelCase" })` was replaced by table/view/schema casing builders from dialect core packages, such as `snakeCase.table(...)` and `camelCase.table(...)`.
- Multidimensional arrays use string dimensions: `column.array("[][]")`, not chained `column.array().array()`.
- RLS uses `pgTable.withRLS(...)`, not `pgTable(...).enableRLS()`.
- `.generatedAlwaysAs()` accepts only `sql\`...\`` or `() => sql\`...\`` expressions, not raw strings.
- Custom types gained a `codec` option for driver-aware mapping.
- Column aliases can use `.as()`, such as `users.id.as("userId")`.

## Validation Packages

New validation work should import from `drizzle-orm` subpaths:

- `drizzle-orm/zod`
- `drizzle-orm/valibot`
- `drizzle-orm/typebox-legacy` for `@sinclair/typebox`
- `drizzle-orm/typebox` for `typebox`
- `drizzle-orm/arktype`
- `drizzle-orm/effect-schema`

Older standalone packages may still exist, but new updates are added in Drizzle ORM directly.

## Drizzle Kit Differences

- Migrations use the v3 folder structure: no `journal.json`; SQL files and snapshots live in migration folders.
- The migration table has new `name` and `applied_at` columns. Migrations are matched by full folder name, not just timestamp.
- The migrator applies every missing migration, regardless of timestamp ordering.
- `drizzle-kit drop` was removed.
- `drizzle-kit push --strict` was removed because confirmation for data-loss statements is now default. Use `--force` to skip prompts.
- `drizzle-kit push --explain` previews SQL without applying it.
- `drizzle-kit check` detects non-commutative migration branches; `--ignore-conflicts` bypasses this when conflicts are known.
- `drizzle-kit generate` detects incompatible migration branches and also accepts `--ignore-conflicts`.
- `drizzle-kit pull --init` creates the migration table and marks the first pulled migration as applied.
- `schemaFilter` now defaults to all schemas for `push` and `pull`, not only `public`; glob patterns such as `app_*` are supported.
- Config and schema files can use top-level `await` on Node.js.
- Schema processing only considers `.js`, `.mjs`, `.cjs`, `.jsx`, `.ts`, `.mts`, `.cts`, and `.tsx`.

## Other V1 RC Additions

- JIT row mappers can be enabled with `drizzle({ ..., jit: true })`.
- Codecs normalize request/response mapping across driver and JSON/array contexts.
- MSSQL and CockroachDB dialect support were added.
- NetlifyDB driver support was added.
- Effect support includes `@effect/sql-pg` and `drizzle-orm/effect-schema`.
- SQLcommenter tags can be appended with `.comment("tag")`.
- `.prepare(name)` can omit the name.
