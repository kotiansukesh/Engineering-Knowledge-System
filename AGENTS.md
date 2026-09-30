# AGENTS.md

## Repository

This is an **Obsidian knowledge vault**. Preserve both standard Markdown readability and Obsidian-native behavior.

## Internal links

Use Obsidian wikilinks:

- `[[Note Name]]`
- `[[Folder/Note Name]]`
- `[[Folder/Note Name|Display Text]]`

Do **not** use filesystem-style relative wikilinks such as `[[../Note]]`.

Before committing structural changes, verify that every new internal link points to an existing note.

## Plugins

This vault uses:

- **Dataview** — dynamic indexes, dashboards, and metadata-driven views.
- **Tasks** — actionable review/checklist work.
- **Templater** — reusable note templates and generated metadata.
- **Excalidraw** — diagrams where visual explanation adds real value.

Keep responsibilities separated:

- Knowledge → Markdown notes
- State → YAML frontmatter
- Derived views → Dataview
- Actions → Tasks
- Reusable note creation → Templater
- Spatial/state-heavy diagrams → Excalidraw

Do not add plugin syntax merely for decoration.

## Coding Patterns

`Coding Patterns` is organized around **pattern recognition and mastery**, not copied problem statements.

Progression:

**Learn → Guided → Blind → Mixed → Mastered**

Pattern notes should emphasize recognition signals, the core invariant, mental model, implementation, variants, limits, complexity, canonical problems, interview reasoning, and review/practice.

Avoid duplicating complete problem statements across pattern notes.

## Frontmatter

For Coding Patterns, preserve the established metadata conventions:

```yaml
type: pattern
pattern:
domain:
category:
advanced:
mastery:
recognition_score:
difficulty:
leetcode:
created:
reviewed:
next_review:
tags:
```

Do not rename or remove fields without checking Dataview queries and templates that depend on them.

## Dataview

Prefer queries based on stable frontmatter instead of manually maintained lists. Keep queries compatible with actual vault paths and metadata.

## Tasks

Use Tasks for actionable review work. Avoid large collections of permanently hard-coded tasks when a dynamic query or review queue is more appropriate.

## Templater

Templates should produce valid YAML, follow existing metadata conventions, avoid unnecessary hard-coded state, and create notes that work immediately after insertion.

## Excalidraw

Use Excalidraw when a visual materially improves understanding, especially for pointer/state transitions, tree or graph state, recursion/backtracking state, and complex data-structure transformations.

Do not create diagrams for concepts that are clearer as Markdown or Mermaid.

## Editing workflow

Before broad changes:

1. Inspect the existing folder/file structure.
2. Check metadata conventions.
3. Check Dataview, Tasks, and Templater dependencies.
4. Preserve useful existing knowledge.
5. Remove duplication only when the replacement remains discoverable.
6. Verify internal links.
7. Verify referenced files actually exist.
8. Review the resulting diff before merging.

## Quality bar

A change is complete only when:

- Markdown remains readable outside Obsidian.
- Obsidian wikilinks resolve to real notes.
- Dataview queries reference real fields and paths.
- Tasks queries target real paths.
- Templates use valid syntax.
- Existing useful knowledge has not been accidentally discarded.
- Navigation remains discoverable from the relevant MOC/index.
- No stale GitHub-style relative wikilinks such as `[[../...]]` remain.

## Git workflow

For substantial repository changes:

- Start from the latest `main`.
- Use a descriptive branch.
- Keep changes focused.
- Use a pull request.
- Review the diff before merging.
- Do not claim a change is complete until GitHub confirms it.
