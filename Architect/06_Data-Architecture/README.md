---
title: "Data Architecture"
type: folder-MOC
tags: [MOC, 06-data-architecture]
---
# Data Architecture

> Data Architecture, the notes below. | Part of [[Architect/README\|Architect MOC]]

## Architecture

| Note | Covers |
|---|---|
| [[Architect/06_Data-Architecture/01_SQL-vs-NoSQL-Selection\|01_SQL-vs-NoSQL-Selection]] | CAP-adjacent; access-pattern-driven choice |
| [[Architect/06_Data-Architecture/02_Consistency-CAP-PACELC\|02_Consistency-CAP-PACELC]] | Partition tolerance is not optional |
| [[Architect/06_Data-Architecture/03_Event-Sourcing-CQRS\|03_Event-Sourcing-CQRS]] | Append-only truth; read/write model split |
| [[Architect/06_Data-Architecture/04_Caching-CDN\|04_Caching-CDN]] | Edge bytes + HTTP caching vs app cache |
| [[Architect/06_Data-Architecture/05_Data-Migration-Strangler\|05_Data-Migration-Strangler]] | Dual-write + expand-contract schemas |
```dataview
TABLE WITHOUT ID file.link as "Note", category as "Category"
FROM "Architect/Architect/06_Data-Architecture"
WHERE file.name != "README"
SORT file.name ASC
```
[[Architect/README|← Back to Architect MOC]]

---
*Category: Architect/Architect/06_Data-Architecture*
