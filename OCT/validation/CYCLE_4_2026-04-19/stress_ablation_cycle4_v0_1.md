# Stress And Ablation - Cycle 4 v0.1
Date: 2026-04-19Scope: sensitivity thresholds D03 (`loss_u`) on benchmark Cycle 3 input.
## Setup
- Stress script: `datasets/cycle4_work/run_d03_threshold_stress.py`- Input: `datasets/cycle3_inputs/D03.csv`- Tested grid:- `low` in {0.272, 0.274, 0.276, 0.278}- `high` in {0.284, 0.286, 0.288}
## Global outcome
- Evaluated combinations: 12- Combinations with complete coexistence (`preservativo` and `degenerativo` in all contexts): 12/12- Combinations with `ambiguous_rate < 0.20`: 9/12
## Robust configurations (selection)
| low | high | ambiguous_rate | Coexistence || ---: | ---: | ---: | --- |
| 0.276 | 0.284 | 0.1077 | YES || 0.276 | 0.286 | 0.1385 | YES || 0.278 | 0.284 | 0.0769 | YES || 0.278 | 0.286 | 0.1077 | YES |
## Interpretation
The D03 revision does not depend on a single point: there is a stable region of thresholdswith multi-context coexistence and sub-threshold ambiguity.
Raw Output:- `datasets/cycle4_outputs/d03_threshold_stress.json`- `datasets/cycle4_outputs/d03_threshold_stress.csv`