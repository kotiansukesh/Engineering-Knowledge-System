---
title: SOLID , Summary & Field Guide
category: Java/02_OOP
tags:
- java
- oop
- solid
- design-principles
- summary
created: 2026-09-04
pattern: 16
difficulty: Medium
completed: false
reviewed: "2026-09-29"
sr-due: "2026-10-06"
excalidraw: ''
source: ''
type: concept
---

## Why it Matters

SOLID is five independent bets about where change hurts: SRP splits reasons to change, OCP keeps shipped code closed, LSP keeps substitutes honest, ISP keeps interfaces lean, DIP points dependencies at abstractions. Memorize the table; internalize the conflicts , principles collide, and judgment is picking the right loser.

## Diagram

```mermaid
flowchart LR
 SRP["SRP: one reason to change"] --> OCP["OCP: extend, don't edit"]
 OCP --> LSP["LSP: substitutes stay honest"]
 LSP --> ISP["ISP: lean role interfaces"]
 ISP --> DIP["DIP: depend on abstractions"]
```

## Code

```java
// All five in one design: LLD Coffee Vending. Run: java SolidSummary.java
interface Payment { void pay(int amt); } // DIP: machine depends on abstraction
record CardPayment(int amt) implements Payment { // OCP: new payment = new record, machine untouched
 public void pay(int a) { System.out.println("card " + a); }
}
interface Brewing { void brew(); } // ISP: role interface, not one fat Machine API
interface Restocking { void restock(); } // ISP again, separate client need
class Machine { // SRP: only orchestrates
 private final Payment payment;
 Machine(Payment p) { this.payment = p; } // DIP: injected, swappable, testable
 void order(int amt) { payment.pay(amt); } // LSP: any Payment subtype works here
}
void main() {
 new Machine(new CardPayment(499)).order(499); // one wiring line to swap providers
}
```
> SRP splits the reasons to change, OCP keeps shipped code closed, LSP keeps substitutes honest, ISP keeps interfaces lean, DIP points dependencies at abstractions.

## When to use / not

- Use SOLID as a **diagnostic** , the smell table answers "which principle is hurting?" in a review.
- Use it **early at boundaries** (persistence, external providers, payment, pricing) where change concentrates.
- NOT as five laws to apply everywhere , forcing SRP produces one-method classes, forcing OCP/DIP produces speculative frameworks.
- NOT when YAGNI/KISS has not yet been violated , principles are tools for *real* pain, not preemptive architecture.

## Trade-offs

| Aspect | SOLID-shaped code | Pragmatic-shaped code |
|---|---|---|
| Change cost | localized, one class per variant | quick today, compounding debt |
| Testability | inject fakes at seams | must boot real resources |
| Complexity | more types/interfaces | fewer moving parts |
| Rule | at volatility boundaries | for stable, local, one-off code |

The payoff is not "all five everywhere" , it is applying each principle where its violation actually hurts.

## Pitfalls

- **Ranking** the principles ("which matters most?") , they are independent bets; SRP enables the rest, DIP is the most probed in interviews.
- Applying all five to **stable, one-off** code , ceremony with no return.
- Forgetting the conflicts , OCP vs YAGNI, SRP vs KISS, ISP vs DIP (interface explosion), LSP vs OCP (inheritance temptation).
- Treating SOLID as a **checklist** rather than a diagnostic for real pain.

## Interview q&a

**Q1: "Which SOLID principle matters most?"**
A: None in isolation , but SRP enables the rest (small cohesive classes are extendable, substitutable, injectable), and DIP is the one interviewers probe via "how would you test this without the DB?". Name the trade-off, don't rank them absolutely.

**Q2: "Show me SOLID in one design."**
A: Take LLD Coffee Vending: SRP (inventory vs recipe vs payment), OCP (new drink = new `Recipe`, no machine edit), LSP (any `PaymentStrategy` substitutes), ISP (brewing vs restocking interfaces), DIP (machine depends on `Recipe`/`Payment` abstractions). One system, five receipts.

: "Which SOLID principle matters most?"?:: A: None in isolation , but SRP enables the rest (small cohesive classes are extendable, substitutable, injectable), and DIP is the one interviewers probe via "how would you test this without the DB?". Name the trade-off, don't rank them absolutely. **Q2: "Show me SOLID in one design."** A: Take LLD Coffee Vending: SRP (inventory vs recipe vs payment), OCP (new drink = new `Recipe`, no machine edit), LSP (any `PaymentStrategy` substitutes), ISP... #flashcard

## Related

- SOLID-Single-Responsibility • SOLID-Open-Closed • SOLID-Liskov-Substitution • SOLID-Interface-Segregation • SOLID-Dependency-Inversion
- Law-of-Demeter • Pragmatic-Principles-DRY-YAGNI-KISS • Class-Relationships

---
*Category: Java/02_OOP*

# SOLID , Summary & Field Guide

> Part of [[README|Java MOC]] • `Java/02_OOP`

## All Five at a Glance

| # | Principle | One-liner | Violation smell | Note |
|---|---|---|---|---|
| S | Single Responsibility | One class, one reason to change | God class; `java.sql` + formatting + network imports in one file | Split by change-axis, not method count |
| O | Open-Closed | Open for extension, closed for modification | `switch` on type in every new feature | New behavior = new class, e.g. `PaymentStrategy` |
| L | Liskov Substitution | Subtypes must honor the base contract | Overridden method throws `UnsupportedOperationException`; strengthened preconditions | If it can't substitute, don't inherit , compose |
| I | Interface Segregation | Small role interfaces over fat ones | Forced empty `implement` stubs; one interface change breaks ten classes | Split `Worker` into `Eater`/`Sleeper` per client |
| D | Dependency Inversion | Depend on abstractions, not concretions | `new PostgresDb()` inside business logic; untestable without a DB | Inject the interface; wire the concrete at the edge |

## When They Conflict

- **OCP vs YAGNI/KISS.** OCP says "seam for extension", YAGNI says "don't build it yet". Rule: shape today's code so extension is *cheap* (small methods, depend on interfaces) but don't *build* the extension , reversible simplicity beats speculative frameworks. See Pragmatic-Principles-DRY-YAGNI-KISS.
- **SRP vs KISS (over-splitting).** one-method classes with a single caller are SRP theater , merging two responsibilities that change together is simpler and still single-axis. Split on the *second* divergent change, not the first suspicion.
- **ISP vs DIP (interface explosion).** too many micro-interfaces make injection sites unreadable. Group by genuine client role , one interface per *caller kind*, not per method.
- **LSP vs OCP (the tempting subclass).** extending via inheritance to satisfy OCP often breaks LSP (Square-Rectangle, read-only file). Prefer composition + Strategy for OCP; reserve inheritance for true is-a with identical contracts.
- **DIP vs pragmatism.** not every `new` needs injection , stable JDK types (`ArrayList`, `String`) and leaf value objects are fine concrete. Invert dependencies at volatility boundaries (DB, clock, network, policy).

## Which Pattern Proves Which Principle

| Principle | Proving pattern | Where it's drilled |
|---|---|---|
| SRP | Observer (notification out of domain) | SOLID-Single-Responsibility · LLD Logging, Task Management |
| OCP | Strategy (new behavior = new class) | SOLID-Open-Closed · LLD Vending, Coffee Vending |
| LSP | Factory + substitutable hierarchies | SOLID-Liskov-Substitution · LLD Parking (Vehicle sizes), Chess (pieces) |
| ISP | Role interfaces per client | SOLID-Interface-Segregation · LLD ATM, Splitwise |
| DIP | Inject abstractions at the edge | SOLID-Dependency-Inversion · LLD Ride Sharing (pricing), Pub-Sub |

## Vs , SOLID vs Pragmatic Principles

- **SOLID** tells you how to **shape** code: split reasons, extend without editing, keep substitutes honest, keep interfaces lean, invert dependencies.
- **DRY / YAGNI / KISS** tell you **when to stop**: one source of truth, nothing speculative, boring readable code.

They compete on purpose , OCP vs YAGNI, SRP vs KISS, judgment is picking the right loser per situation (see the conflict map above).
