# Navigation and orientation

Use for page and screen structure, app shells, tabs, search, overlays, and restoration of context. Recommendations depend on task, platform, and input method; do not select a navigation pattern from a product category.

## Make the information structure legible

Distinguish destinations, actions, and views of the same content. Use labels that match what users seek. A heading, current-location indicator, and meaningful page title often establish location more effectively than extra decorative chrome.

Place frequently used destinations within easy reach. Group secondary destinations coherently and make infrequent but important capabilities findable. Overflow menus are useful when space is constrained, but hiding an essential action can cost more than the space it saves.

Choose top navigation, sidebars, tabs, rails, or bottom navigation according to the number and relationship of destinations, available space, platform conventions, and usage frequency. There is no universal five-destination limit across all navigation types. Avoid competing controls that represent the same hierarchy without a clear relationship.

Keep recognizable labels and current-location cues when adapting navigation to smaller windows. A sidebar becoming a drawer should not change the meaning or ordering of destinations arbitrarily. If a destination becomes unavailable, explain consequential restrictions; hiding options may be appropriate for permissions or irrelevant contexts.

## Links, actions, and local views

On web, use links for navigation and buttons for actions. Preserve useful link behavior such as opening in another tab and copying an address. Do not make ordinary site navigation an ARIA application menu just because it looks like one; use the semantics of the actual interaction.

Tabs usually switch peer panels within a shared context. If they navigate to independent pages, preserve appropriate navigation and URL behavior. Do not add tab roles unless implementing their corresponding keyboard and selection model. Segmented controls, filters, and navigation tabs can look similar while expressing different actions.

For shareable or revisitable web views, consider representing meaningful state in the URL: selected entity, search query, filters, or active section. Keep private or unsuitable values out of URLs. Temporary hover, animation progress, and unfinished field edits usually do not belong there.

## Back behavior and retained work

Preserve relevant search, filters, sort order, selection, and scroll position when returning to a list. Returning from an item should restore the working context rather than drop the user at a fresh landing page. For a changed dataset, restore what remains meaningful instead of pretending removed records still exist.

Browser Back, platform back gestures, an explicit parent link, and closing a temporary overlay can have different meanings. Make their behavior predictable within the product. Avoid trapping history or inserting many history entries for transient state. Breadcrumbs can expose a hierarchy; they need not reproduce the exact sequence of visited pages.

Handle direct entry as well as sequential navigation. A copied detail URL, restored session, missing object, or changed permission needs a useful result. Do not silently redirect to an unrelated starting screen when an explanation or recovery route is needed.

## Search and progressive disclosure

Make search scope visible: this list, this workspace, or the whole product. Preserve the query while opening and returning from a result. Separate no matching results from no content yet, unavailable data, and a failed request. Offer a concrete recovery such as changing the query or clearing a filter.

Autocomplete and command interfaces need predictable keyboard selection and clear distinction between selecting a suggestion and submitting a query. Keep recent or suggested items only when they help the task and respect the privacy of the context. Do not manufacture suggestions to fill an empty panel.

Reveal advanced options when relevant without hiding frequently used operations behind repeated expansion. Persist disclosure state when it helps ongoing work and does not make shared interfaces confusing.

## Overlays and focus

Use a modal for a bounded task that warrants suspending the surrounding interaction. Prefer inline editing, a nonmodal panel, or a dedicated destination when people need comparison, reference material, substantial navigation, or a durable URL. A drawer is not inherently modal; behavior and semantics must agree.

For a modal, choose initial focus based on its content and consequence, keep background interaction unavailable, provide an accessible exit, and restore focus to a logical place when it closes. Do not dismiss meaningful edits through accidental backdrop activation. Avoid stacking dialogs when the task can be expressed within one coherent flow. The [WAI modal dialog pattern](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/) describes web focus and keyboard behavior; a visual scrim alone does not implement it.

On route or screen changes, manage focus and announcements for the navigation context. Do not reset focus on every filter update, background refresh, or restored view. Verify entering a deep page directly, returning to a filtered list, and closing an overlay after its original trigger has disappeared.
