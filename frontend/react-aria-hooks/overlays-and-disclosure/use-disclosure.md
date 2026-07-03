# useDisclosure

Source: https://react-aria.adobe.com/Disclosure/useDisclosure.html

## Import

- Package: `react-aria`
- Import: `import {useDisclosure} from 'react-aria'`
- Install: `yarn add react-aria`
- Source version: 3.50.0

## Signature

```ts
useDisclosure(props: AriaDisclosureProps, state: DisclosureState, ref: RefObject<HTMLElement | null>): DisclosureAria
```

## Use For

Provides the behavior and accessibility implementation for a disclosure component.

## Source Highlights

- Support for mouse, touch, and keyboard interactions to open and close the disclosure
- Support for disabled disclosures
- Follows the disclosure ARIA pattern, semantically linking the trigger button and panel
- Uses [hidden="until-found"](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/hidden#the_hidden_until_found_state) in supported browsers, enabling find-in-page search support and improved search engine visibility for collapsed content

## Implementation Guidance

- Spread every returned `*Props` object onto the exact DOM slot it names; these props carry ARIA attributes, event handlers, ids, and keyboard behavior.
- Pass the ref for the rendered DOM element into the hook and attach that same ref to the element receiving the returned props.
- Create the matching `react-stately` state object once in the owning component and pass that same state to related item, cell, or trigger hooks.
- Preserve user-provided labels and descriptions; icon-only controls still need `aria-label` or `aria-labelledby`.

## Upstream Sections To Recheck

- Features
- Anatomy
- Example
- Usage
- Disclosure Group
