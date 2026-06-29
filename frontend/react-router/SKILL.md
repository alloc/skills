---
name: react-router
description: Build, update, or review React Router apps using createBrowserRouter, lazy route components, route objects, typed route builders, URL/search-param conventions, navigation APIs, pending UI, TanStack Query server state, and createRoutesStub testing. Use for client-owned React Router routing.
---

# React Router

React Router owns addressability and navigation. TanStack Query owns server data. The app owns URL conventions.

## Core Rules

- Configure routes with `createBrowserRouter([...])`, create the router once outside the React tree, and render it with `RouterProvider` from `react-router/dom`.
- Inline route components with `Component: lazy(() => import(...))` in route objects, with a `Suspense` fallback above the route tree.
- Route objects are the app's URL contract. Use nested routes for ownership: parent routes own layout, navigation shell, outlet context, auth shell, and section-level error boundaries; child routes own leaf screens.
- Use pathless parent routes for layout without URL segments, path-only parent routes for URL prefixes without layout, index routes for default children, `:param` for dynamic segments, and `/*` only for deliberate catchalls.
- Pick one trailing-slash and canonical URL convention. Route unknown paths through a single `*` route.

## URL State

Shareable or restorable page state belongs in the URL: current record ID, tab, search, filters, sort, page, selected modal, and similar state. Transient UI state belongs in React state.

Parse URL state at the page boundary with `useParams`, `useSearchParams`, or a small schema helper. Centralize parsing so every component agrees on defaults and valid values for shapes like `?tab=foo&page=bar`.

Use `location.state` only for ephemeral navigation hints, such as "came from modal" or "show toast after redirect". Model shareable modals in the URL, such as `?modal=invite` or `/projects/:projectId/invite`; keep purely local modals in component state.

Clone `URLSearchParams` before modifying it. Treat `setSearchParams` as navigation, and use `replace` for noisy/defaulting updates such as debounced search or cleanup.

## Route Construction

Create typed route builders instead of scattering string paths through components. Prefer React Router utilities such as `generatePath` or `href` where they fit; when constructing paths directly, encode path segments. `Link` may receive object-style `to` values with `pathname`, `search`, and `hash`.

Wrap app-specific imperative navigation in hooks so route changes have one edit surface. Validate `returnTo` or `next` params before navigating; allow only same-origin internal paths.

Use `NavLink`, `useMatch`, or `matchPath` for route-pattern-aware active state instead of manual pathname prefix checks.

## Navigation

Use real links for real navigation. Prefer `<Link>` and `<NavLink>` so users keep browser affordances: open in new tab, copy link, status bar preview, and accessibility semantics.

Use `useNavigate` for imperative results of an event, such as close wizard, after save, auth callback, inactivity timeout, or keyboard shortcut. Use normal navigation for meaningful history entries; use `replace` for defaulting, cleanup, login redirects, and debounced search/filter updates where Back should skip intermediate keystrokes.

Keep analytics, scroll restoration, and title updates in centralized route-aware components built on `useLocation`.

## Server State

Use TanStack Query for server reads, writes, caching, invalidation, and optimistic updates. Feed route params, search params, and relevant component state into query keys and mutation inputs. If data depends on URL state, the cache key must depend on the same URL state.

Pending UI should combine router state for navigation (`useNavigation`, `NavLink` pending state) with TanStack Query state for server requests.

## Testing

Use `createRoutesStub` for unit tests of reusable components that require router context, such as params, matches, links, or outlets. Prefer integration or E2E tests for full route-tree behavior, redirects, canonical URLs, and app shell behavior.
