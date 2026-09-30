---
title: SQL vs NoSQL Selection
category: Architect/06_Data-Architecture
tags:
- concept/cqrs
- concept/event-sourcing
- concept/polyglot-persistence
- concept/sql-vs-nosql
- data
- decision
- difficulty/medium
- mongodb
- nosql
- pattern/data-architecture
- polyglot
- postgres
- sql
created: 2026-09-03
completed: false
reviewed: '2026-09-01'
sr-due: '2026-09-08'
difficulty: Medium
excalidraw: ''
source: ''
type: concept
weeks: ''

---





## 🎯 Intent
Choose the store by access pattern and consistency needs — relational for structured data with joins/invariants, document/key-value/column/graph where shape, scale, or query demands it — defaulting to Postgres until a concrete force pushes elsewhere.

## 💡 Why It Matters
- **Interview signal**: "When would you NOT use Postgres?" and "How do you keep polyglot stores consistent?" — defaulting to familiar store fights the workload; defaulting to fashionable one reimplements joins in app code
- **Polyglot reality**: One system of record per context (usually Postgres) + purpose-built derived stores fed by events covers most systems
- **Operational cost**: Each new store = new backup, monitoring, upgrade, skill set; force the choice to be earned

## Problems
### System Design Problem: SQL vs NoSQL Selection

**Requirements:**
- Functional: Core capabilities for sql vs nosql selection
- Non-functional (SLOs): Latency < 100ms p99, Availability 99.9%, Horizontal scalability

**Constraints:**
- Scale: Handle 10x growth without redesign
- Consistency: Appropriate model for domain (strong/eventual)
- Latency budget: p99 < 100ms for read paths

**API / Interfaces:**
- Primary: REST/gRPC endpoints for core operations
- Internal: Service-to-service contracts
- Events: Domain events for async integration

## 🧩 Diagram: Polyglot Data Architecture
```mermaid
graph LR
    SOT[Postgres: System of Record<br/>ACID + Joins] -->|order.placed via outbox| K[(Kafka)]
    K --> RD[order_views: Mongo<br/>Docs for Reads]
    K --> SX[Elasticsearch<br/>Index]
    K --> TS[Timescale<br/>Metrics]
    RD --> Q[Query per Shape]
    SX --> Q
    SOT --> Q
    style SOT fill:#e8f5e9
    style K fill:#e3f2fd
```

## 💻 Code: Postgres-First + Derived Stores (Java 25 + Spring Data)
```java
// System of record: JPA + Postgres
@Entity class Order {
    @Id Long id;
    @Embedded Money total;
    @Enumerated Status status;
}

// Adjacent document read-model fed by OrderPlaced events (Spring Data Mongo)
@Document("order_views")
record OrderView(@Id String orderId, String status, BigDecimal total) {}

// Choosing in code review: "Can this be a Postgres JSONB + GIN index instead of a new cluster?"
// @Column(columnDefinition = "jsonb") + native query — one less system to operate
@Repository
interface OrderViewRepository extends MongoRepository<OrderView, String> {
    List<OrderView> findByStatus(String status);
}
```

## ✅ When to Use / ❌ When NOT to Use
| Workload | Pick | Reason |
|

## Trade-offs
| Dimension | This Approach | Alternative | Trade-off Rationale | Decision Rule |
|-----------|---------------|-------------|---------------------|---------------|
| Complexity | Not specified | Not specified | Not specified | Not specified |
| Operational Burden | Not specified | Not specified | Not specified | Not specified |
| Latency | Not specified | Not specified | Not specified | Not specified |
| Consistency | Not specified | Not specified | Not specified | Not specified |
| Cost at Scale | Not specified | Not specified | Not specified | Not specified |

## Flashcards (Spaced Repetition)

#flashcard
**Q:** What is the core concept of SQL vs NoSQL Selection? :: **A:** [Key algorithm/architecture pattern] #flashcard

#flashcard
**Q:** When do you apply SQL vs NoSQL Selection? :: **A:** [Trigger scenarios and context] #flashcard

#flashcard
**Q:** What is the primary trade-off in SQL vs NoSQL Selection? :: **A:** [Main tension: e.g., consistency vs latency] #flashcard

#flashcard
**Q:** What breaks first at scale in SQL vs NoSQL Selection? :: **A:** [Primary bottleneck: e.g., coordination, hot keys, replication lag] #flashcard

#flashcard
**Q:** How do you handle failures in SQL vs NoSQL Selection? :: **A:** [Retry, circuit breaker, fallback, graceful degradation] #flashcard

#flashcard
**Q:** What are the key metrics to monitor for SQL vs NoSQL Selection? :: **A:** [RED: rate, errors, duration; USE: utilization, saturation, errors] #flashcard

#flashcard
**Q:** How does SQL vs NoSQL Selection scale to 10x? :: **A:** [Sharding, read replicas, async processing, caching layers] #flashcard

#flashcard
**Q:** What is the consistency model for SQL vs NoSQL Selection? :: **A:** [Strong/eventual/causal - justify with use case] #flashcard

#flashcard
**Q:** How do you test SQL vs NoSQL Selection? :: **A:** [Contract tests, chaos engineering, load tests, fault injection] #flashcard

#flashcard
**Q:** What is the operational cost of SQL vs NoSQL Selection? :: **A:** [Team expertise, tooling, on-call burden, migration risk] #flashcard

#flashcard
**Q:** When would you NOT use SQL vs NoSQL Selection? :: **A:** [Managed service covers need, simple CRUD, team lacks maturity] #flashcard

#flashcard
**Q:** What is the key design decision in SQL vs NoSQL Selection? :: **A:** [The irreversible choice that defines the architecture] #flashcard

#flashcard
**Q:** How do you migrate to SQL vs NoSQL Selection? :: **A:** [Strangler fig, dual-write, canary, feature flags] #flashcard

#flashcard
**Q:** What security considerations for SQL vs NoSQL Selection? :: **A:** [AuthZ, encryption, audit, secrets management] #flashcard

#flashcard
**Q:** How do you debug SQL vs NoSQL Selection in production? :: **A:** [Structured logging, correlation IDs, distributed tracing, SLO alerts] #flashcard


## Practice Tasks (Tasks Plugin)
- [ ] Explain the architecture from memory 📅 {{date:YYYY-MM-DD, +1}}
- [ ] Draw the system diagram without looking 📅 {{date:YYYY-MM-DD, +3}}
- [ ] Answer all Interview Q&A aloud 📅 {{date:YYYY-MM-DD, +7}}
- [ ] Review flashcards (Spaced Repetition) 📅 {{date:YYYY-MM-DD, +1}}

```tasks
not done
path includes Architect/06_Data-Architecture
sort by due
limit 10
```

---|---|---|
| Orders, payments, ledger, joins + ACID invariants | **Postgres** (+ Flyway/Liquibase) | Mature tooling, ACID, JSONB covers 80% "flexible" needs |
| Catalogue/product JSON, flexible schemas, read-heavy | **MongoDB / DocumentDB** | Schema flexibility, horizontal read scale |
| Session/cart, counters, feature flags, hot keys | **Redis** (KV) | Sub-ms latency, TTL, pub/sub |
| Time-series metrics, IoT, event logs at volume | **Timescale / ClickHouse** | Columnar compression, continuous aggregates |
| Fraud rings, recommendations, deep traversals | **Neo4j (graph)** | Native traversals, no recursive CTEs |
| Full-text search, faceting | **Elasticsearch/OpenSearch** | As index, NOT system of record |

**Polyglot rule**: One **system of record** per context (usually Postgres) + purpose-built *derived* stores fed by events.


## 🆚 Vs. Alternatives
| Alternative | When to Choose | Decision Rule |
|---|---|---|
| **Postgres JSONB** | 80% "flexible" needs | Can this be JSONB + GIN instead of new cluster? |
| **CQRS + Event Sourcing** | Audit + divergent reads | See 03_Event-Sourcing-CQRS |
| **Single Shared DB** | Never | Recreates monolith at data layer — ownership unclear |

## ⚠️ Pitfalls
1. **Mongo-as-default** → reimplementing joins/transactions in app code
2. **Elasticsearch as system of record** — it's a *search index* (rebuildable), not authoritative
3. **One shared DB/cluster across contexts** — recreates monolith at data layer
4. **No eventual consistency contract** — derived stores need staleness SLAs (p99 lag < 5s) and alerts


## Pitfalls
1. Underestimating operational complexity (backups, monitoring, upgrades)
2. Ignoring failure modes (network partitions, disk failures, clock drift)
3. Not planning for 10x scale from day one
4. Skipping monitoring/alerting in MVP
5. Premature optimization before measuring
6. Dual-write without transactional outbox
7. Assuming global order in partitioned systems

## 🎤 Interview Q&A (Senior Depth)

**Q1: "When would you NOT use Postgres?"**
> **Answer**: Sustained write throughput past single-primary headroom, truly schemaless high-churn documents at scale, sub-ms KV, or graph traversals unjoinable in SQL. **Rejected**: "When data is unstructured" — Postgres JSONB + GIN covers most.

**Q2: "How do you keep polyglot stores consistent?"**
> **Answer**: Events from SOT (outbox → Kafka) build derived stores; accept eventual consistency there; NEVER dual-write in request path. **Metric**: p99 replication lag < 5s, alert on breach. **Rejected**: "Dual-write" — violates atomicity, causes drift.

**Q3: "Postgres vs Mongo for product catalogue — how do you decide?"**
> **Answer**: If catalogue has stable schema + needs joins to orders/inventory → Postgres. If schema churns weekly + read-heavy + horizontal scale needed → Mongo. Default to Postgres; force Mongo to earn its place. **Decision rule**: "Can this be Postgres JSONB + GIN?"

**Q4: "How do you handle polyglot in local dev / CI?"**
> **Answer**: Testcontainers for each store; `docker-compose` with Postgres, Mongo, Redis, Elasticsearch. CI spins all; local uses same. Cost = disk/RAM, not complexity. **Rejected**: "Mock everything" — integration bugs only surface with real stores.

**Q5: "What's the cost of a second store?"**
> **Answer**: Backup strategy, monitoring dashboards, upgrade cadence, incident runbooks, team skill ramp, schema migration tooling, connection pooling. If the derived store saves <50% latency or <30% compute vs Postgres JSONB, it's not worth it. **Metric**: Store count vs incident frequency correlation.

## 🔗 Related
- 02_Consistency-CAP-PACELC · 03_Event-Sourcing-CQRS · 05_Data-Migration-Strangler