---
title: Adaptive Review Engine
type: guide
category: Coding Patterns
tags:
  - mastery
  - spaced-repetition
  - review
---

# Adaptive Review Engine

> Review intervals should respond to evidence, not a fixed calendar.

## Evidence → next review

| Result | Suggested interval |
|---|---:|
| Pattern missed | 1 day |
| Correct only after hint | 2 days |
| Correct but slow / weak invariant | 4 days |
| Correct blind + invariant | 7 days |
| Blind success twice | 14 days |
| Strong mixed performance | 30 days |

These are starting intervals. Adjust for difficulty and recent failures.

## Evidence fields

~~~yaml
last_attempt: 2026-09-30
last_success: 2026-09-30
attempts: 8
successful_attempts: 6
recognition_attempts: 5
recognition_successes: 4
avg_time_minutes: 18
hint_count: 2
implementation_score: 4
recognition_score: 4
next_review: 2026-10-07
~~~

## Recognition vs implementation

### Recognition score

- 5 = immediate + invariant
- 4 = correct with little exploration
- 3 = correct after brute-force derivation
- 2 = needed hint
- 1 = missed pattern

### Implementation score

- 5 = correct, clean, within target time, invariant explained
- 4 = correct with minor correction
- 3 = correct after debugging
- 2 = substantial hint/debugging required
- 1 = incomplete/incorrect

## Review rule

After every meaningful attempt:

1. update attempt counters;
2. record failure category;
3. update recognition and implementation scores;
4. choose the interval from the evidence table;
5. set next_review;
6. add a Task only when an action is genuinely required.

Do not create permanent Tasks for every possible future review; let Dataview surface due work.

## Mastery gate

Mastered requires evidence across blind + mixed practice, not repeated guided solves.
