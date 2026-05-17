# Example: tRPC with Nitro and Vite

Use this example only when wiring tRPC requests through Nitro in a Vite app.

## Shape

- Configure Vite with the Nitro plugin.
- Define the tRPC router and procedures outside the HTML renderer.
- Route tRPC HTTP requests through a Nitro route or server entry adapter.
- Keep client creation pointed at the Nitro-served tRPC endpoint.

## Boundaries

Keep these pieces separate:

- tRPC router and procedure definitions
- Nitro request adapter or route handler
- HTML/SSR rendering
- browser client initialization

This separation prevents SSR changes from breaking API behavior and makes direct API tests possible.

## Validation

- Call the tRPC endpoint directly.
- Exercise at least one client-side call from the rendered page when the UI is involved.
- Confirm procedure input validation still runs on server requests.
- Confirm context creation sees the incoming Nitro request data it needs.
