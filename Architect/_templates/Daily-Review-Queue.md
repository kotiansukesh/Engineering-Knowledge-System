# Daily Review Queue

> **Auto-generated daily** — Add to your Daily Note template for automatic review scheduling.

---

## Today's Review (Spaced Repetition)

```dataview
TASK
FROM "Java" OR "Architect" OR "AI" OR "Coding Patterns"
WHERE !completed
  AND (due <= date(today) OR scheduled <= date(today))
  AND !path.includes("_templates")
  AND !path.includes("_attachments")
SORT due ASC, scheduled ASC
LIMIT 20
```

---

## Flashcards Due Today

```dataview
TABLE WITHOUT ID
  file.link as "Note",
  category as "Category",
  "sr-due" as "Due",
  reviewed as "Last Reviewed"
FROM "Java" OR "Architect" OR "AI" OR "Coding Patterns"
WHERE "sr-due"
  AND date("sr-due") <= date(today)
  AND !file.name.includes("README")
  AND !path.includes("_templates")
SORT "sr-due" ASC
LIMIT 30
```

---

## Stale Notes (>7 days since review)

```dataview
TABLE WITHOUT ID
  file.link as "Note",
  category as "Category",
  reviewed as "Last Reviewed",
  date(today) - date(reviewed) as "Days Stale"
FROM "Java" OR "Architect" OR "AI" OR "Coding Patterns"
WHERE reviewed
  AND date(today) - date(reviewed) > 7
  AND !file.name.includes("README")
  AND !path.includes("_templates")
SORT (date(today) - date(reviewed)) DESC
LIMIT 20
```

---

## Incomplete Notes (Completion Checklist)

```dataview
TABLE WITHOUT ID
  file.link as "Note",
  category as "Category",
  completion_criteria.intent_written as "Intent",
  completion_criteria.why_it_matters_filled as "Why",
  completion_criteria.diagram_created as "Diagram",
  completion_criteria.problems_section_complete as "Problems",
  completion_criteria.code_example_added as "Code",
  completion_criteria.tradeoffs_filled as "Trade-offs",
  completion_criteria.pitfalls_listed as "Pitfalls",
  completion_criteria.interview_qa_answered as "Q&A",
  completion_criteria.flashcards_created as "Flashcards",
  completion_criteria.practice_tasks_scheduled as "Tasks"
FROM "Architect"
WHERE completion_criteria
  AND !file.name.includes("README")
  AND !path.includes("_templates")
  AND !path.includes("Practice-Problems")
SORT file.name ASC
```

---

## This Week's Practice Problems

```dataview
TASK
FROM "Architect/10_System-Design-Interviews/Practice-Problems"
WHERE !completed
  AND (due <= date(today) + dur(7 days) OR scheduled <= date(today) + dur(7 days))
SORT due ASC
LIMIT 10
```

---

## Quick Actions

- [ ] Review all SR due cards ({{dateformat(date(today), "yyyy-MM-dd")}})
- [ ] Complete 1 practice problem
- [ ] Update 3 stale notes
- [ ] Export Anki deck (run `python3 export_anki.py`)

---

## Weekly Review (Sunday)

```dataview
TABLE WITHOUT ID
  file.link as "Note",
  category as "Category",
  reviewed as "Last Reviewed",
  "sr-due" as "Next Due"
FROM "Java" OR "Architect" OR "AI" OR "Coding Patterns"
WHERE reviewed
  AND date(reviewed) >= date(today) - dur(7 days)
  AND !file.name.includes("README")
SORT reviewed DESC
```

---

*Add this to your Daily Note template: `![[Architect/_templates/Daily-Review-Queue.md]]`*