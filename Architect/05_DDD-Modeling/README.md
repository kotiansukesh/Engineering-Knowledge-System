---
title: "DDD Modeling"
type: folder-MOC
tags: [MOC, 05-ddd-modeling]
---
# DDD Modeling

> DDD Modeling, the notes below. | Part of [[Architect/README\|Architect MOC]]

## Modeling

| Note | Covers |
|---|---|
| [[Architect/05_DDD-Modeling/01_Strategic-DDD\|01_Strategic-DDD]] | Ubiquitous language + subdomain classification |
| [[Architect/05_DDD-Modeling/02_Bounded-Contexts\|02_Bounded-Contexts]] | The model boundary; alignment to teams |
| [[Architect/05_DDD-Modeling/03_Context-Mapping\|03_Context-Mapping]] | ACL, partner, customer/supplier, shared kernel |
| [[Architect/05_DDD-Modeling/04_Tactical-Aggregates-Entities-VO\|04_Tactical-Aggregates-Entities-VO]] | Consistency boundary; identity vs attributes |
| [[Architect/05_DDD-Modeling/05_Domain-Events\|05_Domain-Events]] | What happened in the past tense; integration glue |
```dataview
TABLE WITHOUT ID file.link as "Note", category as "Category"
FROM "Architect/Architect/05_DDD-Modeling"
WHERE file.name != "README"
SORT file.name ASC
```
[[Architect/README|← Back to Architect MOC]]

---
*Category: Architect/Architect/05_DDD-Modeling*
