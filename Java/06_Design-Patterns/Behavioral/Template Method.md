---
title: "Template Method"
category: Design-Patterns
group: Behavioral
tags: [design-patterns, behavioral, template-method]
pattern: template-method
source: "https://refactoring.guru/design-patterns/template-method"
created: 2026-09-02
updated: 2026-09-04
difficulty: Medium
completed: false
reviewed: ""
sr-due: ""
problems-solved: []
problems-solved-dates: {}
excalidraw: ""
---
# Template Method

> Category: Behavioral • Source: [Refactoring.Guru , Template Method](https://refactoring.guru/design-patterns/template-method) • Part of [[Java/README|Java MOC]] → [[06_Design-Patterns/README|Design Patterns MOC]]

## Why it Matters

Defines the **skeleton of an algorithm** and lets **subclasses fill in the details**.

## Diagram

```mermaid
classDiagram
 class GameAI {
 +playTurn()*
 +collect()
 +attack()
 }
 class OrcAI
 class ElfAI
 GameAI <|-- OrcAI
 GameAI <|-- ElfAI
```

## Code

```java
public class TemplateMethodDemo {
 // Skeleton is final in the base; subclasses override only the steps
 static abstract class GameAI {
 final void playTurn() { collect(); attack(); }
 abstract void collect();
 abstract void attack();
 }
 static class OrcAI extends GameAI {
 void collect() { System.out.println("orc mines gold"); } // => orc mines gold
 void attack() { System.out.println("orc charges"); } // => orc charges
 }
 static class ElfAI extends GameAI {
 void collect() { System.out.println("elf gathers mana"); } // => elf gathers mana
 void attack() { System.out.println("elf shoots arrows"); } // => elf shoots arrows
 }
 public static void main(String[] args) {
 GameAI orc = new OrcAI(); GameAI elf = new ElfAI();
 orc.playTurn(); elf.playTurn();
 }
}
```
The demo proves the fixed skeleton: both races run collect-then-attack in the same order while supplying their own step behavior.

## When to use / not

- An algorithm's skeleton is fixed but steps vary (collect → attack).
- Skeleton invariants must be protected from subclasses (final template).
- A few closely related variants share most of the flow.

## Trade-offs

Use when you have a fixed sequence with varying parts. It keeps the order in one place and avoids duplication. In Java, a single abstract class is enough; you do not need a deep hierarchy.

## Vs

| Pattern | Use when |
|---------|----------|
| Template method | Fixed skeleton, subclass steps |
| Strategy | Whole algorithm swapped |
| Factory method | Creation step is the variable part |

## Pitfalls

- Non-final template letting subclasses reorder the skeleton.
- Fragile base class: base changes break silent subclass assumptions.
- Deep inheritance where composition + Strategy would flex better.

## Interview q&a

**Q: When do you pick composition over template method?**

When steps vary a lot or you want to swap without inheritance. Template method ties you to a class hierarchy.

**Q: Template Method vs Strategy?**

Template Method fixes the algorithm skeleton via inheritance and varies individual steps; Strategy swaps the entire algorithm via composition, so prefer Strategy when the whole behavior (not just steps) must change at runtime.

**Q: Why must the template method be final?**

Final protects the skeleton invariant , the order and presence of steps , that all subclasses rely on. Subclasses customize via abstract steps and boolean hooks, never by reordering the algorithm; an overridable template is just a suggestion, not a pattern.

: When do you pick composition over template method?:: When steps vary a lot or you want to swap without inheritance. Template method ties you to a class hierarchy. **Q: Template Method vs Strategy?** Template Method fixes the algorithm skeleton via inheritance and varies individual steps; Strategy swaps the entire algorithm via composition, so prefer Strategy when the whole behavior (not just steps) must change at runtime. **Q: Why must the template method be final?** Final protects the skeleton... #flashcard

## Related

[[06_Design-Patterns/Behavioral/Strategy|Strategy]] (swap whole algorithm) • [[06_Design-Patterns/Creational/Factory Method|Factory Method]] (creation step) • [[06_Design-Patterns/Behavioral/State|State]]

---
*Category: Behavioral • Tags: design-patterns • Source: refactoring.guru*

## Problem

Games run the same turn steps (collect, build, fight) with different behavior per race.

## Solution

Write a final template method that calls abstract steps. Subclasses override the steps, not the skeleton.

## When not to use

| Instead | Use |
|---------|-----|
| Swapping the whole algorithm | Strategy |
| Unrelated classes sharing steps | Composition + delegation |
| Creation step varies | Factory Method |
