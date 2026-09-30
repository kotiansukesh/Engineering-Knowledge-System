---
title: System Design Problem Bank
type: problem-bank
category: Architect
tags: [architecture, system-design, practice]
---

# System Design Problem Bank

Use existing system-design notes as source material, but practice them as problems rather than reading assignments.

## Problem metadata

~~~yaml
type: architecture-problem
difficulty: Medium
primary_domain:
traffic_profile:
consistency:
availability:
latency:
storage:
async: false
multi_region: false
failure_injection: false
mastery_stage: learn
last_attempt:
next_review:
~~~

## Problem modes

| Mode | Input | Expected output |
|---|---|---|
| Guided | Problem + named pattern | Architecture |
| Blind | Requirements only | Architecture + estimates |
| Failure | Architecture + injected incident | Degraded design + recovery |
| Redesign | Existing design + changed constraint | Revised architecture |
| Review | Someone else's design | Risks + evidence requests |
| Interview | Requirements + timer | Complete design |

## Existing problem families

- URL shortener
- Timeline/feed
- Location tracking
- Chat
- Rate limiter
- Notifications
- Media feed
- Video streaming
- File synchronization
- Web crawler
- Seat booking
- Geo reviews

## Problem-writing standard

Every new problem should include functional requirements, traffic and storage assumptions, at least three measurable NFRs, consistency requirements, one operational constraint, one failure injection, one redesign trigger, and one cost question.

## Practice task

- [ ] Pick one problem without opening its solution.
- [ ] Record assumptions and estimates.
- [ ] Design the simplest viable architecture.
- [ ] Inject one failure.
- [ ] Defend two trade-offs.
- [ ] Record one redesign trigger.
