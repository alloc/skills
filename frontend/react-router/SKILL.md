---
name: react-router
description: Build, update, or review React Router apps using createBrowserRouter, lazy route components, route objects, typed route builders, URL/search-param conventions, navigation APIs, pending UI, TanStack Query server state, and createRoutesStub testing. Use for client-owned React Router routing.
---

# React Router

Use React Router when the app owns router creation and route object configuration directly. Use React Router for routing and navigation; use TanStack Query for server reads, writes, caching, invalidation, and optimistic updates.

## Scope

- Use `react-router` for route objects, route APIs, links, navigation state, URL params, outlets, redirects, and tests.
- Import `RouterProvider` from `react-router/dom`.
- Configure routes with `createBrowserRouter([...])`.
- Create the router once outside the React tree.
- Use `patchRoutesOnNavigation` when routes must be added programmatically after router creation.

```tsx
import ReactDOM from "react-dom/client";
import { Suspense, lazy } from "react";
import { createBrowserRouter } from "react-router";
import { RouterProvider } from "react-router/dom";

const App = lazy(() => import("./App"));

const router = createBrowserRouter([
  { path: "/", Component: App },
]);

ReactDOM.createRoot(document.getElementById("root")!).render(
  <Suspense fallback={null}>
    <RouterProvider router={router} />
  </Suspense>,
);
```

## Route Objects

Route objects define URL matching, rendering, layout nesting, error handling, and metadata. Prefer `Component` for route components in route object configs, with route components assigned from React `lazy()`.

```tsx
import { lazy } from "react";
import { createBrowserRouter } from "react-router";

const RootLayout = lazy(() => import("./routes/RootLayout"));
const Home = lazy(() => import("./routes/Home"));
const ProjectsHome = lazy(() => import("./routes/projects/ProjectsHome"));
const Project = lazy(() => import("./routes/projects/Project"));

const router = createBrowserRouter([
  {
    path: "/",
    Component: RootLayout,
    children: [
      { index: true, Component: Home },
      {
        path: "projects",
        children: [
          { index: true, Component: ProjectsHome },
          { path: ":projectId", Component: Project },
        ],
      },
    ],
  },
]);
```

Routing rules:

- Wrap route components with `lazy()` and provide a `Suspense` fallback above the route tree.
- Use `children` for nested routes; parent components render child matches with `<Outlet />`.
- Use nested routes for ownership: parent routes own layout, navigation shell, outlet context, auth shell, and section-level error boundaries; child routes own leaf screens.
- Use pathless parent routes for layout without adding URL segments.
- Use a route with `path` and no component to prefix child URLs without adding a layout.
- Use `{ index: true }` for a default child at the parent URL.
- Use `:param` dynamic segments; read them in components with `useParams`.
- Use `?` for optional static or dynamic segments, and `/*` splats for catchall paths. Destructure splats as `const { "*": splat } = params`.

## Prefer URL-Derived State

Prefer URL-derived state over component state for shareable page state. Search, filters, pagination, selected tabs, and modal IDs should usually live in path params or search params, then be parsed with `useParams`, `useSearchParams`, or a small URL schema helper.

Feed parsed URL state into TanStack Query keys and mutation inputs when it affects server data. Page data that should survive reloads, links, and back/forward navigation should not depend on `useState` plus `useEffect` fetching.

Keep transient UI state in React state. Keep restorable or shareable state in the URL. Use `location.state` only for ephemeral navigation hints such as "came from modal" or "show toast after redirect".

Model modals intentionally: shareable modals belong in the URL, such as `?modal=invite` or `/projects/:projectId/invite`; purely local modals belong in component state.

## URL Builders And Search Params

Create typed route builders instead of scattering string paths through components. Use React Router utilities such as `generatePath` or `href` where they fit, and encode path segments when constructing paths directly.

```ts
import { generatePath } from "react-router";

export const routes = {
  home: () => "/",
  project: (projectId: string) =>
    generatePath("/projects/:projectId", { projectId }),
  projectTab: (projectId: string, tab: "overview" | "settings") => ({
    pathname: routes.project(projectId),
    search: `?tab=${tab}`,
  }),
};
```

Centralize search-param parsing at the page boundary. Give repeated URL shapes a small helper or schema so every component agrees on what `?tab=foo&page=bar` means.

```ts
const TABS = ["overview", "settings", "billing"] as const;

export function readProjectSearch(searchParams: URLSearchParams) {
  const rawTab = searchParams.get("tab");

  return {
    tab: TABS.includes(rawTab as (typeof TABS)[number])
      ? (rawTab as (typeof TABS)[number])
      : "overview",
    page: Math.max(1, Number(searchParams.get("page") || 1)),
  };
}
```

Clone `URLSearchParams` before changing it. `useSearchParams` returns a mutable object, and setting search params causes navigation.

```ts
function setParam(
  params: URLSearchParams,
  key: string,
  value: string | null,
) {
  const next = new URLSearchParams(params);
  value == null ? next.delete(key) : next.set(key, value);
  return next;
}
```

## Server State

Use TanStack Query for server state. Route params, URL search params, and component state should feed query keys and mutation inputs.

```tsx
import { useQuery } from "@tanstack/react-query";
import { useParams } from "react-router";

function Team() {
  const { teamId } = useParams();
  const team = useQuery({
    queryKey: ["team", teamId],
    queryFn: () => fetchTeam(teamId!),
    enabled: Boolean(teamId),
  });

  return (
    <section>
      {team.isPending ? <Spinner /> : <h1>{team.data.name}</h1>}
    </section>
  );
}
```

Use `lazy` on a route when component code should be imported on demand. Use `handle` for route metadata consumed through `useMatches`.

## Navigation

Use declarative navigation first:

- `<Link>` for ordinary links.
- `<NavLink>` for links that need active, pending, or transitioning state; its `className`, `style`, and children props can be functions.
- `Link` object-style `to` values with `pathname`, `search`, and `hash` when building URLs with search or hash.
- `useSearchParams` for URL-search-param navigation from user input; clone params before edits.
- `<Navigate replace to={...} />` for render-time route redirects.

Use normal navigation for user-meaningful transitions. Use `replace` for defaulting, URL cleanup, login redirects, and debounced search/filter updates where Back should not step through every keystroke.

```ts
navigate({ search: nextSearch }, { replace: true });
```

Prefer `<Link>` and `<NavLink>` over button-click `navigate` for real navigation so users keep normal browser affordances: open in new tab, copy link, status bar preview, and link semantics. Reserve `useNavigate` for imperative results of an event such as close wizard, after save, auth callback, inactivity timeout, or keyboard shortcut.

Wrap app-specific navigation in hooks so route changes have one edit surface:

```ts
export function useAppNavigate() {
  const navigate = useNavigate();

  return {
    toProject: (projectId: string) => navigate(routes.project(projectId)),
    replaceWithLogin: () => navigate("/login", { replace: true }),
  };
}
```

Use `NavLink`, `useMatch`, or `matchPath` for active-state checks instead of manual pathname string checks.

Pick one trailing-slash and canonical URL convention. Route unknown paths through a single `*` route. When preserving `returnTo` or `next` redirect params, allow same-origin internal paths only:

```ts
function safeReturnTo(value: string | null) {
  if (!value || !value.startsWith("/") || value.startsWith("//")) return "/";
  return value;
}
```

Keep analytics, scroll restoration, and title updates in centralized route-aware components built on `useLocation`, not scattered through page components.

## Pending And Optimistic UI

Pending UI uses router state for navigation and TanStack Query state for server requests.

- Use `useNavigation()` for global route navigations.
- Use `NavLink` pending state for local link indicators.
- Use query and mutation status for local server request indicators.
- Use TanStack Query optimistic updates when the submitted data predicts the next UI state.

```tsx
import { useQuery } from "@tanstack/react-query";
import { useNavigation, useParams } from "react-router";

function GlobalPending() {
  const navigation = useNavigation();
  return navigation.location ? <Spinner /> : null;
}

function ProjectSummary() {
  const { projectId } = useParams();
  const project = useQuery({
    queryKey: ["project", projectId],
    queryFn: () => fetchProject(projectId!),
    enabled: Boolean(projectId),
  });

  return project.isPending ? <InlineSpinner /> : <h2>{project.data.title}</h2>;
}
```

## Testing

Use `createRoutesStub` to unit test reusable components that depend on router context such as `useParams`, `useMatches`, `<Link>`, or `<Outlet>`.

```tsx
import { createRoutesStub } from "react-router";
import { render, screen, waitFor } from "@testing-library/react";

test("renders a routed component", async () => {
  const Stub = createRoutesStub([
    {
      path: "/projects/:projectId",
      Component: ProjectHeading,
    },
  ]);

  render(<Stub initialEntries={["/projects/123"]} />);

  await waitFor(() => screen.findByText("Project 123"));
});
```

Prefer integration or E2E tests for full route behavior, especially when validating real route trees, redirects, or app shell behavior.
