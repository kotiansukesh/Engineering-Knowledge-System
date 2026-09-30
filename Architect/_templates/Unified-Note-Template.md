---
title: "{{title}}"
category: "Architect/{{category_folder}}"
tags: [architecture, system-design]
created: "{{date:YYYY-MM-DD}}"
completed: false
difficulty: "Medium"
reviewed: ""
sr-due: ""
source: ""
excalidraw: ""
weeks: ""
type: "note"
completion_criteria:
  - intent_written: false
  - why_it_matters_filled: false
  - diagram_created: false
  - problems_section_complete: false
  - code_example_added: false
  - tradeoffs_filled: false
  - pitfalls_listed: false
  - interview_qa_answered: false
  - flashcards_created: false
  - practice_tasks_scheduled: false
---

# {{title}}

> Part of [[README|Architect MOC]] • `{{category}}`
> 🎨 **Visual diagram:** Create Excalidraw drawing from template: `Cmd+P → Excalidraw: New from template → Architecture Diagram`

## Intent
One sentence: what problem does this solve? Define the **key term** in **bold**.

## Why it Matters
- Interview signal: the exact question this answers
- Production impact: cost, latency, availability, operability
- Architecture force: the constraint driving this decision

## Diagram
```mermaid
flowchart LR
    A["Context / Forces"] --> B["Decision / Pattern"]
    B --> C["Quality Attributes Addressed"]
    style B fill:#e3f2fd
```

## Problems
### System Design Problem: {{title}}

**Requirements:**
- Functional:
- Non-functional (SLOs):

**Constraints:**
- Scale:
- Consistency:
- Latency budget:

**API / Interfaces:**

## Code / Example
```java
// Java 25 / Spring Boot 3.5: Core concept for {{title}}
// Architecture pattern - implementation varies by system

record {{title.replace(/\\s+/g, '').replace('-', '').replace('(', '').replace(')', '').replace('/', '')}}Config(
    String component,
    int capacity,
    String strategy
) {
    static {{title.replace(/\\s+/g, '').replace('-', '').replace('(', '').replace(')', '').replace('/', '')}}Config ofDefaults() {
        return new {{title.replace(/\\s+/g, '').replace('-', '').replace('(', '').replace(')', '').replace('/', '')}}Config(
            "{{title}}",
            10000,
            "default"
        );
    }
}
```

### Concrete Example
- **Input:** Design requirements
- **Output:** Architecture diagram + component specs
- **Explanation:** See note for step-by-step design

## When to Use / When NOT
| **Use When** | **Avoid When** |
|--------------|----------------|
| Building this system from scratch | Managed service covers need (AWS SQS, Cloudflare, etc.) |
| Learning architecture patterns | Simple CRUD applications |
| Interview preparation | Requirements don't match |
| Need full control over trade-offs | Team lacks operational maturity |

## Trade-offs
| Dimension | This Approach | Alternative | Trade-off Rationale | Decision Rule |
|-----------|---------------|-------------|---------------------|---------------|
| Complexity | | | | |
| Operational Burden | | | | |
| Latency | | | | |
| Consistency | | | | |
| Cost at Scale | | | | |
## Vs Table
| Aspect | This Design | Managed Service | Decision Rule |
|--------|-------------|-----------------|---------------|
| Flexibility | Full | Limited | Need custom logic? → Self-host |
| Time to Market | Weeks | Hours | Prototype? → Managed |
| Cost at Scale | Optimizable | Fixed/marginal | High volume? → Self-host |
| Team Cognitive Load | High | Low | Team size/experience? |

## Pitfalls
- Underestimating operational complexity (backups, monitoring, upgrades)
- Ignoring failure modes (network partitions, disk failures, clock drift)
- Not planning for 10x scale from day one
- Skipping monitoring/alerting in MVP
- Premature optimization before measuring
- Dual-write without transactional outbox
- Assuming global order in partitioned systems

## Interview Q&A (Senior Depth)

**Q1: Walk me through the high-level architecture for {{title}}.**
**A:** [Key components, data flow, boundaries. Use back-of-envelope to justify scale.]

**Q2: What are the key trade-offs in this design?**
**A:** [CAP, Latency vs Throughput, Build vs Buy, SQL vs NoSQL, Sync vs Async. Cite specific choices.]

**Q3: How does this scale to 10x traffic?**
**A:** [Stateless services, sharding, read replicas, caching layers, async processing via message queues. Identify bottlenecks.]

**Q4: What happens when [critical component] fails?**
**A:** [Retries, circuit breakers, fallback, graceful degradation, data recovery, replay.]

**Q5: How do you monitor and debug this in production?**
**A:** [RED metrics: rate, errors, duration. USE metrics: utilization, saturation, errors. Structured logging, correlation IDs. SLO-based alerting.]

## Flashcards (Spaced Repetition)

#flashcard
**Q:** What is the core pattern for {{title}}? :: **A:** [Key algorithm/architecture] #flashcard

#flashcard
**Q:** When do you use {{title}}? :: **A:** [Trigger scenarios] #flashcard

#flashcard
**Q:** Key trade-off in {{title}}? :: **A:** [Main trade-off] #flashcard

#flashcard
**Q:** Scale bottleneck for {{title}}? :: **A:** [Primary bottleneck] #flashcard

## Practice Tasks (Tasks Plugin)
- [ ] Explain the architecture from memory 📅 {{date:YYYY-MM-DD, +1}}
- [ ] Draw the system diagram without looking 📅 {{date:YYYY-MM-DD, +3}}
- [ ] Answer all Interview Q&A aloud 📅 {{date:YYYY-MM-DD, +7}}
- [ ] Review flashcards (Spaced Repetition) 📅 {{date:YYYY-MM-DD, +1}}

```tasks
not done
path includes {{file.folder}}
sort by due
limit 10
```

## Related
- [[Architect/03_Architecture-Styles/README|Architecture Styles]]
- [[Architect/08_NonFunctional-Ops/README|Non-Functional Requirements]]
- [[Architect/07_Integration-APIs/README|Integration Patterns]]

## ✅ Completion Checklist
- [ ] Intent written (one sentence + key term in **bold**)
- [ ] Why it Matters filled (interview signal, production impact, architecture force)
- [ ] Diagram created (Excalidraw or Mermaid)
- [ ] Problems section complete (requirements, constraints, API)
- [ ] Code example added (Java 25 / Spring Boot 3.5)
- [ ] Trade-offs table filled (all 5 dimensions)
- [ ] Pitfalls listed (5+ items)
- [ ] Interview Q&A answered (all 5 questions with senior depth)
- [ ] Flashcards created (10+ cards with #flashcard syntax)
- [ ] Practice tasks scheduled (Tasks plugin)

```dataviewjs
const page = dv.current();
const criteria = page.completion_criteria || {};
const done = Object.values(criteria).filter(v => v === true).length;
const total = Object.keys(criteria).length;
dv.paragraph(`**Progress: ${done}/${total} (${Math.round(done/total*100)}%)**`);
```

---

*Category: {{category}} • Part of [[README|Architect MOC]]*