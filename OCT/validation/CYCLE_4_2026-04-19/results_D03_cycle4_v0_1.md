# Results D03 - Cycle 4 (Revision Stress)
Theorem: D03 - Ontological loss of forgetting functorsDate: 2026-04-19Objective: recover robust coexistence `preservativo/degenerativo` with non-adaptive rule.
## Input and method
- Input: `datasets/cycle3_inputs/D03.csv` (260 pairs)- Script: `datasets/cycle4_work/run_d03_revision_cycle4.py`- Tested fixed schemes:- `S1_primary_fixed_band`: `loss_u <= 0.276` condom, `loss_u >= 0.284` degenerative, otherwise ambiguous.- `S2_robust_wide_band`: `loss_u <= 0.274` condom, `loss_u >= 0.286` degenerative, otherwise ambiguous.
## Comparative outcome
| Scheme | Condom | Degenerative | Ambiguous | Ambiguous rate | Coexistence in `Omega_A/B/C` || --- | ---: | ---: | ---: | ---: | --- |
| `S1_primary_fixed_band` | 74 | 158 | 28 | 0.1077 | YES || `S2_robust_wide_band` | 66 | 150 | 44 | 0.1692 | YES |
## Selected scheme detail (S1)
| Context | Condom | Degenerative | Ambiguous || --- | ---: | ---: | ---: |
| `Omega_A` | 0.2644 | 0.6552 | 0.0805 || `Omega_B` | 0.2989 | 0.6092 | 0.0920 || `Omega_C` | 0.2907 | 0.5581 | 0.1512 |
## Interpretation
The Cycle 4 revision resolves the critical point that emerged in Cycle 3:- coexistence of the two regimes in all contexts;- ambiguous band below operational threshold (`< 0.20`) in the primary scheme.
## Decision
- Result D03 Cycle 4 (revision): **PASS_REVISED_CANDIDATE**- Theorem status: **in_proof** (waiting for Cycle 4 final audit closure)