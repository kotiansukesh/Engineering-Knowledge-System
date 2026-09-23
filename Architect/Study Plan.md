---
title: "Study Plan — Software Architecture"
category: planning
tags: [study-plan, tasks, architecture, system-design, adr, c4, spaced-repetition]
created: 2026-09-26
completed: false
problems-solved: []
problems-solved-dates: {}
excalidraw: ""
---

# Study Plan — Software Architecture Practice

> Use with **Tasks plugin** (`Cmd+P → Tasks: Create or edit task`). Filter by `#arch` tag.

---

## Weekly Schedule (Recurring)

### Monday — Architecture Foundations
- [ ] 🔄 **What is Architecture** — Review definition & decisions [[Architect/01_Architecture-Foundations/What-is-Architecture]] #arch/foundations/definition 📅 every Monday
- [ ] 🔄 **Architecture Principles** — Review 1 principle [[Architect/01_Architecture-Foundations/Architecture-Principles]] #arch/foundations/principles 📅 every Monday
- [ ] 🔄 **Architect Roles** — Review role archetypes [[Architect/01_Architecture-Foundations/Architect-Roles]] #arch/foundations/roles 📅 every Monday
- [ ] 🔄 **Stakeholders & Concerns** — Map concerns to views [[Architect/01_Architecture-Foundations/Stakeholders-Concerns]] #arch/foundations/stakeholders 📅 every Monday

### Tuesday — Quality Attributes & Fitness Functions
- [ ] 🔄 **Quality Attributes** — Review 1 attribute [[Architect/02_Requirements-Quality-Attributes]] #arch/qualities/attributes 📅 every Tuesday
- [ ] 🔄 **Fitness Functions** — Write 1 ArchUnit test [[Architect/02_Requirements-Quality-Attributes/Fitness-Functions]] #arch/qualities/fitness 📅 every Tuesday
- [ ] 🔄 **Trade-off Analysis** — Practice 1 scenario #arch/qualities/tradeoffs 📅 every Tuesday

### Wednesday — Architecture Styles & Patterns
- [ ] 🔄 **Architecture Styles** — Compare 2 styles [[Architect/03_Architecture-Styles]] #arch/styles/comparison 📅 every Wednesday
- [ ] 🔄 **Design Patterns as Building Blocks** — Apply 1 pattern [[Architect/04_Design-Patterns-Building-Blocks]] #arch/patterns/building-blocks 📅 every Wednesday
- [ ] 🔄 **Integration Patterns** — Review 1 pattern [[Architect/07_Integration-APIs]] #arch/patterns/integration 📅 every Wednesday

### Thursday — DDD, Data Architecture, Non-Functional
- [ ] 🔄 **DDD Modeling** — Practice 1 tactical pattern [[Architect/05_DDD-Modeling]] #arch/ddd/tactical 📅 every Thursday
- [ ] 🔄 **Data Architecture** — Review 1 pattern [[Architect/06_Data-Architecture]] #arch/data/patterns 📅 every Thursday
- [ ] 🔄 **Non-Functional / Ops** — Review 1 concern [[Architect/08_NonFunctional-Ops]] #arch/ops/concerns 📅 every Thursday

### Friday — Governance, Documentation, System Design Interviews
- [ ] 🔄 **Governance & ADRs** — Write 1 ADR [[Architect/09_Governance-Documentation]] #arch/gov/adr 📅 every Friday
- [ ] 🔄 **System Design Interview** — Practice 1 problem [[Architect/10_System-Design-Interviews]] #arch/sysdesign/interview 📅 every Friday
- [ ] 🔄 **Architecture Review** — Review 1 past decision #arch/gov/review 📅 every Friday

### Saturday — Mock Interview / Architecture Kata
- [ ] 🔄 **Timed System Design** — 1 problem (45 min: requirements → API → data → scale → risks) #arch/mock 📅 every Saturday
- [ ] 🔄 **Architecture Kata** — Model 1 kata end-to-end with C4 + ADRs #arch/kata 📅 every Saturday

### Sunday — Review & Spaced Repetition
- [ ] 🔄 **SR Review** — Review all notes where `sr-due <= today` #arch/sr 📅 every Sunday
- [ ] 🔄 **Stale Review** — Review notes not reviewed in >7 days #arch/stale 📅 every Sunday
- [ ] 🔄 **Update Frontmatter** — Set `reviewed = today`, `sr-due = next interval` #arch/admin 📅 every Sunday

---

## Spaced Repetition Intervals

After reviewing a concept **cold** (without looking at notes):

| Repetition | Interval | When to Set `sr-due` |
|------------|----------|---------------------|
| 1st | +3 days | `sr-due = today + 3d` |
| 2nd | +7 days | `sr-due = today + 7d` |
| 3rd | +14 days | `sr-due = today + 14d` |
| 4th | +30 days | `sr-due = today + 30d` |
| 5th | +90 days | `sr-due = today + 90d` |

**Rule**: Only advance interval if you recall it *cold* (no hints, no peeking). If you struggle, reset to +3 days.

---

## How to Track Progress

In the note's frontmatter, add:

```yaml
completed: true          # When you've deeply studied the note
reviewed: "2026-09-26"   # Last review date
sr-due: "2026-09-29"     # Next spaced repetition due date
```

---

## Quick Filters (Tasks Plugin)

```tasks
# All Architecture tasks due this week
not done
tag includes #arch
due before 2026-10-03
```

```tasks
# System Design Interview practice
not done
tag includes #arch/sysdesign
```

```tasks
# ADR writing practice
not done
tag includes #arch/gov/adr
```

---

## Progress Tracking

| Week | Foundations | Qualities | Styles/Patterns | DDD/Data/Ops | Gov/SysDesign | Total |
|------|-------------|-----------|-----------------|--------------|---------------|-------|
| 1 | /4 | /3 | /3 | /3 | /3 | /16 |
| 2 | /4 | /3 | /3 | /3 | /3 | /16 |
| 3 | /4 | /3 | /3 | /3 | /3 | /16 |
| 4 | /4 | /3 | /3 | /3 | /3 | /16 |

*Update manually each week. Target: ~16 topics × 5 reps = 80 reviews over 90 days.*

---

## Related

- [[Dashboard|Architect Dashboard]]
- [[Architect/10_System-Design-Interviews/Interview-Bank|System Design Interview Bank]]
- [[README|Architect MOC]]
- [[Master Dashboard|Global Dashboard]]
- [[_templates/Arch-Note-Template.md|Architecture Note Template]]
- [[_templates/Architecture Diagram.excalidraw.md|Excalidraw Template]]