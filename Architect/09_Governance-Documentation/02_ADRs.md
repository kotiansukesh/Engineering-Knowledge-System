---
title: "ADRs — Architecture Decision Records"
category: "Governance & Docs"
tags: [adr, decisions, documentation, governance]
created: 2026-09-03
completed: false
---

# ADRs — Architecture Decision Records

> **Intent:** Capture *why* in 1 page: context → options → decision → consequences; future-you (and auditors) can replay the reasoning.

## 1. When to Use
- Any irreversible choice (DB, broker, auth, multi-tenancy).
- Overriding a default (why not Postgres?).
- Post-incident pivots.

**When NOT:** ADR for tabs-vs-spaces; writing the ADR after 6 months of drift; decisions without consequences/rollback noted.

## 2. Example (Spring Boot 3.5 + K8s)

```java
# ADR-007: Kafka over SQS for order events
# Status: Accepted (2026-08-14) · Owner: platform
# Context: need replay + ordering per customer, 5k msg/s peak.
# Options: (a) SQS FIFO (b) Kafka (c) Postgres outbox-only.
# Decision: (b) Kafka, 12 partitions keyed by customerId, 7d retention.
# Consequences: + replay, - operate/strimzi cost; rollback: dual-publish 2 wks.

```

## 3. Pros / Cons
| Pros | Cons |
|---|---|
| Decisions searchable, not tribal | Needs curation (superseded vs accepted) |
| Onboards + defends in audits | Templates ignored without review gate |
| Forces consequence thinking | Numbering debates waste time (just sequence) |

## 4. Vs
- **Vs RFC:** RFC debates *before*; ADR records *after* — RFC → decision → ADR, linked.
- **Vs wiki page:** ADR is immutable + timestamped; wiki is living doc — never rewrite history.

## 5. Interview Q&A
**Q: What are the 5 ADR sections?**
A: Title+status, Context, Options considered, Decision, Consequences (+ rollback). One page max.

**Q: When do you supersede?**
A: New ADR references old ('Supersedes ADR-007'), old marked Superseded — never edited.

**Q: Who approves?**
A: Owning team + affected teams' thumbs-up in RFC review; staff+ for cross-cutting.

## 6. Pitfalls
- 'We chose X because it's best' (no criteria).
- No expiry/review date for provisional ADRs.
- Storing ADRs outside the repo (unfindable).

## 7. Links
- [[03_Review-Process-RFC]] · [[01_C4-Modeling]] · [[05_Compliance-Audit]]
