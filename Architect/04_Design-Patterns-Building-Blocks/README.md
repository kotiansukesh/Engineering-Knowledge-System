---
title: "Design Patterns & Building Blocks"
type: folder-MOC
tags: [MOC, 04-design-patterns-building-blocks]
---
# Design Patterns & Building Blocks

> Design Patterns & Building Blocks, the notes below. | Part of [[Architect/README\|Architect MOC]]

## Blocks

| Note | Covers |
|---|---|
| [[Architect/04_Design-Patterns-Building-Blocks/01_Enterprise-Patterns\|01_Enterprise-Patterns]] | Layered supertype, broker, offline lock |
| [[Architect/04_Design-Patterns-Building-Blocks/02_Resilience-Circuit-Breaker-Retry\|02_Resilience-Circuit-Breaker-Retry]] | Fail fast; bulkhead, backoff, jitter |
| [[Architect/04_Design-Patterns-Building-Blocks/03_Caching-Strategies\|03_Caching-Strategies]] | Cache-aside/read-through/write-through/write-back |
| [[Architect/04_Design-Patterns-Building-Blocks/04_API-Gateway-BFF\|04_API-Gateway-BFF]] | Edge concerns; one façade per client |
| [[Architect/04_Design-Patterns-Building-Blocks/05_Decomposition-Bounded-Context\|05_Decomposition-Bounded-Context]] | Seams from the domain, not the DB |
| [[Architect/04_Design-Patterns-Building-Blocks/06_Saga-Outbox-Inbox\|06_Saga-Outbox-Inbox]] | Distributed tx without 2PC; reliable messaging |
| [[Architect/04_Design-Patterns-Building-Blocks/07_Discovery-Config-Registry\|07_Discovery-Config-Registry]] | Service location + externalized config |
```dataview
TABLE WITHOUT ID file.link as "Note", category as "Category"
FROM "Architect/Architect/04_Design-Patterns-Building-Blocks"
WHERE file.name != "README"
SORT file.name ASC
```
[[Architect/README|← Back to Architect MOC]]

---
*Category: Architect/Architect/04_Design-Patterns-Building-Blocks*
