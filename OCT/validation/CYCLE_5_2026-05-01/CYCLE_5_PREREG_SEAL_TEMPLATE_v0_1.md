# CYCLE 5 Preregistration Seal Template v0.1

Date:
Theorem:
Spec file:
Designer:
Auditor:
Auditor independence declared: `yes/no`
Auditor co-authorship with designer in last 24 months:
Auditor school-of-thought affiliation statement:
Cycle budget (`max_independent_cycles` for claim):

## Preregistration payload

1. Claim source path:
2. Claim text hash:
3. Thresholds source path:
4. Thresholds hash:
5. Formula source path:
6. Formula hash:
7. Dataset manifest path:
8. Dataset manifest hash:
9. Script version source path:
10. Script version hash:
11. Context list source path:
12. Context list hash:

## Seal metadata

1. UTC timestamp:
2. Seal method:
3. Immutable storage path:
4. Gate-entry signature (pre-run):
5. Gate-entry timestamp (UTC):
6. Gate-exit signature (post-run):
7. Gate-exit timestamp (UTC):
8. Gate-exit status: `not_executed | executed_no_promotion | executed_promotable | invalidated`
9. Lock acknowledged: `yes/no`

## Lock clauses acknowledged

- No threshold change on same data after first fail.
- No formula substitution on same data after first fail.
- No evidence-class collapse in decision stage.
- No unbounded sequential re-preregistration beyond declared cycle budget.
- Any violation => cycle invalid for theorem promotion.

Acknowledged: `yes/no`
