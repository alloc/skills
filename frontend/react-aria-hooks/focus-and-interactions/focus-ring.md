# FocusRing

Source: https://react-aria.adobe.com/FocusRing

## Import

- Import: `import {FocusRing} from '@react-aria/focus'`

## Use For

A utility component that applies a CSS class when an element has keyboard focus. Focus rings are visible only when the user is interacting with a keyboard, not with a mouse, touch, or other input methods. Example FocusRingExample.css Example FocusRingExample.css Example FocusRingExample.css ``` import {FocusRing} from '@react-aria/focus'; import './FocusRingExample.css'; <FocusRing focusRingClass="focus-ring"> <button className="button">Test</button> </FocusRing> ```

## Implementation Guidance

- Use when a wrapper component with focus CSS classes is simpler than manually wiring `useFocusRing`.
- Use `focusRingClass` for keyboard-visible focus and `focusClass` for any focused state.

## Upstream Sections To Recheck

- Features
