---
title: Architecture Trade-off Simulator
type: practice
category: Architect
tags: [architecture, trade-offs, practice]
---

# Architecture Trade-off Simulator

Architecture decisions are functions of constraints, not technology preferences.

## Scenario

~~~yaml
traffic_rps:
growth:
latency_p99_ms:
availability:
consistency:
data_gb:
regions:
team_size:
deployment_frequency:
monthly_cost_target:
regulatory_constraints:
~~~

## Decision canvas

| Question | Answer |
|---|---|
| Dominant constraint | |
| Simplest viable option | |
| Alternative 1 | |
| Alternative 2 | |
| Why not the alternatives? | |
| First bottleneck | |
| Main failure mode | |
| Operational burden | |
| Cost driver | |
| Evidence required | |
| Redesign trigger | |

## Constraint mutation

Change exactly one constraint and redesign:

- [ ] 10× traffic
- [ ] 10× data
- [ ] 10× deployment frequency
- [ ] 99.9% → 99.99% availability
- [ ] single region → multi-region
- [ ] eventual → strong consistency
- [ ] low cost → low latency
- [ ] small team → large organization

## Rule

Do not change architecture merely because a different technology is available. Change it because the constraint changed.
