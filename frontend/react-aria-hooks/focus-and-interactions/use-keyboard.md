# useKeyboard

Source: https://react-aria.adobe.com/useKeyboard

## Import

- Import: `import {useKeyboard} from 'react-aria/useKeyboard'`

## Signature

```ts
useKeyboard(props: KeyboardProps): KeyboardResult
```

## Use For

Handles keyboard interactions for a focusable element. ``` import React from 'react'; import {useKeyboard} from 'react-aria/useKeyboard'; function Example() { let [events, setEvents] = React.useState<string[]>([]); let {keyboardProps} = useKeyboard({ onKeyDown: e => setEvents( events => [`key down: ${e.key}`, ...events] ), onKeyUp: e => setEvents( events => [`key up: ${e.key}`, ...events] ) }); return ( <> <label htmlFor="example">Example</label> <input {...keyboardProps} id="example" /> <ul style={{ height: 100, overflow: 'auto', border: '1px solid gray', width: 200 }}> {events.map((e, i) => <li key={i}>{e}</li>)} </ul> </> ); } ```

## Implementation Guidance

- Use for custom keyboard shortcuts on a focused element; do not replace native keyboard behavior already provided by component hooks.

## Upstream Sections To Recheck

- Features
