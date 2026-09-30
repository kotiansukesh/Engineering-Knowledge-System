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
## Security architecture

Use defense in depth:

**identity → authorization → isolation → input controls → model policy → tool controls → output validation → audit**

The model is never the final authorization authority.

## Threat-to-control mapping

For each important threat, identify the preventive control, detection signal, response and residual risk.

## Failure modes

Test direct and indirect prompt injection, unauthorized tool use, tenant isolation failure, data exfiltration, unsafe output propagation and privilege escalation.

## Evidence

Maintain a threat model, one adversarial test set and at least one demonstrated blocked attack path. Record residual risk rather than claiming complete prevention.
