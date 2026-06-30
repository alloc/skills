---
name: ai-sdk
description: Build, review, debug, or explain greenfield Vercel AI SDK v7 code, including Node/ESM setup, instructions prompts, streaming, tool context, telemetry, UI messages, multi-step results, MCP transport, Vue, and OpenAI/Anthropic/Google provider behavior.
---

# AI SDK v7

Use AI SDK v7 as the baseline. Design new code around the current APIs, call shapes, and result semantics.

## Project Baseline

- Run AI SDK on Node.js 22 or later. Prefer the current LTS Node version when the project permits it.
- Treat AI SDK packages as ESM-only. Use `import`, not CommonJS `require()`.
- Install provider packages explicitly, such as `@ai-sdk/openai`, `@ai-sdk/anthropic`, or `@ai-sdk/google`.
- Install `@ai-sdk/otel` only when OpenTelemetry span collection is needed.
- Keep framework package usage explicit, such as `@ai-sdk/react` for React UI helpers and `@ai-sdk/vue` for Vue composables.

## Prompting

- Put system-level behavior in the top-level `instructions` option.
- Keep `messages` and `prompt` focused on conversation/user content.
- Allow system messages inside `messages` only for trusted persisted histories by setting `allowSystemInMessages: true`; do not expose that path to user-editable messages.
- In multi-step flows, remember that `prepareStep` returned `instructions` and `messages` carry forward to later steps until replaced.
- Use `initialInstructions`, `initialMessages`, and `responseMessages` inside `prepareStep` when constructing per-step prompt state.

## Generation Defaults

- Use `generateText` and `streamText` for text generation.
- Use `generateObject` and `streamObject` for structured outputs.
- Use `output` for structured text outputs.
- Use `isStepCount` for tool-loop stop conditions.
- Use `include` for optional diagnostic payloads, such as request and response bodies.
- Use `reasoning` for provider-agnostic reasoning effort. Keep provider-specific reasoning settings only when they intentionally override the top-level option.

## Lifecycle And Streaming

- Use `onStart`, `onStepStart`, `onEnd`, and `onStepEnd` for generation lifecycle callbacks.
- Use `onEnd` for completed `embed`, `embedMany`, and `rerank` operations.
- Iterate `streamText` events through `result.stream`.
- Guard `onChunk` by `chunk.type`; it receives lifecycle, content, boundary, terminal, error, tool, reasoning, source, custom, and raw stream parts.
- Use stateless top-level stream helpers:
  - `toUIMessageStream`
  - `createUIMessageStreamResponse`
  - `pipeUIMessageStreamToResponse`
  - `toTextStream`
  - `createTextStreamResponse`
  - `pipeTextStreamToResponse`

## Tools

- Use `tool()` and `dynamicTool()` with explicit schemas.
- Put shared generation or agent data in `runtimeContext`.
- Put per-tool callback data in `toolsContext`, keyed by tool name.
- Add `contextSchema` to tools that need per-tool context; callback `context` is inferred from that schema.
- Provide `toolsContext` whenever any active tool declares contextual data.
- Use `onToolExecutionStart` and `onToolExecutionEnd` for tool execution callbacks.
- Put approval policy in `toolApproval` on `generateText`, `streamText`, or `ToolLoopAgent`, where request-specific policy can vary by call.

## Results

- Treat top-level multi-step result properties as all-step aggregates.
- Use `finalStep` when code needs final-step-only values.
- For `streamText`, await `result.finalStep` before reading final-step-only values.
- Read aggregate token usage from `usage`.
- Read final-step-only token usage from `finalStep.usage`.
- Read cache and reasoning usage from:
  - `usage.inputTokenDetails.cacheReadTokens`
  - `usage.inputTokenDetails.cacheWriteTokens`
  - `usage.outputTokenDetails.reasoningTokens`
- Use `result.responseMessages` for accumulated response messages across steps.
- Read each step's own response messages from `step.response.messages`.
- Request and response bodies are excluded by default. Opt in with `include: { requestBody: true, responseBody: true }` for `generateText`; for `streamText`, only `requestBody` applies.

## Messages And Content Parts

- Represent user-provided files with `file` parts.
- Represent inline tool result file content with `file-data`.
- Prefer canonical generated tool output file parts shaped as `{ type: "file", mediaType, data }`.
- Treat images as files with an image media type, such as `mediaType: "image"` or `mediaType: "image/png"`.
- Handle `reasoning-file` in exhaustive unions, renderers, serializers, and validators.
- Accept that `mediaType` may be a full IANA type or a top-level segment such as `image`, `audio`, `video`, or `text`.

## Telemetry

- Register telemetry once at application startup with `registerTelemetry(new OpenTelemetry(...))` from `@ai-sdk/otel`.
- After a telemetry integration is registered, AI SDK calls emit telemetry by default.
- Use per-call `telemetry` fields for call metadata such as function identifiers.
- Set `telemetry: { isEnabled: false }` to opt out for a specific call.
- Pass custom OpenTelemetry tracers to the `OpenTelemetry` constructor.
- Implement telemetry callbacks with `onEmbedEnd` and `onRerankEnd`.

## Provider Notes

- Use `customProvider` for provider composition.
- Use `generateImage`, `transcribe`, and `generateSpeech` for image, transcription, and speech generation.
- OpenAI Responses defaults `providerOptions.openai.reasoningSummary` to `"detailed"` when reasoning is enabled. Set it to `null` to disable summaries.
- Anthropic cache write/read details are available on `usage.inputTokenDetails`. Raw Anthropic-shaped usage remains under `finalStep.providerMetadata?.anthropic?.usage`.
- In `@ai-sdk/google`, use names such as `createGoogle` and `GoogleProvider`; the `google` entry point is unchanged.

## Framework And Transport Notes

- In Vue, use the `useChat` composable. Pass a getter or ref when chat initialization depends on reactive values such as route params or selected models.
- For MCP HTTP/SSE transport, redirects fail by default. Set `redirect: "follow"` only for trusted servers that require redirects.

## Review Gate

Reject greenfield code that:

- Uses CommonJS imports for AI SDK packages.
- Puts trusted system behavior in user-editable messages.
- Handles stream chunks without checking `chunk.type`.
- Reads request or response bodies without an explicit `include` opt-in.
- Treats top-level multi-step result properties as final-step-only values.
- Stores per-tool data in shared runtime state instead of typed `toolsContext`.
- Omits `reasoning-file` from exhaustive message/content handling.
- Uses provider-specific reasoning settings that unintentionally override the top-level `reasoning` option.
