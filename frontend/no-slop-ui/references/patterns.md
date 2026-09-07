# Generic UI Pattern Diagnostics

Use this guide to notice common shortcuts, then judge them against the product's purpose and visual language. A pattern is a problem when it appears without a content, interaction, brand, or platform reason. Do not remove a justified pattern merely because it appears here.

## Composition

| Signal | Why it often fails | Better direction |
| --- | --- | --- |
| A detached, rounded shell around primary navigation | It spends space and emphasis on application chrome | Integrate navigation into the window or page structure unless separation communicates a real boundary |
| A large hero treatment inside a task-focused product | It delays the user's work and imports a marketing-page hierarchy | Lead with the page identity, relevant actions, and content |
| A uniform grid of metric cards as the default dashboard | It treats every number as equally important and hides relationships | Organize information around decisions, workflows, trends, or exceptions |
| An auxiliary rail filled with generic activity or schedule content | It creates visual balance without supporting the primary task | Include secondary regions only when users need that information alongside the main content |
| Empty space added mainly to imply luxury | It lowers information density without improving comprehension | Use space to group, separate, or emphasize content |
| A narrow layout that simply stacks every desktop region | It preserves component order but not task priority | Recompose around the smaller context, input method, and most important actions |

## Surfaces and Geometry

| Signal | Why it often fails | Better direction |
| --- | --- | --- |
| Every section is a card | Containers stop communicating grouping when everything has one | Use layout, headings, dividers, or whitespace; reserve surfaces for meaningful boundaries |
| Frosted, translucent, glowing, or gradient surfaces appear by default | Effects compete with content and can weaken contrast | Prefer quiet surfaces; add effects only when they support brand, depth, or spatial context |
| Large corner rounding is applied to unrelated elements | Uniform softness erases component hierarchy | Use a small, coherent geometry scale suited to the platform and object type |
| Strong shadows make ordinary content appear to float | Excess elevation invents hierarchy and depth | Use the least separation needed: contrast, a divider, modest elevation, or none |
| Borders and ornamental frames surround most content | Excess chrome fragments the page | Introduce boundaries only where users need to perceive containment or separation |

## Typography and Copy

| Signal | Why it often fails | Better direction |
| --- | --- | --- |
| Small uppercase eyebrow text precedes most headings | It creates a repeated decorative hierarchy with little information | Use a direct heading; keep category labels only when they help orientation |
| Generic aspirational copy describes ordinary product functions | It makes the interface sound templated and obscures the task | Name the object, action, state, or benefit concretely |
| Several unrelated type styles manufacture personality | The resulting hierarchy feels assembled rather than coherent | Use a compact typographic system and create contrast through role, weight, size, and spacing |
| Labels rely on all caps or wide tracking throughout | Repetition reduces readability and makes every label equally loud | Reserve specialized casing for a clear semantic category |
| Headings are oversized relative to the available content | Display typography consumes attention the content has not earned | Size type according to hierarchy, reading distance, and available space |

## Color and Imagery

| Signal | Why it often fails | Better direction |
| --- | --- | --- |
| Several bright accent colors have no stable meaning | Color becomes decoration rather than information | Use a coherent palette and assign semantic roles deliberately |
| A new palette ignores established product or platform colors | The screen feels disconnected from its environment | Start with existing tokens, brand assets, and state conventions |
| Gradients, glows, abstract blobs, or stock illustrations fill otherwise empty regions | They decorate a weak composition instead of strengthening it | Improve content structure first; use imagery when it carries brand or product meaning |
| Color alone communicates status or selection | State becomes ambiguous or inaccessible | Pair color with text, shape, iconography, position, or another suitable cue |

## Components and Data

| Signal | Why it often fails | Better direction |
| --- | --- | --- |
| Most actions and labels use pill shapes | Shape no longer distinguishes action, filter, tag, or status | Match geometry to component role and the surrounding system |
| Badges announce vague states such as “Live” without useful data | They add urgency or novelty without information | Show a badge only when its value changes a decision or aids navigation |
| Decorative charts or fabricated metrics fill a layout | They imply evidence and functionality that do not exist | Use real data with a clear question, or omit the visualization |
| Icons sit inside decorative tiles by default | Extra containers add noise and inflate simple actions | Present icons plainly unless the container conveys selection, category, or affordance |
| Unlabeled icons depend on guesswork | Familiarity varies across platforms and audiences | Add a visible label or an accessible name and supporting affordance as appropriate |
| Idealized sample content hides overflow and state behavior | The design breaks when real data arrives | Test representative, sparse, dense, long, missing, and erroneous content |

## Motion and Feedback

| Signal | Why it often fails | Better direction |
| --- | --- | --- |
| Navigation items, cards, and controls move or scale on routine hover or focus | Constant motion makes the interface restless and may obscure state | Prefer immediate state changes in color, emphasis, border, or other stable cues |
| Page-load entrances reveal ordinary content theatrically | They delay scanning and repeat without adding meaning | Render content immediately, or use subtle transition only when it explains continuity |
| Bounce or spring behavior appears throughout routine controls | Playfulness overwhelms utility and can feel slow | Match motion character to brand and interaction; keep frequent actions restrained |
| Menus, dialogs, or repeated tools use long transitions | The interface feels less responsive with use | Keep frequent transitions short and interruptible, or omit them |
| Motion ignores user or platform accessibility settings | It can create discomfort and violates user expectations | Honor reduced-motion preferences and preserve state clarity without animation |

## Final Check

Ask:

- Does the interface reveal what matters first?
- Can each decorative choice explain its job?
- Are repeated elements genuinely repeated concepts?
- Does the result belong to this product and platform, or could it be pasted into any generated dashboard?
- Do real content and non-ideal states still work?

If a choice is coherent, useful, and intentional, keep it. The goal is not minimalism for its own sake; it is freedom from unexamined defaults.
