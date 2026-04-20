# CYCLE 3 - Execution Template v0.1
Date: 2026-04-18Usage: operational checklist before/during/after running benchmarks #2.
## 1) Pre-run checklist
- [ ] Manifest benchmark #2 compiled (`BENCHMARK_MANIFEST_cycle3_v0_1.md`).- [ ] Pre-registered policies frozen (no changes during run).- [ ] Split data fixed and versioned.- [ ] Seed runs saved.- [ ] Baseline (`P_cls`) and ordinal (`P_ord`) pipelines blocked.- [ ] Active contexts: `Omega_A`, `Omega_B`, `Omega_C`.
## 2) Minimum log per run
For each run:- `theorem_id`: D02 / A01 / D03- `benchmark_id`- `omega_context`- `dataset_version`- `seed`- `pipeline_version`- primary metrics (`Coh`, `Phi`, `Delta`)- auxiliary metrics (`Err_sem`, `Loss_U`, other specific metric)- start/end timestamp- outcome (`ok` / `error`)
## 3) Decision table (draft)
### D02
- PASS candidate if non-empty class `Phi=0` exists in at least 2 out of 3 contexts.- REVIEW if class `Phi=0` appears in only one context.- REJECT candidate if no context has `Phi=0`.
### A01
- PASS candidate if both advantages (`Delta_cum`, `Err_sem`) hold up in at least 2 out of 3 contexts.- REVIEW if only one metric holds.- REJECT candidate if no metric holds.
### D03
- PASS candidates if conservative and degenerative regimes coexist in at least 2 out of 3 contexts and ambiguous rate < 0.20.- REVIEW if ambiguous odds >= 0.20 or if coexistence is fragile.- REJECT candidate if only one regime emerges in a dominant/stable manner.
## 4) Mandatory post-run
- [ ] Fill in `results_D02_cycle3_v0_1.md`- [ ] Fill in `results_A01_cycle3_v0_1.md`- [ ] Fill in `results_D03_cycle3_v0_1.md`- [ ] Fill in `CYCLE_3_REPORT.md`- [ ] Note anomalies and limitations- [ ] Define explicit gate towards Cycle 4