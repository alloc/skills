# Design judgment

Use this reference for a new visual direction or a focused composition review. These are design preferences and diagnostic heuristics, subordinate to accessibility, product requirements, and coherent existing conventions.

## Avoid a template-first composition

Common AI-generated patterns include an oversized centered hero, gradient headline, pill badge, repeated three-card sections, glass panels, floating decorative shapes, and a dashboard full of invented metrics. The problem is using them without a reason grounded in the content. Replacing every rounded card with a square one does not solve that problem.

Design around representative tasks and real content. Do not invent testimonials, customer logos, activity, or statistics to fill a layout. Use clearly identified sample data when necessary. A screen should remain understandable when decorative effects are removed.

## Make hierarchy and density useful

Group information by relationship and align things people compare. Prefer open layout, dividers, or spacing when a card adds no useful boundary. Cards remain useful for independent objects, selectable units, or distinct interactive regions.

Give important actions appropriate emphasis without forcing every screen to have exactly one CTA. A workspace can contain several legitimate action groups. Make their scope clear and avoid competing emphasis within the same task.

Choose density for the work. Large padding can hide important relationships; compact layouts can make targets ambiguous. Preserve readable text and reliable interaction while fitting useful information within reach. Start with the primary working environment rather than imposing mobile-first design on every product.

## Build a coherent visual language

Reuse the existing type system, palette, and spacing conventions. For new work, a small set of deliberate choices is more useful than many arbitrary tokens. Font pairing is optional; one well-used family may be sufficient. Body size, line height, and line length depend on the script, typeface, content, and viewing conditions.

Use accent color to express emphasis, state, or identity. Avoid assigning a different saturated color to every section without semantic purpose. Gradients, dark themes, blur, texture, and expressive typography are legitimate when coherent and readable; they are not requirements for polish.

Use familiar, consistent icon semantics. Give unfamiliar or ambiguous actions text labels. Vector icons are often convenient for scaling and theming, but appropriate raster assets and deliberate emoji use are not inherently unprofessional. Choose assets for clarity, rendering quality, identity, and accessible meaning.

## Preserve information and orientation

Keep navigation placement and behavior predictable while adapting it to available space. Do not force bottom tabs, sidebars, icons, or deep-link behavior onto every platform and screen. Preserve relevant selection, filters, drafts, and position across navigation.

Allow layout to respond to content and input method. Test long labels, localization, and text growth. Avoid page-level overflow caused by broken layout; allow deliberate scrolling for tables, timelines, maps, and other content that needs it. Essential truncated content needs an accessible way to reveal it.

For right-to-left layouts, use direction-aware layout primitives and check directional icons, navigation, and motion. Do not blindly mirror media, logos, or data visualizations.

## Make interaction proportional

Provide prompt feedback, but do not add a spinner, toast, confirmation, or animation to every action. Prefer a visible change at the point of interaction when it communicates enough. Keep important errors and required actions available long enough to act on them.

Validate forms when feedback becomes useful. Avoid reporting errors before a person has had a reasonable chance to enter a value; after an error, timely validation can help recovery. Preserve entries on failure, explain how to fix problems, and make the next action clear.

Motion should fit distance, frequency, platform, and user preferences. Avoid routine scroll reveals, parallax, staggered lists, or count-up numbers that delay access to content. Expressive motion can serve a deliberate experience. Layout animation is not automatically wrong; measure its cost and avoid disruptive movement. Make transitions interruptible and respect reduced-motion preferences.

## Treat data and performance as design concerns

Choose charts for the comparison or question they support. Use honest scales, units, time ranges, and clear aggregation. Direct labels may replace legends. Tooltips can supplement information but should not be the only way to obtain essential values. Offer an accessible equivalent suited to the data, such as a summary and a table or export when detail is necessary.

Optimize observed bottlenecks. List length alone does not determine whether virtualization is beneficial; rendering cost, interaction, find-in-page, and accessibility matter. Reserve space for delayed content and avoid deferring critical content behind lazy loading. Check that optimization preserves reading, focus, selection, and navigation behavior.
