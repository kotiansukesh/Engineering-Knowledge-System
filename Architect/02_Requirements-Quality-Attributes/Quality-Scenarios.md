---
title: Quality Scenarios
category: architect
tags: [quality, scenarios]
created: 2026-09-03
completed: false
---

# Quality Scenarios

## Intent
Make qualities testable: stimulus → environment → response + measure (e.g. "p99 checkout < 300ms at 500 rps").

## When / NOT
- Use before design; each top quality gets ≥1 scenario.
- NOT prose adjectives — if no number, it's not a scenario.

## Example
```text
Why six-part form: Source "1000 rps flash sale" → Stimulus "checkout POST" →
Artifact "order API" → Env "prod EKS" → Response "served" → Measure "p99 < 300ms"
```

## Pros / Cons
- Pros: drives tactics + load tests; ends debates.
- Cons: false precision if measures are guesses — mark assumptions.

## Vs
| Bad | Good (scenario) |
|-----|-----------------|
| "Fast" | p99 < 300ms @ 500 rps |
| "Highly available" | 99.9% monthly, RTO 15m |

## Q&A
1. **How many?** 5–8 total; 1–2 per top quality.
2. **Format?** Stimulus–source–artifact–environment–response–measure.
3. **Link to code?** Each scenario → Gatling/k6 or ArchUnit test.

## Pitfalls
- No environment (prod vs staging numbers differ 10x).
- Unowned scenarios nobody validates.

## Related
- [[Functional-vs-Constraints|Functional vs Constraints]], [[Fitness-Functions|Fitness Functions]]
