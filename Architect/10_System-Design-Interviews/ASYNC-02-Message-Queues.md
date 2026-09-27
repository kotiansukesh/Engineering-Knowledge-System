---
title: Message Queues
category: Architect/10_System-Design-Interviews
tags:
- concept/interview-prep
- difficulty/medium
- kafka
- message-queues
- pattern/system-design
- pub-sub
- rabbitmq
created: '2026-09-27'
completed: false
difficulty: Medium
reviewed: '2026-09-04'
sr-due: '2026-09-11'
source: https://github.com/donnemartin/system-design-primer
excalidraw: Kafka-ExactlyOnce.excalidraw.json
weeks: '5'
type: note
---








# Message Queues

> Part of [[README|MOC]] • `Architect/10_System-Design-Interviews` • Weeks 5
> 🎨 **Visual diagram:** Open Excalidraw template: 

## Intent



## Why it Matters

- **Interview signal**: Frequently asked in system design interviews
- **Production impact**: Fundamental to scalable system design
- **Core concept**: Key building block for distributed systems

## Problems

### System Design Problem: Message Queues

**Requirements:**
- See primer for detailed requirements

**Constraints:**
- High availability, scalability, fault tolerance

## Code / Example

```java
// Java 25 / Spring Boot 3.5: Kafka - Exactly-Once Semantics with Transactional Producer
// Production Kafka configuration for exactly-once processing

package com.architect.messaging;

import org.apache.kafka.clients.producer.ProducerConfig;
import org.apache.kafka.common.serialization.StringSerializer;
import org.springframework.kafka.core.DefaultKafkaProducerFactory;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.kafka.core.ProducerFactory;
import org.springframework.kafka.transaction.KafkaTransactionManager;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.HashMap;
import java.util.Map;

@Service
public class ExactlyOnceOrderService {

    private final KafkaTemplate<String, OrderEvent> kafkaTemplate;
    private final OrderRepository orderRepository;

    public ExactlyOnceOrderService(KafkaTemplate<String, OrderEvent> kafkaTemplate,
                                   OrderRepository orderRepository) {
        this.kafkaTemplate = kafkaTemplate;
        this.orderRepository = orderRepository;
    }

    // Exactly-once: DB write + Kafka send in single transaction
    @Transactional
    public void createOrder(Order order) {
        // 1. Persist to database
        Order saved = orderRepository.save(order);

        // 2. Send to Kafka (same transaction via KafkaTransactionManager)
        OrderEvent event = OrderEvent.created(saved.getId(), saved.getUserId(), saved.getTotal());
        kafkaTemplate.send("orders", saved.getId(), event);
        
        // 3. Send to another topic atomically
        InventoryEvent invEvent = InventoryEvent.reserve(saved.getItems());
        kafkaTemplate.send("inventory", saved.getId(), invEvent);
    }

    // Idempotent consumer with deduplication
    @KafkaListener(topics = "orders", groupId = "order-processor",
                   containerFactory = "kafkaListenerContainerFactory")
    @Transactional
    public void processOrder(ConsumerRecord<String, OrderEvent> record) {
        String orderId = record.key();
        
        // Deduplication: check if already processed
        if (processedEventRepository.existsByEventId(record.headers()
                .lastHeader("event-id").value())) {
            return; // Already processed
        }

        OrderEvent event = record.value();
        processOrderInternal(event);
        
        // Record processed event ID
        processedEventRepository.save(new ProcessedEvent(record.headers()
            .lastHeader("event-id").value()));
    }

    private void processOrderInternal(OrderEvent event) {
        // Business logic
    }
}

// Producer Factory with Exactly-Once
@Configuration
class KafkaProducerConfig {

    @Bean
    public ProducerFactory<String, OrderEvent> producerFactory() {
        Map<String, Object> props = new HashMap<>();
        props.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, "kafka-1:9092,kafka-2:9092,kafka-3:9092");
        props.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class);
        props.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, JsonSerializer.class);
        
        // Exactly-once settings
        props.put(ProducerConfig.ENABLE_IDEMPOTENCE_CONFIG, true); // Idempotent producer
        props.put(ProducerConfig.ACKS_CONFIG, "all"); // Wait for all ISR
        props.put(ProducerConfig.RETRIES_CONFIG, Integer.MAX_VALUE);
        props.put(ProducerConfig.MAX_IN_FLIGHT_REQUESTS_PER_CONNECTION, 5);
        props.put(ProducerConfig.TRANSACTIONAL_ID_CONFIG, "order-service-${spring.application.instance-id}");
        
        // Performance
        props.put(ProducerConfig.LINGER_MS_CONFIG, 5);
        props.put(ProducerConfig.BATCH_SIZE_CONFIG, 16384);
        props.put(ProducerConfig.COMPRESSION_TYPE_CONFIG, "zstd");
        
        return new DefaultKafkaProducerFactory<>(props);
    }

    @Bean
    public KafkaTemplate<String, OrderEvent> kafkaTemplate(ProducerFactory<String, OrderEvent> pf) {
        KafkaTemplate<String, OrderEvent> template = new KafkaTemplate<>(pf);
        template.setDefaultTopic("orders");
        return template;
    }

    @Bean
    public KafkaTransactionManager<String, OrderEvent> transactionManager(
            ProducerFactory<String, OrderEvent> pf) {
        return new KafkaTransactionManager<>(pf);
    }
}
```
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
**A:** ('Design a message queue system. Compare Kafka, RabbitMQ, Pulsar.', 'Kafka: log-based, high throughput, replay, ordered per partition, retention by time/size. RabbitMQ: broker-based, flexible routing (exchange/queue), lower latency, message acknowledgment, TTL. Pulsar: tiered storage, geo-replication, multi-tenancy, separation of compute/storage. Choose Kafka for event streaming/log aggregation; RabbitMQ for task queues/RPC; Pulsar for multi-tenant/cloud-native.')

**Q2: Q2**
**A:** ('How do you guarantee exactly-once semantics?', 'True exactly-once is hard. Kafka: idempotent producer (PID + sequence) + transactional API (atomic write to multiple partitions). Consumer: process + commit offset in same transaction. RabbitMQ: publisher confirms + consumer acks + deduplication (message ID). Application-level: idempotent consumers (dedup keys, upserts).')

**Q3: Q3**
**A:** ('How do you handle message ordering at scale?', 'Per-partition ordering (Kafka) or per-queue (RabbitMQ). Key: partition by correlation key (user_id, order_id). For global ordering: single partition (throughput limit). Trade-off: parallelism vs ordering. Use sequencing tokens for cross-partition ordering.')

**Q4: Q4**
**A:** ('What about dead letter queues and retry strategies?', 'Exponential backoff: 1s, 2s, 4s, 8s, max 5 retries. DLQ after max retries. Separate retry topic/queue per attempt count. Alert on DLQ growth. Poison pill detection: message processed > N times -> DLQ. Replay: fix bug, replay from DLQ or original topic with offset reset.')

**Q5: Q5**
**A:** ('How do you monitor queue health?', 'Lag: consumer offset vs producer offset (target < 1000). Throughput: msg/s in/out. Latency: produce-to-consume (p50/p99). Error rate. DLQ size. Under-replicated partitions (Kafka). Queue depth, memory, disk (RabbitMQ).')
## Flashcards (Spaced Repetition)

#flashcard
**Q:** Kafka vs RabbitMQ vs Pulsar? :: **A:** Kafka: log-based, high throughput, replay. RabbitMQ: broker-based, flexible routing. Pulsar: tiered storage, geo-replication #flashcard

#flashcard
**Q:** What is exactly-once semantics? :: **A:** Message processed exactly one time. Hard to achieve. Requires idempotent producer + transactional consumer #flashcard

#flashcard
**Q:** Kafka idempotent producer? :: **A:** PID + sequence per partition. enable.idempotence=true. Retries + acks=all #flashcard

#flashcard
**Q:** Kafka transactional API? :: **A:** Atomic write to multiple partitions + offset commit in same transaction #flashcard

#flashcard
**Q:** How to handle ordering? :: **A:** Per-partition ordering. Partition by correlation key (user_id, order_id) #flashcard

#flashcard
**Q:** What is consumer lag? :: **A:** Producer offset - consumer offset. Target: < 1000 messages #flashcard

#flashcard
**Q:** What is rebalancing? :: **A:** Consumer group membership change. Cooperative (incremental) since Kafka 2.4 #flashcard

#flashcard
**Q:** Static membership? :: **A:** group.instance.id to avoid rebalance on restart #flashcard

#flashcard
**Q:** Dead letter queue? :: **A:** Messages that fail after max retries. Separate topic per retry count. Alert on DLQ growth #flashcard

#flashcard
**Q:** Exponential backoff? :: **A:** 1s, 2s, 4s, 8s... max 5 retries. Poison pill detection after N attempts #flashcard

#flashcard
**Q:** What is log compaction? :: **A:** Key-based retention: keep latest value per key. Tombstones for deletes #flashcard

#flashcard
**Q:** Tiered storage? :: **A:** Hot data on local SSD, cold data on S3. Transparent to consumers #flashcard

#flashcard
**Q:** MirrorMaker? :: **A:** Cross-DC replication for disaster recovery #flashcard

#flashcard
**Q:** KRaft mode? :: **A:** Kafka without ZooKeeper. Metadata in internal __cluster_metadata topic #flashcard

#flashcard
**Q:** Monitoring Kafka? :: **A:** Under-replicated partitions, offline partitions, controller health, disk, network, lag #flashcard
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