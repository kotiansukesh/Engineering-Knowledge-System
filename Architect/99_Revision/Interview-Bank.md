---
title: "Interview Bank — Architect"
pattern: 0
category: "revision"
tags: [architect, interview, revision]
created: 2026-09-03
updated: 2026-09-23
completed: false
reviewed: ""
sr-due: ""
difficulty: Easy
problems-solved: []
problems-solved-dates: {}
excalidraw: ""
---
# Interview Bank — Architect

> Curated index of killer questions from Architect vault notes. Each links to source note for full answer.

---

## Architecture Foundations (01)

### What is Architecture
| # | Question | Source |
|---|---|---|
| 1 | Define software architecture in one line. | [[What-is-Architecture]] |
| 2 | How much architecture should be done up front? | [[What-is-Architecture]] |
| 3 | Is a monolith "architecture"? | [[What-is-Architecture]] |
| 4 | What separates architecture from infrastructure? | [[What-is-Architecture]] |
| 5 | How do you enforce architectural boundaries in a monolith? | [[What-is-Architecture]] |

### Stakeholders and Concerns
| # | Question | Source |
|---|---|---|
| 1 | Who are the stakeholders for an e-commerce checkout redesign, and what does each care about? | [[Stakeholders-Concerns]] |
| 2 | Two stakeholders have opposed concerns (Security vs Product). How do you resolve? | [[Stakeholders-Concerns]] |
| 3 | Name the stakeholders teams most often forget. | [[Stakeholders-Concerns]] |
| 4 | How do you resolve conflicting stakeholder priorities in an ADR? | [[Stakeholders-Concerns]] |
| 5 | How do you record stakeholders without it becoming bureaucratic? | [[Stakeholders-Concerns]] |

### Views and Viewpoints (4+1)
| # | Question | Source |
|---|---|---|
| 1 | A reviewer says your doc has a container diagram but nothing about runtime or deployment. Which viewpoints are missing and why? | [[Views-and-Viewpoints-4-plus-1]] |
| 2 | What is the "+1" in 4+1, and can you drop it? | [[Views-and-Viewpoints-4-plus-1]] |
| 3 | How do you keep 4+1 views from becoming shelfware? | [[Views-and-Viewpoints-4-plus-1]] |
| 4 | 4+1 versus C4 — are they competing? | [[Views-and-Viewpoints-4-plus-1]] |
| 5 | Which view do you draw first for a new system? | [[Views-and-Viewpoints-4-plus-1]] |

### Architect Roles
| # | Question | Source |
|---|---|---|
| 1 | How do solution, domain, platform, and enterprise architecture differ? Who owns a spanning decision? | [[Architect-Roles]] |
| 2 | Do architects need to code, and how much? | [[Architect-Roles]] |
| 3 | Backend dev moving into architecture — which role first? | [[Architect-Roles]] |
| 4 | How do you avoid becoming an ivory-tower architect? | [[Architect-Roles]] |
| 5 | When does a team need a dedicated Platform Architect? | [[Architect-Roles]] |

### Architecture Principles
| # | Question | Source |
|---|---|---|
| 1 | How do you turn "we should be scalable" into a real architecture principle? | [[Architecture-Principles]] |
| 2 | A team wants to bypass a principle they say is slowing them down. What do you do? | [[Architecture-Principles]] |
| 3 | Where should principles live so they actually get followed? | [[Architecture-Principles]] |
| 4 | How does this map to TOGAF? | [[Architecture-Principles]] |
| 5 | How many principles, and how do you pick them? | [[Architecture-Principles]] |

---

## Data Architecture (06)

### SQL vs NoSQL Selection
| # | Question | Source |
|---|---|---|
| 1 | When would you NOT use Postgres? | [[01_SQL-vs-NoSQL-Selection]] |
| 2 | How do you keep polyglot stores consistent? | [[01_SQL-vs-NoSQL-Selection]] |
| 3 | Postgres vs Mongo for product catalogue — how do you decide? | [[01_SQL-vs-NoSQL-Selection]] |
| 4 | How do you handle polyglot in local dev / CI? | [[01_SQL-vs-NoSQL-Selection]] |
| 5 | What's the cost of a second store? | [[01_SQL-vs-NoSQL-Selection]] |

### Consistency, CAP & PACELC
| # | Question | Source |
|---|---|---|
| 1 | Is CAP "pick two of three"? | [[02_Consistency-CAP-PACELC]] |
| 2 | How do you handle conflicts in AP mode? | [[02_Consistency-CAP-PACELC]] |
| 3 | How do you implement per-operation consistency in Spring? | [[02_Consistency-CAP-PACELC]] |
| 4 | What's the latency cost of CP vs AP in normal operation (PACELC)? | [[02_Consistency-CAP-PACELC]] |
| 5 | How do you test partition behaviour? | [[02_Consistency-CAP-PACELC]] |

### Event Sourcing & CQRS
| # | Question | Source |
|---|---|---|
| 1 | How do you handle schema evolution? | [[03_Event-Sourcing-CQRS]] |
| 2 | How do rebuilds work? | [[03_Event-Sourcing-CQRS]] |
| 3 | Where do you start? | [[03_Event-Sourcing-CQRS]] |
| 4 | How do you handle concurrent commands on same aggregate? | [[03_Event-Sourcing-CQRS]] |
| 5 | CQRS without Event Sourcing — what's the difference? | [[03_Event-Sourcing-CQRS]] |

### Caching & CDN
| # | Question | Source |
|---|---|---|
| 1 | How do you invalidate across layers? | [[04_Caching-CDN]] |
| 2 | Private vs public caching? | [[04_Caching-CDN]] |
| 3 | How do you debug which cache layer served a response? | [[04_Caching-CDN]] |
| 4 | What's the cost of a stale read at each layer? | [[04_Caching-CDN]] |
| 5 | How do you handle cache warming for new deployments? | [[04_Caching-CDN]] |

### Data Migration & Strangler Fig
| # | Question | Source |
|---|---|---|
| 1 | How do you prove the new store is correct before cutover? | [[05_Data-Migration-Strangler]] |
| 2 | Dual-write or change-data-capture? | [[05_Data-Migration-Strangler]] |
| 3 | How do you handle the facade becoming permanent? | [[05_Data-Migration-Strangler]] |
| 4 | What's the Flyway expand→migrate→contract pattern? | [[05_Data-Migration-Strangler]] |
| 5 | How do you migrate a high-traffic table with zero downtime? | [[05_Data-Migration-Strangler]] |

---

## Non-Functional Ops (08)

| Topic | Rapid Links |
|---|---|
| Security | Token storage? Revocation? JWT vs opaque? → [[../08_NonFunctional-Ops/01_Security-OAuth2-JWT|Security-OAuth2-JWT]] |
| Observability | RED vs USE? Cardinality? Head vs tail sampling? → [[../08_NonFunctional-Ops/02_Observability-OTel-Prometheus|Observability]] |
| Performance | Set SLO? Pool sizing? JFR vs profiler? → [[../08_NonFunctional-Ops/03_Performance-SLOs|Performance-SLOs]] |
| Resilience | Safe GameDay? Backpressure? Chaos order? → [[../08_NonFunctional-Ops/04_Resilience-Chaos|Resilience-Chaos]] |
| K8s Deploy | Zero-downtime schema? Promotion gates? HPA for consumers? → [[../08_NonFunctional-Ops/05_Cloud-K8s-Deploy-Helm|K8s-Deploy]] |
| FinOps | First 3 wins? Attribution? Perf vs cost? → [[../08_NonFunctional-Ops/06_Cost-FinOps|Cost-FinOps]] |

---

## Governance & Documentation (09)

| Topic | Rapid Links |
|---|---|
| C4 Modeling | C2 vs C3? Freshness? When C1 enough? → [[../09_Governance-Documentation/01_C4-Modeling|C4-Modeling]] |
| ADRs | 5 sections? Supersede? Approvers? → [[../09_Governance-Documentation/02_ADRs|ADRs]] |
| RFC Process | Triggers? Attendees? Anti-bikeshed? → [[../09_Governance-Documentation/03_Review-Process-RFC|Review-RFC]] |
| TOGAF/iSAQB | ADM phases? iSAQB core? Startup slice? → [[../09_Governance-Documentation/04_TOGAF-iSAQB-Primer|TOGAF-iSAQB]] |
| Compliance | PCI scope? Deletion vs backups? SOC2 evidence? → [[../09_Governance-Documentation/05_Compliance-Audit|Compliance]] |

---

## Design Patterns & Styles (03, 04)

| Topic | Rapid Links |
|---|---|
| Resilience Patterns | Circuit Breaker, Retry, Bulkhead → [[../04_Design-Patterns-Building-Blocks/02_Resilience-Circuit-Breaker-Retry|Circuit-Breaker]] |
| Saga/Outbox/Inbox | [[../04_Design-Patterns-Building-Blocks/06_Saga-Outbox-Inbox|Saga-Outbox]] |
| Decomposition | Bounded Context → [[../04_Design-Patterns-Building-Blocks/05_Decomposition-Bounded-Context|Decomposition]] |
| API Gateway / BFF | [[../04_Design-Patterns-Building-Blocks/04_API-Gateway-BFF|Gateway-BFF]] |
| Discovery/Config/Registry | [[../04_Design-Patterns-Building-Blocks/07_Discovery-Config-Registry|Discovery-Config]] |
| Microservices Decision | [[../03_Architecture-Styles/03_Microservices|Microservices]] |
| Event-Driven Architecture | [[../03_Architecture-Styles/04_Event-Driven-Architecture|EDA]] |

---

## System Design Drills (10)

**Method**: Scope → Capacity → API → High-level → 2 Deep Dives → Tradeoffs

| Drill | Key Questions |
|---|---|
| [[../10_System-Design-Interviews/01_URL-Shortener-TinyURL|TinyURL]] | Counter+base62? CDN on 302s? Async analytics? |
| [[../10_System-Design-Interviews/02_Twitter-Timeline-Feed|Twitter]] | Push vs pull? Celebrity threshold? Cursor pagination? |
| [[../10_System-Design-Interviews/03_Uber-Location-Tracking|Uber]] | Geohash/S2 cells? Offer-lease vs 2PC? Stale-driver TTL? |
| [[../10_System-Design-Interviews/04_WhatsApp-Chat|WhatsApp]] | ClientMsgId dedupe? Per-convo seq? Presence debounce? |
| [[../10_System-Design-Interviews/05_Rate-Limiter|Rate Limiter]] | Token-bucket vs sliding? Gateway Lua? 429+Retry-After? |
| [[../10_System-Design-Interviews/06_Notification-Service|Notifications]] | Prefs gate? Priority lanes? Provider failover? |
| [[../10_System-Design-Interviews/07_Instagram-Media-Feed|Instagram]] | Bytes vs ids? |
| [[../10_System-Design-Interviews/08_YouTube-Video-Streaming|YouTube]] | Presigned chunks? HLS? |
| [[../10_System-Design-Interviews/09_Dropbox-File-Sync|Dropbox]] | 4MB chunks? Delta? |
| [[../10_System-Design-Interviews/10_Web-Crawler|Crawler]] | Per-host queues? Bloom? |
| [[../10_System-Design-Interviews/11_Ticketmaster-Seat-Booking|Ticketmaster]] | Atomic hold? Waiting room? |
| [[../10_System-Design-Interviews/12_Yelp-Geo-Reviews|Yelp]] | Cells? Aggregates? |

---

## Interview Preparation Meta

### How to use this bank
- **Weekly mock**: 3 questions + 1 system-design drill, timed
- **Spaced repetition**: Same-day → +3 days → +7 days → retire after 2 clean cold recalls
- **Pre-interview sweep**: Rapid links day before, not to learn new

### Senior answer criteria
- Names a **number** and a **sacrifice** (measured threshold + quality deliberately given up)
- Describes **decisions under constraint**, not tools
- Every pattern cited comes with the **constraint that justifies it**

### If question not in bank
- Classify: concept / trade-off / design drill
- Answer from template: "The tension is X, deciding constraint is Y, so I'd choose Z and accept cost W"

---

[[Architect/README|← Back to Architect MOC]] • [[Master Dashboard|Master Dashboard]]