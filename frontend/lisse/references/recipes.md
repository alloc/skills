# React Recipes

Use these as compact starting patterns, then adapt markup, accessibility, tokens, and state to the application.

## Button

Use `asChild` so the real interactive element remains the button.

```tsx
import { SmoothCorners } from "@lisse/react";

export function PrimaryButton({ className, ...props }: React.ComponentProps<"button">) {
  return (
    <SmoothCorners asChild corners={{ radius: 12, smoothing: 0.6 }}>
      <button
        type="button"
        {...props}
        className={[
          "bg-neutral-900 px-5 py-2.5 font-medium text-white shadow-sm hover:bg-neutral-800",
          className,
        ].filter(Boolean).join(" ")}
      />
    </SmoothCorners>
  );
}
```

## Card

Let auto-effects lift the Tailwind shadow into an SVG shadow that follows the squircle.

```tsx
import { SmoothCorners } from "@lisse/react";

export function ProfileCard({ name, role, avatar }: { name: string; role: string; avatar: string }) {
  return (
    <SmoothCorners
      as="article"
      corners={{ radius: 20, smoothing: 0.7 }}
      className="max-w-sm bg-white p-6 shadow-md dark:bg-neutral-900"
    >
      <img src={avatar} alt="" className="mb-4 h-12 w-12" />
      <h3 className="text-lg font-semibold">{name}</h3>
      <p className="text-neutral-500">{role}</p>
    </SmoothCorners>
  );
}
```

## Dialog panel

Keep the overlay outside Lisse. Clip only the panel content so backdrop layout and click handling stay simple.

```tsx
import { SmoothCorners } from "@lisse/react";

export function Dialog({
  open,
  onClose,
  title,
  children,
}: {
  open: boolean;
  onClose: () => void;
  title: string;
  children: React.ReactNode;
}) {
  if (!open) return null;

  return (
    <div
      role="dialog"
      aria-modal="true"
      className="fixed inset-0 flex items-center justify-center bg-black/50 p-6"
      onClick={onClose}
    >
      <SmoothCorners
        corners={{ radius: 24, smoothing: 0.7 }}
        className="w-full max-w-lg bg-white p-8 shadow-xl dark:bg-neutral-900"
        onClick={(event) => event.stopPropagation()}
      >
        <h2 className="mb-3 text-xl font-semibold">{title}</h2>
        {children}
      </SmoothCorners>
    </div>
  );
}
```

For production dialogs, preserve the app's existing focus management, escape handling, ARIA labeling, and portal strategy.
