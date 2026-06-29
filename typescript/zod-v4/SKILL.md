---
name: zod-v4
description: Use whenever writing, reviewing, debugging, or explaining Zod code. Focus on Zod v4 APIs, defaults, and feature differences; this is not a v3-to-v4 migration playbook.
---

# Zod v4

## Operating Stance

Treat Zod v4 as a redesigned schema platform, not just a faster Zod 3. Prefer v4-native APIs when they clarify intent, improve TypeScript performance, or preserve runtime introspection.

Do not answer as though this were migration guidance. If the user asks for migration steps or breaking-change audits, use the official migration guide instead.

## Before Answering

1. Identify the task shape: schema design, API review, JSON Schema generation, error customization, recursive types, or explanation.
2. Prefer examples that demonstrate the v4 capability directly. Avoid `zod@3` comparison code unless the user explicitly asks why an old pattern is no longer needed.

## Defaults

- Use regular `zod` for most application code.
- Use top-level string formats such as `z.email()` and `z.uuidv7()` instead of deprecated method forms like `z.string().email()` in new examples.
- Use `.meta()` or registries for schema metadata; keep metadata outside schema definitions unless the global registry is the right target.
- Use `z.toJSONSchema()` for first-party JSON Schema conversion and remember that global registry metadata is included.
- Use getter properties for recursive object fields; do not reach for `z.lazy()` patterns unless the surrounding code still requires them.
- Use `.overwrite()` when a transform preserves the inferred type and must remain introspectable; use `.transform()` when output type can truly change.
- Use unified `error` callbacks or strings for new error customization examples.

## Review Checklist

When reviewing Zod v4 code, check for:

- v4 APIs hidden behind older patterns that are now noisier or less introspectable.
- method-style string formats in new code where a top-level format would be clearer.
- transforms that should be `.overwrite()` because they preserve the output type.
- hand-rolled JSON Schema export paths that can be replaced by `z.toJSONSchema()`.
- recursive object code using casts where getter-based recursion would infer cleanly.
- discriminated unions that could now compose instead of flattening branches manually.

## Performance And Packaging

- Zod v4 is materially faster than v3 in the release benchmarks: roughly 14x faster string parsing, 7x faster array parsing, and 6.5x faster object parsing.
- Zod v4 dramatically reduces TypeScript compiler type instantiations for object-heavy schema composition. The release notes show a simple object/extend file dropping from more than 25,000 instantiations with `zod/v3` to roughly 175 with `zod/v4`.
- Zod v4 regular core bundle size is much smaller than Zod 3 in the release benchmark.

Do not overfit answers to exact benchmark numbers unless the user asks for release-note specifics. Use the trend to justify simpler schema composition and v4-native patterns.

## Metadata And Registries

Zod v4 stores metadata in registries rather than inside schemas.

```ts
import * as z from "zod";

const registry = z.registry<{ title: string; description: string }>();
const email = z.email();

registry.add(email, {
  title: "Email address",
  description: "A reachable user email.",
});

const metadata = registry.get(email);
```

Use `.register()` when fluent code is clearer. It returns the original schema.

```ts
const email = z.email().register(registry, {
  title: "Email address",
  description: "A reachable user email.",
});
```

Use `z.globalRegistry` and `.meta()` for JSON Schema-compatible global metadata:

```ts
const user = z.object({
  email: z.email().meta({
    id: "email_address",
    title: "Email address",
    description: "Provide your email",
    examples: ["person@example.com"],
  }),
});
```

`.describe()` remains available for compatibility, but prefer `.meta({ description })` in new v4 examples.

## JSON Schema Conversion

Zod v4 has first-party JSON Schema conversion:

```ts
const schema = z.object({
  name: z.string(),
  points: z.number(),
});

const jsonSchema = z.toJSONSchema(schema);
```

Metadata from `z.globalRegistry` is automatically included in the output. Prefer this over third-party or hand-rolled conversion unless the project has specific unsupported requirements.

## Recursive Objects

Use getter properties for recursive object schemas:

```ts
const Category = z.object({
  name: z.string(),
  get subcategories() {
    return z.array(Category);
  },
});

type Category = z.infer<typeof Category>;
```

This also supports mutual recursion:

```ts
const User = z.object({
  email: z.email(),
  get posts() {
    return z.array(Post);
  },
});

const Post = z.object({
  title: z.string(),
  get author() {
    return User;
  },
});
```

The resulting schemas are plain `ZodObject` instances, so methods like `.pick()`, `.partial()`, and `.extend()` remain available.

## File Schemas

Use `z.file()` to validate `File` instances:

```ts
const imageFile = z.file()
  .min(10_000)
  .max(1_000_000)
  .mime(["image/png"]);
```

`.min()` and `.max()` constrain file size in bytes. `.mime()` constrains MIME type.

## Internationalization And Errors

Configure global locales through `z.config()`:

```ts
z.config(z.locales.en());
```

Use `z.prettifyError(error)` for official user-readable error formatting:

```ts
const result = schema.safeParse(input);

if (!result.success) {
  console.log(z.prettifyError(result.error));
}
```

Formatting is not currently configurable in the release notes.

## Top-Level String Formats

Prefer top-level string format constructors in new v4 code:

```ts
z.email();
z.uuidv4();
z.uuidv7();
z.uuidv8();
z.ipv4();
z.ipv6();
z.cidrv4();
z.cidrv6();
z.url();
z.e164();
z.base64();
z.base64url();
z.jwt();
z.lowercase();
z.iso.date();
z.iso.datetime();
z.iso.duration();
z.iso.time();
```

The method equivalents, such as `z.string().email()`, still exist but are deprecated and planned for removal in the next major version.

`z.email()` accepts a custom regex pattern. Zod exposes common patterns such as `z.regexes.html5Email`, `z.regexes.rfc5322Email`, and `z.regexes.unicodeEmail`.

```ts
const htmlEmail = z.email({ pattern: z.regexes.html5Email });
```

## Template Literal Schemas

Use `z.templateLiteral()` to model TypeScript template literal types at runtime:

```ts
const cssUnits = z.enum(["px", "em", "rem", "%"]);

const cssLength = z.templateLiteral([z.number(), cssUnits]);
// `${number}px` | `${number}em` | `${number}rem` | `${number}%`
```

Schemas that can be stringified contribute internal regexes to the final regex. Built-in string formats are enforced; custom refinements are not represented in the concatenated regex.

## Number Formats

Use v4 numeric formats for fixed-width ranges:

```ts
z.int();
z.float32();
z.float64();
z.int32();
z.uint32();
z.int64();
z.uint64();
```

`int`, `float32`, `float64`, `int32`, and `uint32` return number schemas with inclusive bounds. `int64` and `uint64` return bigint schemas because their ranges exceed JavaScript safe number precision.

## stringbool

Use `z.stringbool()` for environment-style boolean coercion:

```ts
const flag = z.stringbool();

flag.parse("true"); // true
flag.parse("1"); // true
flag.parse("yes"); // true
flag.parse("false"); // false
flag.parse("0"); // false
flag.parse("no"); // false
```

Customize truthy and falsy strings when the application has a narrower vocabulary:

```ts
const flag = z.stringbool({
  truthy: ["yes", "true"],
  falsy: ["no", "false"],
});
```

Keep `z.coerce.boolean()` when JavaScript truthiness is the intended behavior.

## Error Customization

Use the unified `error` parameter for new v4 code:

```ts
z.string().min(5, { error: "Too short." });
```

Use a function when the message depends on the issue:

```ts
const name = z.string({
  error: (issue) =>
    issue.input === undefined ? "This field is required" : "Not a string",
});
```

Returning `undefined` lets default error handling continue.

## Discriminated Unions

`z.discriminatedUnion()` supports more discriminator schema shapes, including union and pipe discriminators:

```ts
const result = z.discriminatedUnion("status", [
  z.object({ status: z.literal("ok"), data: z.string() }),
  z.object({ status: z.union([z.literal("cached"), z.literal("stale")]) }),
  z.object({ status: z.literal("fail").transform((value) => value.toUpperCase()) }),
]);
```

Discriminated unions can compose:

```ts
const BaseError = z.object({
  status: z.literal("failed"),
  message: z.string(),
});

const result = z.discriminatedUnion("status", [
  z.object({ status: z.literal("success"), data: z.string() }),
  z.discriminatedUnion("code", [
    BaseError.extend({ code: z.literal(400) }),
    BaseError.extend({ code: z.literal(401) }),
    BaseError.extend({ code: z.literal(500) }),
  ]),
]);
```

## Multi-Value Literals

Use `z.literal([...])` instead of unions of literals when representing a fixed literal set:

```ts
const successCode = z.literal([200, 201, 202, 204]);
```

## Refinements And Overwrites

Refinements live inside schemas in v4, so schema methods can be interleaved after `.refine()`:

```ts
const emailish = z.string()
  .refine((value) => value.includes("@"))
  .min(5);
```

Use `.overwrite()` for transforms that preserve the inferred type and should remain introspectable:

```ts
const squaredCapped = z.number()
  .overwrite((value) => value ** 2)
  .max(100);
```

Use `.transform()` for transforms that can change the output type or cannot be represented as same-type overwrites.
