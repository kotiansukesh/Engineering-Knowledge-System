---
title: "<% tp.file.title %>"
type: pattern
pattern: <% await tp.system.prompt('Pattern number') %>
domain: "<% await tp.system.prompt('Domain') %>"
category: "Coding Patterns/<% await tp.system.prompt('Folder') %>"
advanced: false
mastery: learn
recognition_score: 0
implementation_score: 0
attempts: 0
successful_attempts: 0
recognition_attempts: 0
recognition_successes: 0
avg_time_minutes:
hint_count: 0
last_attempt:
last_success:
failure_category:
difficulty: Medium
leetcode: []
created: "<% tp.date.now('YYYY-MM-DD') %>"
reviewed:
next_review: "<% tp.date.now('YYYY-MM-DD', 7) %>"
tags:
  - pattern/<% await tp.system.prompt('Tag') %>
---

# <% tp.file.title %>

> **Purpose:** one reusable reasoning technique, not a collection of copied solutions.

## Recognition

### Think of this pattern when
- 

### Strong signals
- 

### Do not infer it from
- 

## Invariant

> State exactly what remains true after each iteration, recursive call, or state transition.

## Mental model

Explain the pattern in 2–4 sentences without implementation details.

## Core template

~~~java
// Minimal Java template.
// Keep the invariant visible.
~~~

## Variants

| Variant | Use when | What changes |
|---|---|---|
| | | |

## When to use

- 
- 
- 

## When NOT to use

- 
- 
- 

## Complexity

| Metric | Cost |
|---|---|
| Time | |
| Space | |

## Canonical problems

| LeetCode | Problem | Difficulty | Recognition cue |
|---:|---|---|---|
| | | | |

## Pattern combinations

| Primary | Secondary | Why they combine |
|---|---|---|
| | | |

## Edge cases

- 
- 
- 

## Common mistakes

- 
- 
- 

## Interview proof

**Why is the main state transition safe?**

**What work does the invariant eliminate?**

**What alternative would you use if a constraint changed?**

## Flashcards

#flashcard
**Q:** What is the strongest recognition signal? :: **A:** 

#flashcard
**Q:** What is the invariant? :: **A:** 

#flashcard
**Q:** When should this pattern NOT be used? :: **A:** 

## Review evidence\n\nUpdate attempts and scores after every meaningful blind or mixed attempt. Use [[00 - Adaptive Review Engine]] to choose the next interval.\n\n## Review tasks

- [ ] Explain the recognition signals from memory 📅 <% tp.date.now('YYYY-MM-DD', 1) %>
- [ ] Write the core template from memory 📅 <% tp.date.now('YYYY-MM-DD', 3) %>
- [ ] Solve one unseen problem without hints 📅 <% tp.date.now('YYYY-MM-DD', 7) %>
- [ ] Explain the invariant aloud 📅 <% tp.date.now('YYYY-MM-DD', 14) %>

## Visual

Use an Excalidraw diagram only when the algorithm is spatial or state-transition heavy. Prefer Mermaid for simple flow.

## Related

[[Patterns Index]] · [[00 - Pattern Decision Tree]] · [[00 - Blind Practice]] · [[00 - Mistake Log]]
