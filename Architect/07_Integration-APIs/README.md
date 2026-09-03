---
title: "07 Integration APIs — MOC"
type: MOC
tags: [MOC, integration, api, rest, grpc, kafka, gateway]
created: 2026-09-03
completed: false
---

# 07 Integration and APIs — MOC

> Part of [[99_Revision/README|Revision MOC]] • Integration styles: sync vs async, contracts, and edge.

## Notes

- [[REST Maturity and Contracts]]
- [[gRPC and Protobuf]]
- [[Kafka Messaging and Idempotency]]
- [[Gateway and Service Mesh]]

## Decision Guide

| Need | Choose |
|------|--------|
| Public / browser clients | REST + OpenAPI |
| Low-latency service-to-service | gRPC + Protobuf |
| Events, scale-out, replay | Kafka |
| Edge auth, routing, rate-limit | Gateway + Service Mesh |

```dataview
TABLE WITHOUT ID file.link as "Note", tags as "Tags"
FROM "Architect/07_Integration-APIs"
WHERE file.name != "README"
SORT file.name ASC
```

---
*Category: moc • integration*
