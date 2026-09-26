# Styling: scoped `<style>` blocks

Contents: sibling scoping, block placement rules, themes and `apply`, class maps and `$class`, `:global()`, emission order and `injectStyle`, and `STYLE_*`/`CSS_*` diagnostics.

## Sibling-scoped blocks

A `<style>` block inside `.tsrx` markup is scoped to its **siblings**: it styles the items beside it and everything below them — never the element that contains it.

```tsrx
// Styles .card and everything inside it.
<>
	<style>.card { padding: 1rem; }</style>
	<article class="card">…</article>
</>
```

A block inside `<article>` styles the article's other children only — to style an element, the block and the element must be fragment siblings.

- The compiler adds the block's hash to its selectors and adds the same hash class to the elements the block reaches.
- Every children list holding a block is a sibling scope with its own hash; sibling blocks share one hash; nested scopes get their own. An element gets every enclosing hash class outer→inner, so outer rules reach nested scopes and inner rules never reach out.
- Blocks hold static CSS only — runtime values go through CSS custom properties. The only attributes are `ref` and `apply`.

## Placement rules

- A `@{ … }` body or directive body holds exactly one output node, and a block is an output node. A lone block as the output is `STYLE_STANDALONE_NEEDS_FRAGMENT`; a block beside the output is a multiple-outputs error — wrap both in a fragment, in `@if`/`@for`/`@switch`/`@try` branches too.
- Raw CSS in `<style>` is TSRX template syntax: standalone blocks are allowed only lexically inside a `@{ … }` body or a directive body, at any depth. In a plain `return <…>` function or at module scope it is `STYLE_STANDALONE_OUTSIDE_TEMPLATE`.
- A bare standalone `<style>` statement at module scope is an error — assign it to make a theme.
- In plain `.tsx`, `<style>{css}</style>` is an ordinary element passed through untouched — no scope, hash, or injection.

## Themes: assigned blocks, `apply`, class maps

Assigning a block yields a **theme** — a class map usable across components:

```tsrx
const theme = <style>
	.card { padding: 1rem; }
	.card > h2 { margin: 0; }
</style>;

export function Card() @{
	<article class={theme.$class}>…</article>
}
```

- A class map has `$class` (the block's hash, preceded by applied themes' classes) plus one key per class selector (`theme.card` → `hash card`). `$class` is reserved.
- Elements carrying a class-map entry also match its element rules, because the entry includes the hash.
- `<style apply={theme} />` adds `theme.$class` to the items beside it and everything below (never the containing element). `<style apply={theme}>…</style>` with CSS also declares that scope's block. `apply={[a, b]}` composes in order; a theme may apply another theme; a theme must be declared before the block that applies it.
- A same-module theme compiles to a string literal; an imported theme is read at runtime via `theme.$class`.
- Per-element opt-in: give elements `class={theme.$class}` or `class={theme.card}` and leave `apply` out — siblings stay untouched, and a child component can take the class through a prop (`<Card parentClass={theme.$class} />` → `<article class={parentClass}>`), landing before the child's own scope hash.
- Final class list: authored classes, scope hashes outer→inner, applied theme classes.

## Choosing a scoping form

| Need | Use |
| --- | --- |
| Own elements | A block beside them |
| A child component you own | Pass `theme.$class` or a class-map entry as a prop — a rename can't silently break the parent |
| A child you cannot change (third-party, rendered HTML/markdown) | `.wrapper :global(.their-class)` with a scoped prefix |
| Page-level state | `:global(.theme-dark) .card` or `:global([data-theme='dark']) .card` |
| Page-wide rules (`body`, resets, fonts) | A linked `.css` file — never a bare `:global` |

## `:global()`

`:global(…)` unscopes the wrapped part of a selector; the rest stays scoped. It may sit only at the start or end — `.card :global(.x) .title` is `CSS_GLOBAL_PLACEMENT`.

| Form | Output | Reach |
| --- | --- | --- |
| `:global(.toast)` | `.toast` | Page-wide, like a global stylesheet |
| `.card :global(.note)` | `.card.<hash> .note` | Only below your scoped `.card`, including a child's internals — never upward |
| `:global(.theme-dark) .card` | `.theme-dark .card.<hash>` | Your element under a page-level class |
| `.card:global(.is-open)` | `.card.<hash>.is-open` | Your element with a class a library toggles |

Block form: `:global { .toast { … } body { … } }` drops the wrapper and emits page-wide rules — the way to write several page-level rules at once. Nested under a scoped rule, `.card { :global { .note { … } } }` gives the same reach as `.card :global(.note)` with the prefix written once — recommended for styling several classes of a child you cannot change. Plain nesting `.card { .note { … } }` scopes both parts.

A scoped rule hashes only its first compound and adds `:where(.<hash>)` (zero specificity) to the rest, so scoped selectors stay easy to override.

## Emission and injection

- CSS is static: a block inside an `@if`/`@for` branch styles only that branch's elements, but its CSS is always in the module's stylesheet whichever branch renders. Rules wanted everywhere go outside the branch.
- CSS comes out in source order, outer scope first.
- Each compiled module carries one `injectStyle(hash, css)` call per scope: at module scope on the client (runs at module evaluation, deduped by hash, one `<style data-octane>` per sheet) and at the top of each component body on the server (a request collects only the sheets it rendered, returned as the `css` field).
- The CSS rides inside the compiled JavaScript — no bundler virtual CSS module.
- `<style href precedence>` is a React-style Float resource, not a scoped block.

## Diagnostics

Style errors are compile errors: `STYLE_APPLY_VALUE`, `STYLE_APPLY_TARGET`, `STYLE_APPLY_BEFORE_DECLARATION`, `STYLE_APPLY_DUPLICATE`, `STYLE_APPLY_UNSUPPORTED_HOST`, `STYLE_RESERVED_CLASS_KEY`, `STYLE_STANDALONE_AT_MODULE_SCOPE`, `STYLE_STANDALONE_OUTSIDE_TEMPLATE`, `STYLE_STANDALONE_NEEDS_FRAGMENT`, `STYLE_UNKNOWN_ATTRIBUTE`, `CSS_GLOBAL_PLACEMENT`.
