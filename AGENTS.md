# AGENTS.md

## Repository

This is an **Obsidian knowledge vault**. Preserve Markdown readability and Obsidian-native behavior.

## Internal links

Use Obsidian wikilinks:

~~~text
[[Note Name]]
[[Folder/Note Name]]
[[Folder/Note Name|Display Text]]
~~~

Never use filesystem-style relative wikilinks such as:

~~~text
[[../Note]]
~~~

**Markdown-table rule:** do not use pipe aliases inside wikilinks in table rows. Use:

~~~text
[[Folder/Note]]
~~~

in tables; aliases are fine in ordinary prose.

## Plugins

- Dataview — dynamic indexes, dashboards and analytics.
- Tasks — actionable review work.
- Templater — reusable note creation.
- Excalidraw — diagrams where a visual materially improves understanding.

Keep responsibilities separated:

- Knowledge → Markdown
- State → YAML frontmatter
- Derived views → Dataview
- Actions → Tasks
- Reusable creation → Templater
- Spatial/state-heavy visuals → Excalidraw

## Coding Patterns architecture

The vault trains:

**Attempt → Recognition → Implementation → Diagnosis → Review → Re-test → Mastery**

Key layers:

- Pattern Library
- Problem Bank
- Recognition Lab
- Mixed Pattern Sets
- Mistake Engine
- Adaptive Review Engine
- Weakness Heatmap
- Interview Mode
- Senior Trade-offs
- Java Quality Layer

Progression:

**Learn → Guided → Blind → Mixed → Mastered**

Pattern mastery must not be inferred from repeated guided solutions alone.

## Frontmatter

Pattern notes preserve the established fields and may additionally contain:

~~~yaml
implementation_score: 0
attempts: 0
successful_attempts: 0
recognition_attempts: 0
recognition_successes: 0
avg_time_minutes:
hint_count: 0
last_attempt:
last_success:
failure_category:
~~~

Do not rename or remove metadata without checking Dataview queries and templates.

## Dataview

Use stable frontmatter and real vault paths. Avoid queries that depend on manually maintained state.

## Tasks

Tasks should represent actionable work. Do not create permanent tasks for every future review when Dataview can surface due work.

## Templater

Templates must produce valid YAML and immediately usable notes.

## Excalidraw

Use for spatial/state-heavy algorithms. Do not create diagrams merely for decoration.

## Validation

Run:

~~~bash
python3 scripts/validate-coding-patterns.py
~~~

The validator checks:

- broken wikilinks;
- forbidden relative links;
- pipe aliases in Markdown-table wikilinks;
- required pattern metadata;
- duplicate Problem Bank IDs;
- referenced Dataview/Tasks paths.

## Editing workflow

1. Start from latest main.
2. Inspect structure and metadata.
3. Preserve useful knowledge.
4. Verify links and referenced files.
5. Run the validator.
6. Review the diff.
7. Open a focused PR.
8. Merge only after validation is green.

## Quality bar

A change is complete only when:

- Markdown is readable outside Obsidian.
- Wikilinks resolve.
- Dataview fields and paths exist.
- Tasks paths exist.
- Templates produce valid metadata.
- Existing knowledge is preserved.
- New features are discoverable from the relevant MOC.
- No filesystem-style relative wikilinks remain.
