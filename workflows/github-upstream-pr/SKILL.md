---
name: github-upstream-pr
description: Create a GitHub PR from local changes using git and `gh`, branching from upstream/main or origin/main, committing, pushing, and opening a concise pull request.
---

# github-upstream-pr

Use `git` and `gh` only. Do not use GitHub skills, MCP tools, or connector-backed GitHub actions.

## Inspect the repo first

- Run `git status --short --branch`, `git branch --show-current`, and `git remote -v`.
- Set a base remote: use `upstream` when it exists, otherwise fall back to `origin`.
- Fetch `<base-remote> main` before creating the PR branch.

## Create the branch from the base remote

- Base the new branch on `<base-remote>/main`.
- Prefer `fix/<slug>` for fixes and `feat/<slug>` for features.
- Never include `codex` in the branch name, commit message, PR title, or PR body unless the user explicitly asks for it.
- Preserve both committed and uncommitted work before switching branches. Transfer only the requested work onto the new branch from `<base-remote>/main`: use cherry-picks or patches for existing commits and a stash or patch for uncommitted changes. Leave source commits and unrelated user work intact.

## Commit carefully

- Stage only the files relevant to the requested work.
- Preserve unrelated user changes and do not revert them.
- Use a focused commit message that matches the change.

## Push safely

- Before pushing, review `git log <base-remote>/main..HEAD` and `git diff <base-remote>/main...HEAD`. Confirm that the PR includes the complete requested work and no unrelated changes or commits.
- Push explicitly with `git push -u origin <branch>:<branch>`.
- Do not rely on `git push -u origin <branch>` when push defaults might target the wrong remote ref.

## Open the PR with gh

- Use the `gh` CLI to create the PR against the repository that matches the base remote.
- Resolve `<head-owner>/<head-repo>` from `git remote get-url --push origin`; do not assume the authenticated account owns the push destination.
- If the push destination differs from the base repository, prefer `gh pr create --repo <base-owner>/<repo> --base main --head <head-owner>:<branch>`.
- If the push destination is the base repository, prefer `gh pr create --repo <base-owner>/<repo> --base main --head <branch>`.
- For organization-owned forks unsupported by `gh pr create --head`, use `gh api` to [create the PR](https://docs.github.com/en/rest/pulls/pulls#create-a-pull-request) against the base repository with `head=<head-owner>:<branch>`, `head_repo=<head-repo>`, and `base=main`, plus the title and body.
- Target `<base-remote>/main` unless the user explicitly asks for another base.

## Write the PR body

- Lead with the real-world use case: who encounters the problem, what triggers it, and how this change improves the outcome. For internal changes, explain the concrete developer or operational benefit.
- Describe the resulting behavior, using a brief before/after example when it makes the change clearer. Ground the explanation in available evidence; do not invent motivation or impact.
- Make the description easy to scan. Use short paragraphs, bullets, and descriptive headings when useful. Follow the repository's PR template.
- Scale detail to the change. Include validation and material limitations; omit implementation narration and exhaustive file-by-file summaries.
- Describe the final scope for a reviewer who has not seen the conversation. Update the title and body if the scope changes.
