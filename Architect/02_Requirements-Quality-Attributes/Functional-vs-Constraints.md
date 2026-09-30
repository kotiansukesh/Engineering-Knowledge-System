---
title: Functional vs Constraints
category: Architect/02_Requirements-Quality-Attributes
tags:
- concept/quality-attributes
- concept/quality-scenarios
- concept/tactics
- constraints
- difficulty/medium
- requirements
created: 2026-09-03
completed: false
reviewed: '2026-09-05'
sr-due: '2026-09-12'
difficulty: Medium
excalidraw: ''
source: ''
type: concept
weeks: ''

---


## Problems
### System Design Problem: Functional vs Constraints

**Requirements:**
- Functional: Core capabilities for functional vs constraints
- Non-functional (SLOs): Latency < 100ms p99, Availability 99.9%, Horizontal scalability

**Constraints:**
- Scale: Handle 10x growth without redesign
- Consistency: Appropriate model for domain (strong/eventual)
- Latency budget: p99 < 100ms for read paths

**API / Interfaces:**
- Primary: REST/gRPC endpoints for core operations
- Internal: Service-to-service contracts
- Events: Domain events for async integration





Why it Matters

Separate what the system does (functions) from what limits how (constraints) so estimates and style choices rest on facts.

## Diagram

```mermaid
graph LR
 R[Requirements log] --> Fu[Functional: place order]
 R --> Qu["Quality: p99 < 300ms"]
 R --> Co[Constraint: EKS-only, PCI scope]
 Co --> P1[Options pruned instantly]
 Qu --> P2[Tactic chosen: cache/async]
 Fu --> P3[Behaviour to build]
 P1 --> ADR[Design + ADR]
 P2 --> ADR
 P3 --> ADR
```

## Code

```text
Why split: "Checkout with UPI" (functional) vs "PCI-DSS, deploy on EKS,
Java 21 only" (constraints) — second kills half the options instantly
```

## When to use / not

- **Use:** during requirements elicitation, before any style or platform choice, constraints prune the option space instantly, so separate them from functions early.
- **Use:** when a debate won't end, most "technical" arguments are really unstated constraints or qualities; naming the type ends them.
- **Use:** when sizing estimates and ADRs: functions drive build effort, constraints drive risk and rework.

**When NOT:** do not let preferences disguise themselves as constraints, "we've always used Postgres" is a preference; "all payment data stays in the PCI-scoped VPC" is a constraint, and treating the former as the latter burns optionality and trust. Do not bury qualities inside a vague "non-functional requirements" bucket, promote each to a named, measured scenario.





## Trade-offs
| Dimension | This Approach | Alternative | Trade-off Rationale | Decision Rule |
|-----------|---------------|-------------|---------------------|---------------|
| Complexity | [TBD] | [TBD] | [TBD] | [TBD] |
| Operational Burden | [TBD] | [TBD] | [TBD] | [TBD] |
| Latency | [TBD] | [TBD] | [TBD] | [TBD] |
| Consistency | [TBD] | [TBD] | [TBD] | [TBD] |
| Cost at Scale | [TBD] | [TBD] | [TBD] | [TBD] |

## Vs

| Type | Example | Source |
|------|---------|--------|
| Functional | Place order, refund | Product/users |
| Quality | p99 < 300ms | SLO/SLA |
| Constraint | EKS-only, no new DB | Org/policy |

## Pitfalls

- Treating preferences as constraints.
- Functions without qualities (untestable "fast").


## Pitfalls
1. Underestimating operational complexity (backups, monitoring, upgrades)
2. Ignoring failure modes (network partitions, disk failures, clock drift)
3. Not planning for 10x scale from day one
4. Skipping monitoring/alerting in MVP
5. Premature optimization before measuring
6. Dual-write without transactional outbox
7. Assuming global order in partitioned systems

## Interview q&a

**Q: What's the difference between a functional requirement, a quality attribute, and a constraint, and why does the split change your design?**
A: A functional requirement is behaviour the system must perform (place an order); a quality attribute is a measurable property of that behaviour under conditions (p99 checkout < 300 ms at 500 rps); a constraint is a fixed, non-negotiable boundary (EKS-only, PCI-DSS scope, Java 21). The split changes the design because constraints eliminate options immediately, qualities select tactics, and only functions get built, confusing them means either over-building or optimising the wrong axis.

**Q: "We need the checkout to be fast", what's missing?**
A: A scenario: fast for whom, under what load, measured where, with what threshold. Turn it into stimulus → environment → response → measure, "checkout POST from mobile clients at 500 rps in prod EKS returns p99 < 300 ms". If you can't attach a number and an environment, it's not a requirement yet, and "non-functional" is the word that let it stay vague.

**Q: How do you stop constraint creep, every stakeholder preference becoming "mandatory"?**
A: Test each claim against "what breaks if we don't" and "who imposed it and can they be challenged". A real constraint has an owner and a consequence; a preference has neither. Log both, but mark preferences as reversible decisions so an ADR can supersede them when the cost of the constraint exceeds the benefit.

**Q: Where do you record all three so they don't rot?**
A: One requirements log where every row links forward: functional → test case, quality → scenario → fitness function, constraint → ADR or compliance control. Traceability both directions is what an auditor and a new architect both need.


## Flashcards (Spaced Repetition)

#flashcard
**Q:** What is the core concept of Functional vs Constraints? :: **A:** [Key algorithm/architecture pattern] #flashcard

#flashcard
**Q:** When do you apply Functional vs Constraints? :: **A:** [Trigger scenarios and context] #flashcard

#flashcard
**Q:** What is the primary trade-off in Functional vs Constraints? :: **A:** [Main tension: e.g., consistency vs latency] #flashcard

#flashcard
**Q:** What breaks first at scale in Functional vs Constraints? :: **A:** [Primary bottleneck: e.g., coordination, hot keys, replication lag] #flashcard

#flashcard
**Q:** How do you handle failures in Functional vs Constraints? :: **A:** [Retry, circuit breaker, fallback, graceful degradation] #flashcard

#flashcard
**Q:** What are the key metrics to monitor for Functional vs Constraints? :: **A:** [RED: rate, errors, duration; USE: utilization, saturation, errors] #flashcard

#flashcard
**Q:** How does Functional vs Constraints scale to 10x? :: **A:** [Sharding, read replicas, async processing, caching layers] #flashcard

#flashcard
**Q:** What is the consistency model for Functional vs Constraints? :: **A:** [Strong/eventual/causal - justify with use case] #flashcard

#flashcard
**Q:** How do you test Functional vs Constraints? :: **A:** [Contract tests, chaos engineering, load tests, fault injection] #flashcard

#flashcard
**Q:** What is the operational cost of Functional vs Constraints? :: **A:** [Team expertise, tooling, on-call burden, migration risk] #flashcard

#flashcard
**Q:** When would you NOT use Functional vs Constraints? :: **A:** [Managed service covers need, simple CRUD, team lacks maturity] #flashcard

#flashcard
**Q:** What is the key design decision in Functional vs Constraints? :: **A:** [The irreversible choice that defines the architecture] #flashcard

#flashcard
**Q:** How do you migrate to Functional vs Constraints? :: **A:** [Strangler fig, dual-write, canary, feature flags] #flashcard

#flashcard
**Q:** What security considerations for Functional vs Constraints? :: **A:** [AuthZ, encryption, audit, secrets management] #flashcard

#flashcard
**Q:** How do you debug Functional vs Constraints in production? :: **A:** [Structured logging, correlation IDs, distributed tracing, SLO alerts] #flashcard


## Practice Tasks (Tasks Plugin)
- [ ] Explain the architecture from memory 📅 {{date:YYYY-MM-DD, +1}}
- [ ] Draw the system diagram without looking 📅 {{date:YYYY-MM-DD, +3}}
- [ ] Answer all Interview Q&A aloud 📅 {{date:YYYY-MM-DD, +7}}
- [ ] Review flashcards (Spaced Repetition) 📅 {{date:YYYY-MM-DD, +1}}

```tasks
not done
path includes Architect/02_Requirements-Quality-Attributes
sort by due
limit 10
```

## Related

- [[ISO-25010-Qualities|ISO 25010]], [[Quality-Scenarios|Quality Scenarios]]

# Functional vs Constraints

## When / not

- Use during elicitation, before picking styles.
- NOT to bury qualities inside "non-functional" vagueness, promote them to scenarios.

## Q&A

1. **"Non-functional" term?** Avoid, say quality attribute + scenario.
2. **Constraint or quality?** Fixed = constraint; measurable target = quality.
3. **Where record?** Requirements log → link each to scenario/ADR.
