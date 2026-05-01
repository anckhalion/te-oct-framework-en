# CYCLE 5 - D02 Evidence-Class Spec v0.1

Date: 2026-05-01  
Theorem: D02  
Claim type: existential  
Evidence class target: split-lane reporting (`L2 formal` and `L1 empirical`) with no auto-accumulation

## Claim under test

"There exist classical commutative diagrams with Phi = 0."

## Core correction from prior cycles

D02 previously mixed heterogeneous evidence classes as if additive.  
Cycle 5 separates lanes and blocks false accumulation.

## Evidence lanes (mandatory separation)

1. `Lane L2 formal pilot`
   - typed consistency
   - witness construction/proof obligations
2. `Lane L1 empirical external`
   - explicit commutativity check per sample
   - explicit Phi mapping with falsifiability reachability

Decision must report lane-wise status before any global status.

## Mandatory empirical prerequisites

1. `is_commutative` cannot be hardcoded by fiat; it must be verified or constructed with proof trace.
2. Phi mapping must include rationale and not reduce to guaranteed-pass geometry.
3. At least one reachable context where all candidates would fail under absent-phenomenon assumption must be documented.

## Confirmation criterion (pre-registered)

L1 empirical `pass_candidate` only if:
1. non-empty commutative set with `Phi = 0` appears in at least 2/3 contexts,
2. commutativity is explicitly verified for those samples,
3. falsification route is reachable and tested negative.

L2 formal `pass_candidate` only if:
1. witness/proof obligations are independently checked,
2. assumptions and limits are explicitly declared.

## Reject conditions (pre-registered)

D02 empirical lane is `reject_candidate` if one or more hold:
1. `is_commutative` is assigned universally without verification.
2. Phi threshold makes pass structurally guaranteed by dataset sparsity.
3. no reachable fail configuration exists (vacuum-pass).

D02 formal lane is `reject_candidate` if:
1. witness cannot be independently reconstructed, or
2. formal assumptions are internally inconsistent.

## Review conditions (pre-registered)

D02 is `revise_needed` if:
1. one lane passes and one lane fails, or
2. empirical lane passes but with narrow context robustness.

## Anti-pattern lock

1. No false accumulation across lanes.
2. Final theorem status must cite lane-specific status matrix.
3. Any global promotion ignoring lane split is invalid.

