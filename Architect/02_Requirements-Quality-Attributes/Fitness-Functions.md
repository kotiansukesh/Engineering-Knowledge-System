---
title: Fitness Functions
category: Architect/02_Requirements-Quality-Attributes
tags:
- concept/quality-attributes
- concept/quality-scenarios
- concept/tactics
- difficulty/medium
- fitness
- quality
- testing
created: 2026-09-03
completed: false
reviewed: '2026-09-27'
sr-due: '2026-10-04'
difficulty: Medium
excalidraw: ''
source: ''
type: concept
weeks: ''

---


## Problems
### System Design Problem: Fitness Functions

**Requirements:**
- Functional: Core capabilities for fitness functions
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

Automate architectural guardrails (coupling, latency, security) so drift fails the build, not a quarterly review.

## Diagram

```mermaid
graph LR
 S["Quality scenario: p99 < 300ms"] --> F[Fitness function: ArchUnit / k6 / OWASP]
 A[Architecture principle] --> F
 F --> G{CI gate}
 G -->|pass| M[Merge]
 G -->|fail| B[Build red: drift caught now, not in review]
```

## Code

```java
// Why ArchUnit: modular monolith boundary "order may not depend on web"
// Fails PR on violation → principle enforced in CI, not wiki
// @ArchTest: noClasses().that().resideIn("..order..").should().dependOn("..web..")
```
```textWhy
 Gatling budget: scenario "p99 < 300ms" → CI gate on staging deploy
Why dependency check: OWASP scan → security fitness for PCI path
```
## When to use / not

- **Use:** for every architecture principle and every top-3 quality scenario, if it matters, something automated should be protecting it.
- **Use:** as the definition of "done" for governance: a principle without a fitness function is an opinion, a scenario without a test is an aspiration.
- **Use:** onboarding and review prep, the fitness suite is the fastest way for a new architect or reviewer to learn what the system actually guarantees.

**When NOT:** do not gate merges on style nits or flaky load runs, a gate that fires randomly gets quarantine-merged into irrelevance, which is worse than having no gate because it also destroys trust in the real ones. Fitness functions protect a quality or a constraint; everything else is a linter.





## Trade-offs
| Dimension | This Approach | Alternative | Trade-off Rationale | Decision Rule |
|-----------|---------------|-------------|---------------------|---------------|
| Complexity | Not specified | Not specified | Not specified | Not specified |
| Operational Burden | Not specified | Not specified | Not specified | Not specified |
| Latency | Not specified | Not specified | Not specified | Not specified |
| Consistency | Not specified | Not specified | Not specified | Not specified |
| Cost at Scale | Not specified | Not specified | Not specified | Not specified |

## Vs

| Type | Guards | Tool |
|------|--------|------|
| Structural | Coupling/cycles | ArchUnit |
| Behavioral | Latency/throughput | Gatling/k6 |
| Security | Vulns/secrets | OWASP, gitleaks |

## Pitfalls

- Flaky perf gates blocking all merges; quarantine + trend first.
- Fitness without linked scenario (untraceable).


## Pitfalls
1. Underestimating operational complexity (backups, monitoring, upgrades)
2. Ignoring failure modes (network partitions, disk failures, clock drift)
3. Not planning for 10x scale from day one
4. Skipping monitoring/alerting in MVP
5. Premature optimization before measuring
6. Dual-write without transactional outbox
7. Assuming global order in partitioned systems

## Interview q&a

**Q: Your CTO asks you to "make the architecture self-enforcing". What do you actually build?**
A: Three gates, one per failure mode: structural, ArchUnit/Spring Modulith tests asserting module boundaries and dependency direction (catches coupling before it becomes a distributed monolith); behavioural, a k6/Gatling run on staging asserting the top scenarios, e.g. p99 checkout < 300 ms at 500 rps; security/supply chain, OWASP dependency-check, gitleaks, and image CVE scans on the PCI path. Each one traces to a scenario and a principle, runs in PR for fast feedback plus nightly for full load, and only the fast, stable ones block merge.

**Q: A performance fitness test is flaky and now blocks every other PR. What do you do?**
A: Never let noise wear the authority of a gate. Quarantine it from the merge path, keep it reporting as a trend, and fix the cause, shared staging environment variance, cold-start jitter, or a threshold set without a baseline (measure first, then set the budget). Restore it to blocking only when it's stable; meanwhile the nightly full-load run keeps the real signal.

**Q: How many fitness functions should a team start with?**
A: Three: one ArchUnit boundary test, one performance scenario, one security scan. That's enough to prove the loop (principle → test → CI gate) without the team spending a quarter building test infrastructure. Add a gate only when a new quality attribute is named in a scenario.

**Q: Who owns fitness functions, the architect or the team?**
A: The architect defines and the team maintains, reviewed quarterly. If the team can't maintain it, the gate is too brittle or the principle behind it is dead, either way it's a finding, not a deadline.


## Flashcards (Spaced Repetition)

#flashcard
**Q:** What is the core concept of Fitness Functions? :: **A:** [Key algorithm/architecture pattern] #flashcard

#flashcard
**Q:** When do you apply Fitness Functions? :: **A:** [Trigger scenarios and context] #flashcard

#flashcard
**Q:** What is the primary trade-off in Fitness Functions? :: **A:** [Main tension: e.g., consistency vs latency] #flashcard

#flashcard
**Q:** What breaks first at scale in Fitness Functions? :: **A:** [Primary bottleneck: e.g., coordination, hot keys, replication lag] #flashcard

#flashcard
**Q:** How do you handle failures in Fitness Functions? :: **A:** [Retry, circuit breaker, fallback, graceful degradation] #flashcard

#flashcard
**Q:** What are the key metrics to monitor for Fitness Functions? :: **A:** [RED: rate, errors, duration; USE: utilization, saturation, errors] #flashcard

#flashcard
**Q:** How does Fitness Functions scale to 10x? :: **A:** [Sharding, read replicas, async processing, caching layers] #flashcard

#flashcard
**Q:** What is the consistency model for Fitness Functions? :: **A:** [Strong/eventual/causal - justify with use case] #flashcard

#flashcard
**Q:** How do you test Fitness Functions? :: **A:** [Contract tests, chaos engineering, load tests, fault injection] #flashcard

#flashcard
**Q:** What is the operational cost of Fitness Functions? :: **A:** [Team expertise, tooling, on-call burden, migration risk] #flashcard

#flashcard
**Q:** When would you NOT use Fitness Functions? :: **A:** [Managed service covers need, simple CRUD, team lacks maturity] #flashcard

#flashcard
**Q:** What is the key design decision in Fitness Functions? :: **A:** [The irreversible choice that defines the architecture] #flashcard

#flashcard
**Q:** How do you migrate to Fitness Functions? :: **A:** [Strangler fig, dual-write, canary, feature flags] #flashcard

#flashcard
**Q:** What security considerations for Fitness Functions? :: **A:** [AuthZ, encryption, audit, secrets management] #flashcard

#flashcard
**Q:** How do you debug Fitness Functions in production? :: **A:** [Structured logging, correlation IDs, distributed tracing, SLO alerts] #flashcard


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

- Quality Scenarios, [[Architect/02_Requirements-Quality-Attributes/../01_Architecture-Foundations/Architecture-Principles|Principles]], Tech Stack

# Fitness Functions

## When / not

- Use for every principle and top scenario.
- NOT for style nits, fitness = protects a quality or constraint.

## Q&A

1. **How many to start?** 3: one ArchUnit + one perf + one security.
2. **Where run?** PR + nightly (full load); block merge only on fast ones.
3. **Who owns?** Architect defines, team maintains, review quarterly.
