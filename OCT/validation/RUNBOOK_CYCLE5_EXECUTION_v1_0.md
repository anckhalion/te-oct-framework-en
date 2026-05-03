# RUNBOOK CYCLE 5 EXECUTION v1.0

Date: 2026-05-03  
Scope: operational execution for A01, D02, D03 under v5.3.1 governance hardening

---

## 1) Objective

Produce non-minimal, auditable benchmark evidence for Cycle 5 and generate theorem-level decision artifacts aligned with prereg locks.

---

## 2) Preconditions

1. Repo state pinned to a known commit.
2. Gate artifacts in place:
   - `CYCLE_5_2026-05-01/instances/*.md`
   - `CYCLE_5_2026-05-01/seals/*.json`
   - `runtime/check_gate_compliance.py`
3. Local runtime dependencies installed for execution scripts.
4. Dataset manifests frozen and checksummed.

Blocking rule:
- If preconditions fail, execution status = `blocked`.

---

## 3) Execution phases

## Phase A - Lock verification (mandatory)

1. Run governance checker.
2. Verify `compliant=true`.
3. Persist checker output as immutable run artifact.

Expected output:
- `OCT/validation/runtime/compliance_report_v0_1.json`

---

## Phase B - A01 full run

1. Execute both pipelines:
   - `P_cls`
   - `P_ord`
2. Run all preregistered A01 contexts.
3. Collect full trajectory events (not seed-only).
4. Compute:
   - `Delta_cum`
   - `Err_sem_final`
   - `mean_Coh_trajectory`
5. Evaluate A01 pass/reject/revise criteria exactly as spec.

Required outputs:
1. `CYCLE_5_2026-05-01/trajectory/A01_trajectory_events.jsonl` (full)
2. `CYCLE_5_2026-05-01/results/A01_metrics_v1_0.json`
3. `CYCLE_5_EXECUTION_REPORT_A01_v1_0.md`

---

## Phase C - D02 full run (lane-separated)

1. Execute formal lane (L2) and empirical lane (L1) independently.
2. Keep lane metrics and decisions separated end-to-end.
3. Verify no evidence-class collapse.
4. Evaluate existential claim with reachable disconfirming configuration.

Required outputs:
1. `CYCLE_5_2026-05-01/trajectory/D02_trajectory_events.jsonl` (full)
2. `CYCLE_5_2026-05-01/results/D02_metrics_formal_v1_0.json`
3. `CYCLE_5_2026-05-01/results/D02_metrics_empirical_v1_0.json`
4. `CYCLE_5_EXECUTION_REPORT_D02_v1_0.md`

---

## Phase D - D03 full run (locked taxonomy)

1. Execute paired pre/post data with explicit `U` mapping.
2. Apply fixed formula:
   - `Loss_index = 0.5 * abs(Delta_Coh) + 0.5 * abs(Delta_Phi)`
3. Keep fixed thresholds (`t_low`, `t_high`, `max_ambiguous_rate`) preregistered.
4. Evaluate class reachability and ambiguous share criteria.

Required outputs:
1. `CYCLE_5_2026-05-01/trajectory/D03_trajectory_events.jsonl` (full)
2. `CYCLE_5_2026-05-01/results/D03_metrics_v1_0.json`
3. `CYCLE_5_EXECUTION_REPORT_D03_v1_0.md`

---

## Phase E - Decision and release pack

1. Compile lane-level decisions first.
2. Derive theorem-level decision only after lane checks.
3. Update decision matrix with traceable references.
4. Build reproducibility package and checksums.

Required outputs:
1. `CYCLE_5_DECISION_GATE_v1_0.md`
2. `CYCLE_5_REPRO_PACK_MANIFEST_v1_0.md`
3. `CYCLE_5_EVIDENCE_RELEASE_NOTES_v1_0.md`

---

## 4) Minimal command sequence

```powershell
python OCT/validation/runtime/check_gate_compliance.py
```

Then run theorem execution scripts (to be pinned in script locks) and re-run:

```powershell
python OCT/validation/runtime/check_gate_compliance.py
```

Post-run requirement:
- checker output remains compliant and trajectory timestamp precedence is valid.

---

## 5) Quality gates

1. `QG1`: full-context coverage achieved per theorem.
2. `QG2`: no post-hoc lock violation.
3. `QG3`: lane separation preserved in D02.
4. `QG4`: hash-chain integrity in all trajectory logs.
5. `QG5`: theorem decision justified by prereg criteria only.
6. `QG6`: reproducibility rerun succeeds from frozen package.

If any gate fails -> theorem status cannot be promoted.

---

## 6) Autonomy matrix for this runbook

`AUTO` tasks Codex can execute alone:
1. Build/run scripts and collect metrics from available data.
2. Generate full trajectory logs and integrity checks.
3. Produce reports, manifests, checksums, decision artifacts.
4. Synchronize final artifacts across GitHub/Zenodo/OSF/HF.

`SHARED` tasks (Codex + external counterpart):
1. Sign-off on wording for public claims.
2. Final publication narrative and positioning.

`EXTERNAL` tasks:
1. Independent replication by non-internal team.
2. External auditor independence certification.

---

## 7) Definition of done (experimental)

Cycle 5 is experimentally complete only if:
1. A01, D02, D03 full runs completed on prereg contexts.
2. All `QG1..QG6` pass.
3. External replication note exists and is non-self-referential.
4. `FINAL_EVIDENCE_CHECKLIST_v1_0.md` marked `GO`.
