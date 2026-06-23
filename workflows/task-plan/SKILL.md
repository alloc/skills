---
name: task-plan
description: Use TASK.md as an ignored short-term planning file for coding work. Trigger when an agent needs to clarify intended behavior before editing, surface ambiguity, plan commits, or create a human-reviewable implementation contract. Especially useful before non-trivial code changes, risky refactors, bug fixes with unclear scope, multi-file edits, or work that should be reviewed as logical commits.
---

# TASK.md Planning

Use `TASK.md` as a temporary, git-ignored planning file for implementation work.

`TASK.md` is a pre-implementation contract between the agent and its supervisor. It should record the approved task: requested outcome, relevant existing behavior, intended behavior, scope, implementation approach, and commit plan.

It is not a log. Do not use `TASK.md` to track ambiguity, open questions, assumptions, verification notes, progress, discoveries, or retrospectives.

## Core Contract

* Create or update `TASK.md` at the repository root before editing code.
* `TASK.md` is git-ignored; do not force-stage it.
* Treat `TASK.md` as the approved contract for the task.
* Do not begin implementation until the supervisor explicitly approves proceeding.
* Surface high-risk ambiguity before implementation in the conversation, not in `TASK.md`.
* Disclose low-risk ambiguity and intended assumptions in the conversation, not in `TASK.md`.
* Ask 1–3 high-risk questions at a time, each with 2–3 plausible answers ordered by likely correctness.
* Complete the approved commit plan in order.
* After implementation begins, do not edit `TASK.md` unless the supervisor clearly changes the requirements or authorizes restructuring.

## Planning Standard

`TASK.md` should specify intent and constraints, not pretend to know the exact implementation path prematurely.

Unless the task is inherently mechanical, describe the work conceptually. Prefer observable behavior and references to existing packages, subsystems, APIs, commands, user flows, contracts, or ownership boundaries.

Avoid naming exact files, modules, functions, classes, or symbols merely to appear precise. Use them only when they are inherent to the task, supplied by the supervisor, or already clearly necessary.

Mechanical tasks are the exception: renames, moves, codemods, dependency bumps, config changes, generated artifacts, and similarly exact work may name precise paths, symbols, commands, and operations.

## Ambiguity Standard

Classify ambiguity by risk before writing the approved `TASK.md`.

High-risk ambiguity is any unresolved choice where a wrong assumption could materially change behavior, scope, compatibility, data safety, security, architecture, ownership, commit structure, or reviewability.

Low-risk ambiguity is uncertainty the agent can safely resolve from local conventions, nearby code, tests, style, or the most likely interpretation without materially changing the task contract.

Before implementation, surface ambiguity to the supervisor in the conversation:

* List high-risk ambiguity as supervisor-facing questions.
* For each high-risk question, provide 2–3 plausible answers ordered by likely correctness.
* List low-risk ambiguity as assumptions the agent will apply unless the supervisor objects.
* Ask for explicit permission to proceed.

If new high-risk ambiguity appears during implementation, stop and surface it before continuing. Edit `TASK.md` only if the supervisor changes the task contract or authorizes restructuring.

## Commit Standard

The commit plan must contain at least one commit. Do not force multiple commits.

Design commits for review and rollback value, not chronology. Split commits when doing so isolates distinct behavior, tests, schema/data contracts, migrations, compatibility handling, UI wiring, documentation, generated artifacts, mechanical refactors, or materially different risk profiles.

Keep work in one commit when the change is small, cohesive, easier to review together, or would otherwise create artificial or non-working intermediate states.

Each planned commit should state:

* Commit title
* Behavioral purpose
* Likely area of work, conceptual unless exact paths are necessary

## Locked Contract Rule

Once the supervisor approves implementation, `TASK.md` is locked.

Do not edit it to reconcile the plan with discoveries, changed tactics, specific files touched, verification details, progress, completed work, or retrospective corrections.

If implementation materially diverges from the approved `TASK.md`, stop and ask whether to restructure. If the divergence is not material, continue and disclose it in the final response.

## TASK.md Shape

Use this structure by default:

```markdown id="exh8kd"
# Task

## Goal

State the requested outcome in one or two sentences.

## Current Behavior

Describe the relevant existing behavior at the level of observable behavior, packages, subsystems, APIs, UI flows, commands, tests, or ownership boundaries.

Prefer conceptual references over exact implementation details unless exact details are inherent to the task.

## Intended Behavior

Specify the desired behavior in observable terms.

Include relevant user-visible behavior, API/CLI/data/integration contract changes, error handling, edge cases, backward compatibility expectations, and non-goals.

## Scope

Define what is in scope and out of scope when useful.

## Implementation Plan

Describe the expected implementation conceptually.

Prefer packages, subsystems, flows, contracts, or behavior boundaries over exact files, modules, functions, classes, or symbols unless those details are necessary.

## Commit Plan

List one or more logical commits.

For each commit, include title, behavioral purpose, and likely area of work.
```

## Final Check

Before final response or commit preparation, compare the work against the locked `TASK.md`.

Confirm that the implemented work matches the approved intended behavior and commit plan, high-risk ambiguity was resolved before implementation, low-risk assumptions were disclosed and applied safely, and `TASK.md` is not staged.

Useful checks:

```bash id="a7iaqi"
git status --short
git diff --cached --name-only
```

Use the approved commit plan as the source of truth for grouping changes and writing commit messages.
