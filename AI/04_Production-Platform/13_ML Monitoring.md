---
title: "ML Monitoring"
category: "AI/04_Production-Platform"
tags: [monitoring, drift, performance, mlops]
created: "2026-09-30"
completed: false
difficulty: "Advanced"
reviewed: "2026-09-30"
sr-due: "2026-10-04"
type: concept
---

# ML Monitoring

## Intent
Detect changes in inputs, model behavior, service health, and business outcomes early enough to trigger investigation or remediation.

## Monitoring Layers
| Layer | Examples | Typical action |
|---|---|---|
| Service | latency, errors, saturation | scale/fail over |
| Data | missingness, schema, distribution | investigate pipeline |
| Model output | score distribution, refusal rate | investigate model behavior |
| Quality | precision/recall, groundedness, task success | evaluate/retrain/change system |
| Business | conversion, resolution, escalation | validate real-world impact |

## Decision Rule
Do not treat drift as synonymous with model failure. A distribution change is a signal; connect it to quality or business impact before automated retraining or rollback.

## Architecture
~~~~mermaid
flowchart LR
P[Production traffic] --> M[Metrics + traces]
P --> S[Sampled quality evaluation]
M --> A[Alerts]
S --> A
A --> I[Investigation] --> R[Remediation]
~~~~

## Failure Modes
1. Alert on every distribution change → alert fatigue.
2. Monitor only infrastructure → silent quality degradation.
3. No labels available → quality cannot be measured directly; use proxy evaluation.
4. Threshold without seasonality → false alerts.
5. Automatic retraining on noisy signal → model churn and regression.

## Evaluation
Define thresholds from historical baselines and business impact. Track alert precision, time-to-detect, time-to-recover, false-alert rate, service SLOs, and quality regression rate.

## Practice
- [ ] Instrument request latency and error rate.
- [ ] Add an input-distribution monitor.
- [ ] Add a sampled quality evaluation path.
- [ ] Create one alert that requires human investigation before remediation.
- [ ] Replay a known incident and measure detection time.

## Senior Interview Prompts
1. What is the difference between data drift and model degradation?
2. What do you monitor when labels arrive weeks later?
3. Which metrics belong on the service dashboard versus the quality dashboard?
4. Why is automatic retraining dangerous?
5. How do you prevent alert fatigue?

## Flashcards
#flashcard
**Q:** Does drift prove model failure? :: **A:** No. Drift is evidence that the input distribution changed; its impact on model quality must be measured.

#flashcard
**Q:** What are the major ML monitoring layers? :: **A:** Service health, data, model behavior, quality, and business outcomes.
