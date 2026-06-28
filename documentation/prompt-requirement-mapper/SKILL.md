---
name: prompt-requirement-mapper
description: Use when a user asks to unpack, clarify, improve, operationalize, or rewrite a prompt or brief by extracting explicit details, implied requirements, design or execution choices, ambiguities, safe defaults, and next steps; especially for creative, product, UX, writing, research, planning, or artifact-generation prompts.
disable-model-invocation: true
---

# Prompt Requirement Mapper

## Core Purpose

Turn a raw user prompt into a structured reading aid that answers:

* What is the user asking for?
* What details are explicitly specified?
* What choices are implied but not stated?
* What constraints, preferences, and success criteria matter?
* What questions remain unresolved?
* How should the agent proceed?

The output should not merely summarize the prompt. It should organize the prompt into useful decision-making categories.

## Guiding Principles

### 1. Separate What Is Stated From What Is Inferred

Always distinguish between:

* **Explicit details**: directly present in the prompt
* **Implied choices**: reasonable inferences from wording, context, or genre
* **Open questions**: details that cannot be safely inferred

Never present an inference as if the user stated it.

### 2. Optimize for Human Reading

The output should be easy to scan. Prefer:

* Short sections
* Descriptive headings
* Tables for comparisons
* Bullets for grouped attributes
* Bold labels for important fields
* Plain language over internal reasoning jargon

Avoid dense paragraphs unless explaining nuance.

### 3. Preserve the User's Intent

Do not overwrite the user's idea with your own preferences. Extract and clarify before improving. When suggesting design choices, keep them grounded in the prompt.

### 4. Surface Ambiguity Without Stalling

Identify missing information, but do not over-question. If the task can proceed with reasonable defaults, state those defaults clearly.

### 5. Make the Output Actionable

A good extraction should help someone immediately execute, revise, delegate, or critique the prompt.

## Recommended Output Structure

Use this structure by default, adjusting as needed for the user's context.

### 1. One-Line Intent

A concise statement of what the user wants.

Example:

> Create a premium landing page concept for a productivity app aimed at remote teams.

### 2. Extracted Details

List concrete details from the prompt.

Suggested categories:

| Category             | Details                                               |
| -------------------- | ----------------------------------------------------- |
| Deliverable          | What the user wants created or analyzed               |
| Subject              | Main topic, product, character, brand, scene, or idea |
| Audience             | Who it is for                                         |
| Format               | Medium, dimensions, file type, length, or structure   |
| Tone                 | Emotional or stylistic direction                      |
| Content Requirements | Required messages, sections, claims, or elements      |
| Constraints          | Limits, exclusions, rules, or must-haves              |
| Context              | Background information the prompt provides            |

Only include categories that help readability.

### 3. Design Choices

Extract or infer choices that affect execution.

Useful subcategories:

| Design Area  | Stated Choice               | Implied or Recommended Choice | Notes                                      |
| ------------ | --------------------------- | ----------------------------- | ------------------------------------------ |
| Visual Style | Directly named style        | Reasonable interpretation     | Clarify if uncertain                       |
| Layout       | Specified arrangement       | Suggested hierarchy           | Explain why it fits                        |
| Color        | Named palette or mood       | Likely palette direction      | Avoid inventing brand colors unless needed |
| Typography   | Font or type direction      | Readability-based suggestion  | Keep practical                             |
| Imagery      | Required subjects or motifs | Supporting image ideas        | Separate required from optional            |
| Interaction  | UX behavior or flow         | Suggested interaction pattern | For product/UI prompts                     |
| Voice        | Stated tone                 | Editorial treatment           | For writing prompts                        |

For non-visual prompts, rename this section to **Execution Choices** or **Strategic Choices**.

### 4. Implied Requirements

Identify requirements that are not explicitly stated but are necessary for a strong result.

Examples:

* The output should be organized for quick scanning.
* The style should remain consistent across sections.
* The design should prioritize accessibility and legibility.
* The final artifact should match the user's requested format.
* Claims should be supported if the prompt asks for factual or research-based content.

Mark these as inferred.

### 5. Ambiguities and Missing Details

List unresolved details that could affect the result.

Use a table when several items are missing:

| Missing Detail  | Why It Matters                        | Safe Default                  |
| --------------- | ------------------------------------- | ----------------------------- |
| Target audience | Affects tone, examples, and hierarchy | General professional audience |
| Visual style    | Affects layout, color, and imagery    | Clean modern style            |
| Length          | Affects depth and formatting          | Medium-length response        |

Do not ask every possible question. Include only meaningful uncertainties.

### 6. Suggested Defaults

When the prompt leaves details unspecified, recommend practical defaults.

Good defaults are:

* Conservative
* Reversible
* Aligned with the user's stated intent
* Easy to explain
* Suitable for the medium

Example:

> Since no audience is specified, assume an educated general audience and avoid heavy jargon.

### 7. Execution Plan

Provide a short plan for how the agent should fulfill the prompt.

Example:

1. Confirm the intended deliverable and audience.
2. Organize explicit details into a brief.
3. Apply inferred design choices as defaults.
4. Produce the requested artifact or revised prompt.
5. Note remaining assumptions.

Keep this section short unless the user asks for a detailed plan.

### 8. Optional: Rewritten Prompt

If useful, provide a polished version of the user's prompt that incorporates the extracted details and defaults.

Use this format:

```markdown
Create [deliverable] about [subject] for [audience]. Use [tone/style]. Include [required elements]. Follow these constraints: [constraints]. Assume [defaults] unless otherwise specified.
```

Only include a rewritten prompt when it helps the user reuse or improve the original.

## Extraction Checklist

Before responding, check for these detail types:

### Task Details

* What action is requested?
* What is the final deliverable?
* Is the user asking for analysis, creation, editing, transformation, or planning?
* Does the user want a file, a draft, a prompt, a critique, or a recommendation?

### Content Details

* What subject matter is named?
* What facts, examples, sections, or components must be included?
* What should be excluded?
* Are there required terms, names, brands, dates, or data points?

### Audience Details

* Who will read, use, view, or receive the result?
* What knowledge level should be assumed?
* Is the audience internal, external, technical, executive, creative, casual, or public?

### Style and Design Details

* What tone is requested?
* What visual or editorial style is requested?
* Are there references, inspirations, genres, or examples?
* Are color, typography, composition, pacing, or hierarchy implied?

### Format Details

* Is there a requested structure?
* Is there a target length?
* Is a specific file type, platform, or medium required?
* Are there constraints around readability, accessibility, or layout?

### Operational Details

* Does the prompt require current information?
* Does it require citations, sources, calculations, or external files?
* Does it require tools or artifact generation?
* Are there safety, privacy, legal, medical, or financial implications?

## Recommended Response Templates

### Compact Template

Use when the user wants a quick breakdown.

```markdown
## Intent
[One-line explanation]

## Key Details
- **Deliverable:** ...
- **Subject:** ...
- **Audience:** ...
- **Tone/style:** ...
- **Constraints:** ...

## Design / Execution Choices
- **Stated:** ...
- **Implied:** ...
- **Recommended default:** ...

## Open Questions
- ...
```

### Detailed Template

Use when the prompt is complex or design-heavy.

```markdown
## One-Line Intent
...

## Extracted Details
| Category | Details |
|---|---|
| Deliverable | ... |
| Subject | ... |
| Audience | ... |
| Format | ... |
| Tone | ... |
| Constraints | ... |

## Design Choices
| Area | Stated | Inferred / Recommended | Notes |
|---|---|---|---|
| Layout | ... | ... | ... |
| Color | ... | ... | ... |
| Typography | ... | ... | ... |
| Imagery | ... | ... | ... |

## Implied Requirements
- ...

## Ambiguities
| Question | Why It Matters | Safe Default |
|---|---|---|
| ... | ... | ... |

## Suggested Execution
1. ...
2. ...
3. ...
```

### Prompt-Refinement Template

Use when the user wants to improve a prompt.

```markdown
## What the Current Prompt Already Specifies
- ...

## What It Leaves Open
- ...

## Recommended Design Choices
- ...

## Improved Prompt
[Rewritten prompt]
```

## Handling Design Choices

When extracting design choices, look for both direct and indirect signals.

### Direct Signals

Examples:

* “minimalist”
* “cinematic”
* “executive-ready”
* “playful”
* “use a dark background”
* “make it feel premium”
* “for a technical audience”

Treat these as explicit choices.

### Indirect Signals

Examples:

* “for investors” implies concise, polished, evidence-oriented presentation.
* “for children” implies simple language, warmth, and visual clarity.
* “dashboard” implies hierarchy, scannability, and data clarity.
* “luxury” implies restraint, whitespace, refined typography, and selective detail.

Treat these as inferred choices and label them accordingly.

## Reading-Optimized Formatting Rules

Follow these rules unless the user requests another format:

* Start with the most useful summary, not process notes.
* Use headings that describe the content clearly.
* Prefer tables for multi-factor comparisons.
* Keep bullets parallel and concise.
* Use bold labels for important attributes.
* Group related details instead of listing everything chronologically.
* Put assumptions near the details they affect.
* End with next steps, defaults, or a cleaned-up prompt.

## Quality Bar

A strong response should make the original prompt easier to act on. It should feel like a well-organized creative brief, product brief, or execution brief.

The response is successful when a human can quickly understand:

* The user's goal
* The important details
* The design or execution direction
* What is known versus assumed
* What remains undecided
* How to proceed

## Common Mistakes to Avoid

* Blending stated facts and assumptions together
* Adding personal creative preferences without labeling them
* Overloading the user with too many clarifying questions
* Rewriting the prompt before analyzing it
* Ignoring audience, format, or constraints
* Treating “style” as only visual when it may also involve voice, structure, pacing, or level of detail
* Making the output too dense for quick reading
* Failing to mention missing details that materially affect the result

## Default Behavior Summary

When applying this skill:

1. Identify the user's main intent.
2. Extract explicit details into readable categories.
3. Identify design or execution choices.
4. Separate stated facts from inferred choices.
5. Surface meaningful ambiguities.
6. Recommend safe defaults.
7. Present everything in a clean, human-readable structure.
8. Provide a rewritten prompt only when it adds practical value.
