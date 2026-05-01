# CYCLE 5 - A01 Process-Level Spec v0.1

Date: 2026-05-01  
Theorem: A01  
Claim type: comparative  
Evidence class target: L1 empirical external (process-trace based)

## Claim under test

"Compositional pipelines with high ordinative coherence show lower semantic degeneration than classically valid-only pipelines."

## Core correction from Cycle 3

Cycle 3 relied on output-level proxy blending, which does not test process-level ordinativity.  
Cycle 5 enforces process-level comparison with trajectory evidence.

## Required process instrumentation

For each task run and each step `i`:
1. `step_id`
2. `morphism_id`
3. `Syn_i`
4. `Coh_i`
5. `Phi_i`
6. `gate_decision_i` (`admit/refine/reject/abort`)
7. `trajectory_event_hash`
8. timestamp

Both pipelines must be run:
1. `P_cls` (classical baseline)
2. `P_ord` (ordinative gate enabled)

## Primary metrics (pre-registered)

1. `Delta_cum`: cumulative process degradation over trajectory.
2. `Err_sem_final`: final semantic error against gold/anchor.
3. `Reject_rate`: fraction of steps rejected or refined.
4. `Trajectory_length`: number of effective transitions.

## Confirmation criterion (pre-registered)

A01 is `pass_candidate` only if all are true:
1. `E[Delta_cum(P_ord)] < E[Delta_cum(P_cls)]` in at least 2/3 contexts.
2. `E[Err_sem_final(P_ord)] < E[Err_sem_final(P_cls)]` in at least 2/3 contexts.
3. At least one subset shows equal/similar final output but different trajectory quality favoring `P_ord`.

## Reject conditions (pre-registered)

A01 is `reject_candidate` if one or more hold:
1. Process logs are missing/incomplete for either pipeline.
2. Claimed effect is supported only by output-level metric without process advantage.
3. `P_ord` does not beat `P_cls` on either primary metric in all contexts.
4. Gate decisions are not auditable (no append-only trace).

## Review conditions (pre-registered)

A01 is `revise_needed` if:
1. one primary metric passes and one fails, or
2. process advantage exists but semantic advantage is unstable, or
3. contextual variance exceeds pre-registered warning threshold.

## Anti-pattern lock

1. No level-shift: output-only proxy cannot be decisive.
2. No hidden metric substitution after first run.
3. No threshold adjustment on same dataset after fail.

