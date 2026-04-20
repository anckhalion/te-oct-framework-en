# CYCLE 3 - Run Input Requirements v0.1
Date: 2026-04-18Purpose: Specify the minimum inputs needed to run D02, A01, D03 on benchmark #2.
## Current status
- Scripts executable in the workspace: not present- Reason: Text/theory oriented repository, without local runtime pipeline- Effect: Benchmark execution blocked until input/runtime availability
## Minimum inputs required
1. `dataset_bundle_cycle3` (can be zip/folder):- `D02/` commutative diagrams benchmark #2- `A01/` task pipeline benchmark #2 with gold reference- `D03/` pre/post pairs forgetting functor benchmark #22. `execution_method`:- local script,- notebooks,- or external tool with exportable output.3. `result_logs` for context:- `Omega_A`, `Omega_B`, `Omega_C`4. `metadata`:- dataset version,- seeds,- pipeline version (`P_ord`, `P_cls` or equivalent).
## Required output format (for integration into reports)
### D02
- quote `Phi=0` for context- quote `Phi>0` for context- evidence of non-productive class
### A01
- `E[Delta_cum(P_ord)]`, `E[Delta_cum(P_cls)]` for context- `E[Err_sem(P_ord)]`, `E[Err_sem(P_cls)]` for context
### D03
- condom/degenerative/ambiguous quotas by context- cross-context stability indicator
## Operational note
Until input/runtime arrives, `results_*_cycle3_v0_1.md` files remain in `pending` state.