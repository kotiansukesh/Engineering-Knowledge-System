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
2. [[00 - Pattern Decision Tree]] — reason from problem shape and constraints.
3. [[00 - Pattern Confusion Matrix]] — distinguish competing patterns.
4. [[00 - Pattern Recognition Lab]] — train recognition without coding.
5. [[Problem Bank]] — problem-level metadata and progression.
6. [[Canonical Problems]] — compact curated problem index.
7. [[00 - Mixed Pattern Sets]] — remove pattern hints.
8. [[99_Revision/Practice Dashboard]] — current review queue.
9. [[00 - Weakness Heatmap]] — recognition vs implementation gaps.
10. [[00 - Mistake Log]] — diagnose recurring failures.
11. [[00 - Adaptive Review Engine]] — evidence-driven review intervals.
12. [[99_Revision/Study-Plan|Study Plan]] — progression from learning to mastery.

## Mastery model

**Learn → Guided → Blind → Mixed → Mastered**

A solved problem is evidence of practice, not automatically evidence of pattern mastery.

A pattern is mastered when you can:

- recognize it on an unseen problem;
- state the invariant before coding;
- implement the core template from memory;
- explain time and space complexity;
- explain when it does not apply;
- handle a meaningful variation or pattern combination;
- reproduce the result in mixed practice.

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

## Patterns needing attention

~~~dataview
TABLE WITHOUT ID
  file.link as "Pattern",
  domain as "Domain",
  mastery as "Mastery",
  recognition_score as "Recognition",
  implementation_score as "Implementation",
  attempts as "Attempts",
  next_review as "Next review"
FROM "Coding Patterns"
WHERE type = "pattern" AND (next_review = null OR date(next_review) <= date(today) OR recognition_score < 4 OR implementation_score < 4)
SORT recognition_score ASC, implementation_score ASC, date(next_review) ASC
LIMIT 20
~~~

## Training loop

**Attempt → Recognize → Implement → Diagnose → Review → Re-test → Mastery**

| Layer | Responsibility |
|---|---|
| Pattern notes | Durable knowledge, invariants, templates |
| Problem Bank | Problem-level training state |
| Recognition Lab | Pattern identification under uncertainty |
| Mixed Sets | Competing-pattern recognition |
| Confusion Matrix | Resolve plausible alternatives |
| Mistake Log | Failure diagnosis |
| Adaptive Review | Next-review scheduling |
| Weakness Heatmap | Analytics and prioritization |
| Interview Mode | Timed integrated practice |
| Senior Trade-offs | Explain design choices and changed constraints |
| Java Quality Layer | Java-specific correctness/performance checks |
| Validator | Structural quality gate |

## Plugin roles

- **Dataview:** dashboards, indexes, due/weak-pattern queries.
- **Tasks:** actionable review work.
- **Templater:** consistent pattern, recognition, interview and mistake-log creation.
- **Excalidraw:** only for spatial/state-heavy explanations; Mermaid is preferable for simple flows.

## Design rule

> **Keep knowledge in notes. Keep state in frontmatter. Keep derived views in Dataview. Keep actions in Tasks. Validate the vault automatically.**

## Quality gate

Run:

~~~bash
python3 scripts/validate-vault.py
~~~

The validator checks wikilinks, forbidden relative links, table aliases, pattern metadata, duplicate problem IDs, and referenced vault paths.

13. [[00 - Difficulty Progression]] — increase uncertainty and variation, not just problem difficulty.


## Knowledge System Integration

- [[00 - Knowledge System/README|Knowledge System]] — shared learning model
- [[00 - Knowledge System/Cross Domain Map|Cross-Domain Map]] — transfer algorithmic reasoning into engineering
- [[Evidence/README|Evidence]] — implementation and interview-defense evidence
