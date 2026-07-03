# mergeProps

Source: https://react-aria.adobe.com/mergeProps

## Import

- Import: `import {mergeProps} from '@react-aria/utils'`

## Signature

```ts
mergeProps<T extends PropsArg[]>(...args: T): UnionToIntersection<TupleTypes<T>>
```

## Use For

Merges multiple props objects together. Event handlers are chained, classNames are combined, ids are deduplicated, and refs are merged. For all other props, the last prop object overrides all previous ones. ``` import {mergeProps} from '@react-aria/utils'; let a = { className: 'foo', onKeyDown(e) { if (e.key === 'Enter') { console.log('enter') } } }; let b = { className: 'bar', onKeyDown(e) { if (e.key === ' ') { console.log('space') } } }; let merged = mergeProps(a, b); ``` The result of the above example will be equivalent to this: ``` let merged = { className: 'foo bar', onKeyDown(e) { a.onKeyDown(e); b.onKeyDown(e); } }; ```

## Implementation Guidance

- Use whenever combining React Aria returned props with app props so handlers, ids, class names, and refs compose instead of replacing each other.
- Pass app props in the order that should win for non-composed values; later props override earlier ordinary props.
