---
name: react-router
description: Build, update, or review React Router apps using createBrowserRouter, route objects, loaders, actions, fetchers, navigation APIs, pending UI, custom runtime integration, and createRoutesStub testing. Use for client-owned React Router data routers.
---

# React Router

Use React Router when the app owns router creation and route object configuration directly. Prefer route loaders/actions and router primitives over component-level request orchestration.

## Scope

- Use `react-router` for route objects, route APIs, data hooks, forms, fetchers, redirects, and tests.
- Import `RouterProvider` from `react-router/dom`.
- Configure routes with `createBrowserRouter([...])`; do not introduce `@react-router/dev`, file-based route config, or route typegen unless explicitly requested.
- Create the data router once outside the React tree. Do not hold it in React state.
- Use `patchRoutesOnNavigation` when routes must be added programmatically after router creation.

```tsx
import ReactDOM from "react-dom/client";
import { createBrowserRouter } from "react-router";
import { RouterProvider } from "react-router/dom";

const router = createBrowserRouter([
  { path: "/", Component: App },
]);

ReactDOM.createRoot(document.getElementById("root")!).render(
  <RouterProvider router={router} />,
);
```

## Route Objects

Route objects define URL matching, rendering, data loading, mutations, revalidation, error handling, and metadata. Prefer `Component` for route components in route object configs.

```tsx
import { Outlet, createBrowserRouter } from "react-router";

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
          { path: ":projectId", loader: projectLoader, Component: Project },
        ],
      },
    ],
  },
]);

function RootLayout() {
  return <Outlet />;
}
```

Routing rules:

- Use `children` for nested routes; parent components render child matches with `<Outlet />`.
- Use pathless parent routes for layout without adding URL segments.
- Use a route with `path` and no component to prefix child URLs without adding a layout.
- Use `{ index: true }` for a default child at the parent URL; index routes cannot have children.
- Use `:param` dynamic segments; read them from loaders/actions via `params` and components via `useParams`.
- Use `?` for optional static or dynamic segments, and `/*` splats for catchall paths. Destructure splats as `const { "*": splat } = params`.

## Loaders

Loaders run before route components render during navigation. Put route-owned reads in loaders and read the result with `useLoaderData`.

```tsx
import { createBrowserRouter, useLoaderData } from "react-router";

const router = createBrowserRouter([
  {
    path: "/teams/:teamId",
    loader: async ({ params }) => {
      const team = await fetchTeam(params.teamId);
      return { name: team.name };
    },
    Component: Team,
  },
]);

function Team() {
  const { name } = useLoaderData() as { name: string };
  return <h1>{name}</h1>;
}
```

Prefer loader data over component effects for route reads. If loader freshness needs custom control, use `shouldRevalidate`; defining it opts out of the default behavior, so preserve default cases deliberately. Loaders normally revalidate when route params change, URL search params change, or an action returns a non-error status.

Use `lazy` on a route when component, loader, or action code should be imported on demand. Use `handle` for route metadata consumed through `useMatches`.

## Actions

Actions own route mutations. When an action completes successfully, loader data on the page revalidates automatically.

```tsx
import { Form, createBrowserRouter, useActionData } from "react-router";

const router = createBrowserRouter([
  {
    path: "/projects/:projectId",
    loader: projectLoader,
    action: async ({ request, params }) => {
      const formData = await request.formData();
      return updateProject(params.projectId, {
        title: String(formData.get("title") ?? ""),
      });
    },
    Component: Project,
  },
]);

function Project() {
  const actionData = useActionData() as { title?: string } | undefined;
  return (
    <Form method="post">
      <input name="title" />
      <button type="submit">Save</button>
      {actionData?.title ? <p>{actionData.title} saved</p> : null}
    </Form>
  );
}
```

Call actions with the API that matches the UX:

- Use `<Form method="post" action="/path">` when the submission should navigate and add a browser history entry.
- Use `useSubmit` for imperative submissions caused by non-click events such as timers or external callbacks.
- Use `useFetcher` or `<fetcher.Form>` when submitting to actions or loading data without navigation.
- Use `redirect()` inside loaders/actions for route decisions such as auth redirects or redirecting to a newly created record.

## Navigation

Use declarative navigation first:

- `<Link>` for ordinary links.
- `<NavLink>` for links that need active, pending, or transitioning state; its `className`, `style`, and children props can be functions.
- `<Form action="/search">` for URL-search-param navigation from user input.
- `redirect()` from loaders/actions for data-driven navigation.

Reserve `useNavigate` for cases where the user is not directly interacting, such as inactivity timeouts or timed flows. Do not use it as a replacement for links, forms, or redirects.

## Pending And Optimistic UI

Pending UI uses router state from navigation, links, forms, and fetchers.

- Use `useNavigation()` for global route navigations and non-fetcher form submissions.
- Use `NavLink` pending state for local link indicators.
- Use `fetcher.state` for independent pending state around `fetcher.Form`.
- Use `fetcher.formData` for optimistic UI when the submitted data predicts the next UI state.

```tsx
import { useFetcher, useNavigation } from "react-router";

function GlobalPending() {
  const navigation = useNavigation();
  return navigation.location ? <Spinner /> : null;
}

function Task({ task }: { task: { title: string; status: string } }) {
  const fetcher = useFetcher();
  const isComplete = fetcher.formData
    ? fetcher.formData.get("status") === "complete"
    : task.status === "complete";

  return (
    <fetcher.Form method="post">
      <span>{task.title}</span>
      <button name="status" value={isComplete ? "incomplete" : "complete"}>
        {isComplete ? "Mark Incomplete" : "Mark Complete"}
      </button>
    </fetcher.Form>
  );
}
```

## Custom Runtime Integration

Use React Router as the browser runtime when integrating data APIs into custom bundler or server abstractions. Create route objects yourself or from an app-specific abstraction, then pass SSR hydration data if the server prepared it.

```tsx
import { StrictMode } from "react";
import { hydrateRoot } from "react-dom/client";
import { createBrowserRouter } from "react-router";
import { RouterProvider } from "react-router/dom";
import routes from "./routes";

const router = createBrowserRouter(routes, {
  hydrationData: window.__staticRouterHydrationData,
});

hydrateRoot(
  document,
  <StrictMode>
    <RouterProvider router={router} />
  </StrictMode>,
);
```

## Testing

Use `createRoutesStub` to unit test reusable components that depend on router context such as `useLoaderData`, `useActionData`, `useMatches`, `<Link>`, or `<Form>`.

```tsx
import { createRoutesStub } from "react-router";
import { render, screen, waitFor } from "@testing-library/react";
import userEvent from "@testing-library/user-event";

test("renders action errors", async () => {
  const Stub = createRoutesStub([
    {
      path: "/login",
      Component: LoginForm,
      action() {
        return { errors: { username: "Username is required" } };
      },
    },
  ]);

  render(<Stub initialEntries={["/login"]} />);

  await userEvent.click(screen.getByText("Login"));
  await waitFor(() => screen.findByText("Username is required"));
});
```

Prefer integration or E2E tests for full route behavior, especially when validating real route trees, loader/action wiring, redirects, or app shell behavior.
