---
title: Coding Patterns Revision
type: moc
category: Coding Patterns/99_Revision
tags:
  - moc
  - revision
---

# Revision

This folder contains the **operational layer** for coding-pattern mastery.

## Dashboards

- Practice Dashboard
- Study-Plan

## Workflow

**Due pattern → Recognition drill → Blind problem → Mistake log → Update mastery → Schedule review**

## Live pattern queue

~~~dataview
TABLE WITHOUT ID
  file.link as "Pattern",
  mastery as "Mastery",
  recognition_score as "Recognition",
  next_review as "Next review"
FROM "Coding Patterns"
WHERE type = "pattern"
SORT date(next_review) ASC
~~~

## Review tasks

~~~tasks
not done
path includes Coding Patterns
sort by due
group by filename
limit 30
~~~
