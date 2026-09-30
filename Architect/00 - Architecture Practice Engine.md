---
title: Architecture Practice Engine
type: framework
category: Architect
tags: [architecture, practice, mastery]
---

# Architecture Practice Engine

> Architecture skill is demonstrated by making, defending, breaking, and redesigning decisions.

## Progression

**Learn → Recognize → Guided → Constraint Injection → Blind → Failure Injection → Trade-off Defense → Review → Redesign → Interview → Mastered**

| Stage | Evidence |
|---|---|
| Learn | Explain the concept and the constraint it addresses |
| Recognize | Identify the right mechanism from symptoms |
| Guided | Design with the mechanism named |
| Constraint Injection | Adapt when scale/NFR/cost changes |
| Blind | Derive architecture from requirements only |
| Failure Injection | Explain degradation, detection and recovery |
| Trade-off Defense | Reject alternatives with explicit reasoning |
| Review | Critique another design |
| Redesign | Change architecture after a measured constraint |
| Interview | Complete timed end-to-end design |
| Mastered | Repeat successfully under materially different constraints |

## Core loop

~~~text
Problem
  ↓
Requirements
  ↓
Estimates
  ↓
NFRs / SLOs
  ↓
Simplest viable design
  ↓
Bottleneck + failure analysis
  ↓
Alternatives
  ↓
Decision / ADR
  ↓
Evidence
  ↓
Constraint changes
  ↓
Redesign
~~~

## Practice rule

Never count reading, copying a diagram, or repeating a guided solution as mastery evidence.

A mastery claim requires at least one **blind design**, one **failure injection**, one **trade-off defense**, and one **redesign**.

## Related

- [[00 - Architecture Decision Framework]]
- [[00 - Architecture Failure Log]]
- [[00 - Interview Mode]]
- [[00 - Architecture Mastery Dashboard]]
- [[00 - System Design Problem Bank]]
