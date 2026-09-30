---
title: Interview Mode
type: interview
category: Architect
tags:
  - interview
  - system-design
  - practice
---

# Interview Mode

> 45-minute architecture simulation. The goal is reasoning under uncertainty, not drawing the most components.

## Session

**Problem:**  
**Date:**  
**Target role:**  
**Time limit:** 45 minutes

### 0–5 min — Requirements

- [ ] Functional requirements
- [ ] Traffic / storage estimates
- [ ] Latency / availability targets
- [ ] Consistency requirements
- [ ] Security/compliance constraints
- [ ] Explicit assumptions

### 5–10 min — API and data model

- [ ] Critical APIs
- [ ] Core entities
- [ ] Ownership
- [ ] Idempotency strategy

### 10–20 min — High-level design

- [ ] Compute
- [ ] Storage
- [ ] Cache
- [ ] Messaging
- [ ] External dependencies
- [ ] Trust boundaries

### 20–30 min — Deep dive

Choose the highest-risk bottleneck:

- [ ] Scale
- [ ] Consistency
- [ ] Hot partition
- [ ] Queue lag
- [ ] Failure recovery
- [ ] Data model
- [ ] Multi-region

### 30–38 min — Failure and operations

- [ ] Timeout
- [ ] Retry
- [ ] Idempotency
- [ ] Circuit breaker / bulkhead
- [ ] Degraded mode
- [ ] Observability
- [ ] Backup / recovery

### 38–43 min — Trade-offs

- [ ] Simplest alternative
- [ ] Scale-oriented alternative
- [ ] Why chosen
- [ ] What was rejected
- [ ] What would trigger redesign

### 43–45 min — Self-review

| Dimension | Score /5 |
|---|---:|
| Requirements | |
| Estimation | |
| API/data modeling | |
| Architecture | |
| Failure reasoning | |
| Trade-offs | |
| Communication | |

**Biggest gap:**  
**Next review:**  
