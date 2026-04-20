# CYCLE 3 - Benchmark #2 Spec v0.1
Date: 2026-04-18Scopes: D02, A01, D03Status: Pre-recorded, ready to run
## Objective
Define a benchmark #2 that is truly independent of benchmark #1 (Cycle 2),to test out-of-sample robustness of OCT results.
## Mandatory independence criteria
For each theorem (D02, A01, D03), benchmark #2 must respect:
1. `data_independence`: No samples reused from benchmark #1.2. `generator_independence`: different rules/generators from the previous loop.3. `distribution_shift`: different structural distribution (complexity, noise, class balance).4. `context_extension`: Add at least one new context (`Omega_C`).5. `execution_separation`: seed, log and manifest separated by loop 2.
## Benchmark set #2
### D02
- Benchmark ID: `B2_STRUCTURAL_SHIFT_COMMUTATIVE_ORD_2026Q2`- Target samples: 180 classic commutative diagrams- Difference vs B1:- greater compositional depth;- presence of quasi-degenerate borderline cases;- diagrammatic topologies not used in B1.- Contexts: `Omega_A`, `Omega_B`, `Omega_C`- Confirmation criterion:- non-empty class with `Phi_Omega(D)=0_E` exists in at least 2 out of 3 contexts.
### A01
- Benchmark ID: `B2_NOISY_LONGHORIZON_PIPELINE_ORD_2026Q2`- Target samples: 320 multi-step tasks- Difference vs B1:- longer pipelines (average target > 9 steps);- controlled noise injection on intermediate steps;- tasks with non-linear semantic composition.- Contexts: `Omega_A`, `Omega_B`, `Omega_C`- Confirmation criterion:- `E[Delta_cum(P_ord)] < E[Delta_cum(P_cls)]` in at least 2 out of 3 contexts;- `E[Err_sem(P_ord)] < E[Err_sem(P_cls)]` in at least 2 out of 3 contexts.
### D03
- Benchmark ID: `B2_HETEROGENEOUS_FORGETFUL_LOSS_2026Q2`- Target samples: 260 pre/post pairs `U`- Difference vs B1:- expanded forgetting functor classes;- intentional imbalance of families;- cases with local loss but global recovery.- Contexts: `Omega_A`, `Omega_B`, `Omega_C`- Confirmation criterion:- robust coexistence of preservative/degenerative regimes;- "ambiguous" quota below operational threshold (default: < 0.20).
## Pre-recorded operating thresholds
- `alpha_report`: 0.05- `min_context_success`: 2/3 contexts- `max_ambiguous_rate_D03`: 0.20- `max_context_variance_warning`: 0.015
Note: warning thresholds do not falsify a theorem by themselves, but open mandatory audits.
## Required Outputs (Cycle 3)
1. `results_D02_cycle3_v0_1.md`2. `results_A01_cycle3_v0_1.md`3. `results_D03_cycle3_v0_1.md`4. `CYCLE_3_REPORT.md`5. `BENCHMARK_MANIFEST_cycle3_v0_1.md`
## Anti-leakage rules
1. freeze benchmark #2 before running;2. prohibited tuning on final metrics of benchmark #2;3. each rerun must leave a trace with reason and hash log;4. differences compared to benchmark #1 noted in the manifest.
## Post-cycle decision (not yet executed)
After running Cycle 3:- `pass_candidate`: criterion confirmed in at least 2/3 contexts and no serious red flag;- `revise_needed`: mixed criterion or high cross-context instability;- `reject_candidate`: explicit falsification of the pre-registered criterion.