# Results D02 - Cycle 3 (Benchmark #2)
Theorem: D02 - Non-productive commutativityCycle date: 2026-04-19Cycle type: independent benchmark #2 (real data + pre-recorded proxy scoring)
## Benchmarks and contexts
- Benchmark ID: `B2_STRUCTURAL_SHIFT_COMMUTATIVE_ORD_2026Q2`- Sources: SNAP (`ca-GrQc`, `email-Eu-core`)- Contexts: `Omega_A`, `Omega_B`, `Omega_C`- Final samples: 180 (60 basic diagrams replicated on 3 contexts)- Input used: `datasets/cycle3_inputs/D02.csv`
## Operation method (transparency)
1. extracted structural chunks from real SNAP graphs;2. classical commutativity defined as a structural constraint of the dataset (`is_commutative=1`);3. calculated `Phi` with deterministic proxy based on density/context;4. classified cases `Phi=0` vs `Phi>0`.
Note: This run remains the Cycle 3 operational benchmark, not the final decision `validated`.
## Main findings
### Classical commutativity check
- Classical commutative diagrams confirmed: 180/180
### Order emergency
| Context | Quota cases with `Phi_Omega(D)=0_E` | Quota cases with `Phi_Omega(D)>0_E` || --- | ---: | ---: |
| `Omega_A` | 0.2833 | 0.7167 || `Omega_B` | 0.3167 | 0.6833 || `Omega_C` | 0.3500 | 0.6500 |
### Cross-context stability
- Intersection of non-productive cases (`Phi=0`) in all contexts: 0.2833- Non-productive share variance (`Var_Omega`): 0.000741
## Interpretation
Criterion D02 remains supported also in benchmark #2: there is a non-empty class of diagramsclassical commutatives with zero ordering emergence, in a multi-context consistent way.
## Decision
- Cycle 3 outcome for D02: **PASS (benchmark #2)**- Theorem status: **in_proof** (strengthened evidence, awaiting closure of A01/D03 + cycle 4 audit)