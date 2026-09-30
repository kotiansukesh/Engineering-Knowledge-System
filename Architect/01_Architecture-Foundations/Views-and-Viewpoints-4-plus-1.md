---
title: Views and Viewpoints — 4+1
category: Architect/01_Architecture-Foundations
tags:
- 4plus1
- architecture
- c4
- concept/architecture-principles
- concept/quality-attributes
- concept/trade-offs
- difficulty/medium
- documentation
- views
created: 2026-09-03
completed: false
reviewed: '2026-09-22'
sr-due: '2026-09-29'
difficulty: Medium
excalidraw: ''
source: ''
type: note
weeks: ''

---





## 🎯 Intent
Show the system from complementary angles — Logical, Process, Development, Physical + Scenarios — so no single diagram lies by omission. The "+1" scenarios are the only view that validates the other four against real quality requirements.

## 💡 Why It Matters
- **Interview signal**: "A reviewer says your doc has a container diagram but nothing about runtime or deployment. Which viewpoints are missing and why?" — missing Process/Physical = untestable availability/capacity claims
- **Stakeholder communication**: Each audience gets their lens (Product: Context, SRE: Physical, Dev: Development, Security: Threat Model)
- **ADR binding**: The +1 quality scenarios tie views to measurable requirements (p99, RTO, cost/txn)

## Problems
### System Design Problem: Views and Viewpoints — 4+1

**Requirements:**
- Functional: Core capabilities for views and viewpoints — 4+1
- Non-functional (SLOs): Latency < 100ms p99, Availability 99.9%, Horizontal scalability

**Constraints:**
- Scale: Handle 10x growth without redesign
- Consistency: Appropriate model for domain (strong/eventual)
- Latency budget: p99 < 100ms for read paths

**API / Interfaces:**
- Primary: REST/gRPC endpoints for core operations
- Internal: Service-to-service contracts
- Events: Domain events for async integration

## 🧩 Diagram: 4+1 View Model
```mermaid
graph TD
    L[Logical: C4 L2/L3<br/>Domain Structure] --> S["+1: Quality Scenarios<br/>(p99, RTO, Cost/txn)"]
    P[Process: Sequence/Runtime<br/>Concurrency + Failure] --> S
    D[Development: Modules/ArchUnit<br/>Build Boundaries] --> S
    PH[Physical: K8s/Deploy<br/>Replicas, Zones, Failover] --> S
    S --> SYS[(One System, Four Lenses)]
    style S fill:#e8f5e9
    style L fill:#e3f2fd
    style PH fill:#fff3e0
```

## 💻 Code: C4 → 4+1 Mapping + Generation (Java 25)
```java
// Why C4 maps to 4+1:
// Context/Container ≈ Logical + Physical
// Component ≈ Development
// Runtime Sequence ≈ Process
// ADR Scenarios = +1

@ArchTest
static final ArchRule moduleBoundaries = noClasses()
    .that().resideInAPackage("com.shop.order..")
    .should().dependOnClassesThat().resideInAPackage("com.shop.payment.impl..");

// Physical view = K8s manifests (Helm)
// Process view = sequence diagrams from trace replay
// Logical view = Structurizr DSL from repo
// +1 view = ADR quality scenarios with fitness functions

// Example: Checkout flow runtime (Process view)
/*
sequenceDiagram
    Client->>API Gateway: POST /orders
    Gateway->>Order Service: createOrder()
    Order Service->>Payment Service: charge() [sync, timeout 2s]
    Payment Service-->>Order Service: success
    Order Service->>Kafka: OrderPlaced event
    Order Service-->>Client: 201 Created
*/
```

## ✅ When to Use / ❌ When NOT to Use
| Scenario | Use? | Reason |
|

## Trade-offs
| Dimension          | This Approach | Alternative | Trade-off Rationale | Decision Rule |
| ------------------ | ------------- | ----------- | ------------------- | ------------- |
| Complexity         | [TBD]         | [TBD]       | [TBD]               | [TBD]         |
| Operational Burden | [TBD]         | [TBD]       | [TBD]               | [TBD]         |
| Latency            | [TBD]         | [TBD]       | [TBD]               | [TBD]         |
| Consistency        | [TBD]         | [TBD]       | [TBD]               | [TBD]         |
| Cost at Scale      | [TBD]         | [TBD]       | [TBD]               | [TBD]         |

## Flashcards (Spaced Repetition)

#flashcard
**Q:** What is the core concept of Views and Viewpoints — 4+1? :: **A:** [Key algorithm/architecture pattern] #flashcard

#flashcard
**Q:** When do you apply Views and Viewpoints — 4+1? :: **A:** [Trigger scenarios and context] #flashcard

#flashcard
**Q:** What is the primary trade-off in Views and Viewpoints — 4+1? :: **A:** [Main tension: e.g., consistency vs latency] #flashcard

#flashcard
**Q:** What breaks first at scale in Views and Viewpoints — 4+1? :: **A:** [Primary bottleneck: e.g., coordination, hot keys, replication lag] #flashcard

#flashcard
**Q:** How do you handle failures in Views and Viewpoints — 4+1? :: **A:** [Retry, circuit breaker, fallback, graceful degradation] #flashcard

#flashcard
**Q:** What are the key metrics to monitor for Views and Viewpoints — 4+1? :: **A:** [RED: rate, errors, duration; USE: utilization, saturation, errors] #flashcard

#flashcard
**Q:** How does Views and Viewpoints — 4+1 scale to 10x? :: **A:** [Sharding, read replicas, async processing, caching layers] #flashcard

#flashcard
**Q:** What is the consistency model for Views and Viewpoints — 4+1? :: **A:** [Strong/eventual/causal - justify with use case] #flashcard

#flashcard
**Q:** How do you test Views and Viewpoints — 4+1? :: **A:** [Contract tests, chaos engineering, load tests, fault injection] #flashcard

#flashcard
**Q:** What is the operational cost of Views and Viewpoints — 4+1? :: **A:** [Team expertise, tooling, on-call burden, migration risk] #flashcard

#flashcard
**Q:** When would you NOT use Views and Viewpoints — 4+1? :: **A:** [Managed service covers need, simple CRUD, team lacks maturity] #flashcard

#flashcard
**Q:** What is the key design decision in Views and Viewpoints — 4+1? :: **A:** [The irreversible choice that defines the architecture] #flashcard

#flashcard
**Q:** How do you migrate to Views and Viewpoints — 4+1? :: **A:** [Strangler fig, dual-write, canary, feature flags] #flashcard

#flashcard
**Q:** What security considerations for Views and Viewpoints — 4+1? :: **A:** [AuthZ, encryption, audit, secrets management] #flashcard

#flashcard
**Q:** How do you debug Views and Viewpoints — 4+1 in production? :: **A:** [Structured logging, correlation IDs, distributed tracing, SLO alerts] #flashcard


## Practice Tasks (Tasks Plugin)
- [ ] Explain the architecture from memory 📅 {{date:YYYY-MM-DD, +1}}
- [ ] Draw the system diagram without looking 📅 {{date:YYYY-MM-DD, +3}}
- [ ] Answer all Interview Q&A aloud 📅 {{date:YYYY-MM-DD, +7}}
- [ ] Review flashcards (Spaced Repetition) 📅 {{date:YYYY-MM-DD, +1}}

```tasks
not done
path includes Architect/01_Architecture-Foundations
sort by due
limit 10
```

---|---|---|
| Design review, architecture doc, stakeholder walkthrough | ✅ | Single picture cannot carry whole story |
| Onboarding new engineer | ✅ | Read view matching their question (runtime, deploy, modules) |
| ADR work | ✅ | +1 scenarios bind four views to quality requirements |
| One-line bugfix or small refactor | ❌ | Pick 1-2 views answering the decision (usually Context + risk view) |
| Maintaining hand-drawn static diagrams | ❌ | Generate: Structurizr/ArchUnit/PlantUML from repo; stale day after review |


## 🆚 Vs. Alternatives
| View | Answers | Tool | Generation |
|---|---|---|---|
| **Logical** | Domain structure | C4 L2/L3 (Structurizr) | From repo |
| **Process** | Runtime/concurrency | Sequence diagrams | From trace replay |
| **Development** | Build/modules | ArchUnit tests | From code |
| **Physical** | Deploy | K8s manifests/Helm | From IaC |
| **+1 Scenarios** | Qualities (p99, RTO) | ADR + Fitness Functions | From requirements |

## ⚠️ Pitfalls
1. **Only static diagrams** — missing runtime (Process) and deployment (Physical); availability/capacity claims untestable
2. **Level-mixing** — DB tables on Context diagram; containers on Component diagram
3. **Hand-drawn for weekly-changing system** — generate from code (ArchUnit, Structurizr, Helm)
4. **Dropping +1** — Logical view looks identical whether system meets p99 or not; +1 is the only validator


## Pitfalls
1. Underestimating operational complexity (backups, monitoring, upgrades)
2. Ignoring failure modes (network partitions, disk failures, clock drift)
3. Not planning for 10x scale from day one
4. Skipping monitoring/alerting in MVP
5. Premature optimization before measuring
6. Dual-write without transactional outbox
7. Assuming global order in partitioned systems

## 🎤 Interview Q&A (Senior Depth)

**Q1: "A reviewer says your architecture doc has a container diagram but nothing about runtime behaviour or deployment. Which viewpoints are missing and why does it matter?"**
> **Answer**: Process (runtime/concurrency) and Physical (deployment). Container diagram answers "what runs", not "how many, where they fail over, or which calls are synchronous under load". Without them, availability and capacity claims are untestable. I'd add sequence/communication view for two critical flows + deployment view showing replicas, zones, failover before signing off. **Rejected**: "Container diagram is enough" — it's not.

**Q2: "What is the '+1' in 4+1, and can you drop it?"**
> **Answer**: The scenarios — use cases and quality-attribute scenarios that drive design. They are the *only* view that validates the other four. A logical view looks identical whether the system meets p99 or not. Dropping it is why architecture decks drift from qualities stakeholders pay for. **Rejected**: "Scenarios are in requirements" — requirements aren't views; +1 binds views to measurable tests.

**Q3: "How do you keep 4+1 views from becoming shelfware?"**
> **Answer**: Generate, don't draw. Structurizr/C4-DSL/PlantUML from repo for Context/Container; ArchUnit tests for Development view; sequence diagrams from trace replay; K8s manifests/Helm as Physical view. Review views inside the ADR/RFC that changes them. **Metric**: View freshness = last ADR that modified it.

**Q4: "4+1 versus C4 — are they competing?"**
> **Answer**: No. 4+1 is a *viewpoint framework* (which lenses to show). C4 is *notation* (how to draw them at zoom levels). C4 Context ≈ stakeholder-facing slice of Logical+Physical; Container ≈ Process+Development boundaries. I use 4+1 to decide *what* to communicate and C4 to draw it. **Rejected**: "Pick one" — they're different abstraction layers.

**Q5: "Which view do you draw first for a new system?"**
> **Answer**: Context (C4 L1) — aligns non-technical stakeholders before containers. Then the view tied to top risk: usually Process (runtime) for latency-critical, Physical (deployment) for availability-critical. **Rejected**: "All five" — overkill; pick views that answer the decision.

## 🔗 Related
- [[What-is-Architecture|What is Architecture]] • [[Architecture-Principles|Principles]]
- Notation: [[../09_Governance-Documentation/01_C4-Modeling|C4 Modeling]]
- Scenarios that bind views: [[../02_Requirements-Quality-Attributes/Quality-Scenarios|Quality Scenarios]]