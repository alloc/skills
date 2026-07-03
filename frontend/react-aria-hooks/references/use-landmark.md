# useLandmark

Source: https://react-aria.adobe.com/useLandmark

## Import

- Import: `import {useLandmark} from 'react-aria/useLandmark'`

## Signature

```ts
useLandmark(props: AriaLandmarkProps, ref: RefObject<FocusableElement | null>): LandmarkAria
```

## Use For

Provides landmark navigation in an application. Call this with a role and label to register a landmark navigable with F6.

## Implementation Guidance

- Use only for app regions that need F6 landmark navigation; labels must come from Lingui when visible or product-specific.

## Upstream Sections To Recheck

- Region
- Features
- Anatomy
