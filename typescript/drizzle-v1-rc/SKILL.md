---
name: drizzle-v1-rc
description: Migrate, update, or review Drizzle ORM v0 code for the Drizzle v1 RC, including drizzle-orm, drizzle-kit, drizzle-seed, Relational Queries v1 removal, defineRelations-based Relational Queries v2, migration folder changes, casing, validators, RLS, arrays, generated columns, and drizzle-kit push/pull behavior.
---

# Drizzle v1 RC

Treat Drizzle v1 RC upgrades as a source migration, not a package bump. Check schema definitions, database initialization, relation declarations, relational queries, generated migrations, and kit config together.

## Upgrade Pass

1. Inspect installed Drizzle packages, `drizzle.config.*`, schema exports, relation files, database initialization, and migration scripts.
2. Update package names/imports first, then migrate code by compiler errors and targeted searches.
3. Prefer the new v1 APIs instead of compatibility shims. Relational Queries v1 is removed.
4. Run typecheck and the project's migration-generation/check commands before suggesting the upgrade is done.

## Package And Import Changes

- Install the RC packages with the repo's package manager: `drizzle-orm@rc` and `drizzle-kit@rc`.
- Replace validator package imports with the consolidated Drizzle exports for new work:
  - `drizzle-zod` -> `drizzle-orm/zod`
  - `drizzle-valibot` -> `drizzle-orm/valibot`
  - `drizzle-typebox` for `@sinclair/typebox` -> `drizzle-orm/typebox-legacy`
  - `drizzle-typebox` for `typebox` -> `drizzle-orm/typebox`
  - `drizzle-arktype` -> `drizzle-orm/arktype`
  - Effect schema -> `drizzle-orm/effect-schema`
- Replace `getTableColumns` with `getColumns`.
- Remove imports of old relation internals such as `relations`, `Relations`, `extractTablesRelationalConfig`, `createOne`, `createMany`, and `TableRelationsHelpers`.

## Relations V2

Replace per-table `relations(table, ...)` declarations with one `defineRelations(schema, ...)` entrypoint:

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

Pass `relations` to `drizzle()` instead of `schema` for relational queries:

```ts
import { relations } from "./relations";

export const db = drizzle(process.env.DATABASE_URL, { relations });
```

Use `defineRelationsPart(schema, ...)` only when the project already splits relation ownership; merge parts when constructing the DB: `{ relations: { ...baseRelations, ...extraRelations } }`.

Migration mapping:

- `fields` -> `from`; `references` -> `to`. Each can be a single column or an array.
- `relationName` -> `alias`.
- Use `optional: false` only when the related entity is guaranteed to exist and should be required in the result type.
- MySQL `mode` is no longer needed for RQB v2 initialization.
- A `many` relation can now stand alone if `from` and `to` make the join explicit.
- Model many-to-many with `through` instead of exposing junction rows in every query.

```ts
export const relations = defineRelations(schema, (r) => ({
  users: {
    groups: r.many.groups({
      from: r.users.id.through(r.usersToGroups.userId),
      to: r.groups.id.through(r.usersToGroups.groupId),
    }),
  },
}));
```

## Query Migration

- Use `db.query`, not `db._query`.
- Rewrite `where` callbacks to object filters.
- Rewrite `orderBy` callbacks to object sort declarations.
- Use `AND`, `OR`, `NOT`, and `RAW` inside object filters for complex predicates.
- Relation filters and `offset` on related objects are supported; use them directly when they replace hand-rolled joins or post-processing.
- After many-to-many relations use `through`, query the target relation directly instead of selecting junction tables with empty columns.

```ts
await db.query.users.findMany({
  where: {
    OR: [{ id: { gt: 10 } }, { name: { like: "John%" } }],
  },
  orderBy: { id: "asc" },
  with: {
    groups: true,
  },
});
```

Use `RAW: (table) => sql\`...\`` for SQL that cannot be expressed by object filters, especially JSON, array, function, or range predicates.

## Schema And Column Changes

- Replace global `drizzle({ casing: "camelCase" })` with table/view/schema casing builders such as `snakeCase.table(...)` and `camelCase.table(...)` from the dialect core package.
- Replace chained multidimensional arrays such as `column.array().array()` with string dimensions: `column.array("[][]")`.
- Replace `pgTable(...).enableRLS()` with `pgTable.withRLS(...)`.
- Ensure `.generatedAlwaysAs()` receives `sql\`...\`` or `() => sql\`...\``, not raw strings.
- For custom types, use the new `codec` option when driver-aware mapping is needed.

## Drizzle Kit And Migrations

- Expect the v3 migration folder layout: no `journal.json`; SQL files and snapshots are grouped into per-migration folders.
- `drizzle-kit drop` is removed.
- `schemaFilter` now defaults to all schemas for `push` and `pull`, not only `public`. Set `schemaFilter` explicitly, including glob patterns such as `app_*`, when scope must be limited.
- `drizzle-kit push --strict` is removed because strict confirmation is now default. Use `--force` to skip prompts and `push --explain` to preview SQL.
- Use `drizzle-kit check` before merging branches with migration changes; use `--ignore-conflicts` only when conflicts are understood.
- Run `drizzle-kit up` as part of migration upgrade validation because the migration table gains `name` and `applied_at`.
- `drizzle-kit pull --init` can initialize the migration table and mark the first pulled migration as applied.
- Config and schema files may use top-level `await` on Node.js.
- Only `.js`, `.mjs`, `.cjs`, `.jsx`, `.ts`, `.mts`, `.cts`, and `.tsx` schema files are processed.

## Review Checklist

- Search for `drizzle-orm/_relations`, `relations(`, `db._query`, `fields:`, `references:`, `relationName`, `schema:`, `mode:`, `casing:`, `enableRLS`, `array().array`, `generatedAlwaysAs(`, `getTableColumns`, `schemaFilter`, `--strict`, and `drizzle-kit drop`.
- Verify DB initialization uses the new relation object where relational queries are used.
- Verify generated migrations use the new folder structure and no stale `journal.json` assumptions remain in scripts or CI.
- Prefer typecheck failures and generated SQL diffs over broad manual rewrites when validating behavior.
