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
3. Apply the v7 facts below when exact names, result shapes, or provider-specific behavior are relevant.

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

## Package Baseline

- AI SDK v7 requires Node.js 22 or later.
- AI SDK packages are ESM-only. Use `import`, not `require()`.
- OpenTelemetry moved out of `ai` and into `@ai-sdk/otel`.

## Stable API Names

Prefer the v7 names in new code:

| v6 or deprecated name | v7 name |
| --- | --- |
| `experimental_customProvider` | `customProvider` |
| `experimental_generateImage` | `generateImage` |
| `Experimental_GenerateImageResult` | `GenerateImageResult` |
| `experimental_transcribe` | `transcribe` |
| `Experimental_TranscriptionResult` | `TranscriptionResult` |
| `experimental_generateSpeech` | `generateSpeech` |
| `Experimental_SpeechResult` | `SpeechResult` |
| `experimental_output` | `output` |
| `stepCountIs` | `isStepCount` |
| `experimental_prepareStep` | `prepareStep` |
| `experimental_activeTools` | `activeTools` |
| `ToolCallOptions` | `ToolExecutionOptions` |
| `isToolOrDynamicToolUIPart` | `isToolUIPart` |
| `experimental_include` | `include` |
| `includeRawChunks` | `include.rawChunks` |
| `StreamTextResult.fullStream` | `StreamTextResult.stream` |

`CallSettings` was split. For wrapper/helper types that used it, use `LanguageModelCallOptions & Omit<RequestOptions, "timeout">`.

## Prompts And Step Preparation

- The top-level `system` option is now `instructions` for `generateText`, `streamText`, `generateObject`, `streamObject`, and `streamUI`.
- `instructions` also replaces `system` in `prepareStep` results, repair-tool-call inputs, lifecycle callbacks, and agent callbacks.
- If both `instructions` and `system` are present, `instructions` wins.
- System messages in `prompt` or `messages` are rejected by default. Prefer trusted server-side `instructions`. Use `allowSystemInMessages: true` only for trusted persisted messages.
- `prepareStep` returned `instructions` now carry forward to future steps until replaced.
- `prepareStep` returned `messages` now become the base for subsequent steps. To make one-step-only changes, rebuild from `initialMessages` and `responseMessages`.

## Lifecycle Events

Use the `End` naming consistently:

| Old or deprecated callback | v7 callback |
| --- | --- |
| `experimental_onStart` | `onStart` |
| `experimental_onStepStart` | `onStepStart` |
| `onFinish` | `onEnd` |
| `onStepFinish` | `onStepEnd` |
| `experimental_onFinish` for `embed`, `embedMany`, `rerank` | `onEnd` |
| telemetry `onRerankFinish` | `onRerankEnd` |
| telemetry `onEmbedFinish` | `onEmbedEnd` |

`onEnd` result payloads follow the new multi-step result semantics: aggregate top-level values and final-step-only values under `finalStep`.

## Usage And Result Shapes

- `usage.cachedInputTokens` moved to `usage.inputTokenDetails.cacheReadTokens`.
- `usage.reasoningTokens` moved to `usage.outputTokenDetails.reasoningTokens`.
- `generateText` and `streamText` top-level `usage` now includes all steps. `totalUsage` is deprecated. Use `finalStep.usage` for final-step-only usage.
- Top-level `content`, `toolCalls`, `staticToolCalls`, `dynamicToolCalls`, `toolResults`, `staticToolResults`, `dynamicToolResults`, `files`, `sources`, and `warnings` now aggregate all steps.
- `finalStep` holds final-step-only `reasoning`, `reasoningText`, `request`, `response`, and `providerMetadata`.
- For `streamText`, await `result.finalStep` before reading final-step-only values.
- Each `step.response.messages` contains only that step's response messages. Use `result.responseMessages` for accumulated response messages.

## Telemetry

- Register telemetry globally with `registerTelemetry(new OpenTelemetry(...))` from `@ai-sdk/otel`.
- Once a telemetry integration is registered, telemetry is enabled by default for AI SDK calls.
- Remove per-call `telemetry: { isEnabled: true }` unless other fields remain.
- Set `telemetry: { isEnabled: false }` to opt out for one call.
- Use `telemetry`, not `experimental_telemetry`, in new code.
- Pass custom OpenTelemetry tracers to the `OpenTelemetry` constructor, not as a per-call `tracer` property.

## Streaming

- `streamText` `onChunk` receives every `TextStreamPart`, including lifecycle and terminal parts such as `start`, `start-step`, `text-start`, `text-end`, `finish-step`, `finish`, `abort`, and `error`. Guard on `chunk.type`.
- `generateText` and `streamText` exclude request bodies from step results by default.
- `generateText` also excludes response bodies by default.
- Opt in with `include: { requestBody: true, responseBody: true }` for `generateText`; for `streamText`, only `requestBody` applies.
- Result-bound response helpers are deprecated. Prefer stateless top-level helpers:
  - `toUIMessageStream`
  - `createUIMessageStreamResponse`
  - `pipeUIMessageStreamToResponse`
  - `toTextStream`
  - `createTextStreamResponse`
  - `pipeTextStreamToResponse`

## Tools

- Tool execution callbacks are `onToolExecutionStart` and `onToolExecutionEnd`.
- Tool callback `experimental_context` is now `context`.
- Shared generation/agent data belongs in `runtimeContext`.
- Per-tool data belongs in `toolsContext`, keyed by tool name.
- A tool declares its context type with `contextSchema`; callback `context` is typed from that schema.
- If any tool declares `contextSchema`, `toolsContext` is required for the tools that need context.
- Top-level `context` usage in generation calls and `prepareStep` should be `runtimeContext`.
- `needsApproval` on `tool()` and `dynamicTool()` is deprecated. Put request-specific approval policy in `toolApproval` on `generateText`, `streamText`, or `ToolLoopAgent`.

## Messages And Content Parts

- Tool result content part `{ type: "media" }` was removed. Use `{ type: "file-data" }` for inline file content.
- New tool output should prefer the canonical `{ type: "file", mediaType, data }` shape instead of legacy `image-*` and `file-*` variants.
- The deprecated user-message `{ type: "image", image, mediaType? }` part should become `{ type: "file", data, mediaType: "image" }` or a specific image media type.
- Handle the `reasoning-file` part type in exhaustive unions, renderers, serializers, and validators.
- Prefer the top-level `reasoning` option for provider-agnostic reasoning effort. Remove overlapping provider-specific reasoning settings unless intentionally taking provider precedence.

## Package-Specific Changes

- MCP HTTP/SSE transport `redirect` now defaults to `"error"`. Set `redirect: "follow"` only for trusted servers that require redirects.
- `@ai-sdk/vue` deprecates the `Chat` class in favor of the reactive `useChat` composable.
- OpenAI Responses sets `providerOptions.openai.reasoningSummary` to `"detailed"` by default when reasoning is enabled. Set it to `null` to disable summaries.
- Anthropic `providerMetadata.anthropic.cacheCreationInputTokens` was removed. Use `usage.inputTokenDetails.cacheWriteTokens`; raw Anthropic usage remains under `finalStep.providerMetadata?.anthropic?.usage`.
- `@ai-sdk/google` removed the `GoogleGenerativeAI` affix from provider type/class/function names, e.g. `createGoogle` and `GoogleProvider`. The `google` entry point is unchanged.

## Source

This skill was distilled from the AI SDK v7 migration documentation fetched with:

```sh
sitefetch https://ai-sdk.dev/docs/migration-guides/migration-guide-7-0 --limit 0
```
