# CYCLE 6 Overview v0.1

Date: 2026-05-05  
Status: specification package (execution not started)  
Scope: A01 real-pipeline validation (promotion path candidate)

## Objective

Run a focused cycle for A01 with independent real implementations, replacing heuristic proxy scoring as theorem-level evidence basis.

Cycle 6 target:
1. Validate (or falsify) A01 through executable pipeline behavior, not synthetic branch formulas.
2. Enforce benchmark independence from `cycle3_inputs`.
3. Preserve v5.3/v5.3.1 governance constraints (ex-ante gate, prereg seal, role separation, cycle budget).
4. Produce an externally auditable release pack for A01.

## Why Cycle 6 exists

Round-4 external audit established:
1. A01 heuristic proxy mode is non-promotable by policy.
2. Stress test (`0/135`) shows structural non-testability for process-only advantage in current proxy family.
3. A01 promotion requires real pipeline implementations (`P_cls` and `P_ord`) on independent benchmark data.

## Required gate artifacts before execution

1. Filled `OCT_PROXY_PREVALIDATION_SHEET_v0_1.md` instance for A01.
2. Valid prereg seal JSON for A01 with entry/exit signature fields.
3. Locked benchmark manifest with non-overlap proof vs `cycle3_inputs`.
4. Independent auditor designation (primary: Solomon, secondary: TBD external reviewer).

If any artifact is missing, cycle status is `blocked`.

## Cycle 6 spec files

1. `CYCLE_6_A01_REAL_PIPELINES_SPEC_v0_1.md`
2. `CYCLE_6_EXECUTION_AND_REJECT_RULES_v0_1.md`
3. `CYCLE_6_BENCHMARK_INDEPENDENCE_PROTOCOL_v0_1.md`
4. `CYCLE_6_EXTERNAL_AUDIT_PLAN_v0_1.md`
5. `CYCLE_6_PREREG_SEAL_TEMPLATE_v0_1.md`

## Output contract (when executed)

Required outputs:
1. `CYCLE_6_2026-05-05/trajectory/A01_trajectory_events.jsonl`
2. `CYCLE_6_2026-05-05/results/A01_real_pipeline_metrics_v1_0.json`
3. `CYCLE_6_EXECUTION_REPORT_A01_v1_0.md`
4. `CYCLE_6_DECISION_GATE_v1_0.md`
5. `CYCLE_6_REPRO_PACK_MANIFEST_v1_0.md`
6. `CYCLE_6_EXTERNAL_REPLICATION_NOTE_v1_0.md`

