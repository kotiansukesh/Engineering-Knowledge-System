---
title: Architecture Principles
category: architect
tags: [architecture, principles]
created: 2026-09-03
completed: false
---

# Architecture Principles

## Intent
Turn values into testable guardrails (e.g. "API-first, modular monolith first") that prune options before design.

## When / NOT
- Use to settle repeated debates and onboard quickly.
- NOT slogans — every principle needs rationale + implication + test.

## Example
```text
Why principle format: "Modular monolith first — Rationale: deploy simplicity;
Implication: ArchUnit boundaries; Test: mvn test passes boundary rules"
```

## Pros / Cons
- Pros: faster decisions; consistent tradeoffs.
- Cons: rigid if never revisited; ignored if too many (>8).

## Vs
| Principle | Counters | Decide by |
|-----------|----------|-----------|
| Modularity first | Microservices-by-default | Deploy/ops cost |
| API-first | UI-driven schema | Consumer count |
| Boring tech | Resume-driven | Team skill + SLO risk |

## Q&A
1. **How many?** 5–8, each with a fitness check.
2. **Where live?** Vault + repo (ARCHITECTURE.md) + ADR template reference.
3. **TOGAF link?** Principles catalog in Preliminary/ADM — same shape.

## Pitfalls
- Untestable ("be scalable") — rewrite as scenario.
- Principles nobody can veto with.

## Related
- [[What-is-Architecture|What is Architecture]], [[../02_Requirements-Quality-Attributes/Fitness-Functions|Fitness Functions]]
