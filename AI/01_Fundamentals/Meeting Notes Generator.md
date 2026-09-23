---
title: "Meeting Notes Generator"
pattern: 12
category: "AI/01_Fundamentals"
tags: [project, summarization, structured-outputs, eval]
created: 2026-09-02
completed: false
reviewed: ""
sr-due: ""
difficulty: Medium
problems-solved: []
problems-solved-dates: {}
excalidraw: ""
---

## 🎯 Intent
Transcribe/summarize meetings into structured notes — validates prompt engineering + structured outputs. The schema is the integration contract.

## 💡 Why It Matters
- **Interview signal**: "Why structured output for meeting notes?" and "How do you know summaries are good?" — golden-set eval + schema-as-contract are the answers
- **Production reality**: Recurring schema-shaped documents (meeting notes, tickets, summaries) where value = consistency + searchability, not creativity
- **Downstream consumer is a system**: Action items need owner + due date to become reminders; prose notes never become that

## 🧩 Diagram: Meeting Notes Pipeline
```mermaid
flowchart LR
    IN[Audio/Transcript In] --> TS[Transcript<br/>(Whisper-style)]
    TS --> P[Versioned Prompt<br/>(role + schema)]
    P --> L[LLM]
    L --> SO[Structured Output:<br/>MeetingNotes Schema]
    SO --> EV[Eval on Golden Set<br/>(5 sample transcripts)]
    EV -->|regression| CI[CI Gate]
    SO --> OUT[{summary, decisions,<br/>action_items}]
    style SO fill:#e8f5e9
    style EV fill:#fff3e0
```

## 💻 Code: Meeting Notes with Structured Output + Eval (Python)
```python
from pydantic import BaseModel, Field
from typing import Optional
from dataclasses import dataclass

class ActionItem(BaseModel):
    owner: str
    task: str
    due: Optional[str] = None

class MeetingNotes(BaseModel):
    summary: str = Field(description="3-4 sentences, decisions only")
    decisions: list[str] = Field(default_factory=list)
    action_items: list[ActionItem] = Field(default_factory=list)

# Anthropic tool calling for structured output
async def extract_meeting_notes(transcript: str) -> MeetingNotes:
    resp = await anthropic.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=1024,
        tools=[{"name": "save_meeting_notes",
                "description": "Save structured meeting notes",
                "input_schema": MeetingNotes.model_json_schema()}],
        messages=[{"role": "user", "content": transcript}]
    )
    tool_use = next(b for b in resp.content if b.type == "tool_use")
    return MeetingNotes.model_validate(tool_use.input)

# Golden-set eval (Phase 02+)
@dataclass(frozen=True)
class GoldenCase:
    transcript: str
    expected: MeetingNotes

def eval_faithfulness(golden: list[GoldenCase]) -> float:
    """Fraction of generated decisions that appear in ground truth."""
    passed = 0
    for gc in golden:
        generated = extract_meeting_notes(gc.transcript)
        # Faithfulness: no hallucinated decisions
        if all(d in gc.expected.decisions for d in generated.decisions):
            passed += 1
    return passed / len(golden)

# CI gate: faithfulness ≥ 0.9 AND coverage ≥ 0.8
```

## ✅ When to Use / ❌ When NOT to Use
| Scenario | Use? | Reason |
|---|---|---|
| Recurring schema-shaped docs (meeting notes, tickets, summaries) | ✅ | Consistency + searchability > creativity |
| High-stakes / contested decisions | ❌ | Model smooths disagreement into clean false consensus |
| One-off creative notes | ❌ | Free text fine; schema adds constraint for no benefit |

## ⚖️ Trade-offs
| Choice | Cost |
|---|---|
| **Structured output over prose** | Loses nuance; action item reads cleaner than the argument behind it |
| **Eval on 5 transcripts** | Small golden set, weak signal until it grows |
| **Versioned prompts** | Every version needs its own eval baseline |

## 🆚 Vs. Alternatives
| Approach | Meeting Notes Generator | Manual Notes | Off-the-shelf AI Notetaker |
|---|---|---|---|
| **Consistency** | Schema-enforced | Varies by notetaker | Vendor-defined |
| **Ownership** | Your schema, your vault | Best | Data leaves your estate |
| **Eval** | Golden-set regression | None | None visible |

## ⚠️ Pitfalls
1. **Inventing owners/dates for action items** — model prefers complete-looking list over honest one
2. **Treating summary quality as subjective** — without golden-set eval, drift is invisible
3. **Storing transcripts with secrets** next to notes
4. **Schema forcing decisions where there were none** — empty arrays ARE valid output

## 🎤 Interview Q&A (Senior Depth)

**Q1: "Why structured output for meeting notes specifically?"**
> **Answer**: Downstream consumer is a system, not a reader. Action items need owner + due date to become reminders; prose notes never become that. The schema IS the integration contract. **Rejected**: "Because it looks better" — schema enables automation.

**Q2: "How do you know the summaries are any good?"**
> **Answer**: Golden set of 5 transcripts with regression gate in CI. Subjective review catches a bad summary once; eval catches the 5th one that drifts. **Metric**: faithfulness ≥ 0.9, coverage ≥ 0.8.

**Q3: "What is the real risk of AI meeting notes?"**
> **Answer**: Manufactured consensus. Model under pressure to fill schema produces confident decision list from unresolved argument, and that becomes the record. **Mitigation**: Empty arrays are valid — schema forces explicit "no decisions" vs hallucinating them.

**Q4: "How do you handle the case where the meeting had no decisions?"**
> **Answer**: `decisions: []`, `action_items: []` are valid output. Schema forces model to explicitly say "no decisions" rather than hallucinating. **Rejected**: Filling with "N/A" strings — breaks downstream parsing.

**Q5: "What's the minimum viable eval for this?"**
> **Answer**: 5 diverse transcripts (different speakers, topics, lengths). Each has human-annotated `MeetingNotes` ground truth. Scores: faithfulness (no hallucinated decisions), coverage (key decisions captured), format validity (schema passes). Ship only if faithfulness ≥ 0.9 AND coverage ≥ 0.8.

## 🔗 Related
- [[04_Prompt Engineering]] • [[05_Structured Outputs]] • [[AI Evaluation]] • [[AI Backend Template]]