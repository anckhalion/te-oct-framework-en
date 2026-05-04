# OCT Proxy Pre-Validation Sheet v0.1

Date:
Prepared by (proxy designer):
Audited by (independent auditor):
Theorem ID:
Claim ID:
Claim source (chapter/section):
Cycle ID candidate:
Status: `draft | pass | fail`

## 1) Claim logical type

Select one:
- `existential` (there exists x such that P(x))
- `comparative` (E[P_A] > E[P_B] or equivalent)
- `taxonomic` (coexistence/partition of regimes)
- `universal` (for all x, P(x))

Expected dominant anti-pattern risk:
- `existential -> vacuum-pass structural`
- `comparative -> level-shift`
- `taxonomic -> post-hoc rescue`
- `universal -> trivial confirmation without reachable falsification`

## 1.1) Cycle budget control (anti-p-hacking)

Max independent cycles for this claim:
Current cycle sequence index:
Budget policy status: `within_budget | exhausted_requires_escalation`

## 2) Claim statement and falsifier statement

Claim (verbatim):

Primary falsifier (what would disconfirm it):

Secondary falsifier(s):

## 3) Concept-to-observable mapping table

Mandatory: every proxy variable must map to a formal concept with rationale.

| Proxy element (code variable/formula) | OCT concept target | Mapping rationale (chapter/def) | Observable source | Label (O/P/C) |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

Rules:
1. No unnamed proxy term is allowed.
2. No concept can be declared as measured if mapping is missing.
3. Labels must follow: `O=operational`, `P=operationalizable`, `C=conceptual only`.

## 4) Anti-pattern prevention checks (mandatory)

### 4.1 Comparative claim guard (level-shift test)

If claim type is `comparative`, show that A/B differs in process, not only output scoring.

Process-level evidence planned:

Output-only fallback present? `yes/no`

If yes, why it is non-decisive and how it is constrained:

### 4.2 Taxonomic claim guard (post-hoc rescue lock)

Pre-registered variables:

Pre-registered thresholds:

Policy lock:
- no criterion/threshold change on same data after first fail
- any revision requires new preregistration + new data split or new cycle

Lock accepted: `yes/no`

### 4.3 Existential claim guard (vacuum-pass test)

Show at least one concrete, realistic configuration where claim must fail under this proxy if phenomenon is absent.

Concrete fail configuration:

Why reachable:

If not reachable, mark sheet as `fail`.

### 4.4 Universal claim guard (trivial confirmation lock)

If claim type is `universal`, show reachable counterexample strategy.

Concrete reachable counterexample search strategy:

Confirmation is not tautological by construction? `yes/no`

## 5) Falsifiability reachability test

Required before run:
1. At least one executable input bundle expected to produce fail.
2. At least one executable input bundle expected to produce pass.
3. Decision boundary is pre-registered and immutable for this cycle.

Pass/fail of reachability test:

Evidence artifact paths:

### 5.1 Pre-registered context list (mandatory when using multi-context criteria)

| context_id | Distinguishing features | Expected difficulty | Dataset slice |
| --- | --- | --- | --- |
|  |  |  |  |

## 6) Validity space coverage declaration (Coh/Phi/Delta)

Declare explicitly what is measured vs not measured:

| Axis | Measured? (yes/no) | Operational definition used | Path to code/report |
| --- | --- | --- | --- |
| Coh |  |  |  |
| PhiHat |  |  |  |
| Delta |  |  |  |

If any axis is not measured, interpretation limits must be declared here:

## 7) Evidence class declaration

Select one:
- `L1 empirical external`
- `L1 empirical synthetic (auditable)`
- `L2 formal pilot`
- `other` (specify)

Accumulation rule reminder:
- evidence classes are not auto-additive
- cross-class accumulation requires explicit matrix logic

## 8) Role separation confirmation

Proxy designer and proxy auditor must be different.

Designer:
Auditor:
Confirmed different identities: `yes/no`
Auditor co-authorship with designer in last 24 months: `yes/no`
If yes, list:
Auditor school-of-thought affiliation declaration:

## 9) Preregistration seal

Required fields:
- preregistration artifact path:
- checksum/hash:
- timestamp (UTC):
- immutable storage location:
- seal method:
- contexts hash:
- auditor independence declared (`yes/no`):
- gate-entry signature:
- gate-entry timestamp (UTC):
- gate-exit signature:
- gate-exit timestamp (UTC):
- gate-exit status: `not_executed | executed_no_promotion | executed_promotable | invalidated`

Seal valid: `yes/no`

## 10) Gate decision

Decision options:
- `PASS` (cycle execution allowed)
- `FAIL` (cycle blocked, redesign required)
- `HOLD` (claim clarification required before proxy design)

Decision:

Decision rationale (short, technical):

Signer (auditor):
Date:
