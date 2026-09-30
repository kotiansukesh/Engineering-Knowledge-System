---
title: Architect Study Plan
type: plan
category: Architect/99_Revision
tags: [study-plan, architecture, system-design, enterprise, ai]
created: 2026-09-30
---

# Architect Study Plan

## Progression

**Learn → Recognize → Guided → Constraint Injection → Blind → Failure Injection → Trade-off Defense → Review → Redesign → Interview → Mastered**

## 18-week core

| Phase | Weeks | Focus | Evidence |
|---|---:|---|---|
| Foundations | 1–2 | architecture principles, quality attributes | explain decisions from constraints |
| Requirements | 3 | NFRs and estimation | measurable scenarios |
| Styles | 4–5 | monolith, services, event-driven | justify shape |
| Building blocks | 6–7 | resilience, caching, integration | failure-first design |
| DDD | 8–9 | boundaries, aggregates, events | ownership + consistency |
| Data | 10–11 | SQL/NoSQL, CQRS, event sourcing | access-pattern decisions |
| Integration | 12–13 | APIs, messaging, idempotency | delivery semantics |
| Operations | 14–15 | observability, security, deployment | production readiness |
| System design | 16–18 | blind, failure, redesign, interview | independent end-to-end design |

## Extension tracks

### Enterprise Architecture

After the core, study:

- capability mapping
- application portfolio
- architecture principles
- reference architecture
- technology radar
- build vs buy
- governance
- target-state and transition architecture

See [[12_Enterprise-Architecture/README]].

### AI Architecture

Then apply the same decision framework to:

- model gateways
- RAG
- agents
- tools
- memory
- evaluation
- observability
- security and guardrails
- AI cost
- enterprise AI platforms

See [[13_AI-Architecture/README]].

## Weekly practice rhythm

| Session | Activity |
|---|---|
| Day 1 | Concept + recognition |
| Day 2 | Guided design |
| Day 3 | Trade-off simulator |
| Day 4 | Blind design |
| Day 5 | Failure injection |
| Weekend | Architecture review + redesign + interview |

## Promotion gate

Do not advance a topic until you can:

- [ ] clarify requirements;
- [ ] estimate scale;
- [ ] define measurable NFRs;
- [ ] choose the simplest viable architecture;
- [ ] explain data ownership and consistency;
- [ ] identify the first bottleneck;
- [ ] explain one degraded mode;
- [ ] defend two alternatives;
- [ ] estimate major cost drivers;
- [ ] state operational and security concerns;
- [ ] define evidence and a redesign trigger.

## Mastery evidence

A topic becomes **Mastered** only after:

- one blind design;
- one failure injection;
- one trade-off defense;
- one architecture review;
- one redesign after a changed constraint;
- one timed interview or production-style design.

## Weekly task

- [ ] One blind system design
- [ ] One failure injection
- [ ] One redesign exercise
- [ ] One architecture review
- [ ] One ADR
- [ ] Update the failure log
- [ ] Update mastery evidence
