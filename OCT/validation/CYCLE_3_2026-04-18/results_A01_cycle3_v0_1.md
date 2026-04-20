# Results A01 - Cycle 3 (Benchmark #2)
Theorem: A01 - Established ordering in AI pipelineCycle date: 2026-04-19Cycle type: independent benchmark #2 (real STS-B data + proxy scoring)
## Benchmarks and setup
- Benchmark ID: `B2_NOISY_LONGHORIZON_PIPELINE_ORD_2026Q2`- Dataset: STS-B (GLUE), 320 tasks- Contexts: `Omega_A`, `Omega_B`, `Omega_C`- Input used: `datasets/cycle3_inputs/A01.csv`
## Metrics and results
### Cumulative Delta (`Delta_cum`)
| Context | `E[Delta_cum(P_ord)]` | `E[Delta_cum(P_cls)]` | Gap (`ord - cls`) || --- | ---: | ---: | ---: |
| `Omega_A` | 0.5550 | 0.6159 | -0.0609 || `Omega_B` | 0.5717 | 0.6281 | -0.0565 || `Omega_C` | 0.5782 | 0.6345 | -0.0563 |
### Final semantic error (`Err_sem`)
| Context | `E[Err_sem(P_ord)]` | `E[Err_sem(P_cls)]` | Gap (`ord - cls`) || --- | ---: | ---: | ---: |
| `Omega_A` | 0.2525 | 0.2674 | -0.0149 || `Omega_B` | 0.2353 | 0.2480 | -0.0127 || `Omega_C` | 0.2429 | 0.2463 | -0.0034 |
## Interpretation
Criterion A01 is supported in benchmark #2: `P_ord` maintains an advantage over `P_cls`for both `Delta_cum` and `Err_sem` in all 3 contexts.
## Decision
- Cycle 3 outcome for A01: **PASS (benchmark #2)**- Theorem status: **in_proof** (strengthened evidence, awaiting closure of cycle+audit)