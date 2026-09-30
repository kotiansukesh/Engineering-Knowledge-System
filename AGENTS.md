# AGENTS.md

## Repository

This is an Obsidian knowledge repository containing **four independent vaults**. Preserve Markdown readability and Obsidian-native behavior.

### Vault roles

- **Java** — how to build software.
- **Coding Patterns** — how to solve problems.
- **AI** — how to build AI systems.
- **Architect** — how to design systems under constraints.

## Internal links

Use Obsidian wikilinks only for notes inside the current vault:

~~~text
[[Note Name]]
[[Folder/Note Name]]
[[Folder/Note Name|Display Text]]
~~~

Never use filesystem-style relative wikilinks such as:

~~~text
[[../Note]]
~~~

Do not use pipe aliases inside wikilinks in Markdown table cells. Prefer the plain target:

~~~text
[[Folder/Note]]
~~~

If a reference belongs to another vault, do **not** fake it as a local wikilink. Use the cross-vault contract in `_shared/README.md` and, when needed, a GitHub/Markdown URL.

## Learning model

Keep the learning loop simple:

**Learn → Understand → Build → Break → Explain → Review**

Domain adaptations:

- Java: Concept → Code → Test → Break → Explain
- Coding Patterns: Problem → Recognize → Solve → Prove → Review
- AI: Concept → Build → Evaluate → Operate → Explain
- Architect: Requirements → Constraints → Design → Failure → Trade-off → Defend

Do not add a second mastery framework unless it solves a demonstrated problem.

## Plugins

- Dataview — derived indexes, dashboards and analytics.
- Tasks — actionable review work.
- Templater — repeatable note creation.
- Excalidraw — spatial/state-heavy visual reasoning.

Keep responsibilities separated:

- Knowledge → Markdown
- State → YAML frontmatter
- Derived views → Dataview
- Actions → Tasks
- Reusable creation → Templater
- Complex visuals → Excalidraw

## Frontmatter

Keep metadata small and queryable. Use a common core where practical:

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
- See `_shared/Diagram-Guide.md`.

## Dataview

Use stable frontmatter and real local vault paths. Prefer simple Dataview queries. Use DataviewJS only when normal Dataview cannot express the required view.

## Tasks

Tasks represent actionable work. Do not create permanent review tasks when Dataview can surface due work.

## Templater

Templates must produce valid YAML and immediately usable notes. Keep templates short enough that a learner can understand the resulting note at a glance.

## Validation

Run:

~~~bash
python3 scripts/validate-vault.py
~~~

The repository-wide validator is the merge gate.

## Editing workflow

1. Inspect structure and metadata.
2. Preserve useful knowledge.
3. Simplify navigation before adding automation.
4. Verify links and referenced files.
5. Verify diagrams.
6. Run the validator.
7. Review the diff.

## Quality bar

A change is complete only when:

- Markdown is readable outside Obsidian.
- Wikilinks resolve inside their own vault.
- Cross-vault references follow the shared contract.
- Dataview fields and paths exist.
- Tasks paths exist.
- Templates produce valid metadata.
- Existing useful knowledge is preserved.
- New features are discoverable from the relevant MOC.
- No filesystem-style relative wikilinks remain.
