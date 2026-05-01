# OCT Validation Cycles Plan v0.1

Initial date: 2026-04-16  
Update date: 2026-05-01  
Objective: maintain a reproducible cycle architecture for theorem validation.

## Historical baseline (completed)

1. Cycle 1 - pilot formal/setup - `completed`
2. Cycle 2 - independent benchmark #1 - `completed`
3. Cycle 3 - independent benchmark #2 + multi-context replication - `completed (mixed)`
4. Cycle 4 - stress/ablation/repro audit + unified decision baseline - `completed`

## Why a new cycle is required

External and internal audits identified structural anti-pattern risks:
1. comparative level-shift (A01)
2. post-hoc rescue drift (D03)
3. existential vacuum-pass + evidence-class accumulation issues (D02)

Therefore Cycle 5 is defined as a method hardening cycle, not a cosmetic rerun.

## Cycle 5 (v5.3 lane)

Cycle folder: `CYCLE_5_2026-05-01/`  
Status: specification complete, execution pending

Scope:
1. A01 process-level validation refactor
2. D03 locked taxonomy refactor
3. D02 evidence-class split refactor
4. predeclared reject rules

Mandatory gate before execution:
1. `OCT_EX_ANTE_PROXY_GATE_POLICY_v0_1.md`
2. `templates/OCT_PROXY_PREVALIDATION_SHEET_v0_1.md`
3. `OCT_CLAIM_TYPE_ANTIPATTERN_CHECKLIST_v0_1.md`

## Cycle 5 decision policy

Theorem decision options:
1. `pass_candidate`
2. `revise_needed`
3. `reject_candidate`

Promotion to `validated` is blocked unless:
1. gate pass exists
2. preregistration seals are valid
3. reject triggers are absent
4. evidence-class reporting is complete

## Operational note

Cycle count alone is not evidence quality.  
Only cycle outputs that satisfy gate and preregistration constraints are admissible for theorem promotion.

