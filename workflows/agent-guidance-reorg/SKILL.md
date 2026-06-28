---
name: agent-guidance-reorg
description: Reorganize a repository's agent guidance so AGENTS.md contains only critical rules and ruleset routing, `.agents/rules/` contains scoped rulesets, and `.agents/skills/` contains task-oriented workflow skills that do not need root signpost entries.
disable-model-invocation: true
---

# Agent Guidance Reorganization

Reorganize repository agent guidance into a compact always-loaded signpost and scoped on-demand guidance.

## Core Contract

- Preserve the behavior of existing guidance unless the user explicitly requests a policy change. Do not silently weaken, broaden, or drop obligations.
- Keep root `AGENTS.md` short enough to read every turn: only critical global rules and routing to rulesets.
- Put scoped durable obligations in `.agents/rules/`.
- Put procedural task workflows in `.agents/skills/<skill-name>/SKILL.md`.
- Classify content by semantics, not filenames. Rules, prompts, docs, and skill files may contain mixed material.
- Route instead of duplicating full rules across homes.
- Keep the migration documentation-only and reviewable; prefer one single-purpose commit unless the work naturally splits into independent phases.

## Source Sweep

Before editing, read the repository's existing guidance entry points and the project docs they reference. Inspect `AGENTS.md`, `.agents/**`, `.cursor/**`, `.github/copilot-instructions.md`, `CLAUDE.md`, `GEMINI.md`, `CONTRIBUTING.md`, and any equivalent local instruction files.

Inventory repeated rules, stale or conflicting instructions, subsystem-specific constraints, procedural workflows, tool-specific prompts, and human-only background.

## Classification

Use the narrowest durable home:

- `AGENTS.md`: global invariants for all tasks, destructive-action safeguards, user-work protection, required verification/reporting behavior, and routing.
- `.agents/rules/<topic>.md`: obligations triggered by a domain, subsystem, file area, behavior type, lifecycle step, or repository operation.
- `.agents/skills/<skill-name>/SKILL.md`: workflows with ordered steps, required reading or tools, decision gates, handoffs, generated artifacts, verification, cleanup, or completion criteria.
- Project docs: human process, architecture background, rationale, or explanatory material that agents need not load automatically.
- Remove or archive: obsolete or duplicated guidance after confirming it was preserved elsewhere or intentionally dropped.

## Root Routing

Root `AGENTS.md` must let an agent decide which rulesets to read before acting without already knowing the codebase.

- Make critical root rules few, concrete, and genuinely global.
- Describe ruleset triggers in terms of recognizable operations, file areas, behavior types, or review moments.
- Use strong trigger language when missing the route would make required guidance optional.
- Ensure every referenced ruleset exists.
- Do not list `.agents/skills/` in root `AGENTS.md` unless an existing global rule must point to a specific workflow; skills can be discovered from task context or routed from rulesets.
- Keep repo-specific constraints repo-specific; do not import another repository's policies just because its structure is useful.

## Rulesets

Rulesets are scoped obligations, not background essays.

- Start each `.agents/rules/<topic>.md` with a heading and a concise "read this when..." trigger.
- State direct rules and local consequences or exceptions.
- Route to narrower rulesets or workflow skills when scoped guidance needs internal dispatch.
- Avoid restating critical root rules unless the scoped consequence matters.

## Skills

Create `.agents/skills/<skill-name>/SKILL.md` only for actual workflows. Use skill frontmatter:

```md
---
name: example-workflow
description: Do the specific workflow, including when agents should use it.
---
```

Skill bodies should define the workflow contract: required reading, ordering constraints, decision gates, ambiguity handling, expected outputs, cleanup, verification, and commit behavior.

## Migration Protocol

1. Map existing guidance into root rules, rulesets, skills, project docs, or removal.
2. Draft the new `AGENTS.md` routing first.
3. Create or update every root-routed ruleset.
4. Create or update skills only for actual workflows, and route to them from rulesets when useful.
5. Remove obsolete duplicated guidance only after preservation is clear.
6. Re-read the resulting guidance paths for common tasks such as code edits, tests, docs, git finish, workflow tasks, and repo-specific subsystem work.
7. Search for stale entry points and contradictions before finishing.

Useful checks:

```bash
find . -maxdepth 4 \( -name AGENTS.md -o -path './.agents/*' -o -name CLAUDE.md -o -name GEMINI.md -o -path './.cursor/*' -o -path './.github/copilot-instructions.md' \) -print
rg -n "MUST read|Do not|AGENTS|\\.agents|CLAUDE|GEMINI|copilot|cursor" .
```

## Quality Gates

- `AGENTS.md` is a signpost, not a handbook.
- Every root route resolves to an existing ruleset.
- Every ruleset has a clear trigger and scope.
- Every skill is task-oriented and actionable.
- Critical root rules are high-signal and globally applicable.
- No stale guidance entry point contradicts the new structure.
