---
name: github-contributions
description: Write clear GitHub issues and pull requests using git and `gh`. For PRs from local changes, branch from upstream/main or origin/main, commit, push, and open the PR.
---

# github-contributions

Use `git` and `gh` only. Do not use GitHub skills, MCP tools, or connector-backed GitHub actions.

For issue requests, use the shared writing guidance and the issue workflow below; skip the PR branch, commit, and push workflow. Drafting an issue does not authorize publishing it.

## Write for humans

- Lead with the real-world use case: who encounters the problem, what triggers it, and why it matters. For internal work, explain the concrete developer or operational impact.
- Make the description easy to scan. Use short paragraphs, bullets, and descriptive headings when useful. Follow the repository's relevant issue or PR template and scale detail to the scope.
- Ground claims in available evidence. Distinguish observations, unverified reports, and suspected causes; do not invent motivation, impact, or reproduction results.
- Write for someone who has not seen the conversation. Keep the title and body aligned with the final scope.

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

- Explain how the change improves the use case and describe the resulting behavior, using a brief before/after example when it makes the change clearer.
- Include validation and material limitations; omit implementation narration and exhaustive file-by-file summaries.

## Write and open issues

- Use the repository specified by the user. Otherwise, resolve the target from `upstream` when it exists, falling back to `origin`. Check its contribution guidance, issue templates, and related issues before opening a new issue to avoid duplicates.
- For bugs, describe expected and actual behavior, the smallest known reproduction, and relevant environment or version details. State when reproduction is incomplete or unverified; include only evidence that helps assess the problem.
- For feature requests, explain the blocked use case, current workaround, and desired outcome when known. Keep proposed implementation separate from the need so maintainers can assess other solutions.
- Use a specific title that identifies the problem or requested capability. Keep each issue focused on one actionable problem; link related issues instead of combining independent requests.
- Match the requested action: return a draft when asked to draft; when asked to open the issue, use `gh issue create --repo <owner>/<repo> --title <title> --body-file <path>` and return its URL. Preserve actual newlines in the body file.
