# OCT Proxy Pre-Validation Sheet v0.1

Date: 2026-05-03
Prepared by (proxy designer): Fabio Ghioni
Audited by (independent auditor): Solomon
Theorem ID: A01
Claim source (chapter/section): Chapter 10 / A01
Cycle ID candidate: CYCLE_5_2026-05-01
Status: pass

## 1) Claim logical type

Select one:
- comparative

Expected dominant anti-pattern risk:
- comparative -> level-shift

## 2) Claim statement and falsifier statement

Claim (verbatim):
Compositional pipelines with high ordinative coherence show lower semantic degeneration than classically valid-only pipelines.

Primary falsifier (what would disconfirm it):
No process-level advantage on Delta_cum, Err_sem_final, and mean_Coh_trajectory in at least 2/3 contexts.

Secondary falsifier(s):
Output-only advantage without trajectory-quality advantage.

## 3) Concept-to-observable mapping table

Mandatory: every proxy variable must map to a formal concept with rationale.

| Proxy element (code variable/formula) | OCT concept target | Mapping rationale (chapter/def) | Observable source | Label (O/P/C) |
| --- | --- | --- | --- | --- |
| mean_Coh_trajectory | Coh | Chapter 8 validity axis | trajectory logs | O |
| Delta_cum | Delta | Chapter 8 degradation axis | trajectory logs | O |
| Err_sem_final | Phi-related functional degeneration proxy | Chapter 8 functional validity | benchmark anchors | P |

Rules:
1. No unnamed proxy term is allowed.
2. No concept can be declared as measured if mapping is missing.
3. Labels must follow: O=operational, P=operationalizable, C=conceptual only.

## 4) Anti-pattern prevention checks (mandatory)

### 4.1 Comparative claim guard (level-shift test)

If claim type is comparative, show that A/B differs in process, not only output scoring.

Process-level evidence planned:
append-only trajectory traces with Coh/Phi/Syn/decision per step.

Output-only fallback present? no

If yes, why it is non-decisive and how it is constrained:
not applicable

### 4.2 Taxonomic claim guard (post-hoc rescue lock)

Pre-registered variables:
Delta_cum, Err_sem_final, mean_Coh_trajectory

Pre-registered thresholds:
at least 2/3 contexts for each primary criterion

Policy lock:
- no criterion/threshold change on same data after first fail
- any revision requires new preregistration + new data split or new cycle

Lock accepted: yes

### 4.3 Existential claim guard (vacuum-pass test)

Show at least one concrete, realistic configuration where claim must fail under this proxy if phenomenon is absent.

Concrete fail configuration:
P_ord forced to emulate P_cls decisions under ablation.

Why reachable:
ablation mode is executable by construction in Cycle 5 plan.

If not reachable, mark sheet as fail.

### 4.4 Universal claim guard (trivial confirmation lock)

If claim type is universal, show reachable counterexample strategy.

Concrete reachable counterexample search strategy:
not applicable (claim type is comparative)

Confirmation is not tautological by construction? yes

## 5) Falsifiability reachability test

Required before run:
1. At least one executable input bundle expected to produce fail.
2. At least one executable input bundle expected to produce pass.
3. Decision boundary is pre-registered and immutable for this cycle.

Pass/fail of reachability test:
pass

Evidence artifact paths:
- OCT/validation/CYCLE_5_2026-05-01/contexts/A01_contexts_v0_1.md
- OCT/validation/CYCLE_5_2026-05-01/CYCLE_5_A01_PROCESS_LEVEL_SPEC_v0_1.md

### 5.1 Pre-registered context list (mandatory when using multi-context criteria)

| context_id | Distinguishing features | Expected difficulty | Dataset slice |
| --- | --- | --- | --- |
| A01_CTX_01 | short synthetic chains, low noise | low | datasets/cycle3_inputs/case_a |
| A01_CTX_02 | mixed synthetic-external traces, medium noise | medium | datasets/cycle3_inputs/case_b |
| A01_CTX_03 | longer external trajectories, perturbation stress | high | datasets/cycle3_inputs/case_c |

## 6) Validity space coverage declaration (Coh/Phi/Delta)

Declare explicitly what is measured vs not measured:

| Axis | Measured? (yes/no) | Operational definition used | Path to code/report |
| --- | --- | --- | --- |
| Coh | yes | mean_Coh_trajectory over effective transitions | CYCLE_5_A01_PROCESS_LEVEL_SPEC_v0_1.md |
| PhiHat | partial | Err_sem_final as bounded proxy | CYCLE_5_A01_PROCESS_LEVEL_SPEC_v0_1.md |
| Delta | yes | Delta_cum | CYCLE_5_A01_PROCESS_LEVEL_SPEC_v0_1.md |

If any axis is not measured, interpretation limits must be declared here:
Phi is proxied and cannot be over-interpreted as full Phi formalization.

## 7) Evidence class declaration

Select one:
- L1 empirical external

Accumulation rule reminder:
- evidence classes are not auto-additive
- cross-class accumulation requires explicit matrix logic

## 8) Role separation confirmation

Proxy designer and proxy auditor must be different.

Designer: Fabio Ghioni
Auditor: Solomon
Confirmed different identities: yes
Auditor co-authorship with designer in last 24 months: no
If yes, list:
none
Auditor school-of-thought affiliation declaration:
external critical reviewer with independent audit stance

## 9) Preregistration seal

Required fields:
- preregistration artifact path: OCT/validation/CYCLE_5_2026-05-01/seals/A01_PREREG_SEAL_v0_1.json
- checksum/hash: declared in seal payload
- timestamp (UTC): 2026-05-03T08:30:00Z
- immutable storage location: 10.5281/zenodo.19959724
- seal method: zenodo_doi
- contexts hash: declared in seal payload
- auditor independence declared (yes/no): yes

Seal valid: yes

## 10) Gate decision

Decision options:
- PASS (cycle execution allowed)
- FAIL (cycle blocked, redesign required)
- HOLD (claim clarification required before proxy design)

Decision: PASS

Decision rationale (short, technical):
Comparative claim is process-anchored, falsifiability is reachable, and prereg lock is explicit.

Signer (auditor): Solomon
Date: 2026-05-03

