---
name: small-audience-ui-design
description: Design, implement, or review interfaces for a small, known audience, optimizing for speed, precision, and fluency over repeated use.
---

I’d optimize for **speed, precision, and fluency over repeated use**. That permits denser layouts, shared shorthand, and deliberate learning costs. Base those choices on the audience’s actual knowledge and habits; intelligence alone doesn’t establish familiarity.

Here’s how I’d rewrite it.

Universal rules are requirements. Conditional guidance applies within those constraints.

The universal rules:

1. **Reuse established patterns.** Introduce new components or interactions when they materially improve the workflow.
2. **Keep behavior consistent.** Similar controls should behave similarly. Stable meaning matters more than visual uniformity.
3. **Make learning worthwhile.** Unfamiliar interactions need a clear, lasting benefit. Once learned, their behavior must remain predictable.
4. **Acknowledge interactions immediately.** Make progress, success, and failure observable. Prefer changes in the interface over redundant notifications.
5. **Keep state truthful.** Never imply completion before success is established.
6. **Preserve work.** Never silently lose input or progress. Make failures recoverable wherever possible.
7. **Make controls precise.** Users must be able to identify and operate them accurately. Compact targets are acceptable when they work reliably; overlapping or ambiguous targets are not.
8. **Match safeguards to consequences.** Prefer reliable undo. Use previews, warnings, or confirmation when the consequences justify the interruption.
9. **Preserve orientation and context.** Navigation should be predictable and retain relevant work, selection, filters, and position.
10. **Maintain legibility.** Text, controls, and important states must remain clear in the audience’s actual working environment.
11. **Support actual input methods well.** Optimize frequent workflows for the keyboard, pointer, or touch methods users employ.
12. **Make motion useful.** Animate to explain change, relationships, or progress. Keep frequent interactions fast.

Apply conditional guidance where relevant:

- **Copy:** Omit self-evident explanations. Use precise domain terms and established abbreviations when users understand them. Add the shortest label or example that resolves real ambiguity.
- **Density:** Favor useful information within reach. Group related elements, align comparisons, and establish hierarchy. Remove redundancy; retain information that supports decisions.
- **Complexity:** Keep frequent operations direct. Give regularly used advanced capabilities appropriate prominence. Defer information when it is irrelevant to the current task.
- **Discoverability:** Keep essential and occasional actions findable. Use shortcuts and compact controls for learned operations, with an accessible reference when recall is unreliable.
- **Efficiency:** Repeated work warrants shortcuts, batch actions, reusable settings, and sensible persistence. Make the scope and consequences of bulk actions clear.
- **Visual meaning:** Icons, color, position, and shorthand may carry learned meaning. Make consequential distinctions explicit enough to prevent costly mistakes.
- **Layout:** Use stable placement where it helps speed and memory. Reflow or disclose progressively when space requires it, accounting for the navigation and recall cost of hiding information.
- **Platform:** Follow native conventions when they help. Depart deliberately when the audience’s workflow gains enough to justify learning a different interaction.
- **States:** Design applicable empty, loading, disabled, success, and failure states. Explain failures and recovery. Preserve functioning content during partial failure.
- **Forms:** Request necessary input, validate near the relevant field, and preserve entries. Reuse known values where appropriate. Make consequential defaults visible and easy to change.
- **Instruction:** Explain unfamiliar concepts at the point of need. Prefer a concrete example or demonstration when it teaches faster than prose.
- **Audience fit:** Resolve usability questions with the actual users. A small audience makes direct observation, feedback, and targeted refinement practical.

To apply these rules:

1. Inspect the existing interface and observe the audience’s real workflows.
2. Identify frequent tasks, costly errors, and relevant prior knowledge.
3. Design the shortest complete interaction, including recovery.
4. Verify important states and actual input methods with representative users.
5. Remove friction and redundancy while preserving capability and control.

**Core principle: Minimize the effort this audience needs to work accurately and efficiently over time.**
