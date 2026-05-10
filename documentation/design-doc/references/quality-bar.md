# Design Doc Quality Bar

Load this file when drafting a full technical design document or performing a deep review. Use it as a rubric, not as boilerplate.

## Table of Contents

- [Default Stance](#default-stance)
- [Section Requirements](#section-requirements)
- [Preferred Structure](#preferred-structure)
- [Ambiguities and Blockers](#ambiguities-and-blockers)
- [Writing Standards](#writing-standards)
- [Review Pass](#review-pass)
- [Readiness Gate](#readiness-gate)

## Default Stance

- Make the document concrete.
- Remove ambiguity.
- Define terms before using them.
- State assumptions explicitly.
- Separate facts, decisions, rationale, and open questions.
- Refine until the document is safe for implementation review.
- Prefer a simpler design with precise documentation over a more impressive design with ambiguous semantics.

The document should let a competent engineer understand:

- What problem the library solves.
- Who it is for.
- What the library is and is not.
- How its public API behaves.
- How the runtime or execution model works.
- What tradeoffs were chosen and why.
- What edge cases, failure modes, and testing strategies matter.

## Section Requirements

### 1. Overview and Context

State:

- The problem being solved.
- The target users.
- The use cases that matter.
- Why the library should exist.
- What kind of library or subsystem it is.
- Where it fits relative to surrounding systems.

Make the opening section sufficient for a reader to understand purpose and scope.

### 2. Goals, Non-Goals, and Success Criteria

- Make goals concrete enough to guide design decisions.
- Make non-goals meaningfully constrain the design.
- Make success criteria measurable or at least falsifiable.
- Reject vague goals such as "ergonomic," "simple," "modern," or "performant" unless the document explains what those mean in practice.

### 3. Terminology, Assumptions, and Constraints

- Define important terms before using them.
- Use each term consistently.
- Surface hidden assumptions explicitly, including platform, runtime, compatibility, performance, security or trust boundaries, operational limits, and migration constraints.
- Do not rely on examples alone to establish semantics.

### 4. Proposed Design

- Explain the design at the right level of abstraction.
- Show the major components, responsibilities, and boundaries.
- Avoid both underspecification and incidental implementation noise.
- Provide enough detail for implementation planning and critical review.

### 5. Interfaces and Contracts

Specify every important interface, not just its name. This includes public APIs, types, schemas, configuration surfaces, protocol boundaries, persistence formats, and extension points.

For each important interface, define:

- Purpose.
- Inputs.
- Outputs.
- Defaults.
- Ownership or lifecycle semantics.
- Invariants.
- Guarantees.
- Failure or error behavior.
- Compatibility or versioning expectations, when relevant.

If an API is named, explain what it does and what guarantees it provides.

### 6. Behavioral Semantics

Define behavior at critical decision points. Be precise about:

- Order of operations.
- Matching or selection rules.
- State transitions.
- Precedence or conflict resolution.
- Concurrency behavior.
- Idempotency and retries.
- Caching and invalidation semantics.
- Cancellation and cleanup behavior.
- Observable side effects.

If multiple reasonable interpretations exist, the document is incomplete.

### 7. Architecture and End-to-End Flow

- Let a reader trace the main path end to end.
- Show how input moves through the system, how it is transformed, what decisions are made, and how output is produced.
- Explain major components, why they exist, how they interact, where state lives, and where data is created, transformed, and consumed.

### 8. Alternatives, Tradeoffs, and Rationale

- Justify important decisions.
- Name rejected alternatives and explain why they were rejected.
- State the actual trade: simplicity vs flexibility, compile-time vs runtime complexity, latency vs correctness, local reasoning vs global coordination, extensibility vs tight semantics, or safety vs convenience.

### 9. Edge Cases, Failure Modes, and Operational Risks

Address important edge cases and failure modes, including:

- Invalid input.
- Malformed configuration.
- Dependency failure.
- Ambiguous cases.
- Degraded behavior.
- Cleanup semantics.
- Critical operational risks.

When behavior is undefined or intentionally unsupported, say so explicitly.

### 10. Testability, Rollout, and Observability

Make the design easy to verify and safe to introduce. Include:

- Invariants.
- Testable behaviors.
- Observability hooks.
- Logging, metrics, or tracing plans when relevant.
- Migration or rollout strategy when relevant.
- Rollback or containment strategy when relevant.

Avoid generic statements such as "we will add tests." Tie tests to concrete behaviors and guarantees.

### 11. Open Questions

- Keep open questions isolated and bounded.
- Distinguish unresolved details that do not block implementation from unresolved decisions that do block implementation.
- Do not leave central runtime behavior or API semantics as open questions.

### 12. Internal Consistency and Document Quality

- Keep the document coherent, easy to scan, and dense with signal.
- Keep definitions, examples, APIs, and recommendations consistent with one another.
- Do not let a non-goal quietly reappear later as a requirement.
- Do not let examples imply behavior that contradicts stated semantics.

## Preferred Structure

Use this structure unless the document clearly benefits from a tighter variant:

- Overview / Problem Statement
- Context
- Goals
- Non-Goals
- Assumptions and Constraints
- Terminology
- Proposed Design
- API / Interface Specification
- Behavioral Semantics
- Architecture / Data Flow
- Alternatives and Tradeoffs
- Failure Modes and Edge Cases
- Testing and Observability
- Rollout / Migration
- Open Questions
- Ambiguities and Blockers
- Appendix / Examples

Allow compression for small designs, but do not omit semantics that belong in these sections.

## Ambiguities and Blockers

Keep a dedicated section titled `Ambiguities and Blockers` near the end of the document. Update it after every substantial revision.

For each item, include:

- ID.
- Title.
- Status.
- Affected area.
- Description of the ambiguity or blocker.
- Why it matters.
- Proposed resolution or next step.

Use statuses such as:

- `blocking`
- `non-blocking`
- `resolved`
- `deferred`

Use a compact, high-signal format such as:

```md
- AB-1 - Blocking - Sequence timeout semantics
  - Affected area: Behavioral Semantics / API
  - Issue: The document does not specify when a partially matched sequence expires.
  - Why it matters: Implementations may diverge on correctness and UX.
  - Next step: Define timeout semantics and whether timeout is configurable.

- AB-2 - Non-blocking - Trace event schema naming
  - Affected area: Observability
  - Issue: Event field names are not finalized.
  - Why it matters: Affects tooling consistency, but not the core runtime model.
  - Next step: Finalize before beta.
```

Do not let important uncertainty remain implicit in the prose. Surface it here. When an ambiguity is resolved, remove it or move it into a brief resolved-history subsection if the decision trail still matters.

## Writing Standards

- Write like a senior engineer authoring a design doc for other engineers.
- Prefer short declarative sentences over promotional language.
- Prefer precise prose over pseudo-precision.
- Use examples to clarify, not to substitute for specification.
- When an example implies behavior, state that behavior normatively in prose.

When revising an existing design doc:

- Preserve useful content.
- Tighten vague claims.
- Normalize terminology.
- Fill semantic gaps.
- Surface contradictions.
- Isolate unresolved questions.
- Improve structure and scanability.
- Update `Ambiguities and Blockers`.
- Make the document safer to implement from.

## Review Pass

Run this pass before presenting the result:

1. Verify that the opening explains the problem, users, scope, and surrounding system.
2. Verify that goals, non-goals, and success criteria constrain the design.
3. Verify that every major interface has defined semantics and failure behavior.
4. Verify that the main execution path can be traced end to end.
5. Verify that major tradeoffs are justified against named alternatives.
6. Verify that failure modes, testing, observability, and rollout are concrete.
7. Verify that `Open Questions` stay bounded and that `Ambiguities and Blockers` reflects the current state.
8. Verify that examples and terminology do not contradict the normative prose.

## Readiness Gate

Do not present the design as implementation-ready if any of these remain true:

- A major public API or interface exists without defined semantics.
- The core execution path cannot be traced end to end.
- The document contradicts itself on goals, trust model, compatibility, or behavior.
- Key terminology is undefined, overloaded, or unstable.
- An open question blocks implementation of the core path.
- Failure handling is undefined at a critical boundary.

The standard for success is simple: an engineering team should be able to implement the library with only minor clarification requests, and reviewers should be able to challenge the design without first guessing what it means.
