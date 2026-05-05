# RUNBOOK CYCLE 6 EXECUTION v0.1

Date: 2026-05-05  
Scope: A01 real-pipeline execution under v5.3.x governance

## 1) Objective

Produce promotable-or-falsifying evidence for A01 using real implementation behavior on an independent benchmark.

## 2) Preconditions

1. Cycle 6 spec package committed.
2. A01 gate sheet + seal compiled and valid.
3. Independent benchmark manifest + overlap proof available.
4. Script locks frozen with SHA-256 hashes.
5. Primary and secondary auditors declared.

Blocking rule:
If any precondition fails -> status `blocked`.

## 3) Minimal execution sequence

1. `python OCT/validation/runtime/check_gate_compliance.py`
2. Run `P_cls` and `P_ord` on all contexts.
3. Build trajectory logs and metrics.
4. Re-run `check_gate_compliance.py`.
5. Generate decision/report/repro artifacts.

## 4) Quality gates

1. `QG1`: benchmark independence = pass.
2. `QG2`: full-context coverage (>= 3 contexts).
3. `QG3`: no reject trigger activated.
4. `QG4`: decision criteria replayable from prereg thresholds.
5. `QG5`: two external audit notes available before promotion.

## 5) Definition of done

Cycle 6 is complete when:
1. A01 run is finished with full artifact set.
2. Governance checker remains compliant.
3. External audits are published.
4. Decision gate is finalized as `pass_candidate`, `revise_needed`, or `reject_candidate`.

