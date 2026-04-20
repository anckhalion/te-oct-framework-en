# CYCLE 4 Stress Plan v0.1
Date: 2026-04-19Status: startedFocus: D03 (review), robustness audit, final cycle decision.
## Goals
1. Rerun D03 with a revised operating criterion to recover condom/degenerative coexistence.2. Perform sensitivity stress tests on thresholds (`Phi`, `Loss_U`, ambiguous band).3. Consolidate reproducibility audit on D02/A01/D03.
## Work packages
## WP1 - D03 Revision
- Redefine "ambiguous" class with non-adaptive pre-registered rule.- Compare at least 2 robust classification schemes.- Output: `results_D03_cycle4_v0_1.md`.
## WP2 - Stress/Ablation
- Stress on input noise and distributional shift.- Ablation on proxy components (`jaccard`, `soft_overlap`, `loss_u`).- Output: `stress_ablation_cycle4_v0_1.md`.
## WP3 - Final Audit
- Replay of runs with declared seeds.- Check log consistency and aggregate metrics.- Output: `CYCLE_4_REPORT.md`.
## Cycle 4 exit criterion
- `validated` if global protocol criteria met;- `revise` if partial but not robust evidence;- `reject` if falsified criteria.