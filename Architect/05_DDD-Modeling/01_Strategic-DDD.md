---
title: "Strategic DDD"
category: "DDD & Modeling"
tags: [ddd, strategic-design, ubiquitous-language, subdomain]
created: 2026-09-03
completed: false
---

# Strategic DDD

> **Intent:** Model the *business*, not the database: carve the problem space into subdomains, speak one ubiquitous language per context, and invest architecture effort where competitive advantage lives (core) while containing the rest (supporting/generic).

## 1. When to Use
- Any system where misunderstood requirements cost more than code — i.e. most backend systems.
- Precedes every other decision here: no strategic map → [[02_Bounded-Contexts]] and [[03_Microservices|service splits]] are guesses.
- Revisit when language diverges ("order" means 3 things in standup) — that's a missing boundary.

**Triage:** Core (differentiator — best engineers, custom code) · Supporting (necessary, buy-or-boring) · Generic (commodity — adopt, don't build: auth, billing, email).

## 2. Spring Example (language → code)

```java
// Ubiquitous language made executable: "an Order is placed with items,
// then paid, then shipped; a shipped Order cannot be cancelled."
class Order {
    void cancel() {
        if (status == SHIPPED) throw new DomainException("shipped orders cannot be cancelled");
        status = CANCELLED;
        register(new OrderCancelled(id)); // → [[05_Domain-Events]]
    }
}
// Subdomain triage visible in repo layout:
// com.shop.pricing (core, custom) vs com.shop.notification (supporting, thin) vs auth (generic, off-shelf)
```

Event Storming (the workshop): orange stickies = domain events, blue = commands, yellow = aggregates — walk the business flow before drawing boxes.

## 3. Pros / Cons
| Pros | Cons |
|---|---|
| Requirements encoded in code vocabulary (fewer translation bugs) | Upfront workshop time; feels slow |
| Focuses quality spend on core domain | Needs real domain-expert access — scarce |
| Stable seams for services/modules | Over-modelling generic subdomains wastes effort |

## 4. Vs
- **Vs data-first modelling:** data-first asks "what tables?"; strategic DDD asks "what business capabilities, and which matter?" Tables follow contexts, not vice versa.
- **Vs [[03_Architecture-Styles/06_Monolith-vs-Modular-Choice-Guide|tech-first splits]]:** split by subdomain value, not by class count.

## 5. Interview Q&A
**Q: How do you find subdomains?**
A: Event Storming + capability mapping with domain experts; cluster events that change together; confirm with change-frequency and language divergence.

**Q: What marks a core domain?**
A: Competitive edge + complex rules + high change rate. If you'd demo it to win a customer, it's core.

## 6. Pitfalls
- Ubiquitous language that only devs speak — experts must use (and correct) it.
- One shared "Order" object across contexts — see [[02_Bounded-Contexts]].
- Treating generic subdomains as interesting work (build auth yourself = delay).

## 7. Links
- [[02_Bounded-Contexts]] · [[03_Context-Mapping]] · [[04_Tactical-Aggregates-Entities-VO]]

<!-- Concept: strategy first — decide WHERE the complexity deserves to live before modelling HOW. -->
