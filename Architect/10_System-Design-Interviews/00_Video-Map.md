---
title: "Video Reference Map"
category: "System Design"
tags: [system-design, interview, videos, reference]
created: 2026-09-04
completed: false
---

# Video Reference Map

> Watch after reading the drill note, not instead of it — pause before each design decision, draw your version, then compare. Individual video URLs rot; series links don't, so this maps drills to series + what to look for.

## 1. Start-here series

| Series | Link | Use for |
|---|---|---|
| Gaurav Sen — System Design playlist (Grokking repo's own starting point) | [[https://www.youtube.com/playlist?list=PLMCXHnjXnTnvo6alSjVkgxV-VH6EPyvoX\|Gaurav Sen playlist]] | Basics (LB, queues, caching) → full builds (WhatsApp, Tinder-style feed); watch basics first |
| HiredInTech — System Design course | [[https://www.hiredintech.com/system-design/\|HiredInTech course]] | The 4-step method (constraints → abstract → bottlenecks → scale) + worked Twitter problem |

## 2. Per-drill watch guide

| Drill | Look for in the series | Watch-for moment |
|---|---|---|
| [[01_URL-Shortener-TinyURL\|TinyURL]] | URL-shortener build | KGS vs hash decision; cache sizing math |
| [[02_Twitter-Timeline-Feed\|Twitter]] | Twitter + HiredInTech Twitter problem | Push vs pull fork; celebrity threshold |
| [[03_Uber-Location-Tracking\|Uber]] | Uber/location build | Geo-cell partition; matching lease |
| [[04_WhatsApp-Chat\|WhatsApp]] | WhatsApp/chat build | Dedupe + ordering guarantees |
| [[05_Rate-Limiter\|Rate Limiter]] | Rate-limiting episode | Token-bucket vs sliding-window demo |
| [[06_Notification-Service\|Notifications]] | Notification/push episode | Priority lanes; provider failover |
| [[07_Instagram-Media-Feed\|Instagram]] | Instagram/media build | Object-store + CDN rendition flow |
| [[08_YouTube-Video-Streaming\|YouTube]] | YouTube/Netflix build | Chunked upload; transcode DAG |
| [[09_Dropbox-File-Sync\|Dropbox]] | Dropbox/sync build | Chunk-hash commit protocol |
| [[10_Web-Crawler\|Crawler]] | Crawler build | Frontier sharding; politeness queues |
| [[11_Ticketmaster-Seat-Booking\|Ticketmaster]] | Flash-sale/queue discussion | Waiting room; atomic hold |
| [[12_Yelp-Geo-Reviews\|Yelp]] | Geo-search/nearby build | Cell-bounded queries; ranking |

## 3. How to use (HiredInTech practice advice)

- **Solve with a friend:** one drives the whiteboard, one plays interviewer and injects constraints mid-design (HiredInTech's "How to Practice" section).
- **Mock under time:** 45 min per drill using the MOC loop; record where you stall — that's the note to re-read.
- **One video per drill max:** if a video contradicts a note, trust the tradeoff reasoning, not the diagram — interviews grade justification.

## 4. Links

- [[README\|System Design MOC]] · [[../99_Revision/Interview-Bank\|Interview Bank]]

<!-- Concept: video shows one walkthrough; the note holds the method — watch to calibrate, read to retain. -->
