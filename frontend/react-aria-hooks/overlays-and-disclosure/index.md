# Overlays and Disclosure

Read when: implementing popovers, modal overlays, dialogs, tooltips, disclosures, outside dismissal, focus restoration, portal behavior, or hidden dismiss controls.

Avoid when: Avoid these hooks for always-visible content or native disclosure/dialog behavior that does not need custom focus, dismissal, or portal handling.

| API | Consider when |
| --- | --- |
| [DismissButton](./dismiss-button.md) | Use `DismissButton` as a visually hidden dismiss affordance for modals and popups that otherwise have no visible close control for screen-reader users. |
| [FocusScope](./focus-scope.md) | Use for custom focus boundaries, especially overlays that must contain focus or restore focus on close. |
| [Overlay](./overlay.md) | Use as the source-documented portal and focus-scope wrapper for React Aria overlay examples. |
| [useDialog](./use-dialog.md) | Provides the behavior and accessibility implementation for a dialog component. |
| [useDisclosureGroupState](./use-disclosure-group-state.md) | Use for accordions or disclosure sets that coordinate expanded state across multiple disclosure items. |
| [useDisclosureState](./use-disclosure-state.md) | Manages state for a disclosure widget. |
| [useDisclosure](./use-disclosure.md) | Provides the behavior and accessibility implementation for a disclosure component. |
| [useModalOverlay](./use-modal-overlay.md) | Provides the behavior and accessibility implementation for a modal component. |
| [useOverlayTriggerState](./use-overlay-trigger-state.md) | Manages state for an overlay trigger. |
| [usePopover](./use-popover.md) | Provides the behavior and accessibility implementation for a popover component. |
| [useTooltipTriggerState](./use-tooltip-trigger-state.md) | Manages state for a tooltip trigger. |
| [useTooltipTrigger](./use-tooltip-trigger.md) | Use when an element owns tooltip open/close timing and trigger props, paired with `useTooltip`. |
| [useTooltip](./use-tooltip.md) | Use `useTooltip` for the tooltip part of the `useTooltipTrigger` pattern. |
