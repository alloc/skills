---
name: no-slop-ui
description: Design, implement, or review visible product interfaces with restrained, context-specific visual judgment and without generic AI-generated UI tropes. Do not use this skill unless the user explicitly requests it.
---

# No Slop UI

Create interfaces that feel deliberate, useful, and native to their product. Prefer clear hierarchy and direct interaction over decoration whose main purpose is to make the interface look designed.

## Boundaries

Apply this skill to visible interfaces across platforms and rendering technologies. Do not assume a web stack, a component library, a styling system, or any particular implementation primitive.

Treat these instructions as a visual-quality layer. Product requirements, accessibility, platform conventions, localization, data integrity, and an established design system take precedence. A distinctive brand or intentionally expressive experience is not slop merely because it is decorative.

## Establish the Context

Before making material visual decisions, inspect what is available:

- the interface's purpose, primary tasks, content, and expected audience;
- existing screens, components, design tokens, assets, and interaction patterns;
- target-platform conventions, input methods, viewport or window constraints, and accessibility requirements.

Preserve a coherent existing visual language unless the user asks to change it. When no design language exists, define the smallest useful set of choices for type, spacing, color, surfaces, controls, and motion. Do not introduce a new dependency or design system solely to achieve a particular look.

## Design Standard

- Let tasks and content determine the composition. Do not reach for a hero, card grid, side rail, or dashboard template before the information calls for it.
- Create hierarchy with structure, spacing, typography, and contrast before adding containers or effects.
- Use visual treatments coherently. Accents, surfaces, icons, and animation may support hierarchy, state, affordance, feedback, identity, atmosphere, or delight. Judge whether they serve this experience without obscuring content or interaction.
- Match information density to the work. Dense operational interfaces and spacious editorial interfaces have different legitimate needs.
- Write direct interface copy. Avoid vague promotional language in product surfaces unless the product calls for marketing copy.
- Make controls look and behave like controls on the target platform. Provide clear labels, focus or selection states, feedback, and sufficiently large interaction targets.
- Design real states, including loading, empty, error, disabled, selected, overflow, long content, and reduced-motion behavior where relevant.
- Use color semantically and maintain readable contrast. Start with the product's existing palette; if none exists, choose a restrained, coherent palette appropriate to the content and platform.
- Keep motion brief and purposeful. Repeated interactions should feel immediate; animation should explain change or provide feedback rather than advertise itself.

Read [references/patterns.md](references/patterns.md) before creating a new visual direction or conducting a broad visual audit. Use it as a diagnostic guide, not a mechanical ban list.

## Build or Revise

When implementation is in scope, work through the project's existing interface abstractions and platform-native primitives. Reuse suitable components and tokens. Change defaults only when the product or interaction requires it.

For an existing interface, identify the concrete problem before editing: weak hierarchy, excessive chrome, inconsistent geometry, unclear state, poor density, needless motion, or another observable issue. Prefer the smallest change that restores coherence over a broad restyle.

When the environment allows it, inspect the rendered interface at representative sizes and states. Verify usability as well as appearance; static polish does not compensate for broken layout, inaccessible interaction, or missing feedback.

## Review

Tie each finding to user experience or product meaning. Explain what is visually generic or misleading, why it weakens the interface, and what direction would improve it. Distinguish defects from taste preferences, and do not recommend churn when the existing choice is coherent and purposeful.

Prioritize findings that affect hierarchy, comprehension, interaction, consistency, or accessibility. Mention minor aesthetic preferences only when the user asks for exhaustive polish.
