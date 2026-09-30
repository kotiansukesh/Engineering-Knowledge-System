---
title: Mistake Log
type: log
category: Coding Patterns
tags:
  - mistakes
  - review
---

# Mistake Log

> Record reasoning failures. Do not turn every syntax error into documentation.

## Failure categories

- Pattern miss
- Wrong invariant
- Wrong state definition
- Boundary / off-by-one
- Wrong data structure
- Complexity miss
- Premature optimization
- Mutation / aliasing
- Missing proof
- Edge-case failure

## Entry template

~~~markdown
---
type: mistake
pattern: ""
failure_category: ""
review_date: ""
---

# YYYY-MM-DD — Problem

**What I thought:**  
**What was actually true:**  
**Invariant I missed:**  
**Fix:**  
**Would this mistake recur?** Yes / No
~~~

## Promotion rules

- Twice → add a flashcard to the pattern note.
- Three times → add a When NOT to Use rule.
- Repeated confusion between two patterns → add a comparison to both.
- Pure syntax bug → fix it; do not expand the pattern note.

## Review queue

~~~dataview
TABLE WITHOUT ID
  file.link as "Entry",
  pattern as "Pattern",
  failure_category as "Category",
  review_date as "Review"
FROM "Coding Patterns"
WHERE type = "mistake"
SORT date(review_date) ASC
~~~
