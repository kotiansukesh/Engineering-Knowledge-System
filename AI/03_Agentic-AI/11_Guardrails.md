---
title: "Guardrails"
category: "AI/03_Agentic-AI"
tags: [ai, agents, security, guardrails, safety]
created: "2026-09-30"
completed: false
difficulty: "Advanced"
reviewed: "2026-09-30"
sr-due: "2026-10-06"
type: concept
---

# Guardrails

## Intent
Design layered controls for what an AI system may receive, produce, and execute. Guardrails reduce risk; they do not make an untrusted model inherently safe.

## Control Model
~~~~mermaid
flowchart LR
I[Input] --> P[Identity + policy] --> C[Context] --> M[Model] --> V[Output validation] --> A[Tool authorization] --> E[Execution] --> O[Audit]
~~~~

| Threat | Primary control |
|---|---|
| Prompt injection | isolate untrusted content; explicit tool policy; validation |
| Unauthorized action | identity + server-side authorization |
| PII leakage | classification/redaction + access control |
| Unsafe output | policy validation + escalation |
| Excessive autonomy | scoped tools + budgets + approval |
| Tool compromise | least privilege + schema validation + isolation |

## Decision Rule
Hard security and authorization requirements should be enforced deterministically. A prompt saying 'never transfer money without approval' is not an enforcement mechanism; the payment service must verify approval independently.

## Trade-offs
| Control | Stronger option | Cost/impact | Use when |
|---|---|---|---|
| Tool permissions | Per-action authorization | More implementation | Sensitive/side-effecting tools |
| Human approval | Mandatory selected actions | Added latency | Irreversible/high-impact actions |
| Output classifier | Separate policy model | Latency + false positives | Content risk justifies it |
| Sandboxing | Isolated execution | Infrastructure complexity | Untrusted code/tools |

## Failure Modes
1. Model bypasses a prompt rule → enforce outside the model.
2. Retrieved content contains instructions → treat it as untrusted data.
3. False-positive blocking → measure legitimate-task rejection and add escalation.
4. Guardrail outage → define fail-open/closed per risk class.
5. Excessive tool privilege → minimum-scope credentials.
6. Missing audit trail → record policy decisions, approvals, tool calls, and outcomes.

## Evaluation
Track attack success, unauthorized actions, sensitive-data leakage, legitimate-task rejection, escalation rate, false positives/negatives, policy latency, and availability.

## Practice
- [ ] Separate read-only and write permissions.
- [ ] Inject instructions into retrieved content and verify policy cannot change.
- [ ] Add approval for an irreversible action.
- [ ] Simulate guardrail outage and choose safe behavior.
- [ ] Review audit traces for blocked and allowed actions.

## Senior Interview Prompts
1. Which controls must be deterministic?
2. Where should authorization happen?
3. How do you defend against prompt injection in retrieved content?
4. When should the system fail closed?
5. How do you detect overly restrictive guardrails?

## Flashcards
#flashcard
**Q:** What is the key guardrail principle? :: **A:** Use the model for reasoning, but enforce security, authorization, and irreversible-action policy outside the model.
