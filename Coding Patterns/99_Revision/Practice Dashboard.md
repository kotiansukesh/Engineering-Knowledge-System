---
title: Practice Dashboard
type: dashboard
category: Coding Patterns/99_Revision
tags:
  - dashboard
  - dataview
  - tasks
---

# Practice Dashboard

> Operational home for the adaptive training loop.

## Mastery overview

~~~dataview
TABLE WITHOUT ID
  mastery as "Mastery",
  count(rows) as "Patterns"
FROM "Coding Patterns"
WHERE type = "pattern"
GROUP BY mastery
SORT mastery
~~~

## Due / stale patterns

~~~dataview
TABLE WITHOUT ID
  file.link as "Pattern",
  domain as "Domain",
  mastery as "Mastery",
  recognition_score as "Recognition",
  implementation_score as "Implementation",
  next_review as "Next review"
FROM "Coding Patterns"
WHERE type = "pattern" AND (next_review = null OR date(next_review) <= date(today))
SORT date(next_review) ASC
~~~

## Weak recognition

~~~dataview
TABLE WITHOUT ID
  file.link as "Pattern",
  recognition_score as "Recognition",
  implementation_score as "Implementation",
  attempts as "Attempts",
  hint_count as "Hints"
FROM "Coding Patterns"
WHERE type = "pattern" AND recognition_score < 4
SORT recognition_score ASC, pattern ASC
~~~

## Weak implementation

~~~dataview
TABLE WITHOUT ID
  file.link as "Pattern",
  recognition_score as "Recognition",
  implementation_score as "Implementation",
  avg_time_minutes as "Avg min"
FROM "Coding Patterns"
WHERE type = "pattern" AND implementation_score < 4
SORT implementation_score ASC, pattern ASC
~~~

## Recurring failures

~~~dataview
TABLE WITHOUT ID
  failure_category as "Failure",
  count(rows) as "Occurrences"
FROM "Coding Patterns"
WHERE type = "mistake"
GROUP BY failure_category
SORT count(rows) DESC
~~~

## Open tasks

~~~tasks
not done
path includes Coding Patterns
sort by due
group by filename
limit 30
~~~

## Review protocol

1. Pick one due or weak pattern.
2. Read only its Recognition section.
3. Attempt one blind problem.
4. Record recognition and implementation separately.
5. Log the first failure category.
6. Choose the next interval using [[00 - Adaptive Review Engine]].
7. Re-test in a mixed set before promoting mastery.

## Mastery scale

| Level | Meaning |
|---|---|
| learn | Understand the concept |
| guided | Can solve with pattern known |
| blind | Can recognize without hint |
| mixed | Can distinguish among competing patterns |
| mastered | Can recognize, prove, implement and adapt |
