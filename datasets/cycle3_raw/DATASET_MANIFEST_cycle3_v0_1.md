# Cycle 3 Dataset Manifest v0.1

Date: 2026-04-19
Status: downloaded
Base path: `datasets/cycle3_raw`

| theorem | dataset_id | source | file | size_bytes | sha256 |
| --- | --- | --- | --- | ---: | --- |
| D02 | D02_graph_caGrQc | SNAP | D02/ca-GrQc.txt.gz | 109261 | A254442CDF5D684712578B630C2E0D7543518AB154EF2341CABB607572CE7230 |
| D02 | D02_graph_emailEuCore | SNAP | D02/email-Eu-core.txt.gz | 79754 | 4B47ACDB80197B085FE63C819C357AE488131EE904ED93D1B219A68B0F9E245F |
| A01 | A01_text_STS-B | GLUE | A01/STS-B.zip | 802872 | E60A6393DE5A8B5B9BAC5020A1554B54E3691F9D600B775BD131E613AC179C85 |
| D03 | D03_ud_english_ewt_r2.17 | Universal Dependencies | D03/UD_English-EWT-r2.17.tar.gz | 7101256 | E5A52DE22CF076FEC389E8781F8D22784E725A2396423EAFFB1ABAFDAEDF0654 |

## Notes
- D02_graph_caGrQc: Graph benchmark (collaboration network). Source URL: https://snap.stanford.edu/data/ca-GrQc.txt.gz
- D02_graph_emailEuCore: Graph benchmark (email network). Source URL: https://snap.stanford.edu/data/email-Eu-core.txt.gz
- A01_text_STS-B: Semantic similarity benchmark for pipeline quality. Source URL: https://dl.fbaipublicfiles.com/glue/data/STS-B.zip
- D03_ud_english_ewt_r2.17: Structured linguistic treebank for pre/post forgetful mapping. Source URL: https://github.com/UniversalDependencies/UD_English-EWT/archive/refs/tags/r2.17.tar.gz

## Next step
- Convert/extract these archives into the Cycle 3 input tables (`D02.csv`, `A01.csv`, `D03.csv`) and run metrics for Omega_A/B/C.
