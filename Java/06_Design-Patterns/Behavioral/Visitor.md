---
title: "Visitor"
category: "Java/06_Design-Patterns/Behavioral"
tags:
- design-patterns
- behavioral
- visitor
pattern: visitor
source: https://refactoring.guru/design-patterns/visitor
created: "2026-09-29"
difficulty: Medium
completed: false
reviewed: "2026-09-29"
sr-due: "2026-10-06"
excalidraw: ""
type: concept
---

# Visitor

> Category: Behavioral • Source: [Refactoring.Guru , Visitor](https://refactoring.guru/design-patterns/visitor) • Part of [[Java/README|Java MOC]] → Design Patterns MOC

## Why it Matters

Separates an **algorithm** from the **objects it operates on**.

## Diagram

```mermaid
classDiagram
 class Shape {
 <<interface>>
 +accept(v)
 }
 class Dot
 class Circle
 class Visitor {
 <<interface>>
 +visit(Dot)
 +visit(Circle)
 }
 class XmlExport
 Shape <|.. Dot
 Shape <|.. Circle
 Visitor <|.. XmlExport
 Shape ..> Visitor : accept
```

## Code

```java
// Java 25: records, sealed interfaces, pattern matching, virtual threads, Compact Object Headers
public class VisitorDemo {
 interface Shape { String accept(Visitor v); }
 interface Visitor { String visit(Dot d); String visit(Circle c); }
 // Double dispatch: each element calls back the overload for its own type
 record Dot(int x) implements Shape { public String accept(Visitor v) { return v.visit(this); } }
 record Circle(int r) implements Shape { public String accept(Visitor v) { return v.visit(this); } }
 static class XmlExport implements Visitor {
 public String visit(Dot d) { return "<dot x=\"" + d.x() + "\"/>"; }
 public String visit(Circle c) { return "<circle r=\"" + c.r() + "\"/>"; }
 }
 public static void main(String[] args) {
 java.util.List<Shape> shapes = java.util.List.of(new Dot(1), new Circle(5));
 var export = new XmlExport();
 for (var s : shapes) System.out.println(s.accept(export)); // => <dot x="1"/>, <circle r="5"/>
 }
}
```

The demo proves the pattern contract is fulfilled with immutable, sealed implementations.

## When to Use / When NOT

| **Use When** | **Avoid When** |
|--------------|----------------|
| New operations are added often to a stable element set (export, validate, price). |  |
| Elements must stay untouched while operations grow. |  |
| Double dispatch is acceptable to recover concrete types. |  |

## Trade-offs

| Dimension | This Approach | Alternative |
|-----------|---------------|-------------|
| Complexity | [complexity] | [alt complexity] |
| Performance | [performance] | [alt performance] |
| Readability | [readability] | [alt readability] |
| Testability | [testability] | [alt testability] |

## Vs Table

| Pattern | Use when |
|---------|----------|
| Visitor | Add operation without touching elements |
| Strategy | Swap one algorithm |
| Switch visitor | Lightweight alternative when sealed |

## Pitfalls

- Adding element types breaks every visitor , budget for it or use sealed switches.
- Visitors accumulating mutable cross-element state (non-reentrant).
- Exposing element internals through oversized visitor interfaces.

## Interview Q&A (Senior Depth)

**Q: Do you still need classic visitor?**

Only when visitors accumulate state or elements are open. For stable sealed hierarchies a switch visitor is shorter.

**Q: What is double dispatch, and what trade-off does Visitor make?**

accept() re-dispatches on the element's runtime type so the matching visit overload runs , two dispatches (accept, then visit) select the operation; adding new operations is cheap (new visitor), but adding a new element type forces edits to every visitor.

**Q: What happens when you add a new element type?**

You touch the Visitor interface and every visitor implementation , that is the pattern's core trade-off, inverted from subclassing. Sealed hierarchies plus pattern-matching switches make the blast radius compiler-checked, which is why modern Java often skips classic Visitor.

: Do you still need classic visitor?:: Only when visitors accumulate state or elements are open. For stable sealed hierarchies a switch visitor is shorter. **Q: What is double dispatch, and what trade-off does Visitor make?** accept() re-dispatches on the element's runtime type so the matching visit overload runs , two dispatches (accept, then visit) select the operation; adding new operations is cheap (new visitor), but adding a new element type forces edits to every visitor. **Q:... #flashcard

## Flashcards (Spaced Repetition)

#flashcard
Behavioral • Source: [Refactoring.Guru , Visitor](https://refactoring.guru/design-patterns/visitor) • Part of [[Java/README|Java MOC]] → Design Patterns MOC

## Why it Matters

Separates an **algorithm** from the **objects it operates on**.

## Diagram

```mermaid
classDiagram
 class Shape {
 <<interface>>
 +accept(v)
 }
 class Dot
 class Circle
 class Visitor {
 <<interface>>
 +visit(Dot)
 +visit(Circle)
 }
 class XmlExport
 Shape <|.. Dot
 Shape <|.. Circle
 Visitor <|.. XmlExport
 Shape ..> Visitor : accept
```

## Code

```java
public class VisitorDemo {
 interface Shape { String accept(Visitor v); }
 interface Visitor { String visit(Dot d); String visit(Circle c); }
 // Double dispatch: each element calls back the overload for its own type
 record Dot(int x) implements Shape { public String accept(Visitor v) { return v.visit(this); } }
 record Circle(int r) implements Shape { public String accept(Visitor v) { return v.visit(this); } }
 static class XmlExport implements Visitor {
 public String visit(Dot d) { return "<dot x=\"" + d.x() + "\"/>"; }
 public String visit(Circle c) { return "<circle r=\"" + c.r() + "\"/>"; }
 }
 public static void main(String[] args) {
 java.util.List<Shape> shapes = java.util.List.of(new Dot(1), new Circle(5));
 var export = new XmlExport();
 for (var s : shapes) System.out.println(s.accept(export)); // => <dot x="1"/>, <circle r="5"/>
 }
}
```
The demo proves separation: XML export is added as a new visitor without touching Dot or Circle, and each shape dispatches to its own overload.

## When to use / not

- New operations are added often to a stable element set (export, validate, price).
- Elements must stay untouched while operations grow.
- Double dispatch is acceptable to recover concrete types.

## Trade-offs

Use when you add many operations over a stable element set. The sealed switch version is simpler when you own the hierarchy; keep the classic visitor when visitors need mutable accumulation or the set is open.

## Vs

| Pattern | Use when |
|---------|----------|
| Visitor | Add operation without touching elements |
| Strategy | Swap one algorithm |
| Switch visitor | Lightweight alternative when sealed |

## Pitfalls

- Adding element types breaks every visitor , budget for it or use sealed switches.
- Visitors accumulating mutable cross-element state (non-reentrant).
- Exposing element internals through oversized visitor interfaces.

## Interview q&a

**Q: Do you still need classic visitor?**

Only when visitors accumulate state or elements are open. For stable sealed hierarchies a switch visitor is shorter.

**Q: What is double dispatch, and what trade-off does Visitor make?**

accept() re-dispatches on the element's runtime type so the matching visit overload runs , two dispatches (accept, then visit) select the operation; adding new operations is cheap (new visitor), but adding a new element type forces edits to every visitor.

**Q: What happens when you add a new element type?**

You touch the Visitor interface and every visitor implementation , that is the pattern's core trade-off, inverted from subclassing. Sealed hierarchies plus pattern-matching switches make the blast radius compiler-checked, which is why modern Java often skips classic Visitor.

: Do you still need classic visitor?:: Only when visitors accumulate state or elements are open. For stable sealed hierarchies a switch visitor is shorter. **Q: What is double dispatch, and what trade-off does Visitor make?** accept() re-dispatches on the element's runtime type so the matching visit overload runs , two dispatches (accept, then visit) select the operation; adding new operations is cheap (new visitor), but adding a new element type forces edits to every visitor. **Q:... #flashcard

## Practice Tasks (Tasks Plugin)

- [ ] Restate the intent from memory 📅 {date:YYYY-MM-DD, +1}
- [ ] Code the snippet without looking 📅 {date:YYYY-MM-DD, +3}
- [ ] Answer all Interview Q&A aloud 📅 {date:YYYY-MM-DD, +7}
- [ ] Review flashcards (Spaced Repetition) 📅 {date:YYYY-MM-DD, +1}

```tasks
not done
path includes {file.folder}
sort by due
limit 10
```

## Related

Strategy • Interpreter • Composite

---

*Category: Behavioral • Tags: design-patterns • Source: refactoring.guru*

## Problem

Exporting shapes to xml should not add export methods to every shape class.

## Solution

Keep shapes clean and put the operation in a visitor. With sealed shapes, a switch visitor does the same without double dispatch.

## When not to use

| Instead | Use |
|---------|-----|
| Elements change often | Sealed switch / pattern matching |
| One swappable algorithm | Strategy |
| Small stable hierarchy | Instanceof chains |
