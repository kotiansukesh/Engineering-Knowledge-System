---
title: Architecture Principles
category: Architect/01_Architecture-Foundations
tags:
- architecture
- principles
- governance
- fitness-functions
created: 2026-09-03
completed: false
reviewed: ''
sr-due: ''
difficulty: Medium
excalidraw: ''
source: ''
type: note
weeks: ''
---

## 🎯 Intent
Turn values into testable guardrails — "API-first, modular monolith first" — that prune options before design. A principle only becomes governance when a CI gate can fail on its violation.

## 💡 Why It Matters
- **Interview signal**: "How do you turn 'we should be scalable' into a real architecture principle?" — untestable slogans get ignored; testable principles block PRs
- **Decision velocity**: When team relitigates same choices (modularity, tech selection, API style), principles are the axioms; ADRs are the derived decisions
- **Onboarding**: New engineer learns constraints from principles + fitness functions, not "ask the loudest senior"

## 🧩 Diagram: Principle → Fitness Function Pipeline
```mermaid
flowchart LR
    V[Values from Strategy] --> P["Principle: Statement + Rationale + Implication"]
    P --> F[Fitness Test: ArchUnit / Gatling / OWASP]
    F --> G{CI Gate}
    G -->|pass| O[Design Options Pruned Before Design]
    G -->|fail| R[PR Blocked: Fix Drift or Amend Principle]
    R --> P
    style P fill:#e3f2fd
    style F fill:#e8f5e9
    style G fill:#fff3e0
```

## 💻 Code: Testable Principle Format (Java 25 + ArchUnit)
```java
// Why principle format: "Modular monolith first — Rationale: deploy simplicity;
// Implication: ArchUnit boundaries; Test: mvn test passes boundary rules"

@ArchTest
static final ArchRule modularMonolithFirst = layeredArchitecture()
    .layer("Domain").definedBy("com.shop..domain..")
    .layer("Application").definedBy("com.shop..application..")
    .layer("Infrastructure").definedBy("com.shop..infrastructure..")
    .whereLayer("Domain").mayNotBeAccessedByAnyLayer()
    .whereLayer("Application").mayOnlyBeAccessedByLayers("Infrastructure");

// Principle: "Scale horizontally behind gateway"
// Rationale: top SLO risk = stateful single point of failure
// Implication: no session affinity, state externalised to Redis
// Test: k6 ramp asserting p99 holds at 3× peak + ArchUnit banning stateful singletons in web layer

@ArchTest
static final ArchRule noStatefulSingletonsInWeb = noClasses()
    .that().resideInAPackage("..web..")
    .should().beAnnotatedWith("jakarta.ejb.Stateful"); // or custom @Stateful
```

## ✅ When to Use / ❌ When NOT to Use
| Scenario | Use? | Reason |
|---|---|---|
| Team keeps relitigating same choices | ✅ | Principles = axioms; ADRs = derived decisions |
| Input to fitness functions (CI gates) | ✅ | Principle only becomes governance when testable |
| Before writing any ADR | ✅ | Principles are the axioms |
| Shipping untestable slogan ("be scalable") | ❌ | Slogans get ignored within a quarter |
| Exceeding ~8 principles | ❌ | Beyond 8, nobody recalls under deadline pressure |

## ⚖️ Trade-offs
| Dimension | Pros | Cons |
|---|---|---|
| **Faster decisions** | Consistent trade-offs | **Rigid if never revisited** |
| **Testable governance** | CI fails on drift | **Ignored if too many** (>8) |
| **Onboarding** | Constraints documented | **Maintenance burden** if tests drift |

## 🆚 Vs. Alternatives
| Principle | Counters | Decide By |
|---|---|---|
| **Modularity first** | Microservices-by-default | Deploy/ops cost |
| **API-first** | UI-driven schema | Consumer count |
| **Boring tech** | Resume-driven | Team skill + SLO risk |
| **Observability by default** | Logs-as-afterthought | MTTR target |

## ⚠️ Pitfalls
1. **Untestable ("be scalable")** — rewrite as scenario with fitness function
2. **Principles nobody can veto with** — if a principle can't block a PR, it's dead weight
3. **Never revisiting** — amend in ADR when constraint is genuinely wrong; update fitness function
4. **Living only in wiki** — principles belong in repo (`ARCHITECTURE.md`), CI gate, ADR template

## 🎤 Interview Q&A (Senior Depth)

**Q1: "How do you turn 'we should be scalable' into a real architecture principle?"**
> **Answer**: Rewrite as decision-shaped statement with three attachments: rationale, implication, test. "Scale horizontally behind the gateway" → rationale: top SLO risk is stateful single point of failure; implication: no session affinity, state externalised to Redis; test: k6 ramp asserting p99 holds at 3× current peak + ArchUnit rule banning stateful singletons in web layer. What can't be tested becomes a wish, not a principle. **Rejected**: "Add more servers" — that's capacity planning, not architecture.

**Q2: "A team wants to bypass a principle they say is slowing them down. What do you do?"**
> **Answer**: Take it as data, not insubordination: ask which of the three parts is wrong — rationale, implication, or test. If constraint is genuinely wrong now, amend principle in ADR and update fitness function (a principle nobody can be blocked by is dead weight). If it's right but costly, answer is usually automation: remove the friction, not the guardrail. **Rejected**: "Grant exception" — exceptions without ADR rot the principle.

**Q3: "Where should principles live so they actually get followed?"**
> **Answer**: Three places, in order of effectiveness: 1) Repo (`ARCHITECTURE.md` or `docs/principles`) beside the code, 2) CI gate enforcing testable subset, 3) ADR template's "principles applied" field forcing every decision to cite one. A wiki page is where principles go to be ignored. **Metric**: PR blocked by principle test = principle working.

**Q4: "How does this map to TOGAF?"**
> **Answer**: TOGAF's Principles catalogue in Preliminary Phase / ADM has same shape: statement, rationale, implications. Difference: TOGAF leaves enforcement as governance-board activity. Adding automated fitness gate makes the same content stick in a delivery org. **Rejected**: "TOGAF is too heavy" — the shape is right; automation is the delivery adaptation.

**Q5: "How many principles, and how do you pick them?"**
> **Answer**: 5–8 max. Each must have: statement, rationale, implication, test. Pick by: recurring decision pain (modularity, API style, tech selection), top SLO risks, onboarding friction. **Rejected**: "More principles = better governance" — >8 = nobody remembers = ignored.

## 🔗 Related
- [[What-is-Architecture|What is Architecture]] • [[../02_Requirements-Quality-Attributes/Fitness-Functions|Fitness Functions]] • [[../09_Governance-Documentation/02_ADRs|ADRs]]