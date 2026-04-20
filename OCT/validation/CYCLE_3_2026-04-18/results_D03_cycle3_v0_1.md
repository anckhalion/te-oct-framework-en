# Results D03 - Cycle 3 (Benchmark #2)
Theorem: D03 - Ontological loss of forgetting functorsCycle date: 2026-04-19Cycle type: independent benchmark #2 (UD-EWT, scoring proxy)
## Benchmarks and setup
- Benchmark ID: `B2_HETEROGENEOUS_FORGETFUL_LOSS_2026Q2`- Dataset: UD English EWT (260 pairs)- Contexts: `Omega_A`, `Omega_B`, `Omega_C`- Input used: `datasets/cycle3_inputs/D03.csv`
## Main findings
| Class | `Omega_A` | `Omega_B` | `Omega_C` | Average || --- | ---: | ---: | ---: | ---: |
| Condom | 0.0000 | 0.0000 | 0.0000 | 0.0000 || Degenerative | 0.7011 | 0.6322 | 0.5930 | 0.6421 || Ambiguous | 0.2989 | 0.3678 | 0.4070 | 0.3579 |
## Cross-context stability
- Global ambiguous rate: 0.3577- Coexistence of condom/degenerative regimes in all contexts: **NO**
## Interpretation
In the current benchmark #2 the degenerative regime prevails and a preservative class does not emergerobust. This does not satisfy the pre-registered D03 criterion of coexistence of the two regimes.
## Decision
- Cycle 3 outcome for D03: **REVISE_NEEDED**- Theorem status: **in_proof** (setup/operational criterion review required before Cycle 4)