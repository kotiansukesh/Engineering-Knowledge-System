---
title: "Interview Bank"
category: "Revision"
tags: [interview, questions, architect]
created: 2026-09-03
completed: false
---

# Interview Bank

> 3 Q&A per note — jump to the source for depth.

## 08 NonFunctional-Ops
- Security: token storage? revocation? JWT vs opaque? → [[../08_NonFunctional-Ops/01_Security-OAuth2-JWT|Security-OAuth2-JWT]]
- Observability: RED vs USE? cardinality? head vs tail sampling? → [[../08_NonFunctional-Ops/02_Observability-OTel-Prometheus|Observability]]
- Performance: set SLO? pool sizing? JFR vs profiler? → [[../08_NonFunctional-Ops/03_Performance-SLOs|Performance-SLOs]]
- Resilience: safe GameDay? backpressure? chaos order? → [[../08_NonFunctional-Ops/04_Resilience-Chaos|Resilience-Chaos]]
- K8s: zero-downtime schema? promotion gates? HPA for consumers? → [[../08_NonFunctional-Ops/05_Cloud-K8s-Deploy-Helm|K8s-Deploy]]
- FinOps: first 3 wins? attribution? perf vs cost? → [[../08_NonFunctional-Ops/06_Cost-FinOps|Cost-FinOps]]

## 09 Governance-Documentation
- C4: C2 vs C3? freshness? when C1 enough? → [[../09_Governance-Documentation/01_C4-Modeling|C4-Modeling]]
- ADR: 5 sections? supersede? approvers? → [[../09_Governance-Documentation/02_ADRs|ADRs]]
- RFC: triggers? attendees? anti-bikeshed? → [[../09_Governance-Documentation/03_Review-Process-RFC|Review-RFC]]
- TOGAF: ADM phases? iSAQB core? startup slice? → [[../09_Governance-Documentation/04_TOGAF-iSAQB-Primer|TOGAF-iSAQB]]
- Compliance: PCI scope? deletion vs backups? SOC2 evidence? → [[../09_Governance-Documentation/05_Compliance-Audit|Compliance]]

## Core (00-07) rapid links
- [[../04_Design-Patterns-Building-Blocks/02_Resilience-Circuit-Breaker-Retry|Circuit-Breaker]] · [[../03_Architecture-Styles/03_Microservices|Microservices]] · [[../03_Architecture-Styles/04_Event-Driven-Architecture|EDA]]
- Patterns: [[../04_Design-Patterns-Building-Blocks/05_Decomposition-Bounded-Context|Decomposition]] · [[../04_Design-Patterns-Building-Blocks/06_Saga-Outbox-Inbox|Saga-Outbox]] · [[../04_Design-Patterns-Building-Blocks/07_Discovery-Config-Registry|Discovery-Config]] · [[../04_Design-Patterns-Building-Blocks/04_API-Gateway-BFF|Gateway-BFF]]

## 10 System Design drills
- Method: scope → capacity → API → high-level → 2 deep dives → tradeoffs → [[../10_System-Design-Interviews/README|System Design MOC]]
- [[../10_System-Design-Interviews/01_URL-Shortener-TinyURL|TinyURL]]: counter+base62? CDN on 302s? async analytics?
- [[../10_System-Design-Interviews/02_Twitter-Timeline-Feed|Twitter]]: push vs pull? celebrity threshold? cursor pagination?
- [[../10_System-Design-Interviews/03_Uber-Location-Tracking|Uber]]: geohash/S2 cells? offer-lease vs 2PC? stale-driver TTL?
- [[../10_System-Design-Interviews/04_WhatsApp-Chat|WhatsApp]]: clientMsgId dedupe? per-convo seq? presence debounce?
- [[../10_System-Design-Interviews/05_Rate-Limiter|Rate Limiter]]: token-bucket vs sliding? gateway Lua? 429+Retry-After?
- [[../10_System-Design-Interviews/06_Notification-Service|Notifications]]: prefs gate? priority lanes? provider failover?
- Grokking round 2: [[../10_System-Design-Interviews/07_Instagram-Media-Feed|Instagram]] (bytes vs ids?) · [[../10_System-Design-Interviews/08_YouTube-Video-Streaming|YouTube]] (presigned chunks? HLS?) · [[../10_System-Design-Interviews/09_Dropbox-File-Sync|Dropbox]] (4MB chunks? delta?) · [[../10_System-Design-Interviews/10_Web-Crawler|Crawler]] (per-host queues? Bloom?) · [[../10_System-Design-Interviews/11_Ticketmaster-Seat-Booking|Ticketmaster]] (atomic hold? waiting room?) · [[../10_System-Design-Interviews/12_Yelp-Geo-Reviews|Yelp]] (cells? aggregates?)

```dataview
TABLE completed AS Done FROM "Architect/08_NonFunctional-Ops" SORT file.name ASC
```
<!-- Concept: bank = index, not duplicate; answers live in source notes. -->
