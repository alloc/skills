# Typography and color

Use for readable text, hierarchy, labels, numerical content, palette decisions, themes, and visual semantics. Most choices here are product preferences; numeric accessibility requirements belong in [accessibility.md](accessibility.md).

## Build hierarchy from content roles

Use the existing type system before introducing another family or scale. If none exists, define roles that the interface actually needs: page heading, section heading, body, control label, supporting text, and data value. Several roles can share a size and differ through weight, spacing, or placement.

Avoid increasing every heading until the interface resembles a landing page. Frequent operational screens usually need more emphasis on content and actions than introductory display type. Expressive headings can suit a deliberate visual identity, but should not crowd out useful information.

One typeface may provide enough range. Additional families should improve identity, reading, or information distinction, not simply satisfy a font-pairing formula. Check actual script coverage, fallback behavior, available weights, and font loading. A Latin-only sample does not establish suitability for the product's languages.

## Judge text in context

Choose body size, leading, and measure together. Wide reading columns generally need different leading from compact labels; a font with a small x-height may need a larger nominal size. Avoid treating 16px or a 1.5 line height as a universal rule for all body text, scripts, platforms, and densities.

Make secondary text readable rather than fading it until it becomes decorative. Consequential status, units, timestamps, and explanations still need adequate contrast and a usable size. Do not rely on bold or color alone to rescue an unclear information structure.

Preserve natural text wrapping. Balanced heading wrapping can improve short titles when supported, but the title must remain readable without it. Do not bind arbitrary final words with nonbreaking spaces or force manual line breaks that fail in translation. Reserve nonbreaking treatment for relationships that genuinely need it, such as some unit/value pairs.

Truncation is a space tradeoff, not a default polish treatment. Prefer wrapping when the full value matters. If truncating, make the complete content available through an appropriate interaction, detail view, or expanded region. A hover-only tooltip does not serve every input method. Distinguish user content from short controlled labels when deciding what can be shortened.

## Numerical and technical content

Use aligned numerical columns when comparison matters, with explicit units and consistent precision. Right alignment often helps compare magnitudes; dates and identifiers may need different treatment. Tabular figures can stabilize changing counts, prices, and aligned numbers without making all text monospaced. On web, this is available through [`font-variant-numeric: tabular-nums`](https://developer.mozilla.org/en-US/docs/Web/CSS/font-variant-numeric) when the font supports it.

Do not use monospace as a generic signal of sophistication. It can help code and exact identifiers, but long prose or ordinary labels may become harder to scan. Preserve copyable underlying values when a compact display rounds, abbreviates, or formats data.

## Give colors stable roles

Build from the established palette. When creating a new one, choose a restrained set of functional roles such as text, supporting text, surface, border, action, selection, focus, and danger. These roles may share colors; do not invent a different accent for every feature.

Prefer semantic tokens at reusable boundaries so themes and states remain coherent. A local illustration or one-off data encoding need not become a product-wide token solely to avoid a literal color value. The goal is maintainable meaning, not a large token catalog.

Differentiate hover, press, focus, selection, disabled, and loading states by what they communicate. Focus and selection are not interchangeable. A selected item should remain identifiable when the pointer leaves; a pressed action should not resemble persistent selection. Do not rely on hue alone for consequential distinctions.

Choose chart colors for the data relationship: categorical, sequential, or diverging. Avoid reusing semantic danger or success colors in a way that implies a status the data does not have. Consider cultural and domain meaning from actual users and content rather than assigning a palette from an industry label.

## Themes, surfaces, and icons

Treat dark mode as a set of intentional foreground/background relationships, not an inversion filter. Check text, icons, controls, focus, charts, and overlays against their actual surfaces in each supported theme. Translucent surfaces require checking the composed result over representative content.

Use borders, contrast, or elevation where separation is needed; not every section needs all three. Maintain coherent depth so a tooltip, panel, and modal are distinguishable without excessive shadows. Gradients and texture can serve identity or hierarchy but should not mask weak composition.

Choose an icon family that fits the existing product. Keep apparent size, stroke, and alignment consistent within a role; different glyph geometry may require optical adjustment. Filled and outlined forms can express state when the mapping is deliberate. Avoid decorative icons beside every sentence or field when they add no meaning.

Check a real paragraph, a long heading, a compact control, a changing numeric value, and an error on its actual surface. A palette swatch and a font specimen alone cannot establish interface readability.
