# Forms and feedback

Use for input flows, editing, validation, submission, and asynchronous feedback. These are contextual recommendations; use [accessibility.md](accessibility.md) for requirements and platform distinctions.

## Choose the interaction before styling the fields

Ask only for information needed for the task. Reuse known values when appropriate and expose consequential defaults. Separate an editable draft from a committed result when users need to inspect changes before applying them.

Use a single page when the inputs form one understandable task. Consider steps for genuinely separate decisions, dependencies, or substantial complexity, accounting for the navigation cost. A step indicator should describe meaningful progress; allow review without silently losing later entries. Do not split a short form merely to make it feel lighter.

Group related inputs under useful headings. Put prerequisites before dependent choices. A single column often helps sequential entry, while related short fields or dense editing tasks may benefit from a compact grid. Reading and keyboard order should still be understandable.

## Labels, help, and controls

Keep labels available after entry. Placeholders may illustrate a format but should not carry essential instructions. Explain unusual constraints before failure, especially units, accepted formats, and consequences. Mark required or optional fields using a convention suited to the form rather than adding redundant markers everywhere.

Choose controls by the decision involved: a toggle usually changes a setting, a checkbox can collect an independent choice, and a radio group exposes mutually exclusive alternatives. A select saves space; visible choices can make comparison easier. Avoid custom controls when existing primitives already provide the required semantics and keyboard behavior.

On web, distinguish input value from keyboard preference. Identifiers such as postal codes and account numbers are not necessarily quantities: number inputs may introduce steppers or alter leading zeros. Use appropriate input type, input mode, and autocomplete metadata for the actual value. On native platforms, use corresponding keyboard and autofill facilities. Keep paste and password-manager workflows available.

Help belongs near the decision it explains. Avoid tooltips as the sole source of instructions, especially on touch. Make read-only values selectable or copyable when useful; distinguish them from controls temporarily disabled by state.

## Validate when the result is useful

Use validation timing appropriate to the field. Submission validation can suit short forms; blur can suit completed values; immediate feedback can help a constrained editor or password requirement list. Avoid displaying an error for an incomplete value while someone is still entering it. After an error, reevaluation during correction can be helpful.

Separate format errors, cross-field conflicts, and server failures. State the problem and a feasible recovery rather than echoing an error code. Do not claim an address, username, or transaction is valid solely because a client-side check passed.

Associate field errors with their controls. For failed submissions with multiple errors, a linked summary can make the whole problem discoverable while retaining inline messages. Choose focus movement deliberately: the summary or first invalid field may be appropriate after submit; routine validation should not repeatedly steal focus. See [WAI form notifications](https://www.w3.org/WAI/tutorials/forms/notifications/) for accessible notification patterns.

## Submission is a state transition

| State | What the user needs |
| --- | --- |
| Editing | Clear action scope and whether changes are saved automatically |
| Pending | Acknowledgment of the operation and protection against unintended duplicate effects |
| Success | Confirmation through the resulting content or status, plus the next useful action |
| Failure | Preserved input, an explanation, and a recovery path |
| Unknown outcome | Honest uncertainty and a way to check status before repeating consequential work |

Disabling submission can prevent repeated activation, but do not disable the entire interface without a reason. Cancellation, navigation, or unrelated work may remain useful. For high-consequence requests, preventing duplicate effects also requires implementation support; a spinner alone is insufficient.

Use optimistic updates when errors can be corrected and the outcome is reversible. Make rollback understandable and preserve any later edits. For autosave, distinguish saving, saved, and failed states; leaving the page should not silently discard unsaved work. Warn on dismissal when unsaved changes warrant interruption, rather than confirming every close.

## Choose feedback by consequence

Prefer local feedback for local work. Toasts can confirm incidental outcomes, but important errors, next steps, and the only undo action need durable access. Avoid unconditional dismissal timers. Announce meaningful status changes selectively without narrating every keystroke or frame.

Use undo when reversal is reliable. Use confirmation or preview when the scope, cost, or irreversibility justifies interruption; name the affected object and consequence. Do not make every destructive action an identical generic dialog.

Check a failed submission after substantial entry, a slow or ambiguous response, repeated activation, and correction after an error. These reveal more than the empty form alone.
