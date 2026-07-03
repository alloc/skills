# VisuallyHidden

Source: https://react-aria.adobe.com/VisuallyHidden

## Import

- Import: `import {VisuallyHidden} from 'react-aria/VisuallyHidden'`

## Use For

VisuallyHidden hides its children visually, while keeping content visible to screen readers. ``` import {VisuallyHidden} from 'react-aria/VisuallyHidden'; <VisuallyHidden>I am hidden</VisuallyHidden> ``` ### Positioning VisuallyHidden is positioned absolutely, so it must have a `position: relative` or `position: absolute` ancestor. Otherwise, undesired scrollbars may appear.

## Implementation Guidance

- Use for content that must remain available to assistive technology while hidden visually, such as custom checkbox/radio inputs or table selection labels.
- Ensure the visually hidden element has a positioned ancestor when the docs require it to avoid unwanted scrollbars.
- Use application-provided hidden text when it is product-specific user-facing copy.

## Upstream Sections To Recheck

- Example
