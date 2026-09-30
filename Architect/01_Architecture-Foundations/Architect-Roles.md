---
title: Architect Roles
category: Architect/01_Architecture-Foundations
tags:
- architecture
- concept/architecture-principles
- concept/quality-attributes
- concept/trade-offs
- difficulty/medium
- domain
- enterprise
- platform
- roles
- solution
created: 2026-09-03
completed: false
reviewed: '2026-08-29'
sr-due: '2026-09-05'
difficulty: Medium
excalidraw: ''
source: ''
type: note
weeks: ''

---





## 🎯 Intent
Distinguish Solution / Domain / Platform / Enterprise Architect so you operate at the right scope, resolve conflicts via RACI, and avoid becoming a PowerPoint architect who never validates decisions in code.

## 💡 Why It Matters
- **Interview signal**: "How do solution, domain, platform, and enterprise architecture differ, and who owns a spanning decision?" — mapping disagreement to role boundary tells you if it's technical debate or authority gap
- **Org scaling**: Roles scale with org size and concurrency, not ambition; a 5-person team wears multiple hats
- **Accountability**: One accountable owner per decision; RACI prevents every decision landing on one person

## Problems
### System Design Problem: Architect Roles

**Requirements:**
- Functional: Core capabilities for architect roles
- Non-functional (SLOs): Latency < 100ms p99, Availability 99.9%, Horizontal scalability

**Constraints:**
- Scale: Handle 10x growth without redesign
- Consistency: Appropriate model for domain (strong/eventual)
- Latency budget: p99 < 100ms for read paths

**API / Interfaces:**
- Primary: REST/gRPC endpoints for core operations
- Internal: Service-to-service contracts
- Events: Domain events for async integration

## 🧩 Diagram: Architect Role Boundaries
```mermaid
graph LR
    SP[Sponsor] --> SO[Solution: End-to-End<br/>for One System]
    DE[Domain Experts] --> DO[Domain: Bounded-Context<br/>Model + Invariants]
    PT[Platform Team] --> PL[Platform: Paved Road<br/>CI/K8s/Kafka/Identity]
    PO[Portfolio] --> EN[Enterprise: Standards<br/>Constraints + Risk]
    SO --> SYS[(Delivered System)]
    DO --> SYS
    PL --> SYS
    EN --> SYS
    style SO fill:#e3f2fd
    style DO fill:#e8f5e9
    style PL fill:#fff3e0
    style EN fill:#fce4ec
```

## 💻 Code: RACI for Spanning Decision (Java 25)
```java
// Why RACI: Order checkout spans solution (flow), domain (pricing rules),
// platform (Kafka/EKS), enterprise (PCI scope) — one owner per decision

record Decision(String name, String accountable, List<String> consulted, List<String> informed) {}

var pciCheckout = new Decision(
    "PCI-scoped Checkout Flow",
    "Solution Architect",                           // Accountable: end-to-end design
    List.of("Enterprise Arch", "Platform Arch", "Domain Arch"), // Consulted
    List.of("Security", "Finance", "SRE")           // Informed
);

// Solution owns end-to-end fitness for one system
// Domain owns bounded-context model and its invariants
// Platform owns paved road (CI, K8s, Kafka, identity)
// Enterprise owns portfolio constraints, standards, risk
```

## ✅ When to Use / ❌ When NOT to Use
| Scenario | Use? | Reason |
|

## Trade-offs
| Dimension | This Approach | Alternative | Trade-off Rationale | Decision Rule |
|-----------|---------------|-------------|---------------------|---------------|
| Complexity | [TBD] | [TBD] | [TBD] | [TBD] |
| Operational Burden | [TBD] | [TBD] | [TBD] | [TBD] |
| Latency | [TBD] | [TBD] | [TBD] | [TBD] |
| Consistency | [TBD] | [TBD] | [TBD] | [TBD] |
| Cost at Scale | [TBD] | [TBD] | [TBD] | [TBD] |

## Flashcards (Spaced Repetition)

#flashcard
**Q:** What is the core concept of Architect Roles? :: **A:** [Key algorithm/architecture pattern] #flashcard

#flashcard
**Q:** When do you apply Architect Roles? :: **A:** [Trigger scenarios and context] #flashcard

#flashcard
**Q:** What is the primary trade-off in Architect Roles? :: **A:** [Main tension: e.g., consistency vs latency] #flashcard

#flashcard
**Q:** What breaks first at scale in Architect Roles? :: **A:** [Primary bottleneck: e.g., coordination, hot keys, replication lag] #flashcard

#flashcard
**Q:** How do you handle failures in Architect Roles? :: **A:** [Retry, circuit breaker, fallback, graceful degradation] #flashcard

#flashcard
**Q:** What are the key metrics to monitor for Architect Roles? :: **A:** [RED: rate, errors, duration; USE: utilization, saturation, errors] #flashcard

#flashcard
**Q:** How does Architect Roles scale to 10x? :: **A:** [Sharding, read replicas, async processing, caching layers] #flashcard

#flashcard
**Q:** What is the consistency model for Architect Roles? :: **A:** [Strong/eventual/causal - justify with use case] #flashcard

#flashcard
**Q:** How do you test Architect Roles? :: **A:** [Contract tests, chaos engineering, load tests, fault injection] #flashcard

#flashcard
**Q:** What is the operational cost of Architect Roles? :: **A:** [Team expertise, tooling, on-call burden, migration risk] #flashcard

#flashcard
**Q:** When would you NOT use Architect Roles? :: **A:** [Managed service covers need, simple CRUD, team lacks maturity] #flashcard

#flashcard
**Q:** What is the key design decision in Architect Roles? :: **A:** [The irreversible choice that defines the architecture] #flashcard

#flashcard
**Q:** How do you migrate to Architect Roles? :: **A:** [Strangler fig, dual-write, canary, feature flags] #flashcard

#flashcard
**Q:** What security considerations for Architect Roles? :: **A:** [AuthZ, encryption, audit, secrets management] #flashcard

#flashcard
**Q:** How do you debug Architect Roles in production? :: **A:** [Structured logging, correlation IDs, distributed tracing, SLO alerts] #flashcard


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
| Program kickoff, cross-team design | ✅ | Before someone "just starts building" |
| Hiring or slotting yourself | ✅ | Match scope (one system, one domain, platform, portfolio) to actual need, not title |
| Conflict resolution | ✅ | Map disagreement to role boundary: technical debate vs authority gap |
| Instantiating all four on 5-person team | ❌ | One person wears several hats; overhead kills throughput |
| Using model to avoid coding | ❌ | Architect who never validates in code drifts into PowerPoint architecture |


## 🆚 Vs. Alternatives
| Role | Owns | Doesn't Own | Decision Rule |
|---|---|---|---|
| **Solution** | End-to-end fitness for one system | Org-wide standards | One system, one accountable |
| **Domain** | Bounded-context model | Deployment platform | Domain needs independent deploy/evolve |
| **Platform** | Paved road (CI/K8s/Kafka/identity) | Business rules | Infra toil >20% team capacity |
| **Enterprise** | Portfolio constraints, standards | Sprint-level design | Regulatory/compliance scope |

## ⚠️ Pitfalls
1. **Becoming a PowerPoint architect** — keep one concrete artifact per phase: spike, ArchUnit test, load-test run, code review
2. **Owning implementation details instead of constraints** — architect prescribes boundaries, team owns implementation
3. **Title inflation** — roles scale with org concurrency, not headcount ambition
4. **Silos if roles don't code-review** — architect must hold their own designs to same fitness gates as product teams


## Pitfalls
1. Underestimating operational complexity (backups, monitoring, upgrades)
2. Ignoring failure modes (network partitions, disk failures, clock drift)
3. Not planning for 10x scale from day one
4. Skipping monitoring/alerting in MVP
5. Premature optimization before measuring
6. Dual-write without transactional outbox
7. Assuming global order in partitioned systems

## 🎤 Interview Q&A (Senior Depth)

**Q1: "How do solution, domain, platform, and enterprise architecture differ, and who owns a decision that spans all four?"**
> **Answer**: Solution: end-to-end fitness for one system. Domain: bounded-context model + invariants. Platform: paved road (CI, K8s, Kafka, identity). Enterprise: portfolio constraints, standards, risk. For PCI checkout: Enterprise sets constraint (PCI scope), Solution owns design, Platform owns infra contract, Domain owns pricing rules. RACI: one Accountable, others Consulted/Informed. **Rejected**: "Enterprise decides everything" — that's governance, not architecture.

**Q2: "Do architects need to code, and how much?"**
> **Answer**: Enough to stay honest: spikes, ADR prototypes, fitness-function tests, code review. The test isn't velocity but whether their decisions survive contact with the codebase. An architect who hasn't felt the friction they created will keep prescribing it. **Metric**: At least one spike/ADR prototype per phase.

**Q3: "I'm a backend dev moving into architecture — which role do I target first?"**
> **Answer**: Solution or Domain — closest to the code and concerns you already own. From there the capstone is proof: C4 diagrams, an ADR log, and a fitness-function gate, one per role level you claim. **Rejected**: "Enterprise first" — too far from code; you can't govern what you haven't built.

**Q4: "How do you avoid becoming an ivory-tower architect?"**
> **Answer**: Keep one concrete artifact per phase: a spike, an ArchUnit test, a load-test run. Hold your own designs to the same fitness gates as product teams. If a principle can't pass its own test, it isn't one. **Rejected**: "Review PRs" — reviewing ≠ validating your own architectural decisions.

**Q5: "When does a team need a dedicated Platform Architect?"**
> **Answer**: When team spends >20% capacity on infra toil (CI, K8s, Kafka ops) instead of business logic. Before that, platform is a hat the Solution/Domain architect wears. **Rejected**: "When we have microservices" — services don't mandate platform role; toil does.

## 🔗 Related
- [[What-is-Architecture|What is Architecture]] • [[Stakeholders-Concerns|Stakeholders]] • [[../05_DDD-Modeling/01_Strategic-DDD|Strategic DDD]]