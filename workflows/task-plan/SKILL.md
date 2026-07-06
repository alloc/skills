---
name: task-plan
description: Trigger before implementation when the work is broad, ambiguous, risky, design-heavy, architectural, expensive to unwind, or needs explicit scope, behavior, or commit-plan approval. Do not trigger for narrow, obvious, low-risk edits solely because code will change or a commit is needed.
disable-model-invocation: true
---

# TASK.md Planning

Use `TASK.md` as a temporary, git-ignored planning file for implementation work.

`TASK.md` is a pre-implementation contract between the agent and its supervisor. It records the approved task: outcome, relevant current behavior, intended behavior, scope, implementation shape, and commit plan.

It is not a scratchpad, log, checklist, transcript, or retrospective.

## Core Rules

- Create or update `TASK.md` at the repository root before editing code.
- Do not force-stage `TASK.md`; it is temporary and already git-ignored.
- Do not begin implementation until the supervisor explicitly approves proceeding.
- Surface ambiguity and assumptions to the supervisor in conversation, not in `TASK.md`.
- After implementation begins, treat `TASK.md` as locked.
- Edit locked `TASK.md` only when the supervisor changes requirements or explicitly authorizes restructuring.
- Implement the approved commit plan in order.

## Minimum Contract Standard

Write the smallest contract that preserves the supervisor-approved intent.

Include a detail only when omitting it would materially increase the risk of misunderstanding, scope drift, incorrect implementation, incorrect review, or incorrect commit grouping.

For design-driven work, include the full set of supervisor-approved design requirements that affect implementation, review, or acceptance. Preserve required layout, interaction, visual, responsive, accessibility, copy, and asset constraints unless they are clearly out of scope.

Do not include details merely because they are true, inferable, recently discovered, or potentially useful.

Prefer observable behavior and durable constraints over implementation narration.

Unless the task is mechanical, describe the implementation shape conceptually. Prefer packages, subsystems, APIs, commands, user flows, contracts, ownership boundaries, and externally visible behavior over exact files, modules, functions, classes, or symbols.

Use exact implementation references only when they are inherent to the task, supplied by the supervisor, or necessary to prevent misunderstanding.

Mechanical tasks are the exception: renames, moves, codemods, dependency bumps, config changes, generated artifacts, and similarly exact work may name precise paths, symbols, commands, and operations.

## Ambiguity Gate

Before writing or finalizing `TASK.md`, identify whether ambiguity remains.

High-risk ambiguity is any unresolved choice where a wrong assumption could materially change behavior, scope, compatibility, data safety, security, architecture, ownership, reviewability, or commit structure.

Low-risk ambiguity is uncertainty the agent can safely resolve from local conventions, nearby code, tests, style, or the most likely interpretation without materially changing the task contract.

Surface ambiguity in conversation:

- Ask only 1–3 high-risk questions at a time.
- Give each high-risk question 2–3 plausible answers, ordered by likely correctness.
- Prefix each suggested answer with a distinct capital letter within the same response, such as `A.`, `B.`, or `C.`. Reusing letters in a later pass of questions is fine.
- Disclose low-risk assumptions the agent intends to apply.
- Ask for explicit permission to proceed.

Only after high-risk ambiguity is resolved and the supervisor approves proceeding should `TASK.md` become the locked task contract.

Use the approval handoff to make the supervisor’s required attention explicit.

## Approval Handoff

After creating or updating `TASK.md`, respond in conversation with an approval handoff.

The handoff is not a replacement for `TASK.md`. Its purpose is to route the supervisor’s attention.

State:

- Whether high-risk ambiguity remains
- Any low-risk assumptions the agent intends to apply
- Whether the supervisor should answer questions, review the contract, or can approve from the summary
- A brief contract summary only when it helps the approval decision

If high-risk ambiguity remains, do not ask for implementation approval. Ask 1–3 questions. Each question must include 2–3 plausible answers ordered by likely correctness. Prefix each suggested answer with a distinct capital letter within the same response.

If no high-risk ambiguity remains but the task is broad, architectural, risky, or expensive to unwind, recommend reviewing `TASK.md` before approval and identify the parts most worth checking.

If no high-risk ambiguity remains and the task is narrow, summarize the contract briefly and ask for approval to proceed.

## Commit Plan Standard

The commit plan must contain at least one commit.

Use the fewest commits that preserve meaningful review and rollback boundaries. Additional commits are justified only when they isolate distinct behavior, tests, contracts, migrations, generated artifacts, documentation, mechanical refactors, or risk.

Do not split commits merely by chronology, package, implementation step, or because the task touches multiple areas.

Each commit should state its title, purpose, and likely area of work. Keep these conceptual unless exact references are necessary.

## Locked Contract Rule

Once implementation begins, do not edit `TASK.md` to reconcile it with discoveries, changed tactics, specific files touched, verification details, progress, completed work, or retrospective corrections.

If implementation materially diverges from the locked contract, stop and ask the supervisor whether to restructure.

If divergence is immaterial, continue and disclose it in the final response.

## TASK.md Shape

Use this shape by default:

```markdown
# Task

## Goal

State the requested outcome in one or two sentences.

## Current Behavior

Describe only the existing behavior needed to understand the change.

## Intended Behavior

Specify the desired behavior in observable terms, including relevant design requirements, constraints, edge cases, compatibility expectations, and non-goals.

## Scope

Define in-scope and out-of-scope boundaries when doing so prevents misunderstanding.

## Implementation Plan

Describe the implementation shape conceptually. Do not write a step-by-step migration screenplay.

## Commit Plan

List one or more reviewable commits.

For each commit, include title, purpose, and likely area of work.
```

Omit sections that would be empty or redundant.

## Omit From TASK.md

Omit anything that does not preserve the approved contract, including:

- Ambiguity, assumptions, open questions, or supervisor negotiation
- Verification logs, progress notes, discoveries, or retrospectives
- Exhaustive inventories of affected routes, tests, errors, features, or packages
- Design exploration, rationale, or discarded alternatives unless needed to preserve an approved requirement
- Speculative cleanup phases
- Step-by-step implementation narration
- Repeated details across sections
- Exact implementation references unless mechanically necessary

## Final Check

Before committing or giving the final response, compare the work against the locked `TASK.md`.

Confirm that the work matches the approved contract, the commit grouping follows the approved plan, any material divergence was approved, and `TASK.md` is not staged.

Useful checks:

```bash
git status --short
git diff --cached --name-only
```
