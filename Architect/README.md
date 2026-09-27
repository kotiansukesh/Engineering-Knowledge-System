---
title: "Architect Vault"
category: "Architect"
tags: [architecture, system-design, patterns]
created: "2026-09-27"
completed: false
difficulty: "Medium"
reviewed: ""
sr-due: ""
source: ""
excalidraw: ""
weeks: "1-18"
type: "MOC"
---

# Architect Vault

> **Master MOC** for Software Architecture & System Design interview preparation
> 
> **18-Week Roadmap** covering Architecture Styles, System Design Interviews, Non-Functional Requirements, Integration Patterns, Data Architecture, and more

## 📊 Vault Progress

```dataview
TABLE
  rows.length as "Total Notes",
  sum(rows.completed) as "Completed",
  round(sum(rows.completed) * 100.0 / rows.length, 1) as "Progress %",
  sum(rows.difficulty = "Easy") as "Easy",
  sum(rows.difficulty = "Medium") as "Medium",
  sum(rows.difficulty = "Hard") as "Hard"
FROM "Architect"
WHERE type = "note"
```

## 🗓️ 18-Week Study Plan

| Week | Folder | Focus | Notes |
|------|--------|-------|-------|
| **1-2** | [[Architect/01_Architecture-Foundations/README\|Architecture Foundations]] | Principles, Quality Attributes, Trade-offs | 8 |
| **3** | [[Architect/02_Requirements-Quality-Attributes/README\|Requirements & Quality]] | QA Scenarios, Tactics, Patterns | 6 |
| **4-5** | [[Architect/03_Architecture-Styles/README\|Architecture Styles]] | Monolith, Microservices, Event-Driven, Serverless, SOA, Hexagonal, Clean | 12 |
| **6-7** | [[Architect/04_Design-Patterns-Building-Blocks/README\|Design Patterns]] | Enterprise, Integration, Cloud, Resilience | 15 |
| **8-9** | [[Architect/05_Domain-Driven-Design/README\|Domain-Driven Design]] | Bounded Contexts, Aggregates, Events, Sagas | 10 |
| **10-11** | [[Architect/06_Data-Architecture/README\|Data Architecture]] | SQL/NoSQL, CQRS, Event Sourcing, Polyglot | 10 |
| **12-13** | [[Architect/07_Integration-APIs/README\|Integration & APIs]] | REST, gRPC, GraphQL, Async, Kafka, Idempotency | 12 |
| **14-15** | [[Architect/08_NonFunctional-Ops/README\|Non-Functional Ops]] | Observability, Security, Deployment, Chaos Eng | 12 |
| **16-18** | [[Architect/10_System-Design-Interviews/README\|System Design Interviews]] | **82 Notes** (ByteByteGo 28 + Primer 54) | 82 |

## 📁 Folder Structure

```
Architect/
├── 01_Architecture-Foundations/
│   ├── Architecture-Principles.md
│   ├── Quality-Attributes.md
│   ├── Trade-offs-Analysis.md
│   └── ...
├── 02_Requirements-Quality-Attributes/
│   ├── Quality-Scenarios.md
│   ├── Availability-Tactics.md
│   └── ...
├── 03_Architecture-Styles/
│   ├── Monolith.md
│   ├── Microservices.md
│   ├── Event-Driven.md
│   ├── Serverless.md
│   ├── Hexagonal-Clean.md
│   └── ...
├── 04_Design-Patterns-Building-Blocks/
│   ├── Enterprise-Patterns.md
│   ├── Integration-Patterns.md
│   ├── Cloud-Patterns.md
│   ├── Resilience-Patterns.md
│   └── ...
├── 05_Domain-Driven-Design/
│   ├── Bounded-Contexts.md
│   ├── Aggregates.md
│   ├── Domain-Events.md
│   └── ...
├── 06_Data-Architecture/
│   ├── SQL-vs-NoSQL-Selection.md
│   ├── CQRS.md
│   ├── Event-Sourcing.md
│   └── ...
├── 07_Integration-APIs/
│   ├── REST-API-Design.md
│   ├── gRPC.md
│   ├── GraphQL.md
│   ├── Kafka-Messaging.md
│   ├── Idempotency.md
│   └── ...
├── 08_NonFunctional-Ops/
│   ├── Observability.md
│   ├── Security-OAuth2-JWT.md
│   ├── Deployment-Strategies.md
│   ├── Chaos-Engineering.md
│   └── ...
└── 10_System-Design-Interviews/
    ├── README.md (this folder's MOC)
    ├── FND-01-System-Design-Overview.md
    ├── FND-04-CAP-Theorem.md
    ├── NET-01-Load-Balancer.md
    ├── DB-05-Sharding.md
    ├── INT-01-URL-Shortener-Pastebin.md
    ├── INT-02-Twitter-Timeline.md
    ├── INT-03-Web-Crawler.md
    ├── ... (54 Primer notes)
    ├── BB-01-Scaling-Zero-to-Millions.md (ByteByteGo)
    ├── BB-04-Rate-Limiter.md (ByteByteGo)
    ├── BB-08-URL-Shortener.md (ByteByteGo)
    └── ... (28 ByteByteGo notes)
```

## 🎯 System Design Interviews (Deep Dive)

### ByteByteGo (Vol 1 & 2) - 28 Patterns
| Week | Pattern | Key Concepts |
|------|---------|--------------|
| 1 | Scaling: Zero to Millions | Load balancing, caching, DB replication, sharding |
| 1 | Back-of-Envelope | Powers of 2, latency numbers, throughput calc |
| 2 | System Design Framework | 4-step: requirements → design → deep dive → scale |
| 2 | Rate Limiter | Token bucket, sliding window, distributed |
| 2 | Consistent Hashing | Ring, virtual nodes, ketama |
| 3 | Key-Value Store | LSM trees, SSTables, compaction |
| 3 | Unique ID Generator | Snowflake, UUID, timestamp-based |
| 3 | URL Shortener | Base62, collision handling, analytics |
| 3 | Web Crawler | URL frontier, politeness, dedup, storage |
| 4 | Notification System | Push, pull, websocket, FCM/APNs |
| 4 | News Feed | Fan-out, pull vs push, ranking |
| 4 | Chat System | WebSocket, message ordering, presence |
| 4 | Search Autocomplete | Trie, n-gram, Redis, Elasticsearch |
| 5 | YouTube/Video | Transcoding, CDN, adaptive bitrate (HLS/DASH) |
| 5 | Google Drive | File sync, operational transform, CRDT |
| 5 | Proximity Service | Geohash, QuadTree, S2 geometry |
| 6 | Nearby Friends | Geohash + social graph, fan-out |
| 6 | Google Maps | Road network, routing (A*, Contraction Hierarchies) |
| 6 | Distributed Message Queue | Kafka, partitions, consumer groups, exactly-once |
| 6 | Metrics Monitoring | RED/USE metrics, Prometheus, Grafana, alerting |
| 7 | Ad Click Aggregation | Stream processing, windowing, exactly-once |
| 7 | Hotel Reservation | ACID, distributed transactions, saga |
| 7 | Distributed Email | SMTP, queue, retry, spam filtering |
| 7 | S3-like Storage | Multipart upload, consistency, versioning |
| 8 | Gaming Leaderboard | Redis sorted sets, sharding, real-time |
| 8 | Payment System | Idempotency, reconciliation, ledger |
| 8 | Digital Wallet | Balance, transactions, audit trail |
| 8 | Stock Exchange | Order book, matching engine, latency |

### system-design-primer - 54 Topics
| Category | Topics | Weeks |
|----------|--------|-------|
| **Foundational** | CAP Theorem, Consistency, Availability, DNS, CDN | 1-2 |
| **Networking** | Load Balancer, Reverse Proxy, Microservices | 2 |
| **Database** | RDBMS, Replication, Sharding, NoSQL, SQL Tuning | 3 |
| **Caching** | Strategies (Cache-Aside, Write-Through, etc.) | 4 |
| **Asynchronism** | Message Queues, Task Queues, Back Pressure | 5 |
| **Communication** | TCP/UDP, RPC/gRPC, REST | 5 |
| **Security** | Auth, Encryption, HTTPS, OAuth | 5 |
| **Reference** | Powers of 2, Latency Numbers, Back-of-Envelope | 1 |
| **Interview Problems** | Pastebin, Twitter, Web Crawler, Mint, Social Graph | 7 |
| **OOD Problems** | Hash Map, LRU Cache, Call Center, Parking Lot | 8 |

## 🔗 Quick Navigation

| Area | Link |
|------|------|
| **System Design Interviews** | [[Architect/10_System-Design-Interviews/README]] |
| **Architecture Styles** | [[Architect/03_Architecture-Styles/README]] |
| **Non-Functional Ops** | [[Architect/08_NonFunctional-Ops/README]] |
| **Integration Patterns** | [[Architect/07_Integration-APIs/README]] |
| **Data Architecture** | [[Architect/06_Data-Architecture/README]] |
| **Design Patterns** | [[Architect/04_Design-Patterns-Building-Blocks/README]] |

## 📋 Active Practice Tasks

```tasks
not done
path includes Architect
sort by due
limit 15
```

## 🎴 Spaced Repetition Due

```dataview
TABLE
  sr-due as "Due",
  difficulty as "Diff",
  category as "Folder"
FROM "Architect"
WHERE type = "note" AND sr-due != "" AND completed = false
SORT sr-due ASC
LIMIT 20
```

---

*Category: Architect • Part of [[Master Dashboard|Master Dashboard]]*