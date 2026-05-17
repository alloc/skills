# Example: Vite SSR

Use this example only when implementing or repairing Nitro plus Vite SSR. For renderer configuration basics, read [renderer-vite-and-ssr.md](./renderer-vite-and-ssr.md) first.

## Common Shape

Vite config:

```ts
import { defineConfig } from "vite";
import { nitro } from "nitro/vite";

export default defineConfig({
  plugins: [nitro()],
});
```

HTML template:

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>SSR App</title>
  </head>
  <body>
    <div id="app"><!--ssr-outlet--></div>
    <script type="module" src="/src/main.ts"></script>
  </body>
</html>
```

## Framework Variants

Nitro's docs include SSR examples for:

- React
- Preact
- SolidJS
- Vue Router
- TanStack Router
- TanStack Start
- Vite RSC
- Vite SSR HTML
- Mono JSX and Nano JSX

Use the existing app's framework and entry names. Do not introduce a second routing system unless the task requires it.

## Implementation Checklist

- Server entry renders the initial app HTML or stream.
- Client entry hydrates or mounts into the same DOM target.
- The template contains `<!--ssr-outlet-->` where server output belongs.
- Server-side data fetching avoids browser-only globals.
- API routes remain separate from frontend page route definitions.
- Status codes, redirects, and headers survive the SSR path.
- Production build transforms the template and bundles server output.
