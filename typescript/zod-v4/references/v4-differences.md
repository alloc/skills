# Zod v4 Differences

Use this reference for Zod v4 feature orientation. It summarizes the v4 release notes and intentionally avoids migration procedure.

## Performance And Packaging

- Zod v4 is materially faster than v3 in the release benchmarks: roughly 14x faster string parsing, 7x faster array parsing, and 6.5x faster object parsing.
- Zod v4 dramatically reduces TypeScript compiler type instantiations for object-heavy schema composition. The release notes show a simple object/extend file dropping from more than 25,000 instantiations with `zod/v3` to roughly 175 with `zod/v4`.
- Zod v4 regular core bundle size is much smaller than Zod 3 in the release benchmark, and `zod/mini` is smaller still.

Do not overfit answers to exact benchmark numbers unless the user asks for release-note specifics. Use the trend to justify simpler schema composition and `zod/mini` consideration under bundle pressure.

## Import Surfaces

### Regular Zod

Use regular `zod` for most application code:

```ts
import * as z from "zod";
```

It keeps the familiar method-oriented API and should be the default unless bundle constraints or library-author needs say otherwise.

### Zod Mini

Use `zod/mini` for strict bundle-size constraints:

```ts
import * as z from "zod/mini";

const schema = z.optional(z.string());
const union = z.union([z.string(), z.number()]);
const extended = z.extend(z.object({ name: z.string() }), {
  age: z.number(),
});
```

Zod Mini replaces many methods with top-level wrapper functions for tree-shaking. Parsing methods remain methods:

```ts
z.string().parse("value");
z.string().safeParse("value");
await z.string().parseAsync("value");
await z.string().safeParseAsync("value");
```

Use `.check()` with first-class checks and refinements:

```ts
const numbers = z.array(z.number()).check(
  z.minLength(5),
  z.maxLength(10),
  z.refine((items) => items.includes(5)),
);
```

Common Mini checks include `z.lt`, `z.lte`, `z.gt`, `z.gte`, `z.positive`, `z.negative`, `z.multipleOf`, size and length checks, `z.regex`, case checks, substring checks, `z.property`, `z.mime`, and overwrite helpers such as `z.trim`, `z.toLowerCase`, and `z.toUpperCase`.

### zod/v4/core

`zod/v4/core` is the shared substrate beneath regular Zod and Zod Mini. It is mainly for schema-library authors, not ordinary app code. Reach for it when building tooling or libraries on top of Zod internals while supporting the v4 architecture.

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
