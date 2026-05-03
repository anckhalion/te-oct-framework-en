# OCT Proxy Pre-Validation Sheet v0.1

Date: 2026-05-03
Prepared by (proxy designer): Fabio Ghioni
Audited by (independent auditor): Solomon
Theorem ID: D03
Claim source (chapter/section): Chapter 10 / D03
Cycle ID candidate: CYCLE_5_2026-05-01
Status: pass

## 1) Claim logical type

Select one:
- taxonomic

Expected dominant anti-pattern risk:
- taxonomic -> post-hoc rescue

## 2) Claim statement and falsifier statement

Claim (verbatim):
Informational loss of forgetful functors is classifiable into preservative vs degenerative regimes.

Primary falsifier (what would disconfirm it):
Class partition collapses or requires threshold/formula switch on same data after first fail.

Secondary falsifier(s):
One class structurally unreachable under preregistered formula and thresholds.

## 3) Concept-to-observable mapping table

Mandatory: every proxy variable must map to a formal concept with rationale.

| Proxy element (code variable/formula) | OCT concept target | Mapping rationale (chapter/def) | Observable source | Label (O/P/C) |
| --- | --- | --- | --- | --- |
| Delta_Coh | coherence variation under U | Chapter 8 Coh axis | paired pre/post traces | O |
| Delta_Phi | functional variation under U | Chapter 8 Phi axis | paired pre/post traces | O |
| Loss_index | class decision proxy | D03 Cycle 5 locked formula | prereg formula lock | O |

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
Delta_Coh, Delta_Phi, Loss_index

Pre-registered thresholds:
t_low, t_high, max_ambiguous_rate

Policy lock:
- no criterion/threshold change on same data after first fail
- any revision requires new preregistration + new data split or new cycle

Lock accepted: yes

### 4.3 Existential claim guard (vacuum-pass test)

Show at least one concrete, realistic configuration where claim must fail under this proxy if phenomenon is absent.

Concrete fail configuration:
functor family with induced collapse where only one class remains reachable.

Why reachable:
included as high-stress context in prereg list.

If not reachable, mark sheet as fail.

### 4.4 Universal claim guard (trivial confirmation lock)

If claim type is universal, show reachable counterexample strategy.

Concrete reachable counterexample search strategy:
not applicable (claim type is taxonomic)

Confirmation is not tautological by construction? yes

## 5) Falsifiability reachability test

Required before run:
1. At least one executable input bundle expected to produce fail.
2. At least one executable input bundle expected to produce pass.
3. Decision boundary is pre-registered and immutable for this cycle.

Pass/fail of reachability test:
pass

Evidence artifact paths:
- OCT/validation/CYCLE_5_2026-05-01/contexts/D03_contexts_v0_1.md
- OCT/validation/CYCLE_5_2026-05-01/CYCLE_5_D03_LOCKED_TAXONOMY_SPEC_v0_1.md

### 5.1 Pre-registered context list (mandatory when using multi-context criteria)

| context_id | Distinguishing features | Expected difficulty | Dataset slice |
| --- | --- | --- | --- |
| D03_CTX_01 | functor families with low distortion | low | datasets/cycle3_inputs/d03_family_a |
| D03_CTX_02 | mixed families with moderate distortion | medium | datasets/cycle3_inputs/d03_family_b |
| D03_CTX_03 | adversarial families with high distortion | high | datasets/cycle3_inputs/d03_family_c |

## 6) Validity space coverage declaration (Coh/Phi/Delta)

Declare explicitly what is measured vs not measured:

| Axis | Measured? (yes/no) | Operational definition used | Path to code/report |
| --- | --- | --- | --- |
| Coh | yes | Delta_Coh | CYCLE_5_D03_LOCKED_TAXONOMY_SPEC_v0_1.md |
| PhiHat | yes | Delta_Phi | CYCLE_5_D03_LOCKED_TAXONOMY_SPEC_v0_1.md |
| Delta | partial | derived via Loss_index | CYCLE_5_D03_LOCKED_TAXONOMY_SPEC_v0_1.md |

If any axis is not measured, interpretation limits must be declared here:
Delta interpretation is limited to D03 class-partition objective.

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
- preregistration artifact path: OCT/validation/CYCLE_5_2026-05-01/seals/D03_PREREG_SEAL_v0_1.json
- checksum/hash: declared in seal payload
- timestamp (UTC): 2026-05-03T08:50:00Z
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
Taxonomy uses locked formula/threshold regime with explicit anti-rescue constraints.

Signer (auditor): Solomon
Date: 2026-05-03

