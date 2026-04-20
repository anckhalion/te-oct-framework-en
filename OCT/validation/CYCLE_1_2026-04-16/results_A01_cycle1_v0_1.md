# Results A01 - Cycle 1 (Pilot)
Theorem: A01 - Established ordering in AI pipelineCycle date: 2026-04-16Cycle type: operational pilot (setup + pre-registration)
## Cycle objective
Prepare A01 for robust empirical validation:1. definition of metrics and criteria;2. definition of test scheme `P_ord` vs `P_cls`;3. verify traceability in the manuscript.
## Execution Cycle 1
1. Alignment of metrics with protocol:- `Coh_Omega(D_t)`, `Phi_Omega(D_t)`, `Delta_Omega(D_t)`, `Err_sem`.2. Definition of criteria:- `E[Delta_cum(P_ord)] < E[Delta_cum(P_cls)]`- `E[Err_sem(P_ord)] < E[Err_sem(P_cls)]`3. Definition of falsification criteria:- no robust advantage across multiple benchmarks.
## Outcome
- Cycle status 1: **PASS (pilot setup)**- Theorem status: **in_proof** (not yet `validated`)
## What is validated in this cycle
- formal consistency of the theorem with the typified baseline;- complete minimum experimental protocol;- pre-registered confirmation/falsification criteria.
## What's missing for `validated`
1. execution on independent benchmark #1;2. execution on independent benchmark #2;3. replicates in at least 2 contexts `Omega`;4. statistical evidence and reproducible logs.
## Decision
`A01` remains `in_proof` and advances to Cycle 2 (empirical benchmark).