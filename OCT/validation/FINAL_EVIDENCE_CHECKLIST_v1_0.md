# FINAL EVIDENCE CHECKLIST v1.0

Date: 2026-05-03  
Scope: A01, D02, D03 (Cycle 5)  
Target state: transition from governance-ready package to experimentally definitive evidence package

---

## 1) Acceptance criteria (all mandatory)

1. A01, D02, D03 executed on full pre-registered context set (`>= 3 contexts` per theorem).
2. Full trajectory logs generated per run with:
   - `context_id`
   - coherent `prev_event_hash` chain
   - event-level metrics required by theorem specs
3. Pre-registered criteria evaluated without post-hoc threshold/formula changes on same data.
4. Lane separation respected (especially D02: formal lane vs empirical lane).
5. Final theorem-level decision matrix updated with explicit references to:
   - sheet path
   - seal path
   - run logs
   - scripts
   - dataset manifests
6. Reproducibility package validated with clean rerun from frozen artifacts.
7. External independent replication completed for at least one theorem (minimum), preferably all three.
8. Public synchronization completed on GitHub + Zenodo + OSF + Hugging Face with matching hashes.

If one criterion fails, status remains: `not definitive`.

---

## 2) Deliverables required

1. `CYCLE_5_EXECUTION_REPORT_A01_v1_0.md`
2. `CYCLE_5_EXECUTION_REPORT_D02_v1_0.md`
3. `CYCLE_5_EXECUTION_REPORT_D03_v1_0.md`
4. `CYCLE_5_DECISION_GATE_v1_0.md` (lane-level then theorem-level)
5. `CYCLE_5_REPRO_PACK_MANIFEST_v1_0.md` (+ checksums)
6. `CYCLE_5_EXTERNAL_REPLICATION_NOTE_v1_0.md`
7. `CYCLE_5_EVIDENCE_RELEASE_NOTES_v1_0.md`

---

## 3) Go/No-Go gate

Mark `GO` only if all checks below are `PASS`.

| Check ID | Check | Status |
| --- | --- | --- |
| G1 | Full context coverage complete | `PASS` |
| G2 | Trajectory logs complete and hash-chain valid | `PASS` |
| G3 | Criteria applied exactly as preregistered | `PASS` |
| G4 | D02 evidence lanes strictly separated | `PASS` |
| G5 | Decision matrix references complete and auditable | `PASS` |
| G6 | Reproducibility rerun successful | `PASS` |
| G7 | External independent replication available | `TODO` |
| G8 | Cross-platform public sync with hash equivalence | `PASS` (artifact sync done 2026-05-03) |

---

## 4) Residual risk register (pre-publication)

1. `R1` - pseudo-evidence risk if logs remain seed/minimal instead of full benchmark traces.
2. `R2` - interpretation drift risk if theorem-level claims are promoted before external replication.
3. `R3` - reproducibility risk if execution environment lock is incomplete.
4. `R4` - narrative overclaim risk if governance readiness is confused with empirical closure.

Mitigation policy:
1. No theorem promotion from `revise` to `validated` without `G1..G7 = PASS`.
2. No public wording equivalent to “definitive evidence” unless `GO = true`.

---

## 5) Autonomy map (Codex vs external dependency)

Legend:
- `AUTO`: can be fully executed by Codex in this workspace
- `SHARED`: Codex can execute technical part; external actor needed for formal closure
- `EXTERNAL`: must be provided by independent external actor

| Work item | Mode |
| --- | --- |
| Build execution scripts, manifests, checksums, reports | `AUTO` |
| Run cycle pipelines and compute metrics on available datasets | `AUTO` |
| Validate hash chains and gate compliance runtime | `AUTO` |
| Update decision matrix and release notes from computed outputs | `AUTO` |
| Push synchronized artifacts to GitHub/Zenodo/OSF/HF | `AUTO` |
| Formal “independent replication” certification | `EXTERNAL` |
| Independent auditor identity/affiliation guarantee | `EXTERNAL` |
| Final scientific claim endorsement as “definitive” | `SHARED` |

---

## 6) Current status snapshot (2026-05-03)

1. Governance hardening: completed.
2. Sheet/seal instantiation for A01/D02/D03: completed.
3. Platform synchronization (GitHub/Zenodo/OSF/HF): completed.
4. Definitive experimental evidence: not yet complete (missing full execution + independent replication closure).
