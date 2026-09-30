---
title: "ML Data Quality"
category: "AI/04_Production-Platform"
tags: [data-quality, validation, schema, anomaly, drift]
created: "2026-09-30"
completed: false
difficulty: "Advanced"
reviewed: "2026-09-30"
sr-due: "2026-10-14"
type: concept
---

# ML Data Quality

## Intent
Detect data problems before they become model-quality, reliability, or business problems.

## Quality Dimensions
- schema/type validity
- completeness
- uniqueness
- range/domain validity
- freshness
- distribution changes
- referential integrity
- semantic/business rules

## Layered Checks
**Schema → row-level validation → aggregate/statistical checks → drift → downstream model-quality checks**

Not every anomaly should block a pipeline. Classify checks as hard failure, quarantine, warning, or observe.

## Statistical Detection
KS-test, PSI, and similar techniques can detect distribution changes, but statistical significance is not the same as business significance. Thresholds need a baseline, sample-size context, owner, and response action.

## Failure Modes
- Check is too strict → healthy data is blocked.
- Check is too weak → bad data reaches production.
- Drift alert has no owner/action.
- Small sample creates noisy alerts.
- Quality is measured without connecting it to downstream model behavior.

## Practice
- [ ] Define hard and soft quality checks.
- [ ] Inject nulls and schema changes.
- [ ] Simulate a distribution shift.
- [ ] Connect a data-quality alert to a model-quality investigation.
- [ ] Document the action associated with each threshold.

## Senior Interview Prompts
1. Which data checks should block a pipeline?
2. Why is drift not automatically a model failure?
3. How do you reduce alert fatigue?
4. How do you distinguish statistical from practical significance?
5. What evidence connects a data anomaly to model degradation?
