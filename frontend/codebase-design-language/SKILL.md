---
name: codebase-design-language
description: Analyze an existing product UI and write a concise, evidence-based design guide plus a small JSON companion so coding agents can build new screens that fit the product.
---

# Codebase-Derived Design Language

Use this workflow when asked to document how an existing product's interface works so future implementation can reuse its visual and interaction patterns. The goal is practical guidance, not a complete design system or a catalog of every screen.

## Deliverables

Write these files at the repository root unless the user specifies another location:

- `DESIGN_LANGUAGE.md`: roughly 1,500–3,000 words for humans and coding agents.
- `design-language.json`: a small companion containing only high-confidence implementation details.

Keep the guide compact enough to read before implementing a feature. Favor explicit defaults, examples, and references to real components over design jargon or exhaustive token lists. Do not modify product UI code as part of this analysis unless separately requested.

## Workflow

### 1. Discover the foundations

Inspect the codebase to locate:

- global styles, theme definitions, CSS variables, and token files
- shared UI primitives and layout components
- typography and icon setup
- route or page inventory
- recurring shell, navigation, page, panel, and toolbar components

Use focused repository searches and import references to find likely canonical components. Avoid trying to statically parse or inventory every style value.

### 2. Select a representative sample

Choose about 5–10 important screens that together show the app shell, a main workflow, forms, lists, detail views, settings, overlays, and common empty or loading states where available. Do not inspect every route. Follow component usage from those screens back to shared implementations.

Prefer source inspection. Run the application only when source abstractions leave a meaningful question unresolved, such as responsive behavior or conflicting implementations. Do not make screenshot or image analysis a prerequisite.

### 3. Establish dominant patterns and confidence

Look for repeated conventions in typography, color, spacing, shape, layout, controls, navigation, feedback, and interaction. Weigh evidence in this order:

1. Shared primitives and theme definitions.
2. Patterns repeated across multiple screens.
3. Patterns used by newer or core features.
4. Isolated implementations.

Use only these confidence labels when useful:

- **Canonical**: clearly established by shared primitives or consistent product-wide use.
- **Common**: frequent, but not fully consistent.
- **Local**: feature-specific or supported by too little evidence to generalize.

Do not turn a one-off observation into a product rule. If two patterns remain genuinely common, describe the conflict briefly and give a clear default for new work.

### 4. Identify canonical implementation references

Record the actual names and repository paths for components that future work should reuse: buttons, fields, selects, menus, dialogs, tooltips, navigation items, page layouts, and empty states as applicable. Prefer a component reference over restating its visual properties. Include only references verified in the repository.

Cheap searches for common UI imports, route names, and shared layout usage may help choose the sample. Treat counts as clues, not proof: shared primitives and cross-screen consistency matter more than raw frequency.

### 5. Write the guide

Use this structure in `DESIGN_LANGUAGE.md`:

1. **Product Character** — 5–8 concise bullets about density, hierarchy, color restraint, navigation, and overall interaction feel.
2. **Visual Language** — dominant typography, color, spacing, borders and radii, icon, and motion conventions. Include exact values only when supported and useful.
3. **Layout** — the 3–5 primary page or workspace patterns.
4. **Interaction** — action hierarchy, form behavior, menus, dialogs, feedback, and destructive actions.
5. **Canonical Components** — a short purpose-to-component table with repository paths.
6. **Building New UI** — about 10–20 direct, actionable rules for composing new screens.
7. **Inconsistencies** — only conflicts likely to affect future implementation, along with the recommended default.

Write like a field guide. For example: “Use `PageLayout` for standard screens. Most hierarchy comes from spacing and typography; avoid adding nested cards without a clear grouping need.” Explain uncertainty when evidence is mixed. Omit low-value history and obscure one-off styling.

### 6. Write the JSON companion

Keep `design-language.json` small and valid JSON. Include only high-confidence values and real component paths. A useful shape is:

```json
{
  "typography": {
    "fontFamily": "Inter",
    "bodySize": "14px"
  },
  "spacing": {
    "controlGap": "8px",
    "pagePadding": "24px"
  },
  "shape": {
    "controlRadius": "6px"
  },
  "components": {
    "button": "src/components/Button.tsx",
    "dialog": "src/components/Dialog.tsx"
  }
}
```

This is an example schema, not a required set of keys. Omit uncertain or unavailable values rather than guessing. Do not encode the full guide, all tokens, or confidence taxonomy in JSON.

## Completion Review

Before finishing, confirm that:

- Both requested outputs exist and the JSON parses.
- The guide names verified components and gives a usable default for new screens.
- Conclusions reflect repeated evidence, with local exceptions labeled as such.
- The sample covers the product's main structural patterns without claiming exhaustive coverage.
- A coding agent could start a new screen from the guide without needing to rediscover the product's basic conventions.

Report the files produced and any material evidence gaps. Do not refactor or normalize inconsistencies unless separately requested.
