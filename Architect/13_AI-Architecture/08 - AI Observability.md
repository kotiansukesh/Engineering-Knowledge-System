---
title: AI Observability
type: note
category: Architect/13_AI-Architecture
difficulty: Hard
tags: [architecture, ai, observability]
---

# AI Observability

Trace the complete request, not just the model call.

## Observe

- request
- model
- prompt/version
- retrieved context
- tool calls
- latency
- token usage
- cost
- errors
- evaluation result
- human intervention

Do not log sensitive prompts or retrieved data by default.
