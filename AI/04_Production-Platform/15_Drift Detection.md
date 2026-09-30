---
title: "Drift Detection"
category: "AI/04_Production-Platform"
tags: [drift, data-drift, concept-drift, monitoring]
created: "2026-09-30"
completed: false
difficulty: "Advanced"
reviewed: "2026-09-30"
sr-due: "2026-10-05"
type: "note"
---

# Drift Detection

## Intent
Distinguish data-distribution change from changes in model performance or the relationship between inputs and outcomes, then connect detection to a safe operational response.

## Drift Types
- **Data drift:** input distribution changes.
- **Prediction drift:** model output distribution changes.
- **Concept drift:** relationship between inputs and target changes.
- **Label drift:** target prevalence changes.

## Method Selection
| Situation | Useful approach | Caveat |
|---|---|---|
| Numeric distribution comparison | KS or related distribution test | sensitive to sample size |
| Categorical distribution comparison | PSI or frequency comparison | binning/reference choice matters |
| Multivariate change | embedding/statistical monitoring | harder to interpret |
| Streaming change | sequential/adaptive methods | tuning false alarms |

No single test is universally correct. Select the method from feature type, sample size, latency, and operational response.

## Decision Rule
A drift detector should have a defined baseline, sampling window, threshold, owner, and action. If nobody knows what happens after an alert, the detector is observability without operations.

## Failure Modes
1. Tiny statistical change becomes a major alert → combine statistical and practical significance.
2. Reference data becomes stale → version and refresh baselines deliberately.
3. Drift without quality impact triggers retraining → require outcome evidence where available.
4. Multiple correlated features create alert storms → group alerts and prioritize impact.
5. Detector itself changes without versioning → track detector configuration as an artifact.

## Evaluation
Measure false-alert rate, detection delay, detection power on replayed incidents, downstream quality impact, and retraining/rollback outcomes.

## Practice
- [ ] Build a reference distribution from historical traffic.
- [ ] Inject a known distribution shift.
- [ ] Compare two detectors on the same data.
- [ ] Define an operational threshold and response owner.
- [ ] Replay a drift incident without automatically retraining.

## Senior Interview Prompts
1. Why does statistical significance not imply business significance?
2. When can drift be harmless?
3. What makes concept drift harder than data drift?
4. Why should retraining not be the automatic response to every drift alert?
5. How would you evaluate a drift detector before production?

## Flashcards
#flashcard
**Q:** What is the difference between data drift and concept drift? :: **A:** Data drift changes the input distribution; concept drift changes the relationship between inputs and the target.
