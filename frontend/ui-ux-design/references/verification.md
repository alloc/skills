# Verify the affected interface

Choose checks for the changed behavior, supported platforms, and risk. Do not turn a small component fix into a full product audit. Use representative content and verify outcomes rather than merely checking that style values exist.

## Shared checks

Exercise the main task and relevant failure or recovery paths. Check realistic long content, empty or delayed data, selection, disabled behavior, and text growth where they can affect the change. Confirm that interactive elements communicate their action and state.

Test the themes, locales, and configurations the product supports and the change affects. Do not add dark mode, tablet support, or new platforms just to satisfy a checklist. Measure contrast in each affected theme instead of inferring it from another.

Use permitted rendered inspection when available. When visual analysis is unavailable or prohibited, continue with source inspection, accessibility trees, layout measurements, and interaction tests as available. Report the resulting evidence limits. Never describe a state as tested merely because its code exists.

## Web

- Exercise relevant keyboard navigation, focus order, overlays, and form submission. Inspect accessible names and state; automated checks complement manual interaction.
- Check layout at the widths where content or controls change behavior, along with zoom and text resizing. Avoid relying on a fixed list of device widths.
- Check browser back/forward behavior, URLs, and restoration of user context when navigation changes.
- For performance-sensitive changes, measure the relevant loading, layout stability, or interaction cost. Ensure below-the-fold optimization does not defer the main content.

## Native mobile

- Use the supported device and operating-system configurations relevant to the change. Check effective touch targets, safe areas, system bars, software keyboard, and supported orientations.
- Verify system text scaling, assistive-technology semantics, and reduced motion as relevant. Test gesture alternatives and conflicts with system navigation.
- Check app lifecycle and navigation behavior when the change affects drafts, pending work, restoration, or backgrounding.

## Desktop

- Check resizing, minimum useful window dimensions, display scaling, and keyboard-first operation. Dense layouts still need legible content and reliable targets.
- Respect platform focus, menu, shortcut, dialog, and window conventions. Ensure custom shortcuts do not interfere with standard editing and accessibility operations.
- Test pointer hover, selection, scrolling, and context menus where those interactions matter. Verify touch behavior too when the product supports touch-enabled devices.

For desktop web or hybrid apps, combine the relevant sections instead of assuming that one category covers all behavior.

## Handoff

State what changed, what was verified, and any material limitation. Prioritize defects by their effect on the task and the cost of failure. Distinguish measured or observed findings from visual preferences. Do not claim cross-device, screen-reader, performance, or accessibility validation without the corresponding evidence.
