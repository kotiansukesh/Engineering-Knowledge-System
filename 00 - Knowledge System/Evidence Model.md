---
title: "Evidence Model"
type: reference
category: "Knowledge System"
status: active
---

# Evidence Model

## Evidence hierarchy

1. **Implementation** — working code/configuration.
2. **Test** — repeatable correctness or behavior check.
3. **Measurement** — benchmark, evaluation, SLO or cost result with method.
4. **Failure experiment** — deliberate degradation and observed behavior.
5. **Architecture decision** — alternatives, constraints and consequences.
6. **Independent defense** — explain and defend without notes.
7. **Certification** — external validation.

Certification is useful, but it does not replace implementation evidence.

## Evidence record

Every significant project should capture:

- problem
- hypothesis
- environment/version
- workload or dataset
- implementation
- metric
- result
- failure
- decision
- trade-off
- next experiment

## Evidence quality rule

A number without a workload and measurement method is not a benchmark. A claim without a source or experiment is not durable evidence.
