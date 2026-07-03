# useFocusManager

Source: https://react-aria.adobe.com/FocusScope

## Import

- Import: `import {useFocusManager} from '@react-aria/focus'`

## Use For

Use `useFocusManager` inside a `FocusScope` to move focus programmatically among focusable descendants, such as arrow-key navigation within a custom toolbar.

## Implementation Guidance

- Call it only from a component rendered within the matching `FocusScope`.
- Prefer native tab order unless the widget pattern expects arrow-key or programmatic focus movement.
- Test wrap, tabbable-only behavior, disabled items, and focus restoration.

## Upstream Sections To Recheck

- useFocusManager Example
- FocusManager Interface
