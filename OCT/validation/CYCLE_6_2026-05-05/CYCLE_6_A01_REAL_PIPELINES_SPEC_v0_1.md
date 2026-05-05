# CYCLE 6 A01 Real Pipelines Spec v0.1

Date: 2026-05-05  
Theorem: A01  
Cycle ID: `CYCLE_6_2026-05-05`  
Evidence mode: `real_pipeline_execution`

## 1) Claim target

Claim:
Compositional pipelines with high ordinative coherence can show process-level quality advantage without requiring output-score inflation.

Primary falsifier:
No process-level advantage is observed under matched-output constraints in independent contexts.

## 2) Execution architecture

Two independent implementations must exist:
1. `P_cls`: classical-validity-only pipeline.
2. `P_ord`: ordinative pipeline with explicit coherence gate.

Independence constraints:
1. No shared scoring function for trajectory quality.
2. Shared input contract only (same tasks/contexts), but distinct decision logic modules.
3. Separate code paths in repository and separate lock hashes.

## 3) Context set

Minimum:
1. `CTX_A` low perturbation
2. `CTX_B` medium perturbation
3. `CTX_C` high perturbation

Each context must be represented by benchmark data declared independent from `cycle3_inputs`.

## 4) Primary metrics (pre-registered)

For each context and each pipeline:
1. `Delta_cum`
2. `Err_sem_final`
3. `mean_Coh_trajectory`
4. `trajectory_length`
5. `reject_rate`

Matched-output indicator:
`abs(Err_sem_final_ord - Err_sem_final_cls) <= eps_err_match`

Default threshold:
`eps_err_match = 0.01`

Process-advantage indicator:
`mean_Coh_trajectory_ord - mean_Coh_trajectory_cls >= eps_coh_adv`

Default threshold:
`eps_coh_adv = 0.03`

## 5) Decision criteria

`pass_candidate` requires all:
1. At least `2/3` contexts with `Delta_cum_ord < Delta_cum_cls`.
2. At least `2/3` contexts with `mean_Coh_trajectory_ord > mean_Coh_trajectory_cls`.
3. At least one matched-output subset (`Err diff <= eps_err_match`) in at least `2/3` contexts.
4. In matched-output subsets, process advantage holds (`Coh diff >= eps_coh_adv`) in at least `2/3` contexts.
5. No gate/policy violation.

`revise_needed`:
1. Criteria partially satisfied but no reject trigger.

`reject_candidate`:
1. Any hard reject trigger from execution rules.

## 6) Non-promotable conditions

Cycle 6 is non-promotable if any occurs:
1. Heuristic proxy branch formula is reused as decision basis.
2. Benchmark independence proof is missing.
3. `P_cls` and `P_ord` are not implementation-distinct.
4. Lane/report artifacts are incomplete.

## 7) Mandatory artifacts

1. `instances/A01_OCT_PROXY_PREVALIDATION_SHEET_v0_1.md`
2. `seals/A01_PREREG_SEAL_v0_1.json`
3. `claim_locks/A01_claim_lock_v0_1.md`
4. `threshold_locks/A01_thresholds_lock_v0_1.md`
5. `formula_locks/A01_formula_lock_v0_1.md`
6. `dataset_manifests/A01_dataset_manifest_v0_1.md`
7. `script_locks/A01_script_lock_v0_1.md`
8. `contexts/A01_contexts_v0_1.md`

