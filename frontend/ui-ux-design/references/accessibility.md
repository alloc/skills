# Accessibility: requirements and guidance

Use the standard and conformance level applicable to the project. The summaries here are a starting point, not a complete compliance checklist. For a conformance claim or an edge case, consult the criterion and its exceptions directly. WCAG criteria concern web content; native accessibility also requires platform-specific behavior and testing.

## Web requirements

| Concern | Applicable guidance |
| --- | --- |
| Text contrast | WCAG 2.2 AA generally requires 4.5:1 for normal text and 3:1 for large text. Large means at least 18pt, or 14pt bold, in CSS units. Inactive controls, incidental text, and logotypes have exceptions. Measure the actual foreground/background combination. |
| Pointer targets | WCAG 2.2 AA SC 2.5.8 specifies 24×24 CSS px with spacing, equivalent-control, inline, user-agent, and essential exceptions. Larger targets can improve usability; 44×44 is not the universal AA minimum. |
| Reflow | SC 1.4.10 generally requires vertical content to work at a width equivalent to 320 CSS px without two-dimensional scrolling. Content needing two-dimensional layout has exceptions, including tables and maps. |

Primary sources: [contrast](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html), [target size](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html), and [reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html).

Prefer semantic controls and visible labels. Give controls accessible names and appropriate states. Hide decorative icons from the accessibility tree when equivalent meaning is already present; meaningful images need an appropriate text alternative. Do not add redundant announcements or ARIA that overrides correct native semantics.

Make relevant operations keyboard-accessible with visible focus and predictable focus management. Check that overlays and sticky UI do not obscure focused controls. Dragging interactions need appropriate alternatives; inspect [SC 2.5.7](https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html) for single-pointer requirements rather than assuming keyboard support alone is sufficient.

Associate errors with their fields and make submission failures discoverable without losing input. An error summary is useful for multi-error forms; avoid moving focus for routine background validation. Announce changing status selectively, with sufficient context, without stealing focus.

Check color-independent meaning, text resizing, reduced motion, and authentication behavior where relevant. Do not treat an automated scan or these notes as evidence of complete WCAG conformance.

## Native platform guidance

Use the target platform's current accessibility guidance and components. CSS px, Apple points, and Android dp are different units; do not transfer thresholds between them. The visual icon can be smaller than its interaction region, but expanded regions must not overlap ambiguously.

- Apple: use [Human Interface Guidelines: Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility) for platform-specific target, text, assistive-technology, and motion guidance. Verify guidance for the actual Apple platform rather than applying one device's convention everywhere.
- Android: [Android accessibility guidance](https://support.google.com/accessibility/android/answer/7101858?hl=en) recommends touch targets of at least 48×48dp. Check the effective hit region, including padding or platform-provided expansion.

Verify accessible names, roles, states, reading order, text scaling, and focus using the relevant platform APIs and tools. A visually familiar custom control does not automatically inherit native behavior.

## Product preferences

Spacing scales, icon families, font sizes, border radii, animation durations, and theme choices are product decisions unless an applicable requirement says otherwise. Describe them as conventions or recommendations, not accessibility thresholds. Accessibility sets constraints; it does not mandate a particular aesthetic.
