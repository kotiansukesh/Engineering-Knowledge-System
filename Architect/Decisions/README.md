---
title: Architecture Decisions
type: index
category: Architect/Decisions
tags:
  - adr
  - architecture
---

# Architecture Decisions

Use ADRs for decisions that have meaningful consequences, alternatives, or review triggers.

Create with [[Architect/_templates/ADR-Template]].

## Decision lifecycle

**Proposed → Accepted → Superseded / Rejected**

~~~dataview
TABLE WITHOUT ID
  file.link as "ADR",
  status as "Status",
  decision as "Decision",
  date as "Date",
  review_trigger as "Review trigger"
FROM "Architect/Decisions"
WHERE type = "adr"
SORT date DESC
~~~

## ADR quality bar

An ADR is incomplete if it does not explain:

- the constraints;
- the decision;
- alternatives considered;
- consequences;
- validation evidence;
- the condition that would make the decision obsolete.
