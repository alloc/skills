---
name: mermaid-diagrams
description: Read this guide when writing or editing documentation and deciding whether to add, omit, or revise a Mermaid diagram, especially when explaining workflows, dependencies, state transitions, system architecture, or actor interactions where visual structure may clarify the text.
---

# Mermaid Diagrams in Documentation

Use this skill when writing or editing documentation and deciding whether to add, omit, or revise a Mermaid diagram.

## Core Principle

Add a Mermaid diagram only when the **visual structure communicates something that prose alone would make the reader mentally reconstruct**.

A good Mermaid diagram is a map. A bad Mermaid diagram is a paragraph with arrows.

## Use Mermaid When the Relationship Is the Point

Add a diagram when it clarifies one or more of these:

- **Flow:** what happens before, after, or in parallel.
- **Branching:** where decisions change the path.
- **Dependencies:** what relies on what.
- **Ownership or handoff:** which actor, service, team, or component does each step.
- **State:** which states exist and which transitions are allowed.
- **Architecture:** how components connect at a system level.
- **Sequence:** how messages or operations move between participants over time.
- **Cycles or feedback loops:** where the same process can repeat.

Prefer Mermaid when the reader would otherwise need to keep several entities, arrows, states, or branches in working memory.

## Do Not Use Mermaid When Text Is Clearer

Skip the diagram when it would only restate:

- A short linear list.
- A table of contents.
- A set of definitions.
- A simple hierarchy already obvious from headings.
- A paragraph of explanation squeezed into boxes.
- A process with no meaningful branches, dependencies, states, or interactions.
- A concept where nuance, tradeoffs, or judgment matter more than structure.

If a numbered list, table, or paragraph is equally clear, do not add Mermaid.

## Choose the Right Mermaid Form

Use:

- `flowchart` for workflows, decision trees, dependencies, and high-level architecture.
- `sequenceDiagram` for interactions between people, services, systems, or APIs over time.
- `stateDiagram-v2` for lifecycle states and allowed transitions.
- `classDiagram` or `erDiagram` for domain models, data relationships, and schemas.
- `graph` or `flowchart` with `subgraph` groups for component relationships.

Do not force every explanation into a flowchart. Pick the diagram type that matches the structure.

## Quality Rules

A Mermaid diagram should be:

- **Smaller than the explanation, not larger.**
- **Referenced by the surrounding text.**
- **Focused on one idea.**
- **Readable without decoding effort.**
- **Labeled with short noun or verb phrases.**
- **Split into multiple diagrams if it becomes dense.**

Avoid:

- Long sentence labels.
- Decorative arrows.
- Too many nodes.
- Unlabeled edges where the relationship is ambiguous.
- Repeating the same information immediately before or after the diagram.
- Using Mermaid as a substitute for explaining why something matters.

## Decision Checklist

Before adding Mermaid, ask:

1. Does layout, direction, grouping, or connection carry meaning?
2. Does the diagram reduce cognitive load?
3. Does it reveal relationships that are hard to see in prose?
4. Is there branching, sequencing, dependency, state, ownership, or architecture?
5. Would a bullet list or table be just as clear?

Add the diagram only if the answer is yes to at least one structural reason and no simpler format would do the job as well.

## Final Rule

Use Mermaid to show structure. Use prose to explain meaning.
