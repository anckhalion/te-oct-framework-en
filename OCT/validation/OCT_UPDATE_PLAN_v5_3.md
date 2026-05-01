# OCT Update Plan v5.3

Date: 2026-05-01  
Owner: OCT program (Fabio Ghioni + collaborators)  
Status: in progress (Phase 1, Phase 2, and Phase 3 specs completed)

## Objective

Upgrade OCT validation and editorial baseline from v5.2.0 to v5.3 with:
- explicit anti-pattern controls
- ex-ante proxy gate
- A01/D02/D03 validation hardening
- publication sync without overclaiming

## Scope

In scope:
- OCT validation governance artifacts
- theorem decision rationale alignment
- Chapter 17 methodological alignment
- benchmark process and preregistration workflow

Out of scope:
- full theorem re-validation execution (implemented in later cycles)
- complete rewrite of foundational book chapters beyond targeted patches

## Phase 1 - Editorial and methodological alignment

Target window: 2-3 days  
Status: completed (2026-05-01)

Deliverables:
1. Import external review inputs into official validation corpus.
2. Replace generic `revise` motivation with technical rationale tied to Chapter 8 Definition 8.12.
3. Add explicit references to anti-pattern and A01 gate design documents in OCT validation navigation.
4. Log start of v5.3 in publication/validation trackers.

Completion criteria:
- external reviews available in repository
- decision matrix updated with technical `revise` rationale
- v5.3 plan file published and linked

## Phase 2 - Ex-ante proxy gate

Target window: 2 days  
Status: completed (2026-05-01)

Deliverables:
1. `Proxy Pre-Validation Sheet` template (mandatory before benchmark execution).
2. Role-separation rule: proxy designer != proxy auditor.
3. Falsifiability reachability check (must be demonstrable before run).
4. Claim-type to anti-pattern mapping checklist (existential/comparative/taxonomic/universal).

Completion criteria:
- template published
- policy statement published
- no new cycle can start without gate pass

## Phase 3 - A01/D02/D03 validation refactor

Target window: 4-6 days  
Status: specification completed (2026-05-01), execution pending

Deliverables:
1. A01: process-level metric pipeline (trajectory + gate decisions), replacing output-only proxy logic.
2. D03: strict no-post-hoc-rescue policy on same data under same preregistration.
3. D02: strict separation of evidence classes (formal pilot vs empirical benchmark).
4. Updated cycle specs with rejection conditions predeclared.

Completion criteria:
- revised cycle specs committed
- reject conditions and thresholds preregistered
- evidence classes marked in decision artifacts

## Phase 4 - Minimum operational implementation

Target window: 5-7 days  
Status: pending

Deliverables:
1. Append-only trajectory logging schema.
2. `(O)/(P)/(C)` label discipline on metrics.
3. Preregistration sealing (hash + timestamp).
4. Audit script for gate compliance checks.

Completion criteria:
- logging schema in repo
- prereg artifacts testable
- compliance audit runnable

## Phase 5 - Freeze and publication sync

Target window: 2 days  
Status: pending

Deliverables:
1. Freeze candidate v5.3 package.
2. Synced updates on GitHub + Zenodo + OSF + Hugging Face.
3. Release note with anti-pattern controls and validation-state transparency.

Completion criteria:
- DOI/version snapshots aligned
- public links and notes synchronized

## Governance rules (non-negotiable)

1. No theorem promotion without ex-ante gate pass.
2. No threshold/criterion changes post-hoc on the same dataset.
3. No evidence accumulation across heterogeneous epistemic classes without explicit separation.
4. Every claim state change must reference code + proxy sheet + preregistration artifact.

## Current progress log

- 2026-05-01: Plan file created (`OCT_UPDATE_PLAN_v5_3.md`).
- 2026-05-01: External review inputs imported.
- 2026-05-01: Decision matrix motivation updated to technical Def 8.12 rationale.
- 2026-05-01: Phase 2 delivered:
  - `templates/OCT_PROXY_PREVALIDATION_SHEET_v0_1.md`
  - `OCT_EX_ANTE_PROXY_GATE_POLICY_v0_1.md`
  - `OCT_CLAIM_TYPE_ANTIPATTERN_CHECKLIST_v0_1.md`
- 2026-05-01: Phase 3 specification package delivered:
  - `CYCLE_5_2026-05-01/CYCLE_5_A01_PROCESS_LEVEL_SPEC_v0_1.md`
  - `CYCLE_5_2026-05-01/CYCLE_5_D03_LOCKED_TAXONOMY_SPEC_v0_1.md`
  - `CYCLE_5_2026-05-01/CYCLE_5_D02_EVIDENCE_CLASS_SPEC_v0_1.md`
  - `CYCLE_5_2026-05-01/CYCLE_5_EXECUTION_AND_REJECT_RULES_v0_1.md`
  - `CYCLE_5_2026-05-01/CYCLE_5_PREREG_SEAL_TEMPLATE_v0_1.md`
