# CYCLE 5 EXECUTION REPORT - A01 v1.0

Date: 2026-05-04
Theorem: A01
Decision: `revise_needed`

## Context metrics

| Context | delta_cum_cls | delta_cum_ord | err_cls | err_ord | mean_Coh_cls | mean_Coh_ord |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| A01_CTX_01 | 0.416102 | 0.399112 | 0.438484 | 0.421211 | 0.583898 | 0.600888 |
| A01_CTX_02 | 0.423892 | 0.419588 | 0.448109 | 0.443174 | 0.576108 | 0.580412 |
| A01_CTX_03 | 0.431399 | 0.442191 | 0.456571 | 0.465889 | 0.568601 | 0.557809 |

## Criteria summary

- Delta pass contexts: `2`
- Error pass contexts: `2`
- Coh pass contexts: `2`
- Equal-output/trajectory-quality subset count: `0`

## Proxy Stress Test

- Total configurations scanned: `135`
- Qualifying configurations: `0`
- Qualifying rate: `0.0`
- Criterion: `abs(err_ord-err_cls)<=0.01 and (coh_ord-coh_cls)>0.03`

## Notes

- Metrics are computed from deterministic proxy execution over cycle3 input corpus.
- `decision_raw` is de-escalated to `decision=revise_needed` because this runner is non-promotable proxy mode.
- If proxy stress test returns zero qualifying configurations, the runner cannot currently exhibit process-only advantage under this proxy family.
- This report is reproducible from files in `datasets/cycle3_inputs` and script lock artifacts.
