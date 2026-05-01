# OCT Claim-Type to Anti-Pattern Checklist v0.1

Date: 2026-05-01

Use this checklist during pre-validation gate review.

## Step 1 - Identify claim type

Select one:
- `existential`
- `comparative`
- `taxonomic`
- `universal`

## Step 2 - Run the type-specific checks

### A) Existential claims

Dominant risk: `vacuum-pass structural`.

Checks:
1. Is there at least one realistic, reachable fail configuration?
2. Is disconfirmation logically possible under current proxy?
3. Is pass not guaranteed by dataset sparsity/threshold geometry?

Any `no` -> `FAIL`.

### B) Comparative claims

Dominant risk: `level-shift`.

Checks:
1. Does A/B differ in process where claim targets process?
2. Is proxy measured on trajectory/gate behavior, not only final output?
3. Can equifinal outputs still be distinguished by process evidence?

Any `no` -> `FAIL` or `HOLD`.

### C) Taxonomic claims

Dominant risk: `post-hoc rescue`.

Checks:
1. Are classes and thresholds pre-registered before first run?
2. Is both-class occupancy possible under proxy range?
3. Is there an explicit lock against criterion change on same data after fail?

Any `no` -> `FAIL`.

### D) Universal claims

Dominant risk: `trivial confirmation`.

Checks:
1. Is there a reachable counterexample search strategy?
2. Would claim fail under plausible absent-phenomenon scenarios?
3. Is confirmation not tautological by construction?

Any `no` -> `FAIL`.

## Step 3 - Cross-cutting checks (all claim types)

1. Concept-to-observable mapping complete.
2. Coh/Phi/Delta measured-vs-unmeasured explicitly declared.
3. Proxy designer and auditor are different.
4. Preregistration seal exists and is immutable.
5. Evidence class declared and not merged implicitly with other classes.

Any `no` -> `FAIL`.

## Outcome codes

- `PASS`: cycle execution allowed.
- `FAIL`: redesign mandatory before execution.
- `HOLD`: claim statement unclear; clarify theorem first.

