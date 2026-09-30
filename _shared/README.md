# Shared Vault Contract

The repository contains four independent Obsidian vaults:

- **Java** — how to build software.
- **Coding Patterns** — how to solve problems.
- **AI** — how to build AI systems.
- **Architect** — how to design systems under constraints.

## Cross-vault references

Obsidian wikilinks are local to a vault. Therefore:

- Use `[[...]]` only for notes inside the current vault.
- Do not use `[[../...]]` or pretend that another vault is a local folder.
- Record meaningful cross-vault relationships in frontmatter:

```yaml
related:
  - vault: java
    note: "Concurrency"
  - vault: architect
    note: "Distributed Concurrency"
```

Use a GitHub/Markdown URL when the relationship must be directly clickable.

## Shared learning model

**Learn → Understand → Build → Break → Explain → Review**

Domain adaptations:

- Java: Concept → Code → Test → Break → Explain
- Coding Patterns: Problem → Recognize → Solve → Prove → Review
- AI: Concept → Build → Evaluate → Operate → Explain
- Architect: Requirements → Constraints → Design → Failure → Trade-off → Defend

Keep this model stable. Add tooling only when it removes real friction.
