---
title: "{{title}}"
category: ""
tags: []
leetcode: []
created: "{{date:YYYY-MM-DD}}"
completed: false
reviewed: ""
sr-due: ""
difficulty: ""
source: ""
problems-solved: []
problems-solved-dates: {}
excalidraw: ""
weeks: ""
type: "note"
---

# {{title}}

> Part of [[README|MOC]] • `{{category}}` {{#if weeks}}• Weeks {{weeks}}{{/if}}
> 🎨 **Visual diagram:** Create Excalidraw drawing from template: `Cmd+P → Excalidraw: New from template → {{category.replace('/', ' ').replace('_', ' ').toLowerCase()}} Diagram`

## Intent
One sentence: what problem does this solve? Define the **key term** in **bold**.

## Why it Matters
- Where this appears in interviews (FAANG, senior vs. junior)
- Production impact (cost, latency, quality, maintainability)
- Senior signal: recognizing the *disguised* form of this pattern/concept

## Diagram
```mermaid
flowchart TD
    A["Input / Context"] --> B["Core Idea / Mechanism"]
    B --> C["Output / Result"]
    style B fill:#e8f5e9
```

{{#if leetcode.length}}
## Problems
> **Real problem statements from LeetCode.** After creating the note, run the "Fetch LeetCode Problems" script to populate this section with actual problem statements, examples, and tags.

{{#each leetcode}}
### {{this}}. Problem Title ({{difficulty}})
> [LeetCode {{this}}](https://leetcode.com/problems/{{this.toLowerCase().replace(/ /g, '-')}}/) • Tags: [auto-filled after fetch]

**Problem Statement:**
[Fetched from LeetCode GraphQL API]

**Examples:**
[Fetched from LeetCode]

---
{{/each}}
> 📊 **Track progress:** Add solved problem numbers to `problems-solved` array in frontmatter with date in `problems-solved-dates`. Set `sr-due` for spaced repetition.
{{/if}}

## Code / Example
```java
// Java 25: var, record, pattern matching for instanceof, SequencedCollection, virtual threads (if parallel), Compact Object Headers
// Core template for {{title}}

// Minimal runnable snippet — the artifact you can whiteboard
record {{title.replace(/\s+/g, '')}}(/* params */) {
    // factory or builder
    static {{title.replace(/\s+/g, '')}} of(/* params */) {
        // build logic
        return new {{title.replace(/\s+/g, '')}}(/* args */);
    }
    
    // key operation
    /* returnType */ keyMethod(/* params */) {
        // O(1) or O(n) logic
    }
}

// Example usage
void example() {
    var instance = {{title.replace(/\s+/g, '')}}.of(/* args */);
    var result = instance.keyMethod(/* args */);
}
```

### Concrete Example
- **Input:** 
- **Output:** 
- **Explanation:** 

## When to Use / When NOT
| **Use When** | **Avoid When** |
|--------------|----------------|
| - Trigger keywords: | - Data mutates frequently (use Segment Tree / Fenwick) |
| - Constraints: | - Single query (just loop) |
| - Pattern signature: | - Need min/max/gcd on range (use Sparse Table) |
| - Immutable data, repeated queries | - |

## Trade-offs
| Dimension | This Approach | Alternative A | Alternative B |
|-----------|---------------|---------------|---------------|
| Build     |               |               |               |
| Query     |               |               |               |
| Update    |               |               |               |
| Space     |               |               |               |
| Pick when |               |               |               |

## Vs Table
| Aspect | This | Alternative A | Alternative B | Decision Rule |
|--------|------|---------------|---------------|---------------|
| Query type |      |               |               |               |
| Mutability |      |               |               |               |
| Implementation |  |               |               |               |

## Pitfalls
- Off-by-one errors (leading-zero convention, inclusive/exclusive bounds)
- Overflow: use `long` for sums/counts
- Missing base case in hashmap (e.g., `count.put(0, 1)` for prefix sums)

## Interview Q&A (Senior Depth)

**Q1. What is the core insight of this pattern/concept, and why does it work?**
**A:** In 2–3 sentences. Connect the *why* to the data structure invariant or architectural principle.

**Q2. When would you choose an alternative over this pattern/concept?**
**A:** Cite concrete constraints (updates, query type, mutability, scale) and name the alternative.

**Q3. How does this pattern/concept change for streaming / mutable data / distributed systems?**
**A:** Explain the limitation and the exact data structure/architecture that replaces it.

**Q4. Walk me through a non-obvious problem that reduces to this pattern/concept.**
**A:** Describe the reduction step-by-step (e.g., "subarray sum = k → hashmap on prefix sums").

**Q5. What is the space optimization if the input is read-only and huge?**
**A:** Discuss in-place modification, bitset, or streaming variant.

## Flashcards (Spaced Repetition)

#flashcard
**Q:** What is the trigger keyword for {{title}}? :: **A:** [trigger keywords] #flashcard

#flashcard
**Q:** Time/space complexity of {{title}}? :: **A:** Time: O(), Space: O() #flashcard

#flashcard
**Q:** When do you NOT use {{title}}? :: **A:** [mutating data / single query / need min-max] #flashcard

#flashcard
**Q:** Core Java 25 snippet for {{title}}? :: **A:** `record ... { static of(...) {} keyMethod() {} }` #flashcard

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
- [[README|MOC]]
- [[{{file.folder}}/README|{{file.folder.split('/').pop()}} Folder]]

---

*Category: {{category}} • Part of [[README|MOC]] • Java 25*