---
name: clkup
description: Use the clkup command-line client to inspect and manage ClickUp workspaces, hierarchy, tasks, comments, and time entries. Apply when a user wants ClickUp work performed through the shell; do not use for unrelated task trackers or direct ClickUp API development.
---

# clkup

Use `clkup` for compact, script-friendly access to ClickUp. Prefer the default table output while exploring, `--output json-compact` for structured results with selected fields, and `--output json` only when the full API response is needed.

## Before acting

1. Run `clkup status` to inspect the active configuration. If authentication is unconfigured, ask the user to run `clkup setup`; do not request, print, or persist their API token yourself.
2. Run `clkup auth whoami` when identity or access is uncertain.
3. Treat create, update, delete, invite, share, message, comment, time-entry, ACL, and webhook operations as external mutations. Confirm the target from read-only output first, and only perform the mutation when the user's request authorizes it.
4. Use the explicit task ID for destructive or ambiguous task operations. Some ordinary task commands can infer a task from `CLICKUP_TASK_ID` or the current Git branch; do not rely on that inference unless the resolved task is clearly shown and matches the request.

## Find the right place

Walk the ClickUp hierarchy only as far as needed:

```sh
clkup workspace list
clkup space list
clkup folder list --space SPACE_ID
clkup list list --folder FOLDER_ID
clkup list list --space SPACE_ID
```

Use `--archived` on hierarchy commands when the user expects archived objects.

## Work with tasks

List tasks in one list or search across the workspace:

```sh
clkup task list --list LIST_ID
clkup task list --list LIST_ID --status "in progress" --assignee USER_ID --include-closed
clkup task search --status "in progress" --assignee USER_ID
clkup task get TASK_ID
clkup task get TASK_ID --markdown
```

Create or update only after resolving the destination or task:

```sh
clkup task create --list LIST_ID --name "Task name" --priority 3 --due-date 2026-09-30
clkup task update TASK_ID --status "in progress"
clkup task update TASK_ID --name "Revised name" --add-assignee USER_ID
```

Priority values are `1` urgent, `2` high, `3` normal, and `4` low. For long descriptions, use `--description @path`, or `--description @-` to read stdin. Run the exact command's help before using less common update fields.

## Comments and time tracking

```sh
clkup comment list --task TASK_ID
clkup comment create --task TASK_ID --text "Plain-text comment"
clkup time current
clkup time start --task TASK_ID --description "Working on task"
clkup time stop
clkup time list --start-date 2026-09-01 --end-date 2026-09-30
```

ClickUp's v2 comment endpoint stores Markdown syntax as literal text. Use plain text unless the user specifically wants that syntax preserved.

## Control output and pagination

Global flags can be placed on resource commands:

```sh
clkup task list --list LIST_ID --fields id,name,status
clkup task list --list LIST_ID --output json-compact
clkup task list --list LIST_ID --output csv
clkup task list --list LIST_ID --quiet
clkup task list --list LIST_ID --all
clkup task list --list LIST_ID --limit 50
```

Use `--all` only when the task needs every page; otherwise prefer a bounded `--limit`. Use `--page` for v2 page-based endpoints and `--cursor` for v3 cursor-based chat and doc listings.

## Discover commands not taught here

Read [references/commands.md](references/commands.md) for the complete command-group signpost. Before using any command whose syntax is not demonstrated above, run nested help at the narrowest level:

```sh
clkup --help
clkup RESOURCE --help
clkup RESOURCE ACTION --help
```

Trust the installed CLI's help over the bundled signpost when they differ, because the command surface evolves.
