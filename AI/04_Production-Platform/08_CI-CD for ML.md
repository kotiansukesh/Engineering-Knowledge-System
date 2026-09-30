---
title: "CI/CD for ML"
category: "AI/04_Production-Platform"
tags: [mlops, ci-cd, model-validation, deployment, rollback]
created: "2026-09-30"
completed: false
difficulty: "Advanced"
reviewed: "2026-09-30"
sr-due: "2026-10-10"
type: concept
---

# CI/CD for ML

## Intent
Treat model and data changes as deployable artifacts with automated quality, compatibility, security, and rollout checks.

## Pipeline
**Commit → unit tests → data/schema checks → model/eval tests → artifact build → security checks → deploy → canary → monitor → promote/rollback**

## What Changes from Conventional CI/CD?
Software tests remain necessary, but ML systems also require:
- data/schema validation
- model artifact integrity
- offline evaluation
- serving compatibility
- latency/cost checks
- rollout monitoring
- reproducibility and lineage

## Release Gate
A release should have explicit thresholds for correctness/quality, safety, latency, error rate, and cost where relevant. Avoid making every metric a hard gate; classify checks as block, warn, or observe.

## Rollout Strategies
| Strategy | Useful when | Main risk |
|---|---|---|
| Rolling | routine compatible changes | broad exposure during rollout |
| Canary | uncertain behavioral change | requires reliable comparison signals |
| Shadow | compare behavior without user impact | doubles inference cost |
| Blue/green | rapid environment switch | higher temporary capacity |

## Failure Modes
- Offline eval passes but production traffic differs.
- Canary sample is too small or biased.
- Rollback restores software but not an incompatible model/data artifact.
- Automated retraining creates noisy releases.
- Cost regression is invisible to CI.

## Practice
- [ ] Define release gates for one model service.
- [ ] Build a canary comparison.
- [ ] Simulate a quality regression and block promotion.
- [ ] Simulate an inference latency regression and roll back.
- [ ] Record model + code + data versions for one release.

## Senior Interview Prompts
1. What should block an ML deployment?
2. Why is shadow testing different from canary?
3. How do you roll back a model safely?
4. When should retraining be automated?
5. Which production signals should complete the release loop?
