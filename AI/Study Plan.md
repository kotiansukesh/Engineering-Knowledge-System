---
title: "Study Plan — AI / LLM Engineering"
category: planning
tags: [study-plan, tasks, ai, llm, rag, agents, spaced-repetition]
created: 2026-09-26
completed: false
problems-solved: []
problems-solved-dates: {}
excalidraw: ""
---

# Study Plan — AI / LLM Engineering Practice

> Use with **Tasks plugin** (`Cmd+P → Tasks: Create or edit task`). Filter by `#ai` tag.

---

## Weekly Schedule (Recurring)

### Monday — LLM Fundamentals
- [ ] 🔄 **LLM Fundamentals** — Review 1 concept [[AI/01_Fundamentals/01_LLM Fundamentals]] #ai/fundamentals/llm 📅 every Monday
- [ ] 🔄 **Embeddings & Vector Search** — Review 1 concept [[AI/01_Fundamentals/02_Embeddings and Vector Search]] #ai/fundamentals/embeddings 📅 every Monday
- [ ] 🔄 **LLM APIs** — Review 1 concept [[AI/01_Fundamentals/03_LLM APIs]] #ai/fundamentals/apis 📅 every Monday
- [ ] 🔄 **Prompt Engineering** — Practice 1 technique [[AI/01_Fundamentals/04_Prompt Engineering]] #ai/fundamentals/prompting 📅 every Monday

### Tuesday — RAG Engineering
- [ ] 🔄 **RAG Architecture** — Review 1 pattern [[AI/02_RAG-Engineering]] #ai/rag/architecture 📅 every Tuesday
- [ ] 🔄 **Retrieval Strategies** — Practice 1 technique #ai/rag/retrieval 📅 every Tuesday
- [ ] 🔄 **Evaluation/Observability** — Review metrics [[AI/02_RAG-Engineering]] #ai/rag/eval 📅 every Tuesday

### Wednesday — Agentic AI
- [ ] 🔄 **Agent Frameworks** — Review 1 pattern [[AI/03_Agentic-AI]] #ai/agents/frameworks 📅 every Wednesday
- [ ] 🔄 **Tool Calling / Function Calling** — Practice [[AI/01_Fundamentals/06_Tool Calling]] #ai/agents/tools 📅 every Wednesday
- [ ] 🔄 **Multi-Agent Patterns** — Review 1 pattern #ai/agents/multi-agent 📅 every Wednesday

### Thursday — Production Platform
- [ ] 🔄 **Serving / Inference** — Review 1 topic [[AI/04_Production-Platform]] #ai/prod/serving 📅 every Thursday
- [ ] 🔄 **Fine-tuning / LoRA** — Review 1 concept #ai/prod/finetuning 📅 every Thursday
- [ ] 🔄 **Cost / Latency Optimization** — Practice 1 technique #ai/prod/optimization 📅 every Thursday

### Friday — K8s Operations + Governance
- [ ] 🔄 **K8s for AI Workloads** — Review 1 topic [[AI/05_Kubernetes-Operations]] #ai/k8s/ai-workloads 📅 every Friday
- [ ] 🔄 **Architecture Governance** — Review 1 ADR [[AI/06_Architecture-Governance]] #ai/gov/adr 📅 every Friday
- [ ] 🔄 **Cross-Cutting Concerns** — Security, Compliance [[AI/07_Cross-Cutting]] #ai/cross-cutting 📅 every Friday

### Saturday — Mock Interview / Project
- [ ] 🔄 **Timed Mock** — 5 Q&A from Interview-Bank + 1 coding task (60 min) #ai/mock 📅 every Saturday
- [ ] 🔄 **Mini Project** — Build/tweak 1 RAG/agent component #ai/project 📅 every Saturday

### Sunday — Review & Spaced Repetition
- [ ] 🔄 **SR Review** — Review all notes where `sr-due <= today` #ai/sr 📅 every Sunday
- [ ] 🔄 **Stale Review** — Review notes not reviewed in >7 days #ai/stale 📅 every Sunday
- [ ] 🔄 **Update Frontmatter** — Set `reviewed = today`, `sr-due = next interval` #ai/admin 📅 every Sunday

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
# All AI tasks due this week
not done
tag includes #ai
due before 2026-10-03
```

```tasks
# Completed AI tasks this week
done
tag includes #ai
done after 2026-09-22
```

```tasks
# Specific topic (e.g., RAG)
not done
tag includes #ai/rag
```

---

## Progress Tracking

| Week | Fundamentals | RAG | Agentic | Production | K8s/Gov | Cross-Cutting | Total |
|------|--------------|-----|---------|------------|---------|---------------|-------|
| 1 | /4 | /3 | /3 | /3 | /3 | /2 | /18 |
| 2 | /4 | /3 | /3 | /3 | /3 | /2 | /18 |
| 3 | /4 | /3 | /3 | /3 | /3 | /2 | /18 |
| 4 | /4 | /3 | /3 | /3 | /3 | /2 | /18 |

*Update manually each week. Target: ~18 topics × 5 reps = 90 reviews over 90 days.*

---

## Related

- [[Dashboard|AI Dashboard]]
- [[Interview-Bank|AI Interview Bank]]
- [[README|AI MOC]]
- [[Master Dashboard|Global Dashboard]]
- [[_templates/AI Note Template.md|AI Note Template]]
- [[_templates/AI Diagram.excalidraw.md|Excalidraw Template]]