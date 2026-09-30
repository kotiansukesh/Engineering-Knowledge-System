---
title: ADRs, Architecture Decision Records
category: Architect/09_Governance-Documentation
tags:
- adr
- company/youtube
- concept/adr
- concept/fitness-function
- concept/governance
- decisions
- difficulty/easy
- documentation
- governance
created: 2026-09-03
completed: false
reviewed: '2026-09-24'
sr-due: '2026-09-27'
difficulty: Easy
excalidraw: ''
source: ''
type: concept
weeks: ''

---






## Why it Matters

Code shows *what* was built; without a record of *why*, every future team re-derives the decision or silently overturns it. A one-page ADR per significant choice, context, options, decision, consequences, turns tribal memory into a searchable, immutable log that defends the system in audits and onboarding alike.

## Problems
### System Design Problem: ADRs, Architecture Decision Records

**Requirements:**
- Functional: Core capabilities for adrs, architecture decision records
- Non-functional (SLOs): Latency < 100ms p99, Availability 99.9%, Horizontal scalability

**Constraints:**
- Scale: Handle 10x growth without redesign
- Consistency: Appropriate model for domain (strong/eventual)
- Latency budget: p99 < 100ms for read paths

**API / Interfaces:**
- Primary: REST/gRPC endpoints for core operations
- Internal: Service-to-service contracts
- Events: Domain events for async integration

## Diagram

```mermaid
graph LR
 RFC[RFC: options debated] --> DEC[ADR: context / options / decision / consequences]
 DEC --> LOG[immutable log in repo: doc/adr]
 DEC -.assumption shifts|→ SUP[ADR-009 supersedes ADR-007]
 SUP --> LOG
 LOG --> REV[review: status + owner + review date]
```

## Code

```java

## When to use / NOT

- Any irreversible choice (DB, broker, auth, multi-tenancy).
- Overriding a default (why not Postgres?).
- Post-incident pivots.

**When NOT:** ADR for tabs-vs-spaces; writing the ADR after 6 months of drift; decisions without consequences/rollback noted.


## Vs

- **Vs RFC:** RFC debates *before*; ADR records *after* — RFC → decision → ADR, linked.
- **Vs wiki page:** ADR is immutable + timestamped; wiki is living doc — never rewrite history.






## Trade-offs
| Dimension | This Approach | Alternative | Trade-off Rationale | Decision Rule |
|-----------|---------------|-------------|---------------------|---------------|
| Complexity | Not specified | Not specified | Not specified | Not specified |
| Operational Burden | Not specified | Not specified | Not specified | Not specified |
| Latency | Not specified | Not specified | Not specified | Not specified |
| Consistency | Not specified | Not specified | Not specified | Not specified |
| Cost at Scale | Not specified | Not specified | Not specified | Not specified |

## Pitfalls

- 'We chose X because it's best' (no criteria).
- No expiry/review date for provisional ADRs.
- Storing ADRs outside the repo (unfindable).


## Pitfalls
1. Equating architecture with microservices/K8s — service count ≠ architecture
2. Diagrams without decisions (no ADR = no traceability)
3. 60-page doc nobody reads — risk-driven beats completeness-driven
4. Slack decisions becoming load-bearing without record
5. Underestimating operational complexity (backups, monitoring, upgrades)
6. Ignoring failure modes (network partitions, disk failures, clock drift)
7. Not planning for 10x scale from day one

## Interview Q&A

**Q: What are the 5 ADR sections?**
A: Title+status, Context, Options considered, Decision, Consequences (+ rollback). One page max.

**Q: When do you supersede?**
A: New ADR references old ('Supersedes ADR-007'), old marked Superseded — never edited.

**Q: Who approves?**
A: Owning team + affected teams' thumbs-up in RFC review; staff+ for cross-cutting.


## Flashcards (Spaced Repetition)

#flashcard
**Q:** What is the core concept of ADRs, Architecture Decision Records? :: **A:** Not specified #flashcard

#flashcard
**Q:** When do you apply ADRs, Architecture Decision Records? :: **A:** Not specified #flashcard

#flashcard
**Q:** What is the primary trade-off in ADRs, Architecture Decision Records? :: **A:** Not specified #flashcard

#flashcard
**Q:** What breaks first at scale in ADRs, Architecture Decision Records? :: **A:** Not specified #flashcard

#flashcard
**Q:** How do you handle failures in ADRs, Architecture Decision Records? :: **A:** Not specified #flashcard

#flashcard
**Q:** What are the key metrics to monitor for ADRs, Architecture Decision Records? :: **A:** Not specified #flashcard

#flashcard
**Q:** How does ADRs, Architecture Decision Records scale to 10x? :: **A:** Not specified #flashcard

#flashcard
**Q:** What is the consistency model for ADRs, Architecture Decision Records? :: **A:** Not specified #flashcard

#flashcard
**Q:** How do you test ADRs, Architecture Decision Records? :: **A:** Not specified #flashcard

#flashcard
**Q:** What is the operational cost of ADRs, Architecture Decision Records? :: **A:** Not specified #flashcard

#flashcard
**Q:** When would you NOT use ADRs, Architecture Decision Records? :: **A:** Not specified #flashcard

#flashcard
**Q:** What is the key design decision in ADRs, Architecture Decision Records? :: **A:** Not specified #flashcard

#flashcard
**Q:** How do you migrate to ADRs, Architecture Decision Records? :: **A:** Not specified #flashcard

#flashcard
**Q:** What security considerations for ADRs, Architecture Decision Records? :: **A:** Not specified #flashcard

#flashcard
**Q:** How do you debug ADRs, Architecture Decision Records in production? :: **A:** Not specified #flashcard


## Practice Tasks (Tasks Plugin)
- [ ] Explain the architecture from memory 📅 {{date:YYYY-MM-DD, +1}}
- [ ] Draw the system diagram without looking 📅 {{date:YYYY-MM-DD, +3}}
- [ ] Answer all Interview Q&A aloud 📅 {{date:YYYY-MM-DD, +7}}
- [ ] Review flashcards (Spaced Repetition) 📅 {{date:YYYY-MM-DD, +1}}

```tasks
not done
path includes Architect/09_Governance-Documentation
sort by due
limit 10
```

## Related

- 03_Review-Process-RFC · 01_C4-Modeling · 05_Compliance-Audit

# ADRs — Architecture Decision Records

> **Intent:** Capture *why* in 1 page: context → options → decision → consequences; future-you (and auditors) can replay the reasoning.
> Watch: [CodeOpinion — ADRs as a Log that Answers WHY](https://www.youtube.com/watch?v=6H6zfCNeqek)

# ADR-007: Kafka over SQS for order events

# Status: Accepted (2026-08-14) · Owner: platform

# Context: need replay + ordering per customer, 5k msg/s peak.

# Options: (a) SQS FIFO (b) Kafka (c) Postgres outbox-only.

# Decision: (b) Kafka, 12 partitions keyed by customerId, 7d retention.

# Consequences: + replay, - operate/strimzi cost; rollback: dual-publish 2 wks.

```