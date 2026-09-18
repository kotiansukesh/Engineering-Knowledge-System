# File naming convention

Vault-wide convention, applies to `AI/`, `Coding Patterns/`, `Java/`.

## Folders

| Pattern | Example | Notes |
|---------|---------|-------|
| `NN_Name` | `01_Core-Java`, `01_Fundamentals`, `01_Array` | Number + underscore + Title. Multi-word: hyphen `RAG-Engineering`. |
| `99_Revision` / `_templates` / `_attachments` | `_templates`, `_attachments` | Meta folders keep underscore prefix. |

## Files

| Area | Pattern | Example |
|------|---------|---------|
| `Java/` curriculum | `Title Case.md` | `String Handling.md`, `JVM Memory Model.md` |
| `AI/` lessons | `NN_Title.md` | `01_Python for AI.md`, `02_FastAPI Backend.md` |
| `AI/` projects | `Title Case.md` | `Prompt Playground.md`, `AI Backend Template.md` |
| `Coding Patterns/` | `NN - Title.md` | `01 - Prefix Sum.md`, `05 - Trie.md` |
| `Cross-cutting` | `NN_Title.md` or `Title Case.md` | `01_MCP.md`, `MCP Comparison Table.md` |

### Rules

- **Spaces** are allowed in titles (`String Handling.md` not `string-handling.md`), keeps `[[wikilinks]]` readable and Dataview `file.link` clean.
- **No parentheses** `()`, `05 - Trie.md` not `05 - Trie (Prefix Search).md`
- **No `&`**, use `and`, `01 - Fast and Slow Pointers.md`
- **No ` or `** in filename, pick one term, `Nested Classes Overview.md`
- **No `snake_case.md`**, use `Title Case.md`, `Comparison Table.md` not `comparison_table.md`
- **No file+folder basename collision**, cannot have `01_MCP.md` and `01_MCP/` folder simultaneously.

### Fixes applied 2026-09-02

- `01 - Fast & Slow Pointers.md` → `01 - Fast and Slow Pointers.md`
- `05 - Trie (Prefix Search).md` → `05 - Trie.md`
- `Nested Class or Inner Class.md` → `Nested Classes Overview.md`
- `AI/07_Cross-Cutting/01_MCP/comparison_table.md` → `AI/07_Cross-Cutting/MCP Comparison Table.md` (+ frontmatter, removed empty `01_MCP/` folder)
- Removed duplicate `AI/AI/01_Fundamentals/` tree
- Both dashboards (`Java/Dashboard.html`, `AI/Dashboard.html`) patched for 2K: `wrap 680px → 920@900 → 1280@1200 → 1480@1600 → 1580@1920 → 1720@2560`

### Why not kebab-case?

Obsidian resolves `[[String Handling]]` by display name. Title Case keeps links short. Kebab would require `[[string-handling|String Handling]]` aliases everywhere and breaks `SORT file.name` expectations.
