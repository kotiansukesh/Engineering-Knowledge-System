---
title: Architecture Failure Log
type: log
category: Architect
tags:
  - architecture
  - mistakes
  - review
---

# Architecture Failure Log

> Record reasoning failures, not just missing facts.

## Failure taxonomy

### Requirements
- missed requirement
- unstated assumption
- wrong scale estimate
- wrong SLO

### Architecture
- premature distribution
- wrong boundary
- inappropriate storage
- synchronous where async was needed
- missing bottleneck
- over-engineering

### Reliability
- retry amplification
- missing idempotency
- no degraded mode
- single point of failure
- weak recovery model

### Data
- wrong consistency model
- hot partition
- bad ownership
- missing retention/lifecycle

### Operations
- missing observability
- unrealistic deployment model
- operational burden ignored
- security boundary missing

## Review rule

- Same failure twice → add a checklist item to the relevant guide.
- Three times → add a concrete counterexample.
- Repeated component overuse → add a "When NOT to Use" rule.
- Repeated trade-off omission → add it to 00 - Architecture Decision Framework.

## Session fields

~~~yaml
type: architecture-review
problem:
failure_category:
severity:
review_date:
~~~
