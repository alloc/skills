# useFocusRing

Source: https://react-aria.adobe.com/useFocusRing

## Import

- Import: `import {useFocusRing} from 'react-aria/useFocusRing'`

## Signature

```ts
useFocusRing(props: AriaFocusRingProps): FocusRingAria
```

## Use For

Determines whether a focus ring should be shown to indicate keyboard focus. Focus rings are visible only when the user is interacting with a keyboard, not with a mouse, touch, or other input methods. ``` import {useFocusRing} from 'react-aria/useFocusRing'; function Example() { let {isFocusVisible, focusProps} = useFocusRing(); return ( <button {...focusProps} style={{ WebkitAppearance: 'none', appearance: 'none', background: 'green', border: 'none', color: 'white', fontSize: 14, padding: '8px 12px', borderRadius: 8, outline: isFocusVisible ? '2px solid dodgerblue' : 'none', outlineOffset: 2 }}> Test </button> ); } ```

## Implementation Guidance

- Prefer this hook over manual `:focus` bookkeeping when styling keyboard focus state.
- Use `FocusRing` when a wrapper component with CSS classes is simpler than hook props.

## Upstream Sections To Recheck

- Features
