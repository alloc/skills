# useFocusVisible

Source: https://react-aria.adobe.com/useFocusVisible

## Import

- Import: `import {useFocusVisible} from 'react-aria/useFocusVisible'`

## Signature

```ts
useFocusVisible(props: FocusVisibleProps): FocusVisibleResult
```

## Use For

Manages focus visible state for the page, and subscribes individual components for updates. Focus visible: true ``` import {useFocusVisible} from 'react-aria/useFocusVisible'; function Example() { let {isFocusVisible} = useFocusVisible({isTextInput: true}); return ( <> <div>Focus visible: {String(isFocusVisible)}</div> <label style={{display: 'block'}}> First Name: <input /> </label> <label style={{display: 'block'}}> Last Name: <input /> </label> </> ); } ```

## Implementation Guidance

- Use sparingly for app-level focus-visible state; prefer `useFocusRing` for element-level styling.

## Upstream Sections To Recheck

- Features
