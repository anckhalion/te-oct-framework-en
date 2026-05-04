# CYCLE 5 DECISION GATE v1.0

Date: 2026-05-04

| Theorem | Lane/class | Decision | Reference artifacts |
| --- | --- | --- | --- |
| A01 | L1 empirical process | revise_needed | results/A01_metrics_v1_0.json; trajectory/A01_trajectory_events.jsonl |
| D02 | L1 empirical | reject_candidate | results/D02_metrics_empirical_v1_0.json; trajectory/D02_trajectory_events.jsonl |
| D02 | L2 formal | pass_candidate | results/D02_metrics_formal_v1_0.json |
| D02 | theorem global | revise_needed | lane split matrix above |
| D03 | L1 empirical paired pre/post | reject_candidate | results/D03_metrics_v1_0.json; trajectory/D03_trajectory_events.jsonl |

## Theorem-level outcome summary

- A01: `revise_needed`
- D02: `revise_needed`
- D03: `reject_candidate`

## Promotion rule

- No theorem status promotion to `validated` is allowed without independent external replication closure.
