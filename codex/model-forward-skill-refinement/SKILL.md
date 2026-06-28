---
name: model-forward-skill-refinement
description: Use when refining an existing skill document so it better supports capable current and future models. Especially useful when a skill has become verbose, procedural, template-heavy, example-heavy, or overfit to current model weaknesses.
---

# Model-Forward Skill Refinement

Refine skill documents so they define durable behavior, not temporary scaffolding.

A model-forward skill trusts the agent to understand ordinary requirements, infer local context, and exercise judgment. It encodes only the constraints, protocols, artifacts, and failure modes that should remain important as models improve.

## Core Standard

A skill should define what must be true, not teach the model how to think.

Prefer:

* durable invariants
* contract semantics
* artifact boundaries
* escalation gates
* human-agent coordination protocols
* compact judgment tests
* known failure modes worth preventing

Avoid:

* obvious reasoning steps
* exhaustive inventories
* checklist theater
* model-specific crutches
* implementation narration
* repeated instructions
* verbose templates
* examples that merely restate the rule

## Refinement Rule

Keep an instruction only when it materially reduces the risk of incorrect behavior, ambiguity, scope drift, unsafe action, poor reviewability, or coordination failure.

Remove or compress instructions that are merely true, inferable, repeated, procedural, speculative, or useful only for weaker current models.

A shorter skill is not automatically better. The target is durable clarity: the fewest rules that preserve the intended behavior.

## Rewrite Heuristics

Prefer constraints over procedures.

Better:

> Do not edit the approved task contract after implementation begins unless the supervisor changes requirements.

Worse:

> After each step, check whether the task contract should be updated, then decide whether to ask...

Prefer judgment tests over inventories.

Better:

> Treat ambiguity as high-risk when a wrong assumption could materially alter behavior, scope, safety, compatibility, reviewability, or rollback.

Worse:

> High-risk ambiguity includes API behavior, UI behavior, CLI behavior, schema behavior, database behavior...

Prefer artifact semantics over templates.

Better:

> The file is a locked pre-implementation contract, not a log.

Worse:

> Include sections for assumptions, open questions, verification, progress, and discoveries.

Prefer communication protocols only when they improve coordination.

Useful protocols make review, approval, correction, or reference easier. Avoid requiring the agent to prove routine compliance or restate artifacts unnecessarily.

## Compression Pass

Before finalizing a refined skill, ask:

1. Would a stronger model still need this instruction?
2. What failure would happen if this sentence were removed?
3. Does this belong in the skill, or would a capable agent infer it from the task?
4. Is this repeated elsewhere?
5. Could this list become a principle?
6. Could this template become an artifact-purpose statement?
7. Does this example clarify a real boundary?
8. Does this instruction improve an artifact, decision, escalation, or human handoff?
9. Could this make the agent overly literal, verbose, hesitant, or bureaucratic?
10. Does this addition replace older text that should now be removed?

Keep the sentence only when the answer justifies its cost.

## Skill Shape

Treat this as a menu, not a required structure:

```markdown
---
name: <skill-name>
description: <when to use this skill>
---

# <Skill Title>

<Purpose statement>

## Core Rules

<Non-negotiable invariants>

## Standards

<Durable judgment principles>

## Required Protocols

<Human-agent, artifact, or tool protocols that must be followed>

## Artifact Shape

<Only when the skill creates or modifies a durable artifact>

## Omit / Avoid

<Only when negative constraints prevent common failure modes>
```

Omit any section that does not serve the skill.

## Success Standard

A model-forward refinement succeeds when the skill becomes easier for a capable agent to obey without losing the behavior that matters.

The result should trust ordinary reasoning while preserving the boundaries, gates, and protocols that prevent predictable failure.
