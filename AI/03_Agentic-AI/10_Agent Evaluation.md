---
title: "Agent Evaluation"
category: "AI/03_Agentic-AI"
tags: [ai, agents, evaluation, reliability]
created: "2026-09-30"
completed: false
difficulty: "Advanced"
reviewed: "2026-09-30"
sr-due: "2026-10-05"
type: concept
---

# Agent Evaluation

## Intent
Measure whether an agent completes its intended task safely, reliably, and within latency and cost constraints.

## Evaluation Layers
| Layer | Metric examples | Failure caught |
|---|---|---|
| Final answer | correctness, groundedness | bad output |
| Tool selection | selection accuracy | wrong capability |
| Arguments | schema/semantic validity | bad parameters |
| Trajectory | transition/step correctness | unnecessary or unsafe actions |
| Outcome | task success | business failure |
| Operations | p95 latency, cost, errors | production viability |
| Safety | policy violations, unauthorized actions | unacceptable behavior |

## Dataset
Version representative success cases, ambiguous requests, known failures, adversarial cases, tool failures, permission boundaries, long-context cases, and production regressions. Keep a held-out set for tuning.

## Evaluation Loop
~~~~mermaid
flowchart LR
D[Versioned eval set] --> R[Agent run] --> T[Trace] --> M[Metrics] --> G[Regression gate]
G -->|pass| P[Release]
G -->|fail| F[Failure analysis] --> X[Change] --> R
~~~~

## Decision Rule
Choose metrics from the system's failure modes, not from a generic benchmark list. A transactional agent needs strong controls for authorization and duplicate side effects even if language quality is high.

## Trade-offs
| Method | Benefit | Limitation |
|---|---|---|
| Reference answers | Reproducible | Expensive to author |
| LLM judge | Scalable semantic comparison | Bias/calibration drift |
| Human review | Nuanced business quality | Slow/expensive |
| Offline replay | Repeatable regression gate | Misses live distribution shifts |
| Online monitoring | Real traffic evidence | Slower feedback/privacy constraints |

## Failure Analysis
Classify the first meaningful failure as **retrieval → reasoning → tool selection → argument → execution → policy → state → final response**. Preserve the trace and turn important incidents into regression cases.

## Release Gate
Define application-specific thresholds for critical safety regressions, task success, tool validity, p95 latency, and cost per successful task. There is no universal good-agent score.

## Practice
- [ ] Build a 30-case evaluation set.
- [ ] Add adversarial and tool-failure cases.
- [ ] Capture full traces.
- [ ] Compute task success, tool accuracy, latency, and cost.
- [ ] Introduce a regression and verify the gate blocks release.

## Senior Interview Prompts
1. Why is final-answer accuracy insufficient?
2. How do you evaluate irreversible actions?
3. How do you calibrate an LLM judge?
4. What belongs offline versus online?
5. How do incidents become regression tests?

## Flashcards
#flashcard
**Q:** What is the unit of evaluation for an agent? :: **A:** The task plus trajectory and side effects, not only the final text.

#flashcard
**Q:** How should evaluation thresholds be chosen? :: **A:** From business, safety, latency, and cost requirements of the application.
