---
title: "Knowledge Model"
type: reference
category: "Knowledge System"
status: active
---

# Knowledge Model

## Note types

| Type | Purpose | Expected output |
|---|---|---|
| concept | Explain one durable mechanism | explanation + example + trade-offs |
| pattern | Reusable solution shape | signal + invariant + implementation |
| reference | Stable factual lookup | concise facts + sources |
| exercise | Practice under constraints | attempt + result + diagnosis |
| project | Buildable system | architecture + implementation + evidence |
| ADR | Record a decision | context + alternatives + decision + consequences |
| failure | Explain a failure | trigger + blast radius + detection + recovery |
| evaluation | Measure behavior | dataset/workload + metric + result |
| certification | External validation | requirements + evidence mapping |
| MOC | Navigation | links and derived views |

## Canonical lifecycle

**Learn → Recognize → Build → Measure → Break → Explain → Review → Redesign**

## Quality dimensions

Every major concept should eventually answer:

1. What problem does it solve?
2. What mechanism makes it work?
3. What are its invariants?
4. What does it cost?
5. How does it fail?
6. How do I measure it?
7. What alternatives exist?
8. When would I change the decision?
