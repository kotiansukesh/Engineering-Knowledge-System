---
title: "System Design Interviews MOC"
category: "MOC"
tags: [system-design, interview, moc]
created: 2026-09-04
completed: false
---
# 10_System-Design-Interviews, moc

> Classic FAANG-style drills: same method every time, requirements → capacity → API → high-level → deep dives → tradeoffs. Companion: [[00_Video-Map|Video Reference Map]] (what to watch per drill).

## Method (45-min Loop)

1. **Scope** (5m): functional + NFRs, scale, read/write ratio
2. **Capacity** (5m): QPS, storage, bandwidth, one-line math
3. **API** (5m): 2–3 endpoints, idempotency keys
4. **High-level** (10m): client → CDN/gateway → services → stores
5. **Deep dives** (15m): the 2 hard parts only (feed fan-out, geo index, …)
6. **Tradeoffs** (5m): what breaks first, what you'd do with 10×

## Designs

| # | Design | Hard parts | Links |
|---|--------|------------|-------|
| 01 | [[01_URL-Shortener-TinyURL\|URL Shortener]] | key gen, redirect hot path | caching, CAP |
| 02 | [[02_Twitter-Timeline-Feed\|Twitter Timeline]] | fan-out, timeline merge | Kafka, Redis |
| 03 | [[03_Uber-Location-Tracking\|Uber Location]] | geo index, matching | quadtrees, websockets |
| 04 | [[04_WhatsApp-Chat\|WhatsApp Chat]] | delivery guarantees, presence | idempotency, EDA |
| 05 | [[05_Rate-Limiter\|Rate Limiter]] | distributed counters, burst | gateway, Redis |
| 06 | [[06_Notification-Service\|Notification Service]] | fan-out, retries, preferences | saga, outbox |
| 07 | [[07_Instagram-Media-Feed\|Instagram]] | media pipeline, CDN renditions | object store, feed |
| 08 | [[08_YouTube-Video-Streaming\|YouTube]] | chunked upload, transcode DAG | HLS/DASH, edge |
| 09 | [[09_Dropbox-File-Sync\|Dropbox]] | chunking, delta sync | dedupe, versions |
| 10 | [[10_Web-Crawler\|Web Crawler]] | frontier, politeness, dedupe | Bloom, per-host queues |
| 11 | [[11_Ticketmaster-Seat-Booking\|Ticketmaster]] | contention, fair queue | bitmap holds, saga |
| 12 | [[12_Yelp-Geo-Reviews\|Yelp]] | geo search, aggregates | cells, Elastic |

Grokking cross-map (topics with no dedicated note, covered by the drill named):
Pastebin → TinyURL variant (blobs + TTL) · Facebook Newsfeed → Twitter feed + ranking ·
Twitter Search → crawler + inverted index (see Web Crawler).

## Progress

```dataview
TABLE completed AS Done, category AS Category
FROM "Architect/10_System-Design-Interviews"
SORT file.name ASC
```

## Links

- [[../99_Revision/Interview-Bank|Interview Bank]] · [[../99_Revision/Case-Studies|Case Studies]] · [[../06_Data-Architecture/02_Consistency-CAP-PACELC|CAP/PACELC]] · [[../04_Design-Patterns-Building-Blocks/03_Caching-Strategies|Caching]]
