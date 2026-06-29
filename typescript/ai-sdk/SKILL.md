---
name: ai-sdk
description: Use when writing, reviewing, debugging, or explaining Vercel AI SDK code where v7 APIs or behavior matter, especially Node/ESM requirements, instructions prompts, lifecycle events, telemetry, streaming, tool context, UI messages, multi-step results, MCP transport, Vue, and OpenAI/Anthropic/Google provider changes. This is a focused AI SDK v7 correction layer, not a v6-to-v7 migration walkthrough.
---

# AI SDK v7

Treat this as a compact correction layer for AI SDK knowledge that may still reflect v6. Prefer v7-native APIs and result semantics in new examples and reviews.

Do not answer as though this were a migration guide. If the user asks for a full migration plan, use the official migration guide or codemods separately. For normal coding/review tasks, assume the agent already knows AI SDK concepts and only apply the v7-specific deltas.

## First Checks

1. Confirm the project can run AI SDK v7: Node.js 22 or later and ESM imports. For production guidance, prefer current LTS Node where the project permits it.
2. Inspect package usage across `ai`, framework packages such as `@ai-sdk/react` or `@ai-sdk/vue`, provider packages, and telemetry packages.
3. Load [references/v7-changes.md](references/v7-changes.md) when exact names, result shapes, or provider-specific v7 behavior are relevant.

## Defaults

- Use `instructions`, not `system`, for top-level system instructions.
- Do not place system messages in `prompt` or `messages` unless the messages are trusted and the call explicitly uses `allowSystemInMessages: true`.
- Use stable names in examples: `customProvider`, `generateImage`, `transcribe`, `generateSpeech`, `prepareStep`, `activeTools`, `isStepCount`, `include`, and `telemetry`.
- Use `onStart`, `onStepStart`, `onEnd`, and `onStepEnd` for lifecycle callbacks.
- Use `onToolExecutionStart` and `onToolExecutionEnd` for tool execution callbacks.
- Use `result.stream`, not `result.fullStream`, for `streamText` event streams.
- Use stateless top-level stream helpers such as `toUIMessageStream`, `createUIMessageStreamResponse`, `toTextStream`, and `createTextStreamResponse`; avoid result-bound response helper methods in new code.
- Use `runtimeContext` for shared generation or agent state and `toolsContext` plus each tool's `contextSchema` for per-tool callback data.
- Treat top-level multi-step result properties as all-step aggregates. Use `finalStep` when the code needs final-step-only values.

## Review Gate

Flag v6-shaped code when it relies on:

- CommonJS `require()` imports for AI SDK packages.
- Deprecated experimental names where v7 has stable names.
- `system` prompt options in new code, or system messages mixed into `messages` without an explicit trust boundary.
- `prepareStep` overrides that assume returned `instructions` or `messages` apply to only one step.
- `onFinish` or `onStepFinish` callback names in new code.
- Usage fields such as `cachedInputTokens`, `reasoningTokens`, or Anthropic `cacheCreationInputTokens` instead of `usage.inputTokenDetails` / `usage.outputTokenDetails`.
- `experimental_telemetry`, per-call `isEnabled: true`, or a telemetry `tracer` passed on each model call instead of global telemetry registration.
- `onChunk` handlers that assume only content-like stream parts and do not guard part types.
- Request or response body reads without an explicit `include` opt-in.
- Tool callbacks that destructure `experimental_context` or use one shared object where v7 expects `runtimeContext` plus `toolsContext`.
- Tool or message content unions that do not handle canonical `file` parts or `reasoning-file`.
- Code that expects top-level `usage`, `content`, `toolCalls`, `files`, `sources`, or `warnings` to mean final-step-only values.

## Provider Notes

- OpenAI Responses defaults reasoning summaries to `detailed` when reasoning is enabled. Set `providerOptions.openai.reasoningSummary` to `null` to keep summaries disabled.
- Anthropic cache creation tokens are standard usage details now; use `usage.inputTokenDetails.cacheWriteTokens`.
- Google provider names dropped the `GenerativeAI` affix, such as `createGoogle` and `GoogleProvider`; the `google` entry point is unchanged.

## Source

The bundled reference was distilled from the AI SDK v7 migration documentation fetched with:

```sh
sitefetch https://ai-sdk.dev/docs/migration-guides/migration-guide-7-0 --limit 0
```
