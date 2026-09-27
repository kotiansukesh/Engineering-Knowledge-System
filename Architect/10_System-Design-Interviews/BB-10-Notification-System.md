---
title: Design a Notification System
category: Architect/10_System-Design-Interviews
tags:
- apns
- concept/interview-prep
- difficulty/medium
- fcm
- notification
- pattern/system-design
- pull
- push
- websocket
created: '2026-09-27'
completed: false
difficulty: Medium
reviewed: '2026-08-28'
sr-due: '2026-09-04'
source: https://github.com/donnemartin/system-design-primer
excalidraw: ''
weeks: '4'
type: note
---






# Design a Notification System

> Part of [[README|MOC]] • `Architect/10_System-Design-Interviews` • Weeks 4
> 🎨 **Visual diagram:** Create Excalidraw drawing from template: `Cmd+P → Excalidraw: New from template → System Design Interviews Diagram`

## Intent



## Why it Matters

- **Interview signal**: Frequently asked in system design interviews
- **Production impact**: Fundamental to scalable system design
- **Core concept**: Key building block for distributed systems

## Problems

### System Design Problem: Design a Notification System

**Requirements:**
- See primer for detailed requirements

**Constraints:**
- High availability, scalability, fault tolerance

## Code / Example

```java
// Java 25 / Spring Boot 3.5: Core concept for Design a Notification System
// Architecture pattern - implementation varies by system

record DesignaNotificationSystemConfig(
    String component,
    int capacity,
    String strategy
) {
    static DesignaNotificationSystemConfig ofDefaults() {
        return new DesignaNotificationSystemConfig(
            "Design a Notification System",
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
**A:** ('Design a notification system (push, email, SMS, in-app).', '1) API Gateway -> Notification Service (stateless). 2) Template Engine: render per channel. 3) Channel Adapters: FCM/APNs (push), SendGrid/Twilio (email/SMS), WebSocket (in-app). 4) Queue: Kafka (high throughput) or RabbitMQ (lower). 5) Preferences: user opt-in/out per channel/type. 6) Deduplication: prevent duplicate sends. 7) Retry: exponential backoff + DLQ. 8) Analytics: delivery, open, click rates.')

**Q2: Q2**
**A:** ('How do you handle 10M concurrent WebSocket connections?', 'Connection server cluster (stateless). Redis pub/sub for message routing. Connection sharding by user_id. Heartbeat (ping/pong) for liveness. Offload TLS to load balancer. Horizontal scale: add connection servers.')

**Q3: Q3**
**A:** ('How do you guarantee delivery for critical notifications (OTP, alerts)?', 'Multi-channel fallback: push -> SMS -> email. Idempotent send (dedup key). Synchronous send for critical (wait for provider ack). Retry with exponential backoff. Alert on DLQ.')

**Q4: Q4**
**A:** ('How do you handle user preferences and timezone?', 'Preference service: per-user, per-type, per-channel. Quiet hours (timezone-aware). Frequency capping (max N/day). Unsubscribe link in every email. GDPR compliance (right to delete).')

**Q5: Q5**
**A:** ('How do you scale the notification pipeline?', 'Partition Kafka by user_id. Consumer groups per channel. Horizontal scale workers. Backpressure: pause consumption if downstream slow. Metrics: queue lag, delivery latency, success rate per channel.')
## Flashcards (Spaced Repetition)

#flashcard
**Q:** Notification channels? :: **A:** Push (FCM/APNs), Email (SendGrid), SMS (Twilio), In-app (WebSocket) #flashcard

#flashcard
**Q:** Template engine? :: **A:** Per-channel rendering. Variables, localization, preview. Jinja2/Handlebars #flashcard

#flashcard
**Q:** 10M WebSocket connections? :: **A:** Connection server cluster (stateless). Redis pub/sub routing. Shard by user_id. Heartbeat #flashcard

#flashcard
**Q:** Critical notification delivery? :: **A:** Multi-channel fallback: push → SMS → email. Idempotent send. Sync wait for provider ack #flashcard

#flashcard
**Q:** User preferences? :: **A:** Per-user, per-type, per-channel. Quiet hours (TZ-aware). Frequency capping. Unsubscribe link #flashcard

#flashcard
**Q:** Deduplication? :: **A:** Dedup key per notification. Prevent duplicate sends. TTL on dedup keys #flashcard

#flashcard
**Q:** Retry strategy? :: **A:** Exponential backoff + DLQ. Alert on DLQ growth. Max retries per channel #flashcard

#flashcard
**Q:** Scaling pipeline? :: **A:** Partition Kafka by user_id. Consumer groups per channel. Backpressure: pause consumption #flashcard

#flashcard
**Q:** Delivery tracking? :: **A:** Message ID → provider ID. Webhooks for delivery/read/click. Analytics pipeline #flashcard

#flashcard
**Q:** GDPR compliance? :: **A:** Right to delete. Consent management. Data retention policies. Unsubscribe in every email #flashcard

#flashcard
**Q:** In-app notifications? :: **A:** WebSocket for real-time. Fallback to poll. Badge counts. Mark read sync #flashcard

#flashcard
**Q:** Rate limiting providers? :: **A:** Respect provider limits (FCM: 1000/req, SendGrid: 600/sec). Queue locally, throttle #flashcard

#flashcard
**Q:** Template versioning? :: **A:** Version templates. A/B test. Rollback capability. Preview before send #flashcard

#flashcard
**Q:** Monitoring? :: **A:** Delivery rate, open rate, click rate, bounce rate, latency, DLQ size, provider errors #flashcard

#flashcard
**Q:** Idempotent sends? :: **A:** Client generates idempotency key. Server dedups on key. Safe retry #flashcard
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