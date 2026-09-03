---
title: Fitness Functions
category: architect
tags: [quality, fitness, testing]
created: 2026-09-03
completed: false
---

# Fitness Functions

## Intent
Automate architectural guardrails (coupling, latency, security) so drift fails the build, not a quarterly review.

## When / NOT
- Use for every principle and top scenario.
- NOT for style nits — fitness = protects a quality or constraint.

## Example (concept-level — why, not line-by-line)
```java
// Why ArchUnit: modular monolith boundary "order may not depend on web"
// Fails PR on violation → principle enforced in CI, not wiki
// @ArchTest: noClasses().that().resideIn("..order..").should().dependOn("..web..")
```

```text
Why Gatling budget: scenario "p99 < 300ms" → CI gate on staging deploy
Why dependency check: OWASP scan → security fitness for PCI path
```

## Pros / Cons
- Pros: continuous governance; fast feedback.
- Cons: brittle/flaky gates; maintenance cost.

## Vs
| Type | Guards | Tool |
|------|--------|------|
| Structural | Coupling/cycles | ArchUnit |
| Behavioral | Latency/throughput | Gatling/k6 |
| Security | Vulns/secrets | OWASP, gitleaks |

## Q&A
1. **How many to start?** 3: one ArchUnit + one perf + one security.
2. **Where run?** PR + nightly (full load); block merge only on fast ones.
3. **Who owns?** Architect defines, team maintains — review quarterly.

## Pitfalls
- Flaky perf gates blocking all merges; quarantine + trend first.
- Fitness without linked scenario (untraceable).

## Related
- [[Quality-Scenarios|Quality Scenarios]], [[../01_Architecture-Foundations/Architecture-Principles|Principles]], [[../00_Overview/Tech Stack|Tech Stack]]
