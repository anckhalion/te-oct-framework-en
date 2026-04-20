# Results D03 - Cycle 2 (Benchmark #1)
Theorem: D03 - Ontological loss of forgetting functorsCycle date: 2026-04-17Cycle Type: Independent Benchmark #1 (Controlled/Synthetic)
## Cycle objective
Verify that loss induced by forgetting functors can be separatedin two distinct regimes:1. condom;2. degenerative.
## Benchmarks and setup
- Benchmark ID: `B1_SYNTH_FORGETFUL_LOSS_2026Q2`- Benchmark nature: controlled, synthetic, reproducible (not yet external dataset)- Pre/post pairs `U`: 180- Forgetting functor families: 5- Observational contexts: `Omega_A`, `Omega_B`- Measurements: `Loss_U`, `Delta_Omega`, variation of `Phi_Omega`
## Class operating policy
- Condom: formal loss does not lead to organizational collapse (`Phi` remains above the minimum threshold).- Degenerative: formal loss leads to orderly collapse (`Phi` drops to zero or almost zero regime).- Ambiguous: extreme case that cannot be robustly classified.
## Main results
| Class | `Omega_A` | `Omega_B` | Average || --- | ---: | ---: | ---: |
| Condom | 0.561 | 0.539 | 0.550 || Degenerative | 0.344 | 0.356 | 0.350 || Ambiguous | 0.095 | 0.105 | 0.100 |
### Cross-context stability
- Absolute difference in share per class (`Omega_A` vs `Omega_B`): max 0.022- `Var_Omega` average on class shares: 0.00014
## Interpretation
Benchmark #1 supports D03: the two regimes (condom/degenerative)they coexist stably and do not collapse into a single class.
## Loop limits
1. still synthetic benchmark;2. definition of class thresholds to stress on benchmark #2;3. lacks replication on noisy/unbalanced distributions.
## Decision
- Cycle 2 outcome for D03: **PASS (benchmark #1)**- Theorem status: **in_proof** (strengthened evidence, not yet `validated`)- Subsequent action: benchmark #2 + threshold sensitivity analysis in Cycle 3.
