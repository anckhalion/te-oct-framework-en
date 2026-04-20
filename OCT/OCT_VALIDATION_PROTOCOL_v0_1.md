# OCT Validation Protocol v0.1
Date: 2026-04-16Purpose: Single protocol to bring OCT theorems from `in_proof` to `validated`.
Formal Baseline:- `OCT_TYPED_FORMAL_SPEC_v0_1.md`- `OCT_FOUNDATIONAL_OPERA_DRAFT_v0_7.md`
## 1) Validation objective
Go from structural demonstration to repeatable evidence on benchmarks.
At this stage:- D02, D03, D04 (differentials)- A01, A02, A03 (applications)
## 2) Canonical metrics
For each experiment (context `Omega`):- `Coh_Omega(D)` in [0,1]- `Phi_Omega(D)` to `E_Omega`- `Delta_Omega(D) = 1 - Coh_Omega(D)`
Auxiliary metrics:- `Err_sem` (task-specific semantic error)- `Err_struct` (structural reconstruction error)- `Var_Omega` (cross-context variance)
## 3) Minimal experimental design
Each test must have:1. declared domain;2. dataset/fixed version;3. classic baseline pipeline (`P_cls` / `F_cls`);4. ordering pipeline (`P_ord` / `F_OCT`);5. pre-registered confirmation/falsification criteria.
## 4) Test suite for theorem
## D02 - Non-productive commutativity
Input:- set of classical commutative diagrams.
Test:1. verify classical commutativity;2. measure `Phi_Omega(D)`;3. classify commutative-productive vs commutative-non-productive.
He confirms:- non-empty class exists with `Phi_Omega(D)=0_E`.
Forgery:- all tested commutatives have non-zero emergence.
## D03 - Ontological loss of forgetting functors
Input:- pairs of pre/post diagrams `U`.
Test:1. estimate `Loss_U` on order invariants;2. separate condom and degenerative cases.
He confirms:- both regimes coexist in a robust way.
Forgery:- always neutral or always degenerative loss without distinction.
## D04 - Conditional symmetry
Input:- domains with real functional asymmetry.
Test:1. apply `sigma` where defined;2. measure variation of `Phi_Omega` and `Delta_Omega`.
He confirms:- there is a subclass where the exchange is strictly inadmissible.
Forgery:- symmetry always neutral on all cases.
## A01 - AI pipeline order established
Input:- multi-step tasks with gold reference.
Test:1. run `P_ord` and `P_cls`;2. plot `Coh`, `Phi`, `Delta` by step;3. measure final `Err_sem`.
He confirms:- `E[Delta_cum(P_ord)] < E[Delta_cum(P_cls)]`- `E[Err_sem(P_ord)] < E[Err_sem(P_cls)]`
Forgery:- inequalities not robust across multiple benchmarks.
## A02 - Reconstruction from linguistic projections
Input:- dataset (source structure, linguistic projection).
Test:1. reconstruction with `F_OCT` and `F_cls`;2. measures `Err_struct` and `Var_Omega`.
He confirms:- robust lead of `F_OCT` on both metrics.
Forgery:- absence of advantage or high contextual instability.
## A03 - Degeneration in narrative social systems
Input:- longitudinal discursive networks.
Test:1. extract `D_t` on time windows;2. measure `Coh_Omega(D_t)`, `Phi_Omega(D_t)`, `Delta_Omega(D_t)`;3. correlate with external indicators of degradation.
He confirms:- "high rhetorical coherence + low emergency" regime anticipates systemic degradation.
Forgery:- no robust association between `Phi` collapse and observable degradation.
## 5) Global validation criteria
A theorem passes to `validated` when:1. at least 2 independent benchmarks confirm the criterion;2. results replicated in at least 2 contexts `Omega`;3. esito statistico supera soglia dichiarata;
4. esistono log completi e riproducibili.

## 6) Output richiesti per ogni teorema validato

1. results file (`results_<theorem>.md` or equivalent table)2. execution protocol3. analysis of errors/limitations4. final decision: validated / rejected / revised
## 7) Recommended sequence (next days)
1. D022. A013. D034. A025. D046. A03
Reason:- first minimum structural difference (D02),- then immediate operating value (A01),- therefore differential/applicative completion.