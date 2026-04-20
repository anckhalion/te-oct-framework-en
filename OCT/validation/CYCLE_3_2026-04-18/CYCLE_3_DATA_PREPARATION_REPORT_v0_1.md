# CYCLE 3 Data Preparation Report v0.1
Date: 2026-04-19Status: Completed
## Objective
Convert Cycle 3 raw datasets into unified operational tables:- `D02.csv` (180 samples),- `A01.csv` (320 samples),- `D03.csv` (260 samples).
## Raw inputs used
- `datasets/cycle3_raw/D02/ca-GrQc.txt.gz`- `datasets/cycle3_raw/D02/email-Eu-core.txt.gz`- `datasets/cycle3_raw/A01/STS-B.zip`- `datasets/cycle3_raw/D03/UD_English-EWT-r2.17.tar.gz`
## Pipelines
- Script: `datasets/cycle3_work/build_cycle3_inputs.py`- Output directory: `datasets/cycle3_inputs/`- Generated outputs:- `D02.csv`- `A01.csv`- `D03.csv`- `metadata.json`- `run_summary.json`
## Final tallies
- D02: 180 lines- A01: 320 lines- D03: 260 lines
## Methodological note
For D02 a deterministic `Phi` proxy (density/context) useful for the phase was appliedoperational validation of the cycle; it does not yet constitute the final test for `validated` status.