---
title: "Architecture Styles"
type: folder-MOC
tags: [MOC, 03-architecture-styles]
---
# Architecture Styles

> Architecture Styles, the notes below. | Part of [[Architect/README\|Architect MOC]]

## Styles

| Note | Covers |
|---|---|
| [[Architect/03_Architecture-Styles/01_Layered-Architecture\|01_Layered-Architecture]] | The default; testability, the sink-hole anti-pattern |
| [[Architect/03_Architecture-Styles/02_Hexagonal-Ports-Adapters\|02_Hexagonal-Ports-Adapters]] | Domain in the center; adapters plug in |
| [[Architect/03_Architecture-Styles/03_Microservices\|03_Microservices]] | Deploy/run/scale independently; distributed-systems tax |
| [[Architect/03_Architecture-Styles/04_Event-Driven-Architecture\|04_Event-Driven-Architecture]] | Async, eventually consistent; choreography vs orchestration |
| [[Architect/03_Architecture-Styles/05_Serverless\|05_Serverless]] | Scale-to-zero + per-run billing; cold starts |
| [[Architect/03_Architecture-Styles/06_Monolith-vs-Modular-Choice-Guide\|06_Monolith-vs-Modular-Choice-Guide]] | Decision table: which style when |
```dataview
TABLE WITHOUT ID file.link as "Note", category as "Category"
FROM "Architect/Architect/03_Architecture-Styles"
WHERE file.name != "README"
SORT file.name ASC
```
[[Architect/README|← Back to Architect MOC]]

---
*Category: Architect/Architect/03_Architecture-Styles*
