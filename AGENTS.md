# AGENTS.md

## Repository model

This repository is **one Obsidian vault**.

The top-level domains are:

- **Java** — how to implement and operate backend software.
- **Coding Patterns** — how to recognize and solve constrained problems.
- **AI** — how to build and operate AI systems.
- **Architect** — how to design systems under constraints and reason about trade-offs.
- **Build Lab** — where concepts become working systems.
- **Evidence** — where measurements, failures, decisions and defenses are recorded.

Do not reintroduce separate-vault assumptions.

## Internal links

Use normal Obsidian wikilinks for any note in this repository:

~~~text
[[Note Name]]
[[Folder/Note Name]]
[[Folder/Note Name|Display Text]]
~~~

Prefer explicit paths when names could be ambiguous:

~~~text
[[Java/04_Concurrency/Threads]]
[[AI/03_Agentic-AI/08_Multi-Agent Orchestration]]
[[Architect/13_AI-Architecture/04 - Agent Architecture]]
~~~

Never use filesystem-style relative wikilinks such as:

~~~text
[[../Note]]
~~~

Avoid pipe aliases inside Markdown table cells when a plain path is enough.

## Canonical knowledge rule

A concept should have **one canonical explanation**.

If a concept matters to multiple domains:

1. Keep the detailed explanation in the most natural domain.
2. Reference it from other domains with a local wikilink.
3. Put domain-specific implications in the consuming note rather than duplicating the concept.

Example:

~~~text
[[Java/04_Concurrency/CompletableFuture]]
[[Architect/04_Design-Patterns-Building-Blocks/02_Resilience-Circuit-Breaker-Retry]]
[[AI/03_Agentic-AI/10_Agent Evaluation]]
~~~

## Learning model

Keep the learning loop simple:

**Learn → Understand → Build → Break → Explain → Review**

Domain adaptations:

- Java: Concept → Code → Test → Break → Explain
- Coding Patterns: Problem → Recognize → Solve → Prove → Review
- AI: Concept → Build → Evaluate → Operate → Explain
- Architect: Requirements → Constraints → Design → Failure → Trade-off → Defend

Do not add another mastery framework unless it solves a demonstrated problem.

## Plugins

- **Dataview** — derived indexes, dashboards and analytics.
- **Tasks** — actionable review work.
- **Templater** — repeatable note creation.
- **Excalidraw** — spatial reasoning, distributed topology and exploratory diagrams.

Keep responsibilities separated:

- Knowledge → Markdown
- State → YAML frontmatter
- Derived views → Dataview
- Actions → Tasks
- Reusable creation → Templater
- Complex visuals → Excalidraw

## Frontmatter

Keep metadata small and queryable:

~~~yaml
type: concept
domain: java
status: active
difficulty: intermediate
created: 2026-09-30
reviewed:
next_review:
tags: []
~~~

Add domain-specific fields only when a query or workflow needs them.

## Diagrams

A diagram should answer **one question**.

- Mermaid for simple flow, sequence, state and structure.
- Excalidraw for spatial reasoning, distributed topology, concurrency and exploratory diagrams.
- Do not mix runtime flow, class structure and deployment topology into one diagram.
- Avoid static screenshots when a maintainable source can be kept.

## Dataview

Use stable frontmatter and real vault paths. Prefer simple Dataview queries. Use DataviewJS only when normal Dataview cannot express the required view.

## Tasks

Tasks represent actionable work. Do not create permanent review tasks when Dataview can surface due work.

## Templater

Templates must produce valid YAML and immediately usable notes. Keep templates short enough that a learner can understand the resulting note at a glance.

## Validation

Run:

~~~bash
python3 scripts/validate-vault.py
~~~

Then, when useful:

~~~bash
python3 scripts/validate-vault-health.py
~~~

## Editing workflow

1. Inspect structure and metadata.
2. Preserve useful knowledge.
3. Simplify navigation before adding automation.
4. Keep concepts canonical and link across domains.
5. Verify links and referenced files.
6. Verify diagrams.
7. Run the validator.
8. Review the diff.

## Quality bar

A change is complete only when:

- Markdown is readable outside Obsidian.
- Wikilinks resolve within this single vault.
- Dataview fields and paths exist.
- Tasks paths exist.
- Templates produce valid metadata.
- Existing useful knowledge is preserved.
- New features are discoverable from the relevant MOC.
- No filesystem-style relative wikilinks remain.
- No new cross-vault contract is introduced.
