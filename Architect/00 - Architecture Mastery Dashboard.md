---
title: Architecture Mastery Dashboard
type: dashboard
category: Architect
tags: [architecture, mastery, dataview]
---

# Architecture Mastery Dashboard

> Measure demonstrated capability, not note count.

## Interview evidence

~~~dataview
TABLE WITHOUT ID
  file.link as "Session",
  requirements_score as "Requirements",
  estimation_score as "Estimation",
  design_score as "Design",
  reliability_score as "Reliability",
  tradeoff_score as "Trade-offs",
  communication_score as "Communication",
  review_date as "Review"
FROM "Architect"
WHERE type = "interview"
SORT date(review_date) DESC
LIMIT 20
~~~

## Due practice

~~~dataview
TABLE WITHOUT ID
  file.link as "Note",
  mastery_stage as "Stage",
  difficulty as "Difficulty",
  "sr-due" as "Due"
FROM "Architect"
WHERE type IN ("note", "architecture-problem", "practice") AND "sr-due" != null
SORT date("sr-due") ASC
LIMIT 30
~~~

## Assessment evidence

~~~dataview
TABLE WITHOUT ID
  file.link as "Assessment",
  skill as "Skill",
  score as "Score",
  date as "Date"
FROM "Architect"
WHERE type = "assessment" AND skill
SORT date(date) DESC
LIMIT 30
~~~

## Rule

Completion is activity. Mastery requires evidence from independent design, failure reasoning, trade-off defense, review and redesign.
