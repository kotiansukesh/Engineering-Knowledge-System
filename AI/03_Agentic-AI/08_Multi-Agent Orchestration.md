---
title: "Multi-Agent Orchestration"
category: "AI/03_Agentic-AI"
tags: [ai, agents, orchestration, multi-agent]
created: "2026-09-30"
completed: false
difficulty: "Advanced"
reviewed: "2026-09-30"
sr-due: "2026-10-04"
type: concept
---

# Multi-Agent Orchestration

## Intent
Understand when multiple specialized agents are justified and how to make state, authority, termination, retries, and failures explicit.

## Core Model
Supervisor, pipeline, parallel specialists, and decentralized collaboration are different control-flow choices. Treat the system as distributed software with probabilistic components.

## Decision Rule
Start with **deterministic code → workflow → single agent → multi-agent**. Split into agents only when specialization, isolation, parallelism, or independent context materially improves measured outcomes.

## Architecture
~~~~mermaid
flowchart LR
U[Goal] --> S[Supervisor / Workflow]
S --> A[Research]
S --> B[Analysis]
S --> C[Action]
A --> R[(Evidence)]
B --> R
C --> P[External system]
P --> S
~~~~

## Real Trade-offs
| Decision | Simpler option | Multi-agent option | Evidence needed |
|---|---|---|---|
| Specialization | One agent + tools | Specialist agents | Different context/tools measurably improve success |
| Parallelism | Sequential workflow | Parallel agents | Independent work dominates latency |
| Context | Shared context | Per-agent context | Size or security boundaries justify isolation |
| Coordination | Function calls | State graph/messages | Dynamic delegation is actually required |

## State Contract
Every agent should have an input schema, output schema, allowed tools, authority, timeout, retry policy, termination condition, and observable events. Prefer structured state over large natural-language transcripts.

## Failure Modes
1. Coordination loop → step/iteration budget.
2. Conflicting side effects → one owner per mutation.
3. State corruption → versioned state + validation.
4. Cascading retries → retry budgets and failure propagation.
5. Agent disagreement → explicit escalation/tie-breaker.
6. Cost explosion → per-task token/call budgets.
7. Poor reproducibility → trace every transition and tool call.

## Evaluation
Compare against a single-agent/workflow baseline using task success, unnecessary calls, latency, cost, recovery rate, and unsafe actions. The baseline is essential because complexity has to earn its place.

## Practice
- [ ] Implement the single-agent baseline.
- [ ] Split only one justified responsibility into a second agent.
- [ ] Add typed shared state and termination limits.
- [ ] Inject timeout and contradictory-result failures.
- [ ] Compare success, latency, cost, and recovery against baseline.

## Senior Interview Prompts
1. What does a second agent solve that a tool or workflow cannot?
2. Who owns shared-state mutations?
3. How do you prevent duplicate side effects?
4. How do you cap runaway coordination?
5. What evidence would make you collapse the design back into a workflow?

## Flashcards
#flashcard
**Q:** What is the default before introducing multiple agents? :: **A:** Deterministic logic or a workflow; add autonomy only when requirements and evaluation justify it.

#flashcard
**Q:** What must every agent contract specify? :: **A:** Input/output schema, tools, authority, timeout, retry policy, termination condition, and observable events.
