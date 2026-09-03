---
title: Tech Stack
category: overview
tags: [java, spring-boot, postgres, kafka, redis, k8s]
created: 2026-09-03
completed: false
---

# Tech Stack

## Intent
Fixed baseline so every phase builds on the same platform instead of re-choosing tools.

## Stack

| Layer | Choice | Why |
|-------|--------|-----|
| Language | Java 21 (LTS; 25 when GA stable) | Virtual threads, records, pattern matching |
| Framework | Spring Boot 3.5 | Baseline the user knows; modular + native-ready |
| DB | Postgres 16 | Relational core, JSONB, transactional outbox |
| Cache | Redis 7 | Session, rate-limit, read-through cache |
| Messaging | Kafka (KRaft) | Event-driven backbone, replay |
| K8s | Kubernetes 1.30+ (EKS/kind) | Deployment target W19–20 |
| Observability | OTel + Prometheus + Grafana + Loki | SRE phase |
| IaC | Terraform or Pulumi | EKS + MSK provisioning |
| Tests | JUnit 5, ArchUnit, Testcontainers, Gatling | Fitness functions + load |

## When / NOT
- Use for all labs. NOT for comparing every alternative — record rejected options in ADRs.

## Example (concept-level — why, not line-by-line)
```java
// Why virtual threads: high-throughput I/O (API → DB/Kafka) without reactive rewrite
// Spring Boot 3.5 enables them in one property; fits existing MVC code
// spring.threads.virtual.enabled=true
```

```yaml
# Why outbox table in Postgres: atomic business write + event publish intent
# A relay publishes to Kafka → avoids dual-write loss
```

## Pros / Cons
- Pros: boring + hireable; matches AWS-SA and iSAQB labs.
- Cons: Kafka/K8s heavy locally → use Docker Compose + kind, single-broker Kafka for dev.

## Vs
| Option | When | Tradeoff |
|--------|------|----------|
| Java 21 vs 17 | 21 for greenfield | 17 if org pinned |
| Kafka vs RabbitMQ/SQS | Kafka for replay/stream | SQS for pure ops simplicity |
| EKS vs ECS | EKS for K8s phase | ECS cheaper for capstone demo |

## Q&A
1. **Java 25?** Adopt when LTS/CI supports it; code stays 21-compatible.
2. **Spring Boot 3.5 requirements?** Java 17+; virtual threads need 21+.
3. **Local Kafka without ZooKeeper?** Yes — KRaft mode, single node.

## Pitfalls
- Version drift across notes; pin versions here, update once.
- Running full stack always-on; compose profiles per phase.

## Related
- [[Roadmap Overview|Roadmap]], [[Dashboard|Dashboard]], [[../02_Requirements-Quality-Attributes/Fitness-Functions|Fitness Functions]]
