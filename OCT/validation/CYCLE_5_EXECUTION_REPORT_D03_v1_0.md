# CYCLE 5 EXECUTION REPORT - D03 v1.0

Date: 2026-05-04
Theorem: D03
Decision: `reject_candidate`

## Locked thresholds

- t_low: `0.1`
- t_high: `0.22`
- max_ambiguous_rate: `0.35`
- formula: `0.5*abs(Delta_Coh)+0.5*abs(Delta_Phi)`

## Context summary

| Context | n | preservative | degenerative | ambiguous | ambiguous_rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| D03_CTX_01 | 87 | 0 | 77 | 10 | 0.114943 |
| D03_CTX_02 | 87 | 0 | 76 | 11 | 0.126437 |
| D03_CTX_03 | 86 | 0 | 77 | 9 | 0.104651 |

## Criteria / Reject triggers

- Criteria: `{"both_classes_non_empty_in_2_of_3_contexts": false, "ambiguous_below_threshold_in_2_of_3_contexts": true, "coh_and_phi_participate": true}`
- Reject triggers: `{"missing_explicit_U_mapping": false, "criterion_shift_after_fail": false, "class_unreachable_under_locked_formula": true, "coh_absent_from_logic": false}`
- Decision raw: `reject_candidate`

## Notes

- Under locked formula and thresholds, preservative regime remains unreachable in required contexts.
