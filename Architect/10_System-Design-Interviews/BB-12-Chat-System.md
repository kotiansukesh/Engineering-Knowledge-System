---
title: Design a Chat System (WhatsApp/Slack)
category: Architect/10_System-Design-Interviews
tags:
- chat
- company/slack
- concept/interview-prep
- difficulty/hard
- message-ordering
- pattern/system-design
- presence
- websocket
created: '2026-09-27'
completed: false
difficulty: Hard
reviewed: '2026-09-21'
sr-due: '2026-10-05'
source: https://github.com/donnemartin/system-design-primer
excalidraw: ''
weeks: '4'
type: note
---






# Design a Chat System (WhatsApp/Slack)

> Part of [[README|MOC]] • `Architect/10_System-Design-Interviews` • Weeks 4
> 🎨 **Visual diagram:** Create Excalidraw drawing from template: `Cmd+P → Excalidraw: New from template → System Design Interviews Diagram`

## Intent



## Why it Matters

- **Interview signal**: Frequently asked in system design interviews
- **Production impact**: Fundamental to scalable system design
- **Core concept**: Key building block for distributed systems

## Problems

### System Design Problem: Design a Chat System (WhatsApp/Slack)

**Requirements:**
- See primer for detailed requirements

**Constraints:**
- High availability, scalability, fault tolerance

## Code / Example

```java
// Java 25 / Spring Boot 3.5: Core concept for Design a Chat System (WhatsApp/Slack)
// Architecture pattern - implementation varies by system

record DesignaChatSystemWhatsAppSlackConfig(
    String component,
    int capacity,
    String strategy
) {
    static DesignaChatSystemWhatsAppSlackConfig ofDefaults() {
        return new DesignaChatSystemWhatsAppSlackConfig(
            "Design a Chat System (WhatsApp/Slack)",
            10000,
            "default"
        );
    }
}
```

### Concrete Example
- **Input:** Design requirements
- **Output:** Architecture diagram + component specs
- **Explanation:** See primer for step-by-step design

## When to Use / When NOT

| **Use When** | **Avoid When** |
|--------------|----------------|
| Building this system from scratch | Managed service covers need |
| Learning architecture patterns | Simple CRUD applications |
| Interview preparation | Requirements don't match |

## Trade-offs

| Dimension | This Approach | Alternative |
|-----------|---------------|-------------|
| Complexity | | |
| Operational Burden | | |
| Latency | | |
| Consistency | | |
| Cost at Scale | | |

## Vs Table

| Aspect | This Design | Managed Service | Decision Rule |
|--------|-------------|-----------------|---------------|
| Flexibility | Full | Limited | Need custom logic? → Self-host |
| Time to Market | Weeks | Hours | Prototype? → Managed |
| Cost at Scale | Optimizable | Fixed/marginal | High volume? → Self-host |

## Pitfalls

- Underestimating operational complexity
- Ignoring failure modes
- Not planning for 10x scale
- Skipping monitoring/alerting in MVP
- Premature optimization before measuring

## Interview Q&A (Senior Depth)

**Q1: Q1**
**A:** ('Design WhatsApp/Slack. 1-on-1 and group chat.', '1) Gateway: WebSocket/long-polling, connection management. 2) Message Service: persist (Cassandra/ScyllaDB, partition by conversation_id), assign sequence ID. 3) Delivery: push to online (WebSocket), offline -> push notification (FCM/APNs). 4) Group: fan-out to members, message ordering per conversation. 5) Presence: heartbeat, last-seen. 6) Media: upload to S3, send thumbnail + CDN URL.')

**Q2: Q2**
**A:** ('How do you guarantee message ordering and exactly-once?', 'Per-conversation sequencing (single partition in Kafka/Scylla). Client: local ID + server ID, dedup on receive. Idempotent writes (upsert by message_id). Ack: client ack -> server confirms. Unacked -> retry with same ID.')

**Q3: Q3**
**A:** ('How do you scale to 1B messages/day?', 'Partition by conversation_id (hash). Read replicas for recent messages. Archive old messages to cold storage (S3). Media separate (S3 + CDN). Connection servers stateless, scale horizontally. Redis for presence/counters.')

**Q4: Q4**
**A:** ('How do you handle group chat with 1000 members?', 'Fan-out: write once, notify all (async). Message ID per recipient for ack tracking. Mute/notification settings per user. Admin controls. Search: inverted index per conversation.')

**Q5: Q5**
**A:** ('How do you handle end-to-end encryption?', 'Signal Protocol (Double Ratchet). Client generates keys. Server never sees plaintext. Group: Sender Keys (per-member ratchet). Key rotation on member join/leave. Backup: encrypted key backup to cloud (optional).')
## Flashcards (Spaced Repetition)

#flashcard
**Q:** Chat architecture? :: **A:** Gateway (WS) → Message Service (Cassandra/Scylla, partition by conversation_id) → Delivery (WS + Push) #flashcard

#flashcard
**Q:** Message ordering? :: **A:** Per-conversation sequencing (single Kafka partition/Scylla partition). Client dedup #flashcard

#flashcard
**Q:** Exactly-once? :: **A:** Client local ID + server ID. Idempotent writes (upsert by message_id). Ack: client→server #flashcard

#flashcard
**Q:** Group chat 1000 members? :: **A:** Fan-out: write once, notify all (async). Message ID per recipient for ack tracking. Mute settings #flashcard

#flashcard
**Q:** Scale to 1B msg/day? :: **A:** Partition by conversation_id. Read replicas for recent. Archive old to S3. Media separate (CDN) #flashcard

#flashcard
**Q:** Presence? :: **A:** Heartbeat (ping/pong). Last-seen in Redis. Online/offline/away. Broadcast presence changes #flashcard

#flashcard
**Q:** E2E encryption? :: **A:** Signal Protocol (Double Ratchet). Client keys. Server never sees plaintext. Group: Sender Keys #flashcard

#flashcard
**Q:** Media handling? :: **A:** Upload → S3. Send thumbnail + CDN URL. Compress images. Video: transcoding pipeline #flashcard

#flashcard
**Q:** Message search? :: **A:** Inverted index per conversation. Elasticsearch. Paginate by timestamp #flashcard

#flashcard
**Q:** Offline delivery? :: **A:** Push notification (FCM/APNs) for offline. Store until online. Sync on reconnect #flashcard

#flashcard
**Q:** Connection scaling? :: **A:** Stateless gateway. Horizontal scale. Redis for presence/counters. TLS offload at LB #flashcard

#flashcard
**Q:** Message acknowledgment? :: **A:** Client ack → server confirms. Unacked → retry with same ID. Read receipts: per-recipient #flashcard

#flashcard
**Q:** Group admin? :: **A:** Add/remove members. Promote/demote. Delete messages. Mute. Admin-only announcements #flashcard

#flashcard
**Q:** Message edit/delete? :: **A:** Edit: version + edit_ts. Delete: soft delete (tombstone). Sync across devices #flashcard

#flashcard
**Q:** Monitoring? :: **A:** Message latency (p50/p99), delivery rate, connection count, presence accuracy, WS errors #flashcard
## Practice Tasks (Tasks Plugin)

- [ ] Explain the architecture from memory 📅 {date:YYYY-MM-DD, +1}
- [ ] Draw the system diagram without looking 📅 {date:YYYY-MM-DD, +3}
- [ ] Answer all Interview Q&A aloud 📅 {date:YYYY-MM-DD, +7}
- [ ] Review flashcards (Spaced Repetition) 📅 {date:YYYY-MM-DD, +1}

```tasks
not done
path includes 10_System-Design-Interviews
sort by due
limit 10
```

## Related

- [[Architect/10_System-Design-Interviews/README|System Design Interviews Folder]]
- [[Architect/03_Architecture-Styles/README|Architecture Styles]]
- [[Architect/08_NonFunctional-Ops/README|Non-Functional Requirements]]
- [[Architect/07_Integration-APIs/README|Integration Patterns]]

---

*Category: Architect/10_System-Design-Interviews • Part of [[README|MOC]]*