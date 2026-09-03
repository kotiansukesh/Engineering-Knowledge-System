---
title: "Uber Location Tracking and Matching"
category: "System Design"
tags: [system-design, interview, geo, quadtree, websockets, matching]
created: 2026-09-04
completed: false
---

# Uber Location Tracking and Matching

> **Intent:** track moving drivers and match riders to nearby cars in seconds — the geo-index + realtime interview drill.

## 1. When to Use

- High-frequency location writes (driver ping every 4s), low-latency geo reads (ETA, nearby search < 300ms).
- Scale anchor: 1M drivers × ping/4s ≈ 250k writes/s; quadkey-indexed, Redis geo + durable log.
- **When NOT:** exact-fare correctness on the hot path — price after match, not during search.

## 2. Example (Spring Boot 3.5 + K8s)

```java
// WS /location (driver pings) → Kafka(driver-loc, keyed by geohash) → Geo-Svc updates Redis GEORADIUS index
// POST /api/v1/rides {lat,lng} → Dispatch-Svc: GEORADIUS 3km → rank by ETA → offer with 15s lease
@PostMapping("/api/v1/rides") public Ride request(@RequestBody RideReq r) {
    List<Driver> near = geo.nearby(r.lat(), r.lng(), 3_000); // Redis GEOSEARCH / S2 cell
    return dispatch.offer(near, r, Duration.ofSeconds(15));  // idempotency key per ride
}
```

Design: `Driver-GW (WebSocket, sticky) → Kafka → Geo-Svc (Redis GEO / S2 cells + Cassandra history) + Dispatch-Svc (offer/lease state machine) + Trip-Svc (Postgres)`. Partition the world: geohash/S2 cells as Kafka keys so one consumer owns one area. ETA via precomputed OSRM tiles, not live routing per candidate.

## 3. Pros / Cons

| Pros | Cons |
|---|---|
| Geohash/S2 cells: O(1) nearby, easy sharding | Cell boundaries: edge drivers missed (check neighbours) |
| Redis GEO: ms reads, TTL = stale-driver eviction | WS sticky: rebalancing complexity on deploy |
| Offer-lease: no double-book without 2PC | Eventual driver position (4s stale by design) |

## 4. Vs

- **Vs WhatsApp presence:** both heartbeat-driven, but Uber adds spatial queries — geo index is the differentiator.
- **Vs Twitter:** location is write-heavy state; feed is read-heavy broadcast.

## 5. Interview Q&A

**Q: How do you find nearby drivers?**
A: Geohash/S2 cell index (Redis GEOSEARCH), query own + 8 neighbour cells, rank by ETA tile. Quadtrees work on paper; S2/geohash shards better in prod.

**Q: How do you avoid double-booking?**
A: Offer with lease (15s hold in Redis, Lua compare-and-set); accept → Trip-Svc saga (driver-reserved → rider-confirmed, compensations on timeout).

**Q: Driver goes offline mid-trip?**
A: Heartbeat TTL (12s) marks stale; trip state machine re-offers; last-known position from Cassandra trail.

## 6. Pitfalls

- Polling location over HTTP — battery + QPS death; use WebSocket/MQTT with delta pings.
- Exact-distance ranking on full table scan — must pre-filter by cell.
- Pricing on the match path — decouple; match first, price async.

## 7. Links

- [[../07_Integration-APIs/Kafka Messaging and Idempotency|Kafka-Idempotency]] · [[../04_Design-Patterns-Building-Blocks/06_Saga-Outbox-Inbox|Saga-Outbox]] · [[../08_NonFunctional-Ops/02_Observability-OTel-Prometheus|OTel]] · [[04_WhatsApp-Chat|WhatsApp Chat]]

<!-- Concept: shard the world into cells — nearby search is a cell lookup, not a distance sort. -->
