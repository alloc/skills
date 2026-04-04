---
name: design-doc
description: Draft, review, and iteratively refine technical design documents for new or changing programming libraries, SDKs, or internal subsystems. Use when Codex needs to turn requirements into an implementation-ready design doc, tighten an existing proposal, define public API and runtime semantics, justify tradeoffs, surface failure modes, or maintain an explicit Ambiguities and Blockers section before implementation begins.
---

# design-doc

Use this skill to write or revise technical design documents for real libraries and similar programmable systems.

## Default Stance

- Prefer a simpler design with precise semantics over an ambitious design with ambiguous behavior.
- Make the document concrete.
- Define terms before using them.
- Separate facts, decisions, rationale, alternatives, and open questions.
- Reduce the number of plausible interpretations.
- Refuse false completeness. Do not call the design implementation-ready while blocking ambiguities remain.

## Start Here

- Determine whether the task is to draft a new document, review an existing one, or rewrite sections of an existing draft.
- Identify the library or subsystem boundary, target users, surrounding systems, and intended reviewers.
- Gather missing constraints from the repository, existing specs, APIs, or user-provided context before making design claims.
- If the request is only for critique, still propose concrete rewrites instead of commentary alone.

## Workflow

1. Diagnose the current state.
   - Identify undefined terms, vague goals, hidden assumptions, underspecified interfaces, weak rationale, contradictions, and unresolved blockers.
   - Distinguish blockers from polish problems.
2. Establish the core model.
   - State the problem, target users, motivating use cases, scope, and why the library should exist.
   - State concrete goals, meaningful non-goals, measurable or falsifiable success criteria, and relevant assumptions or constraints.
3. Specify interfaces and contracts.
   - Define every important public API, config surface, schema, protocol boundary, persistence format, or extension point.
   - For each one, define purpose, inputs, outputs, defaults, lifecycle or ownership, invariants, guarantees, failure behavior, and compatibility expectations.
4. Specify behavioral semantics.
   - State order of operations, matching rules, precedence, state transitions, concurrency behavior, retries, caching, cancellation, cleanup, and observable side effects wherever relevant.
   - Do not rely on examples alone to establish semantics.
5. Trace the main path end to end.
   - Show the major components, where state lives, how data moves, what decisions are made, and how output is produced.
6. Justify the design.
   - Name the important alternatives and the actual tradeoffs behind the selected approach.
   - Prefer explicit trade statements such as simplicity vs flexibility or latency vs correctness over generic claims.
7. Close the operational gaps.
   - Cover edge cases, invalid input, malformed configuration, dependency failure, degraded behavior, cleanup semantics, observability, testing, rollout or migration, and rollback or containment.
8. Maintain explicit uncertainty.
   - Keep `Open Questions` limited and bounded.
   - Keep `Ambiguities and Blockers` near the end of the document and update it after each substantial revision.
   - Mark each item as `blocking`, `non-blocking`, `resolved`, or `deferred`.

## Quality Gates

Treat the document as not ready if any of these remain true:

- Name a major public interface without defining its semantics.
- Leave the core execution path untraceable from input to output.
- Contradict the document on goals, trust model, compatibility, or behavior.
- Use undefined, overloaded, or unstable terminology.
- Leave a blocking open question on the core path.
- Leave failure handling undefined at a critical boundary.

## Output Rules

- Produce improved document text, not only critique.
- Use examples to clarify semantics, not to substitute for them.
- Preserve useful content from existing drafts, but tighten vague claims and normalize terminology.
- Call out remaining blockers explicitly.
- Do not mark the document as implementation-ready while any hard-fail condition or blocking ambiguity remains.

## Reference

Read [quality-bar.md](./references/quality-bar.md) when drafting a full design doc or performing a serious review. It contains the section-by-section rubric, preferred structure, and the required format for `Ambiguities and Blockers`.
