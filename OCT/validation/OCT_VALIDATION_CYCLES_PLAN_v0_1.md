# OCT Validation Cycles Plan v0.1
Date: 2026-04-16Objective: Complete pre-publication validation of theorems in `in_proof`.
## How many cycles are needed
### Realistic minimum: **4 cycles**
Why:- the protocol requires at least 2 independent benchmarks;- requires replication in at least 2 contexts `Omega`;- requires reproducible logs and final decision.
With 4 cycles we get:1. Cycle 1: pilot (formal + setup) [completed]2. Cycle 2: Independent Benchmark #1 [completed - 2026-04-17]3. Cycle 3: independent benchmark #2 + cross-context replication [completed - 2026-04-19, mixed result]4. Cycle 4: stress/ablation + reproducibility audit + decision `validated/revise` [completed - 2026-04-19, decision matrix pending consolidation]
## Cycle-by-cycle plan
## Cycle 1 (completed)
Scopes: D02, A01Output: formal/operational readiness, no `validated`.
## Cycle 2 (completed)
Scopes: D02, A01, D03Outputs:- quantitative results benchmark #1 on D02/A01/D03;- PASS outcome for the three theorems in the cycle;- no promotion to `validated` (global criteria still incomplete).
## Cycle 3 (completed)
Scope: D02, A01, D03, A02Outputs:- benchmark #2 completed on D02/A01/D03 with `Omega_A/B/C` replication;- D02: PASS;- A01: PASS;- D03: REVISE_NEEDED;- closed cycle report with gate conditional on revision D03 in Cycle 4.
## Cycle 4 (completed)
Scope: D04, A03 + final audit on the entire in_proof block.Expected output:- stress tests and limit analysis;- final decision for each theorem: `validated/revise/reject`.
Outputs:- D03 revision completed (`results_D03_cycle4_v0_1.md`);- threshold stress completed (`stress_ablation_cycle4_v0_1.md`);- reproducibility audit completed (`audit_repro_cycle4_v0_1.md`, PASS outcome);- closed cycle report (`CYCLE_4_REPORT.md`, completed status);- final consolidation of theorem decisions left to the next step.- decision matrix phase 1 started (`DECISION_MATRIX_phase1_v0_1.md`).- decision consolidation completed with unified baseline (`DECISION_MATRIX_FINAL_UNIFIED_v0_1.md`).- formal basic freeze completed in candidate mode (`OCT_V1_0_FREEZE_CANDIDATE_v0_1.md`).- final editing started (`OCT_EDITORIAL_PLAN_v1_0_candidate_v0_1.md`).- notational standardization pass 1 completed on `OCT_FOUNDATIONAL_OPERA_DRAFT_v0_8.md`.
## Operational note
If the benchmarks are already ready and clean, some theorems can close in 3 cycles.For a robust foundational release, the recommendation remains **4 cycles**.