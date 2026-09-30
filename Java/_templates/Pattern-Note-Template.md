---
title: "{{title}}"
category: "Java/06_Design-Patterns/{{category_type}}"
tags:
- design-patterns
- {{category_type}}
- {{pattern_name}}
pattern: {{pattern_name}}
source: https://refactoring.guru/design-patterns/{{pattern_name}}
created: "{{date:YYYY-MM-DD}}"
difficulty: Medium
completed: false
reviewed: "2026-09-29"
sr-due: "2026-10-06"
excalidraw: ""
type: note
---

# {{title}} *Also Known as: {{alias}}*

> Category: {{category_type^}} • Source: [Refactoring.Guru , {{title}}](https://refactoring.guru/design-patterns/{{pattern_name}}) • Part of [[Java/README|Java MOC]] → [[06_Design-Patterns/README|Design Patterns MOC]]

## Why it Matters

One sentence: what problem does this solve? Define the **key term** in **bold**.

## Diagram

```mermaid
classDiagram
    class Client
    class {{title.replace(" ", "")}} {
        <<interface>>
        +operation()
    }
    class Concrete{{title.replace(" ", "")}} {
        +operation()
    }
    {{title.replace(" ", "")}} <|.. Concrete{{title.replace(" ", "")}}
    Client --> {{title.replace(" ", "")}} : uses
```

## Code

```java
// Java 25: records, sealed interfaces, pattern matching, virtual threads
public class {{title.replace(" ", "")}}Demo {

    // Sealed interface for the pattern contract
    sealed interface {{title.replace(" ", "")}} permits Concrete{{title.replace(" ", "")}} {
        void operation();
    }

    // Immutable record implementation
    record Concrete{{title.replace(" ", "")}}(/* dependencies */) implements {{title.replace(" ", "")}} {
        public void operation() {
            // Core algorithm here
        }
    }

    // Context/client using the pattern
    static class Context {
        private final {{title.replace(" ", "")}} strategy;
        Context({{title.replace(" ", "")}} s) { strategy = s; }
        void execute() { strategy.operation(); }
    }

    public static void main(String[] args) {
        var impl = new Concrete{{title.replace(" ", "")}}(/* args */);
        var ctx = new Context(impl);
        ctx.execute();
    }
}
```

The demo proves the pattern contract is fulfilled with immutable, sealed implementations.

## When to Use / When NOT

| **Use When** | **Avoid When** |
|--------------|----------------|
| - Trigger keywords: [pattern-specific triggers] | - Over-engineering simple cases |
| - Constraints: [constraints where pattern shines] | - Premature optimization |
| - Pattern signature: [recognizable structure] | - When standard library suffices |

## Trade-offs

| Dimension | This Approach | Alternative |
|-----------|---------------|-------------|
| Complexity | [complexity] | [alt complexity] |
| Performance | [performance] | [alt performance] |
| Readability | [readability] | [alt readability] |
| Testability | [testability] | [alt testability] |

## Vs Table

| Aspect | This | Alternative | Decision Rule |
|--------|------|-------------|---------------|
| [aspect] | [this] | [alt] | [rule] |

## Pitfalls

- Common mistake 1 → Fix
- Common mistake 2 → Fix

## Interview Q&A (Senior Depth)

**Q1. What is the core insight of this pattern, and why does it work?**
**A:** In 2–3 sentences. Connect the *why* to the language/runtime invariant.

**Q2. When would you choose an alternative over this pattern?**
**A:** Cite concrete constraints and name the alternative.

**Q3. How does this change with virtual threads / Project Loom?**
**A:** Explain the impact on concurrency model.

**Q4. Walk me through a non-obvious problem that reduces to this pattern.**
**A:** Describe the reduction step-by-step.

**Q5. What is the memory/performance implication at scale?**
**A:** Discuss heap, GC, JIT interaction.

## Flashcards (Spaced Repetition)

#flashcard
**Q:** What is the trigger keyword for {{title}}? :: **A:** [trigger keywords] #flashcard

#flashcard
**Q:** Time/space complexity of {{title}}? :: **A:** Time: O(), Space: O() #flashcard

#flashcard
**Q:** When do you NOT use {{title}}? :: **A:** [anti-pattern scenarios] #flashcard

#flashcard
**Q:** Core Java 25 snippet for {{title}}? :: **A:** `sealed interface ... permits ... record ... implements ... {}` #flashcard

## Practice Tasks (Tasks Plugin)

- [ ] Restate the intent from memory 📅 {{date:YYYY-MM-DD, +1}}
- [ ] Code the snippet without looking 📅 {{date:YYYY-MM-DD, +3}}
- [ ] Answer all Interview Q&A aloud 📅 {{date:YYYY-MM-DD, +7}}
- [ ] Review flashcards (Spaced Repetition) 📅 {{date:YYYY-MM-DD, +1}}

```tasks
not done
path includes {{file.folder}}
sort by due
limit 10
```

## Related

- [[README|Java MOC]]
- [[Java/_templates/README|{{file.folder.split('/').pop()}} Folder]]
- Related pattern 1
- Related pattern 2

---

*Category: {{category_type^}} • Tags: design-patterns • Source: refactoring.guru*

## Problem

[Describe the concrete problem this pattern solves with a realistic scenario]

## Solution

[Explain the pattern's solution structure and key participants]

## When not to use

| Instead | Use |
|---------|-----|
| [scenario] | [alternative] |
| [scenario] | [alternative] |
