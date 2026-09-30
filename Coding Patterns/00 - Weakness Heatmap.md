---
title: Weakness Heatmap
type: dashboard
category: Coding Patterns
tags:
  - dashboard
  - mastery
  - analytics
---

# Weakness Heatmap

> Track recognition and implementation separately.

~~~dataview
TABLE WITHOUT ID
  file.link as "Pattern",
  domain as "Domain",
  mastery as "Mastery",
  recognition_score as "Recognition",
  implementation_score as "Implementation",
  attempts as "Attempts",
  successful_attempts as "Successes",
  avg_time_minutes as "Avg min",
  hint_count as "Hints",
  next_review as "Next review"
FROM "Coding Patterns"
WHERE type = "pattern"
SORT recognition_score ASC, implementation_score ASC, attempts ASC
~~~

## Recognition risk

~~~dataview
TABLE WITHOUT ID
  file.link as "Pattern",
  recognition_score as "Recognition",
  mastery as "Mastery",
  last_attempt as "Last attempt"
FROM "Coding Patterns"
WHERE type = "pattern" AND (recognition_score < 4 OR mastery = "learn" OR mastery = "guided")
SORT recognition_score ASC, date(last_attempt) ASC
~~~

## Failure categories

~~~dataview
TABLE WITHOUT ID
  failure_category as "Failure",
  count(rows) as "Occurrences"
FROM "Coding Patterns"
WHERE type = "mistake"
GROUP BY failure_category
SORT count(rows) DESC
~~~

## Interpretation

- Low recognition + good implementation → recognition drills.
- Good recognition + low implementation → timed coding.
- Good correctness + high time → template fluency.
- Repeated same failure → update the pattern pitfall or When NOT to Use section.
