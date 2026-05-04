# OCT Proxy Pre-Validation Sheet v0.1

Date: 2026-05-03
Prepared by (proxy designer): Fabio Ghioni
Audited by (independent auditor): Solomon
Theorem ID: D02
Claim ID: D02
Claim source (chapter/section): Chapter 10 / D02
Cycle ID candidate: CYCLE_5_2026-05-01
Status: pass

## 1) Claim logical type

Select one:
- existential

Expected dominant anti-pattern risk:
- existential -> vacuum-pass structural

## 1.1) Cycle budget control (anti-p-hacking)

Max independent cycles for this claim: 3
Current cycle sequence index: 1
Budget policy status: within_budget

## 2) Claim statement and falsifier statement

Claim (verbatim):
There exist classically commutative diagrams with Phi=0 under OCT constraints.

Primary falsifier (what would disconfirm it):
No reachable disconfirming configuration exists under the proxy design.

Secondary falsifier(s):
Commutativity assigned by construction without verification.

## 3) Concept-to-observable mapping table

Mandatory: every proxy variable must map to a formal concept with rationale.

| Proxy element (code variable/formula) | OCT concept target | Mapping rationale (chapter/def) | Observable source | Label (O/P/C) |
| --- | --- | --- | --- | --- |
| is_commutative | syntactic commutativity | classical commutative check | diagram checker | O |
| Phi_proxy | functional emergence axis | Chapter 8 functional axis | execution trace + semantic anchor | P |
| fail_config_reachable | falsifiability reachability | ex-ante gate requirement | prereg context list | O |

Rules:
1. No unnamed proxy term is allowed.
2. No concept can be declared as measured if mapping is missing.
3. Labels must follow: O=operational, P=operationalizable, C=conceptual only.

## 4) Anti-pattern prevention checks (mandatory)

### 4.1 Comparative claim guard (level-shift test)

If claim type is comparative, show that A/B differs in process, not only output scoring.

Process-level evidence planned:
not applicable

Output-only fallback present? no

If yes, why it is non-decisive and how it is constrained:
not applicable

### 4.2 Taxonomic claim guard (post-hoc rescue lock)

Pre-registered variables:
is_commutative, Phi_proxy

Pre-registered thresholds:
reachability of both confirming and disconfirming configurations

Policy lock:
- no criterion/threshold change on same data after first fail
- any revision requires new preregistration + new data split or new cycle

Lock accepted: yes

### 4.3 Existential claim guard (vacuum-pass test)

Show at least one concrete, realistic configuration where claim must fail under this proxy if phenomenon is absent.

Concrete fail configuration:
explicit non-commutative candidate set under same proxy instrumentation.

Why reachable:
included as mandatory context in D02 context set.

If not reachable, mark sheet as fail.

### 4.4 Universal claim guard (trivial confirmation lock)

If claim type is universal, show reachable counterexample strategy.

Concrete reachable counterexample search strategy:
not applicable (claim type is existential)

Confirmation is not tautological by construction? yes

## 5) Falsifiability reachability test

Required before run:
1. At least one executable input bundle expected to produce fail.
2. At least one executable input bundle expected to produce pass.
3. Decision boundary is pre-registered and immutable for this cycle.

Pass/fail of reachability test:
pass

Evidence artifact paths:
- OCT/validation/CYCLE_5_2026-05-01/contexts/D02_contexts_v0_1.md
- OCT/validation/CYCLE_5_2026-05-01/CYCLE_5_D02_EVIDENCE_CLASS_SPEC_v0_1.md

### 5.1 Pre-registered context list (mandatory when using multi-context criteria)

| context_id | Distinguishing features | Expected difficulty | Dataset slice |
| --- | --- | --- | --- |
| D02_CTX_01 | formal pilot diagrams | low | datasets/cycle3_inputs/d02_formal_a |
| D02_CTX_02 | empirical structured diagrams | medium | datasets/cycle3_inputs/d02_empirical_b |
| D02_CTX_03 | stress diagrams with perturbation | high | datasets/cycle3_inputs/d02_stress_c |

## 6) Validity space coverage declaration (Coh/Phi/Delta)

Declare explicitly what is measured vs not measured:

| Axis | Measured? (yes/no) | Operational definition used | Path to code/report |
| --- | --- | --- | --- |
| Coh | partial | structural stability proxy in lane-specific checks | CYCLE_5_D02_EVIDENCE_CLASS_SPEC_v0_1.md |
| PhiHat | partial | Phi proxy via mapped observables | CYCLE_5_D02_EVIDENCE_CLASS_SPEC_v0_1.md |
| Delta | no | not primary for D02 existential claim | CYCLE_5_D02_EVIDENCE_CLASS_SPEC_v0_1.md |

If any axis is not measured, interpretation limits must be declared here:
No theorem-level claim expansion beyond D02 existential scope.

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
- preregistration artifact path: OCT/validation/CYCLE_5_2026-05-01/seals/D02_PREREG_SEAL_v0_1.json
- checksum/hash: declared in seal payload
- timestamp (UTC): 2026-05-03T08:40:00Z
- immutable storage location: 10.5281/zenodo.19959724
- seal method: zenodo_doi
- contexts hash: declared in seal payload
- auditor independence declared (yes/no): yes
- gate-entry signature: declared in seal payload
- gate-entry timestamp (UTC): declared in seal payload
- gate-exit signature: declared in seal payload
- gate-exit timestamp (UTC): declared in seal payload
- gate-exit status: declared in seal payload

Seal valid: yes

## 10) Gate decision

Decision options:
- PASS (cycle execution allowed)
- FAIL (cycle blocked, redesign required)
- HOLD (claim clarification required before proxy design)

Decision: PASS

Decision rationale (short, technical):
Existential claim has reachable disconfirming configuration and lane split lock.

Signer (auditor): Solomon
Date: 2026-05-03

