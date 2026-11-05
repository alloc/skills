# Motion and performance

Use for interaction timing, animated transitions, reduced motion, loading behavior, and perceived or measured responsiveness. Motion is a design choice; responsive, truthful state is an implementation obligation.

## Decide what motion communicates

Useful motion can connect an action to its result, preserve object continuity, expose a spatial relationship, show direct manipulation, or support a deliberate expressive experience. A transition is optional when the state change is already clear.

Avoid routine entrance effects that delay reading, make every section announce itself, or replay during repeated work. Count-up metrics can obscure the actual value; scroll reveals can hide content until a trigger fires. Keep essential content available when animation is unavailable, disabled, or interrupted.

Choose timing by distance, scale, frequency, platform, and interaction. A subtle press response and a full-screen transition have different needs. Shared timing and easing tokens help coherence, but one duration for every animation does not. Repeated actions should not accumulate delay or require waiting for choreography to finish.

## Preserve correctness under interruption

The committed application state should determine the final presentation. Do not rely on an animation-end event to save data, enable the only exit, or establish selection. Reduced-motion settings, removal of a component, or an interrupted transition can change which completion events occur.

When the user reverses an action, cancel, retarget, or replace the animation toward the current state. Avoid queuing obsolete transitions. A rapidly toggled disclosure should end in the state requested by the last action, with matching accessibility state and hit targets.

Handle exiting elements deliberately. A visually hidden or fading control should not remain an unexpected keyboard target or intercept input after its action is unavailable. Conversely, removing a focused element needs a logical focus destination. Direct-manipulation motion should track input, with a stable outcome if the gesture is canceled.

## Provide a reduced-motion experience

On web, use [`prefers-reduced-motion`](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion); on native platforms, use the corresponding system facilities. Reduce motion that can cause discomfort, such as large spatial movement, zoom, or parallax, while retaining understandable feedback through suitable alternatives. Respect changes to the setting during use when supported.

Do not implement reduced motion only by making every duration almost zero. Infinite motion, delayed content, and animation-dependent logic can remain problematic. Check the resulting interaction and information, not just the presence of a media query.

## Loading without deception

Choose feedback for the expected wait and available knowledge. An immediate local change may need no spinner. A pending command may need a status label. Skeletons can reserve structure when the shape is predictable; they should not imitate precision about unknown content.

Avoid flashing loading indicators for near-instant work or fabricating percent progress for an operation without a meaningful denominator. For determinate progress, make the number reflect actual work and identify distinct phases when necessary. For uncertain waits, communicate the pending state and relevant options honestly.

Preserve usable content during refresh or partial failure when it remains valid. Mark stale data when freshness affects decisions. Prevent a late response for an old query from replacing newer results. Cancellation and retry should not duplicate consequential work or silently discard entries.

## Measure the actual rendering cost

Transforms and opacity often make efficient animation possible, but compositor behavior depends on content and rendering. Large blurs, shadows, layers, or images can still be expensive. Layout-affecting animation may be appropriate when measured cost and behavior are acceptable; avoid a blanket ban that forces incorrect geometry or inaccessible content.

Batch layout reads and writes when repeated interleaving causes thrashing. Profile an affected interaction before spreading memoization, promoted layers, or caching throughout the interface. Choose a rendering budget for the supported hardware and refresh rate rather than treating one frame duration as universal.

Reserve layout space for images, async sections, and font changes where feasible. Optimize and defer noncritical assets without delaying the main content. Load only the font weights and resources the experience uses. These are decisions about the delivery path, not reasons to add a new library by default.

Virtualize when rendering or memory cost warrants it. Consider the effect on keyboard traversal, selection, assistive technology, find-in-page, printing, and restored position. Pagination, aggregation, or a simpler representation may better serve the task. Item count alone is not a performance diagnosis.

Exercise repeated toggles, navigation during transition, slow responses, changed queries, and reduced motion. Measure performance on relevant hardware or representative constraints when it materially affects the work; report what remains unmeasured.
