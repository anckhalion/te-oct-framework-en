# OCT Typed Formal Spec v0.1
Scope:fix a unified typed scheme for `Coh`, `Phi`, `Delta`, `Omega`compatible with classical category theory and usable in OCT theorems.
## 1) Formal layers
The specification separates three layers:1. **Syntactic**: classical category.2. **Ordering**: consistency and validity thresholds.3. **Emergent**: emergent function and degeneration.
## 2) Typed basic data
Is:- `O` a locally small category.- `Diag_fin(O)` the class of finished diagrams in `O`.- `ObsCtx` a category (or preorder) of observational contexts.- `Omega in Ob(ObsCtx)` an observational context.
For each `Omega` we assign:
1. **Local consistency on morphisms**- `coh_Omega^1 : Mor(O) -> [0,1]`
2. **Diagrammatic coherence**- `Coh_Omega : Diag_fin(O) -> [0,1]`
3. **Emergent space**- `E_Omega = (E_Omega, +, 0_E, <=_E)`- `E_Omega` and a preordained commutative monoid with null element `0_E`
4. **Emergent function**- `Phi_Omega : Diag_fin(O) -> E_Omega`
5. **Threshold of reality**- `tau_Omega in (0,1]`
6. **Degeneration**- `Delta_Omega : Diag_fin(O) -> [0,1]`- defined by `Delta_Omega(D) = 1 - Coh_Omega(D)`
## 3) Fundamental predicates
### 3.1 OCT-valid morphism
For `f in Mor(O)`:
`OCTVal_Omega(f) := coh_Omega^1(f) >= tau_Omega`
### 3.2 OCT-real diagram
For `D in Diag_fin(O)`:
`Real_Omega(D) := (Coh_Omega(D) >= tau_Omega) and (Phi_Omega(D) != 0_E)`
### 3.3 OCT-degenerate diagram
`Deg_Omega(D) := (D != vuoto) and (Phi_Omega(D) = 0_E)`
## 4) Minimal typed axioms (TS1-TS8)
### TS1 - Classic compatibility
The classic definitions of identity and composition in `O` remain unchanged.
### TS2 - Consistency normalization
`coh_Omega^1(f) in [0,1]` and `Coh_Omega(D) in [0,1]`.
### TS3 - Identity coherence
For each `A` object:
`coh_Omega^1(id_A) = 1`.
### TS4 - Local compositional stability
There exists a t-norm `T : [0,1] x [0,1] -> [0,1]` such that,for each composite pair `f: A->B`, `g: B->C`:
`coh_Omega^1(g o f) >= T(coh_Omega^1(g), coh_Omega^1(f))`.
### TS5 - Local/global compatibility
For each finished diagram `D`:
`Coh_Omega(D) <= inf { coh_Omega^1(f) : f e freccia di D }`.
### TS6 - Canonical emerging nullity
If `D` is empty or trivially devoid of dynamics, then`Phi_Omega(D) = 0_E`.
### TS7 - Strong anti-degeneration
If `Real_Omega(D)` then `Deg_Omega(D)` is false.
### TS8 - Observational reindexing
For each context morphism `u: Omega -> Omega'` in `ObsCtx`,There are transport maps:- `R_u^Coh : [0,1] -> [0,1]`- `R_u^Phi : E_Omega -> E_Omega'`
with compatibility:- `Coh_Omega'(D) = R_u^Coh(Coh_Omega(D))`- `Phi_Omega'(D) = R_u^Phi(Phi_Omega(D))`
in a declared regime (exact or approximate with controlled error).
## 5) Immediate consequences
1. **F03** and well typed via TS4.2. **F08** and well-typed via `0_E` and `Real_Omega`.3. **F10** and can be formalized by imposing limit regime:- `coh_Omega^1 = 1`,- `Coh_Omega = 1`,- `Phi` filter disabled.
## 6) Choices open for v0.2 of the specification
1. explicit choice of the t-norm `T` (min, product, Lukasiewicz, other).2. choice of space `E_Omega` (ordered monoid vs semiring vs lattice).3. threshold policy `tau_Omega` (fixed, adaptive, domain dependent).4. formalization of transport error between contexts (`epsilon`-consistency).
## 7) Criterion for adoption in the work
The specification is considered adopted when:1. all foundation theorems use the same typed signatures;2. untyped uses of `Phi`, `Coh`, `Omega` no longer appear;3. the empirical protocol (Volume IV) uses these same quantities without redefinitions.