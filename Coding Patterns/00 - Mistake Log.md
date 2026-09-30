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

## Failure taxonomy

### Recognition

- Pattern miss
- Wrong competing pattern
- Keyword anchoring

### Reasoning

- Wrong invariant
- Wrong state definition
- Missing proof
- Complexity miss
- Constraint ignored
- Premature optimization

### Implementation

- Boundary / off-by-one
- Wrong data structure
- Mutation / aliasing
- Edge-case failure
- Java API misuse
- Integer overflow
- Comparator bug
- Recursion-depth issue

## Entry fields

Use _templates/Mistake-Log-Template for new entries.

Minimum metadata:

~~~yaml
type: mistake
pattern: ""
problem_id:
failure_category: ""
severity: medium
review_date:
~~~

## Promotion rules

- Twice → add a flashcard to the pattern note.
- Three times → add a When NOT to Use rule.
- Repeated confusion between two patterns → update the Confusion Matrix.
- Repeated Java-specific failure → update the Java Quality Layer.
- Pure syntax bug → fix it; do not expand the pattern note.

## Review queue

~~~dataview
TABLE WITHOUT ID
  file.link as "Entry",
  pattern as "Pattern",
  problem_id as "Problem",
  failure_category as "Category",
  severity as "Severity",
  review_date as "Review"
FROM "Coding Patterns"
WHERE type = "mistake"
SORT date(review_date) ASC
~~~
