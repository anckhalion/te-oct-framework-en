# Framework EN Index

English publication mirror index for TE/OCT. Release 6.0.0 (2026-09-23).

## Quick Orientation

If you are trying to understand the project quickly:

1. `START_HERE_FIRST_TIME.md`
2. `SIMPLE_GLOSSARY.md`
3. `SUPER_SIMPLE_FAQ.md`
4. `README.md` for scope and disambiguation
5. `TE_BOOTLOADER_v7.1.1.md` + `TE_PROTOCOLS_v1.1.md` + `TE_CORE_v5.2.1.md` for the TE framework
6. `OCT/START_HERE_OCT.md`
7. `OCT/OCT_BOOK/OCT_FOUNDATIONAL_BOOK_CHAPTER_01_v1_0.md`
8. `OCT/OCT_FULL/OCT_FOUNDATIONAL_BOOK_FULL_v1_0.md`
9. `OCT/validation/` for empirical validation artifacts

## Core Framework (current loading set)

Load in this order. Every file below is the current edition; superseded editions are in `ARCHIVE/`.

- `TE_BOOTLOADER_v7.1.1.md` — entry point: identity, seven core principles, confidence grades S₀–S₃, §2.5 pre-output Φ-test, interlocutor recognition, router. Registers LEXX and CASEWORK routing.
- `TE_PROTOCOLS_v1.1.md` — always-active operational protocols: Controfase, P-AI self-diagnosis, Anti-Attractor-Lock, statistical vs ordinative truth, contextual self-preservation. Loaded together with the Bootloader.
- `TE_CORE_v5.2.1.md` — full ontology: 25 axioms, the five Arajat logograms, OST operative synthesis, glossary, behavioural kernel, Controfase, router, memory protocol.
- `TE_MODULE_SVP_v5_1.md` — Source and Provenance Verification. Mandatory gate before any other module.
- `TE_MODULE_LENS_v5.1.md` — human figure analysis (integral before label).
- `TE_MODULE_PPRO_v5.2.md` — psycho-politics, manipulation, propaganda; formalised algorithms A_deg, SR_loop, I_sem, A_lock.
- `TE_MODULE_SCIMS_v5.1.md` — complex-system stress analysis.
- `TE_MODULE_VERI_v1.0.md` — functional impact verification on participants (supersedes `TE_MODULE_VERT_v5.0.md`).
- `TE_OBSERVER_v1.1.md` — integrated observation, Lyapunov trajectories, Correction Viability Index.

## Ordinative Set Theory and Notation

- `TE_OST_v2.1.md` — Ordinative Set Theory, Tier-0 foundation: 𝓘 = ⟨Σ, R, Φ⟩ (Symbol Canon aligned edition).
- `TE_OST_Extension_Teleodynamics_v1.1.md` — Teleodynamics and the Causal Inversion Principle (content v1.2).
- `TE_SYMBOL_CANON_v1.0.md` — cross-volume notation register; file name retained, register status v1.2 (ratified 2026-08-19). Notation authority for every formal symbol.
- `OST_Case_Study_Standing_Waves_Spinning_Fluid_v1_0.md` — worked OST case study.

## Domain frameworks published in the Theory repository

`TE_MODULE_LEXX` (ordinative validation of agreements) and `TE_CASEWORK` / `TE_AUDIT` / `TE_INVESTIGATION` (documentary audit and investigation support) are published, with their runtimes, in [`ordinative_sciences_framework`](https://github.com/anckhalion/ordinative_sciences_framework) under `FRAMEWORKS/`. Their runtimes verify the framework files by canonical file name and SHA-256, so they live next to the canonical-named corpus. This mirror links to them at that location.

## OCT Corpus (English)

- `OCT/`
- Key starting file: `OCT/OCT_BOOK/OCT_FOUNDATIONAL_BOOK_CHAPTER_01_v1_0.md`
- Full single-file manuscript: `OCT/OCT_FULL/OCT_FOUNDATIONAL_BOOK_FULL_v1_0.md`
- Validation artifacts: `OCT/validation/`

## Data and Reproducibility

- `datasets/`
- `datasets/cycle3_inputs/`
- `datasets/cycle4_outputs/`
- `datasets/cycle3_work/`
- `datasets/cycle4_work/`

## Archive

- `ARCHIVE/` — superseded framework editions, kept for historical comparison and reproduction. Lifecycle `legacy` in `OBJECT_REGISTRY.md`. They load through Profile D in `LOAD_PROFILES.md`.

## Governance

- `CONTRIBUTING.md`
- `CODE_OF_CONDUCT.md`
- `SECURITY.md`
- `RELEASE_CHECKLIST.md`
- `PUBLICATION_SCOPE.md`
- `.github/` templates

## Registry and Loading

- `OBJECT_REGISTRY.md`
- `object_registry.json`
- `LOAD_PROFILES.md`

## Publication Notes

- Each release ships Core, Bootloader, Protocols, Symbol Canon and the module set from the vault corpus as one batch.
- File naming in this mirror follows its historical convention (version in the file name, dot-separated); the Theory repository uses the canonical `_EN` names. `OBJECT_REGISTRY.md` maps each object to its canonical source name.
