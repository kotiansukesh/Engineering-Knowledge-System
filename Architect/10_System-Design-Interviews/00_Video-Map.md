---
title: Video Reference Map
category: System Design
tags:
- system-design
- interview
- videos
- reference
created: 2026-09-04
completed: false
reviewed: ''
sr-due: ''
difficulty: Easy
excalidraw: ''
source: ''
type: note
weeks: ''
---

## Why it Matters

Videos teach *recognition*; interviews test *production*. The map exists to keep the two in the right order: watch after attempting the drill note, never instead of it, and pause before each decision is made, because the moment you watch a solution is the moment you stop practising.

## Diagram

```mermaid
graph LR
 D[Attempt drill note: 45 min timed] --> S{Stuck point}
 S -->|concept| V[Single-topic video, this map]
 S -->|decision| P[Pause before reveal: draw your answer]
 V --> R[Re-attempt the drill cold]
 P --> R
 R --> A[Trade-off note: what + why + what was sacrificed]
 A --> MOC[[README|Drill MOC]]
```

## Code

```text
Watch protocol that keeps video learning honest:
1. Before pressing play: attempt the drill for 45 min, timed, whiteboard only.
2. On the video: pause at every design fork; commit to an answer out loud.
3. Compare: if your reasoning matches the trade-off (not the diagram) → pass.
4. If not: note the concept missed, watch the single-topic deep dive, re-attempt cold.
5. Never watch a second build of the same drill until you can draw the first from memory.
```

## When to use / not

- **Use:** after attempting a drill and hitting a specific stuck point, the map routes that one concept to one video, which is how video actually helps.
- **Use:** for topics no vault note covers yet (consistent hashing, back-of-envelope estimation, key-value stores), the map is the interim index for those gaps.
- **Use:** for one-topic deep dives from the Shrayansh playlist, one row per question you got wrong, not a full playlist binge.

**When NOT:** do not watch instead of practising, recognition of a correct diagram feels like understanding but doesn't survive a whiteboard, and interviews grade justification, not recall of someone else's boxes. Do not treat individual video URLs as durable references; they rot, which is why this maps to *series* and to what to look for.

## Trade-offs

| Pros | Cons |
|---|---|
| Routes a stuck point to the single right video in seconds | URLs rot; series links outlive individual videos |
| Visual/system design intuition builds fast from worked builds | Passive watching creates false confidence vs timed practice |
| Covers vault gaps (consistent hashing, estimation) | Easy substitute for the 45-minute drill that builds the skill |

## Vs

| Companion | Use it for |
|---|---|
| [[README\|System Design MOC]] | The drills themselves, the method and the loop |
| [[../99_Revision/Interview-Bank\|Interview Bank]] | Short-form concept questions, no video needed |
| Drill notes (e.g. [[01_URL-Shortener-TinyURL\|TinyURL]]) | The canonical trade-off reasoning, videos are the fallback, not the source |

## Pitfalls

- Watching a full build before attempting the drill, the solution then feels obvious and the skill never forms.
- Trusting the video's diagram over the note's trade-off reasoning: when they conflict, trust the trade-off justification.
- Bookmarking videos instead of the concept: you can't recall a URL in an interview.

## Interview q&a

**Q: Watching system-design videos helps recognition, but how do you know you can actually produce the design under interview conditions?**
A: Only timed production proves it. My rule is video-after-attempt: 45 minutes on a whiteboard with no references first, then the video is a comparison, not a lesson. The signal is whether I can draw the whole flow from memory and defend each fork, and if I stall, that exact stall point routes to one topic on this map, which I re-attempt cold afterwards. Recognition is what you feel; production is what's measured.

**Q: You've watched dozens of system-design videos. What did you actually learn from them that transferred?**
A: Two things, and neither is a diagram. First, the *shape* of a defensible answer, scope → capacity → API → high-level → two deep dives → trade-offs, which converts an open question into a controlled one. Second, the repeated trade-off vocabulary (push vs pull fan-out, consistency vs availability, batch vs latency) that lets me pick a stance fast and spend the remaining time justifying it. Diagrams don't transfer; the shape and the vocabulary do.

**Q: Two videos disagree on how to design the same system. Which do you trust?**
A: Neither, I trust the trade-off reasoning that survives a constraint change. The disagreement is usually a different assumption about scale, read/write ratio, or consistency needs, so I find the assumption and evaluate both designs against *our* constraint. Interviews grade justification, and a candidate who can reconcile two designs against a stated constraint has shown more than either video.

**Q: Which video-derived idea changed your own design thinking most?**
A: The celebrity/fan-out threshold on timeline design, the moment a system needs two code paths (push for normal users, pull for celebrities), general design thinking breaks and constraint-driven thinking takes over. That idea transfers to everything: find the quantity that breaks the uniform solution, and design for the fork instead of the average.

## Related

- [[README\|System Design MOC]] · [[../99_Revision/Interview-Bank\|Interview Bank]]

# Video Reference map

> Watch after reading the drill note, not instead of it, pause before each design decision, draw your version, then compare. Individual video URLs rot; series links don't, so this maps drills to series + what to look for.

## 1. Start-here Series

| Series | Link | Use for |
|---|---|---|
| Gaurav Sen, System Design playlist (Grokking repo's own starting point) | [[https://www.youtube.com/playlist?list=PLMCXHnjXnTnvo6alSjVkgxV-VH6EPyvoX\|Gaurav Sen playlist]] | Basics (LB, queues, caching) → full builds (WhatsApp, Tinder-style feed); watch basics first |
| HiredInTech, System Design course | [[https://www.hiredintech.com/system-design/\|HiredInTech course]] | The 4-step method (constraints → abstract → bottlenecks → scale) + worked Twitter problem |

## 2. Per-drill Watch Guide

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

## 3. how to use (HiredInTech Practice Advice)

- **Solve with a friend:** one drives the whiteboard, one plays interviewer and injects constraints mid-design (HiredInTech's "How to Practice" section).
- **Mock under time:** 45 min per drill using the MOC loop; record where you stall, that's the note to re-read.
- **One video per drill max:** if a video contradicts a note, trust the tradeoff reasoning, not the diagram, interviews grade justification.

## 5. Concept && Coding Playlist (Shrayansh), Exact Videos

Playlist: [LLD + HLD complete series](https://www.youtube.com/playlist?list=PL6W8uoQQ2c63W58rpNFDwdrBnq5G3EfT7), Hindi with English dubs for the early episodes. Unlike the series above (watch whole builds), use these as single-topic deep dives: one row per question you got wrong.

| Video | Vault note |
|---|---|
| [Design URL Shortener like TinyURL](https://www.youtube.com/watch?v=C7_--hAhiaM) | [[01_URL-Shortener-TinyURL\|TinyURL]] |
| [WhatsApp System Design](https://www.youtube.com/watch?v=a8KUKOh3YXk) | [[04_WhatsApp-Chat\|WhatsApp]] |
| [Rate Limiter + algorithms](https://www.youtube.com/watch?v=X5daFTDfy2g) | [[05_Rate-Limiter\|Rate Limiter]] |
| [Rate Limiter implementation](https://www.youtube.com/watch?v=o9uCQHdh4DU) | [[05_Rate-Limiter\|Rate Limiter]] (code angle) |
| [Thundering herd on ticket booking](https://www.youtube.com/watch?v=1aamH7sA8FY) | [[11_Ticketmaster-Seat-Booking\|Ticketmaster]] |
| [SAGA + Strangler + CQRS](https://www.youtube.com/watch?v=qGlUKtjqaEQ) | [[../04_Design-Patterns-Building-Blocks/06_Saga-Outbox-Inbox\|Saga]] · Strangler · CQRS |
| [2PC, 3PC, SAGA transactions](https://www.youtube.com/watch?v=ET_DnJgfplY) | [[../04_Design-Patterns-Building-Blocks/06_Saga-Outbox-Inbox\|Saga]] (why 2PC fails) |
| [Dual-write problem, event-driven](https://www.youtube.com/watch?v=QaH7r4V4RmE) | [[../04_Design-Patterns-Building-Blocks/06_Saga-Outbox-Inbox\|Saga]] (outbox motive) |
| [Distributed cache + strategies](https://www.youtube.com/watch?v=RtOyBwBICRs) | [[../04_Design-Patterns-Building-Blocks/03_Caching-Strategies\|Caching]] |
| [SQL vs NoSQL](https://www.youtube.com/watch?v=fG8c-huFt70) | [[../06_Data-Architecture/01_SQL-vs-NoSQL-Selection\|SQL vs NoSQL]] |
| [CAP theorem](https://www.youtube.com/watch?v=3qRBeZsUa18) ([English dub](https://www.youtube.com/watch?v=SckoiQefVEE)) | [[../06_Data-Architecture/02_Consistency-CAP-PACELC\|CAP]] |
| [Messaging queue like Kafka](https://www.youtube.com/watch?v=oVZtzZVe9Dg) | [[../07_Integration-APIs/Kafka Messaging and Idempotency\|Kafka]] |
| [Idempotent POST API](https://www.youtube.com/watch?v=mI73eTlSqeU) | [[../07_Integration-APIs/Kafka Messaging and Idempotency\|Kafka]] (idempotency) |
| [HA and resilience, active-active](https://www.youtube.com/watch?v=iL7_8TmrePM) | [[../04_Design-Patterns-Building-Blocks/02_Resilience-Circuit-Breaker-Retry\|Resilience]] |
| [Circuit breaker](https://www.youtube.com/watch?v=_kCWAf8kEYI) | [[../04_Design-Patterns-Building-Blocks/02_Resilience-Circuit-Breaker-Retry\|Resilience]] |
| [Retry pattern](https://www.youtube.com/watch?v=oOFnyUpUDtg) | [[../04_Design-Patterns-Building-Blocks/02_Resilience-Circuit-Breaker-Retry\|Resilience]] |
| [Bulkhead pattern](https://www.youtube.com/watch?v=Ax0ycLJvvfc) | [[../04_Design-Patterns-Building-Blocks/02_Resilience-Circuit-Breaker-Retry\|Resilience]] |
| [OAuth 2.0 with samples](https://www.youtube.com/watch?v=3Gx3e3eLKrg) | [[../08_NonFunctional-Ops/01_Security-OAuth2-JWT\|OAuth2/JWT]] |
| [JWT vs SessionID](https://www.youtube.com/watch?v=gjVYRl167RQ) | [[../08_NonFunctional-Ops/01_Security-OAuth2-JWT\|OAuth2/JWT]] |
| [Decomposition pattern](https://www.youtube.com/watch?v=l1OCmsBnQ3g) | [[../03_Architecture-Styles/03_Microservices\|Microservices]] |
| [How many microservices is too many](https://www.youtube.com/watch?v=NE_LPGHYrMc) | [[../03_Architecture-Styles/06_Monolith-vs-Modular-Choice-Guide\|Monolith guide]] |
| [Scale zero to million users](https://www.youtube.com/watch?v=rExh5cPMZcI) ([English dub](https://www.youtube.com/watch?v=TKbPkO0VJ1Y)) | Scaling primer before any drill |
| [Consistent hashing](https://www.youtube.com/watch?v=jqUNbqfsnuw) ([English dub](https://www.youtube.com/watch?v=NHvGbXB46qU)) | No vault note yet, TinyURL/Instagram hashing sections |
| [Back-of-envelope estimation](https://www.youtube.com/watch?v=WZjSFNPS9Lo) | No vault note yet, use inside every drill's capacity step |
| [Key-value store, DynamoDB](https://www.youtube.com/watch?v=VKNIhztQnbY) | No vault note yet |
