---
title: AI Security and Guardrails
type: note
category: Architect/13_AI-Architecture
difficulty: Hard
tags: [architecture, ai, security]
---

# AI Security and Guardrails

Treat model output as untrusted.

## Threats

- prompt injection
- data exfiltration
- excessive agency
- insecure tool use
- indirect prompt injection
- tenant data leakage
- unsafe output propagation

## Controls

- least-privilege tools
- authorization outside the model
- input/output validation
- isolation
- approval gates
- audit
- evaluation
- rate limits
