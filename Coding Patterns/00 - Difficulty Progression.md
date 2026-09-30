---
title: Difficulty Progression
type: guide
category: Coding Patterns
tags:
  - difficulty
  - mastery
  - progression
---

# Difficulty Progression

> Do not increase difficulty merely by choosing harder LeetCode problems. Increase the amount of uncertainty and variation.

## Five levels

| Level | Training objective | Evidence |
|---|---|---|
| 1 — Recognition | identify the pattern from obvious signals | name pattern + invariant |
| 2 — Implementation | solve a direct representative problem | correct template from memory |
| 3 — Variation | handle changed constraints or edge cases | adapt without abandoning invariant |
| 4 — Combination | combine the pattern with a second technique | explain primary + secondary roles |
| 5 — Interview Hard | solve under time and ambiguity | recognition + implementation + variation |

## Example: Prefix Sum

| Level | Example direction |
|---|---|
| 1 | Running Sum — 1480 |
| 2 | Range Sum Query — 303 |
| 2 | Subarray Sum Equals K — 560 |
| 3 | Contiguous Array — 525 |
| 3 | Binary Subarrays With Sum — 930 |
| 4 | Prefix Sum + HashMap |
| 5 | Mixed target-sum problem with no pattern hint |

## Example: Sliding Window

| Level | Example direction |
|---|---|
| 1 | fixed-size window |
| 2 | Longest Substring Without Repeating Characters — 3 |
| 3 | Minimum Size Subarray Sum — 209 |
| 4 | Minimum Window Substring — 76 |
| 5 | mixed window/frequency problem with changed constraints |

## Promotion rule

Move upward only when the current level is reliable.

Reliability means:

- at least two successful attempts;
- recognition without a pattern hint;
- invariant stated before implementation;
- no recurring unresolved mistake.

A Hard problem solved with the pattern already named does not automatically demonstrate Level 5 mastery.
