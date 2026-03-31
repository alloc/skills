---
name: github-upstream-pr
description: Create a branch from upstream/main, commit local changes, push to a fork, and open a pull request against the upstream repository with the gh CLI. Use when the user wants an upstream PR created from local work and cares about branch naming, concise PR copy, or avoiding GitHub app skills/connectors.
---

# github-upstream-pr

Use `git` and `gh` only. Do not use GitHub skills, MCP tools, or connector-backed GitHub actions.

## Inspect the repo first

- Run `git status --short --branch`, `git branch --show-current`, and `git remote -v`.
- Confirm that `upstream` exists. If it does not, stop and ask the user how to proceed.
- Fetch `upstream main` before creating the PR branch.

## Create the branch from upstream

- Base the new branch on `upstream/main`, not `origin/main`.
- Prefer `fix/<slug>` for fixes and `feat/<slug>` for features.
- Never include `codex` in the branch name, commit message, PR title, or PR body unless the user explicitly asks for it.
- If the relevant changes are on another branch, preserve them with a stash or patch, switch to the new branch from `upstream/main`, and reapply only the requested changes.

## Commit carefully

- Stage only the files relevant to the requested work.
- Preserve unrelated user changes and do not revert them.
- Use a focused commit message that matches the change.

## Push safely

- Push explicitly with `git push -u origin <branch>:<branch>`.
- Do not rely on `git push -u origin <branch>` when push defaults might target the wrong remote ref.

## Open the PR with gh

- Use the `gh` CLI to create the PR against the upstream repository.
- Resolve the fork owner with `gh api user -q .login` when needed.
- Prefer `gh pr create --repo <upstream-owner>/<repo> --base main --head <login>:<branch>`.
- Target `upstream/main` unless the user explicitly asks for another base.

## Write the PR body

- Keep the PR body to one short paragraph.
- Use plain language and state what is being fixed or added.
- Avoid headings, checklists, formal templates, and overly polished wording.
