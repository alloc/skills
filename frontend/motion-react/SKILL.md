---
name: motion-react
description: Use when building React animations with Motion primitives, including motion components, animation props, gestures, layout/scroll/SVG animation, transitions, variants, Motion values, and core React Motion hooks/components.
---

# Motion for React

Use Motion for React from `motion/react` for declarative React animations.

```tsx
import { motion } from "motion/react"
```

## Signpost: related guide files

This skill documents only Motion primitives. For non-primitive setup and project guidance, read the matching guide first:

- `guides/installation.md` — install and quick start.
- `guides/accessibility.md` — reduced motion and accessible animation defaults.
- `guides/reduce-bundle-size.md` — `LazyMotion`, feature bundles, and import choices.
- `guides/upgrade-guide.md` — migration notes.
- `guides/motion-plus.md` — Motion+ installation overview.
- `guides/animate-number.md`, `guides/carousel.md`, `guides/scramble-text.md`, `guides/ticker.md`, `guides/typewriter.md`, `guides/use-curtains.md` — Motion+ feature pages.

Docs were gathered with:

```sh
sitefetch https://motion.dev/docs/react -m '/docs/react-*' --link-source-selector '[id="learn-mobile-sidebar"]'
```

## Core primitives

- `motion`: animated HTML/SVG components like `<motion.div />`, `<motion.path />`.
- Animation props: `initial`, `animate`, `exit`, `transition`, `variants`.
- Gesture props: `whileHover`, `whileTap`, `whileFocus`, `whileInView`, drag props.
- Layout primitives: `layout`, `layoutId`, `<LayoutGroup>`.
- Presence/view primitives: `<AnimatePresence>`, `<AnimateActivity>`, `<AnimateView>`.
- Configuration/loading: `<MotionConfig>`, `<LazyMotion>`.
- Reordering: `<Reorder.Group>`, `<Reorder.Item>`.
- Motion values: `motionValue`, `useMotionValue`, `useTransform`, `useSpring`, `useScroll`, etc.
- Hooks: `useAnimate`, `useAnimationFrame`, `useDragControls`, `useInView`, `useReducedMotion`.

## Basic animation

```tsx
<motion.div
  initial={{ opacity: 0, y: 12 }}
  animate={{ opacity: 1, y: 0 }}
  transition={{ duration: 0.25, ease: "easeOut" }}
/>
```

Motion can animate CSS values, independent transforms (`x`, `y`, `scale`, `rotate`), SVG attributes, CSS variables, and complex values when value shapes match.

## Variants and orchestration

Use variants to name visual states and coordinate parent/child animations.

```tsx
const list = {
  hidden: { opacity: 0 },
  show: { opacity: 1, transition: { staggerChildren: 0.06 } },
}
const item = { hidden: { opacity: 0, y: 8 }, show: { opacity: 1, y: 0 } }

<motion.ul variants={list} initial="hidden" animate="show">
  {items.map((x) => <motion.li key={x.id} variants={item} />)}
</motion.ul>
```

## Exit animations

Wrap conditionally-rendered children in `<AnimatePresence>` and give exiting nodes an `exit` prop.

```tsx
<AnimatePresence mode="popLayout">
  {open && <motion.div key="panel" exit={{ opacity: 0, scale: 0.98 }} />}
</AnimatePresence>
```

## Gestures and drag

```tsx
<motion.button whileHover={{ scale: 1.04 }} whileTap={{ scale: 0.96 }} />

<motion.div drag dragConstraints={constraintsRef} dragElastic={0.2} />
```

Use `useDragControls` when drag should start from another handle.

## Layout animation

Add `layout` to animate size/position changes. Use the same `layoutId` across components for shared layout transitions, and wrap groups that need coordination with `<LayoutGroup>`.

```tsx
<motion.div layout />
{selected && <motion.div layoutId="underline" />}
```

## Scroll animation

Use `whileInView` for scroll-triggered entry states and `useScroll` for scroll-linked values.

```tsx
const { scrollYProgress } = useScroll()
return <motion.div style={{ scaleX: scrollYProgress }} />
```

## Motion values

Motion values update without triggering React renders. Use them for high-frequency state, derived values, and direct styles.

```tsx
const x = useMotionValue(0)
const opacity = useTransform(x, [-100, 0, 100], [0, 1, 0])
return <motion.div style={{ x, opacity }} />
```

Use `useMotionValueEvent(value, "change", callback)` to subscribe, `useSpring` to smooth, and `useVelocity` for velocity.

## Reduced motion

Prefer transform/opacity animations, and respect users with `useReducedMotion` or `<MotionConfig reducedMotion="user">`.
