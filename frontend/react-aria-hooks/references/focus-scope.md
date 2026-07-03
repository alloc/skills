# FocusScope

Source: https://react-aria.adobe.com/FocusScope

## Import

- Import: `import {FocusScope} from '@react-aria/focus'`

## Use For

A FocusScope manages focus for its descendants. It supports containing focus inside the scope, restoring focus to the previously focused element on unmount, and auto focusing children on mount. It also acts as a container for a programmatic focus management interface that can be used to move focus forward and back in response to user events.

## Implementation Guidance

- Use for custom focus boundaries, especially overlays that must contain focus or restore focus on close.
- Do not add it around every widget; many higher-level overlay examples get this behavior through `Overlay`.
- Use `contain` and `restoreFocus` deliberately and test Tab/Shift+Tab behavior.

## Upstream Sections To Recheck

- Introduction
- Example
- useFocusManager Example
