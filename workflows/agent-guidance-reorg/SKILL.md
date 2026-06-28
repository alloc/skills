---
name: agent-guidance-reorg
description: Reorganize a repository's agent guidance so AGENTS.md contains only critical rules and routing, `.agents/rules/` contains scoped rulesets, and `.agents/skills/` contains task-oriented workflow skills.
disable-model-invocation: true
---

# Agent Guidance Reorganization

Use this skill when asked to reorganize a repository's agent instructions, rules, prompts, or skills into a compact `AGENTS.md` signpost with detailed `.agents/rules/` and `.agents/skills/` files.

The target pattern:

- `AGENTS.md`: critical always-on rules plus a routing index for more specific guidance.
- `.agents/rules/`: concise rulesets loaded by trigger, such as editing production code, testing, documentation, git, UI, data, or subsystem-specific work.
- `.agents/skills/`: task-oriented procedures with frontmatter when the workflow has steps, required reading, tools, inputs, outputs, or completion criteria.

## Before Editing

1. Read the target repo's current agent guidance, including `AGENTS.md`, `.agents/**`, `.cursor/**`, `.github/copilot-instructions.md`, `CLAUDE.md`, `GEMINI.md`, `CONTRIBUTING.md`, and any project-specific docs the existing guidance references.
2. Inventory repeated rules, stale instructions, subsystem-specific guidance, task workflows, and tool-specific prompts.
3. Identify guidance scope from content, not filenames. A file named "rules" may contain a workflow; a file named "prompt" may contain durable rules.
4. Preserve semantics unless the user explicitly asks to rewrite policy. Reorganizing should not silently weaken obligations.
5. Keep changes reviewable. Prefer a single documentation-only commit unless the repo already has unrelated changes or the migration naturally splits into independent phases.

## Classify Guidance

Put each instruction in the narrowest durable home:

- **Critical root rule**: applies to every agent task, protects user work, prevents destructive operations, defines required verification, or establishes an invariant whose violation is high risk.
- **Ruleset**: applies when touching a specific domain, subsystem, file area, behavior type, lifecycle step, or repo operation.
- **Skill**: describes a task workflow with ordered steps, required reading, tools, handoffs, generated artifacts, review criteria, or completion conditions.
- **Local project doc**: explains human process, background, or architecture but does not need to be agent-loaded automatically.

Do not duplicate full rules across homes. Root `AGENTS.md` should route to detailed files instead of restating them.

## `AGENTS.md` Shape

Keep root `AGENTS.md` short enough for agents to read every turn. Use stable sections:

```md
<critical-rules>
- Do not overwrite or revert unrelated user changes.
- Do not use destructive git commands unless explicitly requested.
- Run or attempt required verification before finishing, and report limitations.
</critical-rules>

<rulesets>
Rules live in `.agents/rules/`. Read every matching ruleset before acting:

- `implementation.md`: MUST read when editing production code, refactoring, changing architecture, adding abstractions or exports, or changing dependencies.
- `testing.md`: MUST read when adding, changing, reviewing, or deciding whether to add tests, and when verifying behavior changes.
- `git.md`: MUST read before staging, committing, reviewing diffs, splitting work, or finishing any file-changing task.
</rulesets>
```

Adapt the exact rules to the target repo. Keep trigger language concrete: name file areas, operations, behavior types, or review moments that an agent can recognize before acting.

## Ruleset Files

Create `.agents/rules/<topic>.md` for scoped obligations. Each ruleset should:

- Start with a heading and a one-sentence "read this when..." trigger.
- Contain direct rules, not background essays.
- Prefer specific constraints over vague preferences.
- Route to more specific rules or skills when needed.
- Avoid repeating critical root rules unless the local consequence or exception is important.

Use domain rulesets when a broad area needs internal routing. For example, an `app.md` ruleset can say to read it before editing `app/`, then route app UI, app state, app data, and app-local skills.

## Skill Files

Create `.agents/skills/<skill-name>/SKILL.md` when guidance is procedural. Use skill frontmatter:

```md
---
name: example-workflow
description: Do the specific workflow, including when agents should use it.
---
```

Skill bodies should state:

- when to use the skill;
- required reading;
- ordered workflow steps;
- decision gates and ambiguity handling;
- expected output, cleanup, verification, and commit behavior.

Keep task skills separate from rulesets. A rule says what must be true; a skill says how to perform a workflow.

## Migration Workflow

1. Map existing guidance into `critical`, `ruleset`, `skill`, or `archive/remove`.
2. Draft the new `AGENTS.md` routing first.
3. Create or update `.agents/rules/` files so every route in `AGENTS.md` resolves.
4. Create or update `.agents/skills/` only for actual workflows.
5. Remove obsolete duplicated guidance after confirming it was preserved or intentionally dropped.
6. Re-read the full new guidance path for common tasks: code edit, test change, docs change, git finish, and any repo-specific subsystem.
7. Verify with searches that no stale guidance entry points contradict the new pattern.

Useful checks:

```bash
find . -maxdepth 4 \( -name AGENTS.md -o -path './.agents/*' -o -name CLAUDE.md -o -name GEMINI.md -o -path './.cursor/*' -o -path './.github/copilot-instructions.md' \) -print
rg -n "MUST read|Do not|AGENTS|\\.agents|CLAUDE|GEMINI|copilot|cursor" .
```

## Quality Bar

- `AGENTS.md` is a signpost, not a handbook.
- Every referenced ruleset or skill exists.
- Every ruleset has a clear trigger.
- Every skill is task-oriented and actionable.
- Critical rules are few, high-signal, and genuinely global.
- Repo-specific constraints remain repo-specific; do not import another repo's policies just because its structure inspired the pattern.
- Agents can decide what to read before making changes without already knowing the codebase.
