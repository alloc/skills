# Layout and responsive behavior

Use for composition, density, resizing, content growth, localization, and overflow. Start with the actual working environment, then adapt across supported configurations. Mobile-first and desktop-first are approaches, not quality standards.

## Compose around relationships

Identify what users read, compare, edit, and act on together. Put related information within reach and align repeated fields or numbers so comparison is easy. Avoid distributing one decision across distant cards merely to balance a grid.

Use spacing and typography to establish hierarchy before adding borders or surfaces. A boundary should communicate grouping, independent interaction, status, or elevation. Nested cards with the same visual weight often obscure which boundary matters. A coherent grid can coexist with deliberate asymmetry; symmetry is not a prerequisite for clarity.

Choose content width by the activity. Reading benefits from controlled text measure, while tables, editors, and visual workspaces may need most of the window. Do not constrain an operational workspace to a marketing-page max width or stretch a short form just because the display is wide.

Spacing should express relationships: close within a group, more separation between groups. Reuse the product's rhythm, with optical adjustments where they improve alignment. A four- or eight-unit scale can be useful but does not replace judgment about glyphs, borders, or control geometry.

## Adapt when the content requires it

Choose breakpoints where composition or interaction stops working, rather than treating a list of phone and laptop widths as the design. Account for the component's available space inside sidebars, split views, and resizable panels, not just the whole viewport.

| Pressure | Useful responses | What to preserve |
| --- | --- | --- |
| Navigation no longer fits | Reflow, collapse secondary destinations, or change navigation presentation | Location, labels, and access to important destinations |
| A comparison becomes cramped | Adjust columns, expose details on demand, or provide deliberate scrolling | The values and relationships needed to compare |
| Actions overflow a toolbar | Prioritize frequent actions and group secondary ones in overflow | Action meaning, scope, and keyboard access |
| A form becomes too narrow | Stack related fields and let labels/help wrap | Logical entry order and visible validation |
| Text grows | Let containers expand and reflow before truncating | Essential labels, status, and actionable controls |

Do not remove capability solely to make a screenshot fit. If secondary information moves behind disclosure, keep it discoverable and ensure it is not required to interpret the remaining content.

## Diagnose overflow at its source

Check intrinsic sizing, long tokens, unshrinkable children, fixed dimensions, and positioned elements. Avoid globally hiding horizontal overflow as a way to conceal clipped content or offscreen focus.

On web, a flex or grid child's automatic minimum size can prevent shrinking. A shrinkable text region may need `min-inline-size: 0`; flexible grid tracks may need a zero minimum, such as `minmax(0, 1fr)`. Apply these to the region intended to shrink instead of erasing meaningful minimum sizes everywhere. See [MDN minimum sizing](https://developer.mozilla.org/en-US/docs/Web/CSS/min-width).

Allow ordinary prose to wrap naturally. Use appropriate overflow wrapping for long URLs, identifiers, and user content. Keep a short label on one line only when it can fit or has a usable fallback. For a chip collection, wrapping the collection often works better than crushing each label. A `+n` summary should open the hidden items when access matters.

Intentional scroll regions can suit tables, timelines, canvases, and panes. Make their extent and interaction understandable and retain keyboard access. Avoid incidental nested scrolling that leaves users unsure which region will move. Keep sticky headers and frozen columns from consuming the usable viewport.

## Fixed UI, keyboards, and viewport changes

Fixed bars, banners, and overlays should not cover the last row, focused field, or primary action. Account for software keyboards, safe areas, browser chrome, display scaling, and text growth on the relevant platform. Do not double-apply insets when a native container already manages them.

Treat full-height layouts as responsive to available space. Fixed screen-height assumptions can break when browser controls change or a keyboard opens. Prefer the platform's appropriate layout primitives and verify the supported behavior rather than applying one viewport-unit rule to every screen.

## Localization and direction

Use logical start/end relationships for direction-aware layouts. Test longer translated labels and mixed-direction content such as identifiers within right-to-left text. Mirror directional affordances where meaning requires it; do not mirror logos, photographs, or charts mechanically.

Check compact controls at large text sizes and the narrowest supported working space. Ensure reflow preserves source reading order. Visual rearrangement that leaves keyboard traversal jumping unpredictably across the screen is not a complete responsive solution.
