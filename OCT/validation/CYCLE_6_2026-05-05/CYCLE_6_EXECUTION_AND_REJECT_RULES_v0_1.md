# CYCLE 6 Execution and Reject Rules v0.1

Date: 2026-05-05  
Cycle: `CYCLE_6_2026-05-05`  
Scope: A01 only

## 1) Execution order (fixed)

1. Run governance compliance check.
2. Verify dataset independence proof.
3. Run `P_cls` on all contexts.
4. Run `P_ord` on all contexts.
5. Build full trajectory logs.
6. Compute pre-registered metrics.
7. Produce decision artifact.

No permutation of step order is allowed without new preregistration.

## 2) Hard reject triggers

Any trigger below sets theorem decision to `reject_candidate`:
1. Reuse of synthetic proxy formula as decisive metric source.
2. Missing context coverage (`< 3` contexts executed).
3. Benchmark overlap with `cycle3_inputs` above allowed limit (`> 0` record-level overlap by ID/hash).
4. Missing hash-chain integrity in trajectory logs.
5. Post-hoc threshold/criterion change after first failed evaluation.
6. Role-separation failure (`designer == auditor`).
7. Gate-entry or gate-exit signature invalid/missing.

## 3) Soft fail / revise triggers

If no hard reject is triggered, mark `revise_needed` when:
1. Fewer than `2/3` contexts satisfy process advantage criteria.
2. Matched-output subsets exist in fewer than `2/3` contexts.
3. Metrics are complete but insufficient for promotion.

## 4) Integrity checks

Required integrity checks:
1. All reports reference exact script-lock hashes.
2. Seal timestamp is earlier than first trajectory event.
3. Decision criteria are evaluated from pre-registered thresholds only.
4. Final report includes explicit non-claim section.

## 5) Output naming contract

1. `results/A01_real_pipeline_metrics_v1_0.json`
2. `trajectory/A01_trajectory_events.jsonl`
3. `CYCLE_6_EXECUTION_REPORT_A01_v1_0.md`
4. `CYCLE_6_DECISION_GATE_v1_0.md`
5. `CYCLE_6_REPRO_PACK_MANIFEST_v1_0.md`

