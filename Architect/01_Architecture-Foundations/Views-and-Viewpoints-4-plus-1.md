---
title: Views and Viewpoints — 4+1
type: concept
category: Architect/01_Architecture-Foundations
difficulty: Intermediate
completed: false
reviewed:
sr-due:
tags: [architecture, foundations, views, C4, documentation]
---

# Views and Viewpoints — 4+1

## Purpose

A model should answer a question for a specific audience. No single diagram adequately communicates structure, runtime behavior, deployment and quality concerns.

## View vs viewpoint

- **Viewpoint:** rules for constructing a view for a concern/audience.
- **View:** an actual representation produced using that viewpoint.

## 4+1

1. **Logical** — important structure and responsibilities
2. **Process** — runtime behavior, concurrency and communication
3. **Development** — code/module organization
4. **Physical** — deployment and infrastructure
5. **Scenarios (+1)** — use cases that validate the other views

## C4 relationship

4+1 answers **which perspective is needed**.

C4 provides a practical structural hierarchy:

**Context → Container → Component → Code**

They are complementary, not competing frameworks.

## Choose a view by question

| Question | Useful view |
|---|---|
| Who uses the system? | Context |
| What major containers exist? | Container |
| How does a critical request flow? | Runtime/sequence |
| Where does it run? | Deployment/physical |
| How is code organized? | Component/module |
| Will it meet p99/RTO? | Scenario + runtime/deployment evidence |

## Diagram quality

A useful view has:

- explicit scope;
- consistent abstraction;
- named relationships;
- a question it answers;
- relevant ownership;
- freshness/review trigger.

Do not create every view automatically.

## Practice

For a payment flow create:

1. context;
2. container;
3. runtime sequence;
4. deployment/failure view;
5. one quality scenario validating the design.

Then remove one diagram that does not answer a real question.

## Practice tasks

- [ ] Draw Context and Container
- [ ] Draw one runtime sequence
- [ ] Draw one deployment/failure view
- [ ] State the stakeholder for each
- [ ] Identify the scenario that validates the views
