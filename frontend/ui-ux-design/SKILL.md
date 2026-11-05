---
name: ui-ux-design
description: Design, implement, or review web, native, and desktop interfaces with clear hierarchy, thoughtful interaction, and accessible behavior. Use for UI composition, usability improvements, or interface reviews, especially when avoiding generic AI-generated design.
---

# UI/UX Design

Create clean, thoughtful interfaces whose structure and behavior serve the people using them. Clean means coherent and easy to understand; it does not require sparse layouts, monochrome palettes, or a particular visual style.

## Start from the product

Use the actual tasks, content, audience, input methods, and operating environment to make design decisions. Do not prescribe aesthetics, palettes, or layouts from industry labels.

Inspect existing components, tokens, screens, assets, and platform conventions before changing the visual language. Detect the implementation stack from the project rather than assuming one. Preserve established patterns unless the requested change or a concrete usability problem justifies departing from them.

- **Extend an existing interface:** compose with its components and tokens. A new page does not require a new design system.
- **Establish a new direction:** choose the smallest coherent set of typography, spacing, color, surface, and interaction decisions needed for the work. Ground the composition in representative content before expanding it.
- **Fix or review an interface:** identify the observable problem and its effect on users. Prefer focused corrections over a broad restyle.

Do not generate design-system documents, style catalogs, or new dependencies by default. When reusable documentation is requested or necessary, record verified decisions in the project's existing home for design guidance. Read existing guidance before editing it and preserve unrelated decisions.

## Design standard

- **Content determines composition.** Choose layout and density for the task. Use hierarchy, alignment, typography, and spacing before adding containers or decorative effects.
- **Controls communicate meaning.** Make actions, selection, scope, and consequences clear. Keep common operations direct and preserve context across navigation.
- **State stays truthful.** Distinguish pending, successful, failed, and partial outcomes. Preserve user input and provide recovery where possible. Match confirmation or undo to the consequences.
- **Quality includes difficult states.** Account for relevant loading, empty, error, disabled, overflow, long-content, and interrupted-interaction states while designing the normal path.
- **Presentation supports comprehension.** Use coherent type, color, icons, and surfaces. Distinguish meaningful states without relying on color alone. Icons need semantics appropriate to their use, not just a consistent appearance.
- **Motion earns its place.** Use it for feedback, relationships, continuity, or intentional expression. Immediate state changes are valid. Keep interactions responsive and correctness independent of animation completion.
- **Accessibility shapes the design.** Support the relevant keyboard, pointer, touch, assistive-technology, text-scaling, and reduced-motion behavior from the start.

Read [design-judgment.md](references/design-judgment.md) when establishing a visual direction or diagnosing generic, cluttered, or poorly composed UI. Its examples are diagnostic clues, not a ban list.

Load the relevant detailed reference when designing or reviewing these areas; do not load every reference for a focused change. They provide decision criteria, common failures, and implementation considerations rather than fixed recipes.

| Area | Reference |
| --- | --- |
| Field design, validation, submission, async feedback, recovery | [Forms and feedback](references/forms-and-feedback.md) |
| Navigation structure, search, overlays, back behavior, restored context | [Navigation and orientation](references/navigation-and-orientation.md) |
| Composition, density, resizing, overflow, localization | [Layout and responsive behavior](references/layout-and-responsive.md) |
| Type hierarchy, readable content, semantic color, themes, icon use | [Typography and color](references/typography-and-color.md) |
| Interaction timing, interruption, reduced motion, rendering cost | [Motion and performance](references/motion-and-performance.md) |
| Chart selection, honest comparisons, tables, filtering, live data | [Data presentation](references/data-presentation.md) |

## Apply guidance at the right level

Keep these distinct when making decisions or reporting findings:

| Kind | How to apply it |
| --- | --- |
| Standard or project requirement | Identify the applicable criterion, platform, units, and exceptions. Verify it rather than treating a rule of thumb as proof of compliance. |
| Platform guidance | Prefer the target platform's interaction and accessibility conventions; account for input method and device context. |
| Product convention | Reuse established meaning and behavior. Resolve conflicts through evidence from shared components and actual workflows. |
| Design preference | Recommend with a concrete rationale and acknowledge reasonable alternatives. Do not present taste as a defect. |

Read [accessibility.md](references/accessibility.md) for accessibility decisions or reviews, especially before citing a numeric threshold. Read the relevant section of [verification.md](references/verification.md) when implementing or validating an interface; web, native, and desktop checks differ.

Prioritize by user impact, task frequency, and failure cost. Accessibility and correctness are baseline concerns; the remaining order depends on the interface. Data accuracy and comparison may dominate an analytics screen, while input and recovery may dominate a form. Decoration should not displace an unresolved usability problem.

## Deliver reviewable work

Verify the affected tasks and states with the tools and permissions available. Use representative content and relevant sizes or window configurations. Visual inspection can help when permitted, but source, semantics, interaction tests, and measurements remain useful evidence when it is unavailable.

For reviews, connect findings to comprehension, operability, consistency, or task outcomes. For implementation, explain material design choices and what was verified. Separate observed defects from preferences, and report unverified behavior without claiming comprehensive accessibility or visual validation.
