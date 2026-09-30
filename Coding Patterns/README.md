---
title: Coding Patterns
type: moc
domain: coding-patterns
tags: [dsa, interview-prep, pattern-recognition]
---

# Coding Patterns

> **Recognize the problem shape → state the invariant → implement → prove → review.**

This vault is a **pattern-training system**, not a LeetCode archive.

## Start here

1. [[Patterns Index|Patterns]]
2. [[00 - Pattern Decision Tree|Decision Tree]]
3. [[00 - Pattern Recognition Lab|Recognition Lab]]
4. [[Problem Bank|Problem Bank]]
5. [[Canonical Problems|Canonical Problems]]
6. [[00 - Mixed Pattern Sets|Mixed Practice]]
7. [[99_Revision/Practice Dashboard|Review]]
8. [[00 - Mistake Log|Mistake Log]]
9. [[99_Revision/Study-Plan|Study Plan]]

## Pattern mastery

A pattern is useful when you can:

- recognize it on an unseen problem;
- state the invariant before coding;
- implement from memory;
- explain time and space complexity;
- explain when it does **not** apply;
- handle a meaningful variation.

## Training loop

**Problem → Recognize → Solve → Prove → Review**

Do not maintain separate mastery frameworks for every tool. Keep the learning loop simple; let Dataview derive status.

## Patterns needing attention

```dataview
TABLE WITHOUT ID
  file.link as "Pattern",
  mastery as "Mastery",
  recognition_score as "Recognition",
  implementation_score as "Implementation",
  next_review as "Next review"
FROM "Coding Patterns"
WHERE type = "pattern"
  AND (next_review = null OR date(next_review) <= date(today) OR recognition_score < 4 OR implementation_score < 4)
SORT recognition_score ASC, implementation_score ASC, date(next_review) ASC
LIMIT 20
```

## Diagram rule

- **Mermaid:** simple flow/state.
- **Excalidraw:** spatial/state-heavy reasoning.
- Prefer diagrams that explain **one invariant or transition**, not the entire solution.

## Plugin roles

- **Dataview:** derived status.
- **Tasks:** review actions.
- **Templater:** repeatable note creation.
- **Excalidraw:** visual reasoning.

## Quality gate

Run:

```bash
python3 scripts/validate-vault.py
```

Keep validation focused on broken internal links, metadata consistency, duplicate problem IDs and invalid references.

## Vault boundary

This is a separate Obsidian vault. Do not use ordinary `[[...]]` links to another vault.

Use the shared cross-vault contract:

```yaml
related:
  - vault: java
    note: "Collections"
  - vault: architect
    note: "Rate Limiting"
```

## Rule

> **Knowledge in notes. State in frontmatter. Views in Dataview. Actions in Tasks.**
