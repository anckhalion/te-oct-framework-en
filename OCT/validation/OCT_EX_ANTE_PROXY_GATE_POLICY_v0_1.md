# OCT Ex-Ante Proxy Gate Policy v0.1

Date: 2026-05-01  
Status: active for all cycles started after this date

## Purpose

Prevent structural anti-patterns in theorem validation by enforcing an ex-ante gate before benchmark execution.

## Binding rule

No cycle can start without a `PASS` decision on:
- `templates/OCT_PROXY_PREVALIDATION_SHEET_v0_1.md`

If gate status is `FAIL` or `HOLD`, execution is blocked.

## Mandatory controls

1. **Logical type declaration**: existential/comparative/taxonomic/universal must be explicit.
2. **Concept-to-observable mapping**: every proxy term must map to OCT concept with chapter/definition rationale.
3. **Falsifiability reachability**: both expected-pass and expected-fail configurations must be concretely reachable.
4. **Role separation**: proxy designer and proxy auditor must be distinct.
5. **Preregistration seal**: immutable hash+timestamp before run.
6. **Evidence class declaration**: L1/L2/synthetic classes must be explicit and non-collapsed.

## Anti-pattern lock clauses

### Clause A - No level-shift (comparative claims)

Comparative claims must be tested at process level when process is the claim target.  
Output-only proxies are non-decisive unless explicitly constrained and justified.

### Clause B - No post-hoc rescue (taxonomic claims)

After first fail on preregistered criterion, no threshold/criterion change is allowed on same data within the same cycle.  
Any revision requires:
- new preregistration
- new cycle identifier
- documented rationale

### Clause C - No vacuum-pass (existential claims)

Existential claims must include at least one reachable disconfirming configuration under the proposed proxy.  
If no disconfirming configuration is reachable, gate must return `FAIL`.

### Clause D - No false accumulation across evidence classes

Formal pilot pass, synthetic pass, and empirical pass are separate evidence classes and cannot be auto-summed as independent confirmations.

## Enforcement

Minimum artifacts required per theorem-cycle:
1. Filled pre-validation sheet
2. Preregistration artifact with seal
3. Auditor signature
4. Link to planned cycle spec

Missing any artifact -> automatic gate `FAIL`.

## Governance integration

Decision state changes in matrix artifacts (`validated/revise/reject`) must reference:
- proxy sheet path
- preregistration path
- cycle report path
- code path

## Effective date and migration

Effective date: 2026-05-01.  
Historical cycles remain unchanged as historical record, but are interpreted under this policy when reassessed.

