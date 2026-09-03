# Metrics Dashboard — Per-Phase Tracker

| Phase | Metric | Target | Week Observed | Value | Trend | Notes |
|-------|--------|--------|--------------|-------|-------|-------|
| **01 Fundamentals** | API p95 latency (ms) | < 300 ms | W1–W4 |  |  | Record per `api_latency` note |
| | Error rate on retries | < 5% | W1–W4 |  |  | Count 429 / timeout / parse failures |
| | `pytest` pass % | 100% | W4 |  |  | All 3 test files pass |
| **02 RAG-Engineering** | Retrieval precision@5 | ≥ 0.50 | W5–W10 |  |  | On golden set |
| | Recall@10 | ≥ 0.70 | W5–W10 |  |  |  |
| | Citation fidelity | ≥ 0.80 | W5–W10 |  |  | % of answers fully grounded |
| | Latency p95 (ms) | < 500 ms | W5–W10 |  |  | Including embedding call |
| | Cost per query ($) | ≤ 0.01 | W5–W10 |  |  | Embedding + LLM only |
| **03 Agentic-AI** | Agent success rate (per goal) | ≥ 0.70 | W11–W16 |  |  | HITL gate outcomes |
| | Orchestration latency (s) | < 3.0 s | W11–W16 |  |  | Planner → response |
| | Memory hit rate | ≥ 0.60 | W11–W16 |  |  | Vector lookup vs recompute |
| | Audit log completeness | 100% | W11–W16 |  |  | Every agent action logged |
| **04 Production** | gRPC p95 latency (ms) | < 200 ms | W17–W24 |  |  |  |
| | HPA scale-up time (s) | < 30 s | W17–W24 |  |  |  |
| | Circuit breaker trips / day | < 5 | W17–W24 |  |  |  |
| | Prometheus alert failures | 0 | W17–W24 |  |  |  |
| | Cost per request ($) | ≤ 0.005 | W17–W24 |  |  |  |
| **05 K8s Ops** | CKAD pass % | 100% | W25–W30 |  |  | Exam result |
| | Pod readiness time (s) | < 60 s | W25–W30 |  |  |  |
| | Persistent volume errors | 0 | W25–W30 |  |  |  |
| | Dashboard green (Grafana) | 100% | W25–W30 |  |  |  |
| **06 Governance** | ADRs written | ≥ 3 | W31–W36 |  |  |  |
| | EU AI Act compliance checklist | 100% | W31–W36 |  |  |  |
| | Drift detection lead time | ≥ 2 weeks | W31–W36 |  |  |  |
| | MLOps pipeline CI passes | 100% | W31–W36 |  |  |  |

```dataview
TABLE WITHOUT ID weeks as "Weeks", file.link as "Metric", target as "Target", value as "Observed", trend as "Trend", notes as "Notes"
FROM "AI/99_Revision"
WHERE category AND file.folder != "AI/99_Revision" AND file.name != "README"
SORT file.path ASC
```