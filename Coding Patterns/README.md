---
title: Coding Patterns
type: moc
category: Coding Patterns
tags:
  - moc
  - dsa
  - interview-prep
  - pattern-recognition
---

# Coding Patterns

> **Learn the reasoning. Recognize the pattern. Implement from memory. Prove the invariant.**

This vault is a **pattern-training system**, not a LeetCode archive.

## Start here

1. [[Patterns Index]] — canonical pattern catalog and live mastery status.
2. [[00 - Pattern Decision Tree]] — choose candidate patterns from problem shape.
3. [[00 - Pattern Confusion Matrix]] — distinguish commonly confused patterns.
4. [[Canonical Problems]] — compact problem index without copied statements.
5. [[99_Revision/Practice Dashboard|Practice Dashboard]] — what needs attention now.
6. [[00 - Blind Practice]] — recognition without pattern hints.
7. [[00 - Mistake Log]] — reasoning failures and recurring gaps.
8. [[99_Revision/Study-Plan|Study Plan]] — progression from learning to mastery.

## Mastery model

**Learn → Guided → Blind → Mixed → Mastered**

A solved problem is evidence of practice, not automatically evidence of pattern mastery.

A pattern is mastered when you can:

- recognize it on an unseen problem;
- state the invariant before coding;
- implement the core template from memory;
- explain time and space complexity;
- explain when it does not apply;
- handle a meaningful variation or pattern combination.

## Live status

~~~dataview
TABLE WITHOUT ID
  mastery as "Mastery",
  count(rows) as "Patterns"
FROM "Coding Patterns"
WHERE type = "pattern"
GROUP BY mastery
SORT mastery
~~~

### Patterns needing attention

~~~dataview
TABLE WITHOUT ID
  file.link as "Pattern",
  domain as "Domain",
  mastery as "Mastery",
  recognition_score as "Recognition",
  next_review as "Next review"
FROM "Coding Patterns"
WHERE type = "pattern" AND (next_review = null OR date(next_review) <= date(today) OR recognition_score < 4)
SORT recognition_score ASC, date(next_review) ASC
LIMIT 15
~~~

### Open tasks

~~~tasks
not done
path includes Coding Patterns
sort by due
limit 15
~~~

## Architecture

| Layer | Responsibility |
|---|---|
| Pattern notes | Durable knowledge and invariants |
| Canonical Problems | Small problem set for application |
| Blind Practice | Recognition under uncertainty |
| Confusion Matrix | Resolve competing pattern candidates |
| Mistake Log | Feedback loop |
| Practice Dashboard | Dataview + Tasks control plane |
| Study Plan | Mastery progression |
| Templates | Templater-driven note creation |

## Plugin roles

- **Dataview:** dashboards, indexes, due/weak-pattern queries.
- **Tasks:** actionable review/checklist work.
- **Templater:** consistent pattern and practice-log creation.
- **Excalidraw:** only for spatial/state-heavy explanations where a visual adds information; Mermaid remains preferable for simple flows.

## Design rule

> **Keep knowledge in notes. Keep state in frontmatter. Keep queries in Dataview. Keep actions in Tasks.**

That separation keeps the vault readable while allowing Obsidian to render the operational layer dynamically.
