# Benchmark Manifest - Cycle 3 v0.1
Freeze date: 2026-04-18Cycle: 3Status: frozen (pre-run)
## Scope
- Theorems: D02, A01, D03- Benchmark type: #2 independent (compared to Cycle 2)- Mandatory contexts: `Omega_A`, `Omega_B`, `Omega_C`
## Dataset/benchmark frozen
### D02
- Benchmark ID: `B2_STRUCTURAL_SHIFT_COMMUTATIVE_ORD_2026Q2`- Target samples: 180- Shift declared: new topologies + quasi-degenerate cases + greater compositional depth- Reuse Cycle 2 samples: `NO`
### A01
- Benchmark ID: `B2_NOISY_LONGHORIZON_PIPELINE_ORD_2026Q2`- Target samples: 320- Shift declared: longer pipelines + controlled noise + non-linear semantic composition- Reuse samples Cycle 2: `NO`
### D03
- Benchmark ID: `B2_HETEROGENEOUS_FORGETFUL_LOSS_2026Q2`- Target samples: 260- Shift declared: expanded functor families + intentional imbalance + global recovery cases- Reuse samples Cycle 2: `NO`
## Preregistration lock
- `alpha_report`: 0.05- `min_context_success`: 2/3- `max_ambiguous_rate_D03`: 0.20- `max_context_variance_warning`: 0.015
## Execution lock
- seed policy: separate from Cycle 2- log namespace: `cycle3/*`- post-freeze tuning: prohibited- rerun policy: reason requirement + hash log
## Operational signature
- Freeze completed: `YES`- Ready to run D02/A01/D03: `YES`