---
title: Roadmap Overview
category: overview
tags: [architect, roadmap]
created: 2026-09-03
completed: false
---

# Roadmap Overview

## Intent
One-page map of the 24-week architect journey so every week connects to the capstone.

## Phases

| Weeks | Theme | Key deliverable |
|-------|-------|-----------------|
| 1–2 | Architecture Foundations | 4+1 views of monolith |
| 3–4 | Requirements + Qualities | Scenarios + fitness functions |
| 5–6 | Styles + Patterns | Style decision ADR |
| 7–8 | DDD + C4 | Bounded contexts |
| 9–10 | Data | Postgres/Redis scheme |
| 11–12 | Event-driven | Outbox + saga |
| 13–14 | APIs | Versioned API + gateway |
| 15–16 | Security | Threat model |
| 17–18 | Observability/SRE | SLOs + dashboards |
| 19–20 | Cloud/K8s | EKS deploy |
| 21–22 | Docs/Review | arc42 + 10 ADRs |
| 23–24 | Capstone | Reference architecture |

## When / NOT
- Use when planning the week — pick rows from [[Study Plan - Architect|Study Plan]].
- NOT a substitute for doing the labs in [[Tech Stack|Tech Stack]].

## Platform thread
Monolith → modular → microservices → event-driven. Same codebase evolves; every fork gets an ADR.

## Q&A
1. **Why 24 weeks?** Depth without burnout at 6–8h/week.
2. **What if I fall behind?** Dashboard flags overdue; compress, don't skip ADRs.
3. **Cert overlap?** iSAQB early, AWS late — see [[../README|Master MOC]] cert map.

## Pitfalls
- Tutorial-hopping; anchor everything to the one platform.
- Skipping writing (ADR/C4) — that IS the architect skill.

## Related
- [[Study Plan - Architect|Study Plan]], [[Dashboard|Dashboard]], [[../01_Architecture-Foundations/What-is-Architecture|What is Architecture]]
