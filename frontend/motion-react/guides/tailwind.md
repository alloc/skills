# Motion React with Tailwind

Use Tailwind for static styling and Motion props for animated state.

```tsx
<motion.div
  className="rounded-xl bg-white shadow"
  initial={{ opacity: 0, y: 8 }}
  animate={{ opacity: 1, y: 0 }}
/>
```

Prefer Motion's independent transform props (`x`, `y`, `scale`, `rotate`) for animated transforms to avoid conflicts with Tailwind transform utilities.
