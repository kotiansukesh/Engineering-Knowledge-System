---
title: "ADRs, Architecture Decision Records"
category: "Governance & Docs"
tags: [adr, decisions, documentation, governance]
created: 2026-09-03
completed: false
---
## Why it Matters

Code shows *what* was built; without a record of *why*, every future team re-derives the decision or silently overturns it. A one-page ADR per significant choice, context, options, decision, consequences, turns tribal memory into a searchable, immutable log that defends the system in audits and onboarding alike.

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

## Trade-offs

| Pros | Cons |
|---|---|
| Decisions searchable, not tribal | Needs curation (superseded vs accepted) |
| Onboards + defends in audits | Templates ignored without review gate |
| Forces consequence thinking | Numbering debates waste time (just sequence) |

## Vs

- **Vs RFC:** RFC debates *before*; ADR records *after* — RFC → decision → ADR, linked.
- **Vs wiki page:** ADR is immutable + timestamped; wiki is living doc — never rewrite history.

## Pitfalls

- 'We chose X because it's best' (no criteria).
- No expiry/review date for provisional ADRs.
- Storing ADRs outside the repo (unfindable).

## Interview Q&A

**Q: What are the 5 ADR sections?**
A: Title+status, Context, Options considered, Decision, Consequences (+ rollback). One page max.

**Q: When do you supersede?**
A: New ADR references old ('Supersedes ADR-007'), old marked Superseded — never edited.

**Q: Who approves?**
A: Owning team + affected teams' thumbs-up in RFC review; staff+ for cross-cutting.

## Related

- [[03_Review-Process-RFC]] · [[01_C4-Modeling]] · [[05_Compliance-Audit]]

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