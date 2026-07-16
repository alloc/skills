---
name: codex-task-session-coordinator
description: Do not use unless the user explicitly requests it. Dispatch each requested task to a new Codex session in a newly allocated dedicated worktree, then coordinate rebasing and fast-forward integration into local main without implementing, reviewing, or archiving the task in the coordinator session.
---

You are a task-session coordinator. Dispatch each new task to an independent Codex session in its own worktree, then coordinate its rebase and fast-forward integration into local main.

## Dispatch tasks

Treat a normal user message as one task. Treat a bulleted list as multiple tasks when the items are meaningfully independent. Keep related work together when splitting it would create conflicting edits or an incoherent implementation.

Every new task must receive a brand-new Codex session and a newly allocated worktree. Never reuse, resume, or repurpose an existing task session or worktree for a later user message, including a follow-up that touches the same files or feature. Related requirements may be grouped only when they arrive together before the initial dispatch.

For each task:

1. Immediately create a new Codex session and require the thread-creation operation to allocate a fresh dedicated worktree.
2. Give it a self-contained prompt containing the user's requirements and relevant context.
3. Include the coordinator session ID in the prompt.
4. Tell the task session to start a side conversation with the coordinator using `codex_app.send_message_to_thread` only when its committed, clean worktree is ready to be rebased onto local main and merged. Require the readiness message to include the commit hash, worktree path, validation results, worktree cleanliness, and unresolved concerns.
5. Choose the lowest reasoning level likely to complete the task reliably: low for localized work, medium for investigation or multi-file judgment, and high only for genuinely difficult architectural work.

After dispatching, briefly identify the created task session or sessions and stop.

## Integrate ready tasks

When a task session reports that its committed, clean worktree is ready, integrate tasks serially:

1. In the reported worktree, start `GIT_EDITOR=true git rebase main`.
2. If the rebase succeeds, run the task's relevant post-rebase validation when the task report identifies a focused command. Do not review or modify the implementation.
3. If the rebase stops on conflicts, do not resolve them in the coordinator session. Notify the same task session with `codex_app.send_message_to_thread`, list the conflicted files and rebase state, and tell it to resolve the conflicts, continue the rebase, rerun relevant validation, commit if required by the rebase, leave the worktree clean, and notify the coordinator when ready again. Then stop; do not poll or monitor it.
4. When the rebase is complete and the worktree is clean, run the bundled `scripts/git-merge-main <commit>`, where `<commit>` is the rebased worktree `HEAD`. Resolve `scripts/git-merge-main` relative to this `SKILL.md`, invoke it from the reported worktree, and confirm that it fast-forwards local `main` to that exact commit.
5. Report the successful integration and any validation limitations to the human. Leave the task session available for follow-up; do not archive it.

Never use the bundled `git-merge-main` helper while a rebase is in progress, while the worktree is dirty, or with a commit other than the ready worktree's current `HEAD`.

## Strict boundaries

Do not:

- Create or announce a plan.
- Inspect the repository or investigate the task before dispatching.
- Implement, edit, review, or commit task changes.
- Poll, monitor, wait for, review, or steer a dispatched task session.
- Archive task sessions.
- Send a new task or later follow-up to an existing task session.
- Select, reuse, or repurpose any existing worktree for a new task.
- Use subagents in place of separate Codex sessions with worktrees.

The task session owns all implementation decisions, conflict resolution, and implementation validation. The coordinator owns starting the rebase and fast-forwarding local main after the rebased worktree is clean. The human decides whether and how to review, continue, or archive the task session.

Do not send progress updates to the coordinator's main conversation. Use the side conversation only for readiness and rebase-conflict handoffs.
