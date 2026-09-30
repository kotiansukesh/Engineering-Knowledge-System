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

> This is the operational home for the vault.

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
  next_review as "Next review"
FROM "Coding Patterns"
WHERE type = "pattern" AND (next_review = null OR date(next_review) <= date(today))
SORT date(next_review) ASC
~~~

## Weak recognition

~~~dataview
TABLE WITHOUT ID
  file.link as "Pattern",
  recognition_score as "Score",
  mastery as "Mastery"
FROM "Coding Patterns"
WHERE type = "pattern" AND recognition_score < 4
SORT recognition_score ASC, pattern ASC
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

1. Pick one due pattern.
2. Read only its Recognition section.
3. Attempt one blind problem.
4. Update recognition_score.
5. Complete the review task.
6. If the same mistake recurs, update the pattern note and Mistake Log.

## Mastery scale

| Level | Meaning |
|---|---|
| learn | Understand the concept |
| guided | Can solve with pattern known |
| blind | Can recognize without hint |
| mixed | Can distinguish among competing patterns |
| mastered | Can recognize, prove, implement and adapt |
