# CYCLE 5 - D03 Locked Taxonomy Spec v0.1

Date: 2026-05-01  
Theorem: D03  
Claim type: taxonomic  
Evidence class target: L1 empirical external (paired pre/post)

## Claim under test

"Informational loss of forgetful functors is classifiable into preservative vs degenerative regimes."

## Core correction from Cycle 3-4

Cycle 3-4 showed post-fail criterion drift risk.  
Cycle 5 enforces preregistered locked taxonomy with explicit no-rescue clause.

## Mandatory data structure

Each sample must be an explicit pair:
1. `D_pre`
2. `D_post = U(D_pre)` with declared forgetful functor `U`
3. functor family label
4. context label

Single-instance sentence proxies without explicit `U` mapping are invalid for D03.

## Primary metrics (pre-registered)

1. `Delta_Coh = Coh(D_post) - Coh(D_pre)`
2. `Delta_Phi = Phi(D_post) - Phi(D_pre)`
3. `Loss_index = f(Delta_Coh, Delta_Phi)` (formula fixed in preregistration)

## Class partition (pre-registered)

1. `preservative`: `Loss_index <= t_low`
2. `degenerative`: `Loss_index >= t_high`
3. `ambiguous`: `t_low < Loss_index < t_high`

All thresholds fixed before first run.

## Confirmation criterion (pre-registered)

D03 is `pass_candidate` only if all are true:
1. Both classes (`preservative`, `degenerative`) are non-empty in at least 2/3 contexts.
2. Ambiguous share remains below `max_ambiguous_rate` in at least 2/3 contexts.
3. Coh and Phi both participate in classification (no single-axis collapse).

## Reject conditions (pre-registered)

D03 is `reject_candidate` if one or more hold:
1. No explicit `U` mapping and no pre/post pairs.
2. Classification changes criterion/threshold on same dataset after first fail.
3. One class is structurally unreachable under preregistered formula/range.
4. Coh is absent from effective decision logic.

## Review conditions (pre-registered)

D03 is `revise_needed` if:
1. both classes appear but stability is fragile across contexts, or
2. ambiguous share is borderline around threshold, or
3. independence checks reveal family imbalance risk.

## Anti-pattern lock

1. No post-hoc rescue on same data.
2. No variable switch (`drop` to `loss`, or equivalent) after fail without new preregistration + new cycle.
3. Any rescue attempt triggers automatic `reject_candidate` for that cycle.

