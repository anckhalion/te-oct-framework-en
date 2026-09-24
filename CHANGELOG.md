# Changelog

All notable changes to this repository should be documented in this file.

The format is inspired by Keep a Changelog and semantic versioning principles for documentation releases.

## [6.0.0] - 2026-09-23

### Added
- `TE_PROTOCOLS_v1.1.md` — always-active operational protocols (Controfase, P-AI, Anti-Attractor-Lock, statistical vs ordinative truth, contextual self-preservation). First publication of the Protocols module in this mirror.
- `TE_MODULE_VERI_v1.0.md` — Functional Impact Verification, universalised successor of `TE_MODULE_VERT_v5.0.md`.
- `TE_BOOTLOADER_v7.1.1.md`, `TE_CORE_v5.2.1.md`, `TE_MODULE_LENS_v5.1.md`, `TE_MODULE_PPRO_v5.2.md`, `TE_MODULE_SCIMS_v5.1.md`, `TE_OBSERVER_v1.1.md` — current editions of the framework set (Bootloader and Core register the LEXX and CASEWORK routing).
- `ARCHIVE/` — superseded editions kept for reference (lifecycle `legacy`).

### Updated
- `TE_MODULE_SVP_v5_1.md`, `TE_OST_v2.1.md`, `TE_OST_Extension_Teleodynamics_v1.1.md` (content v1.2), `TE_SYMBOL_CANON_v1.0.md` (register status v1.2, Lyapunov-volume batch ratified 2026-08-19) — refreshed to the canonical corpus.
- Register patch applied in place, version numbers kept, as with the 2026-06-18 Symbol Canon alignment patch: a wording change; each file carries a dated patch note. Prescriptive uses of «honest / honestly / honesty» in `TE_CORE_v5.2.1.md` (§1.3, §6.7), `TE_BOOTLOADER_v7.1.1.md` (§4), `TE_MODULE_LENS_v5.1.md` (two notes) and `TE_OBSERVER_v1.1.md` (§10.1, §10.2) are restated as operations, in accordance with Bootloader §2.5.2 where such words are listed among the compliance markers (Φ = 0 patterns). Same register rule, one wording change each: `CODE_OF_CONDUCT.md` (opening commitment) and `OST_Case_Study_Standing_Waves_Spinning_Fluid_v1_0.md` («a declared inventory»).
- `INDEX.md`, `OBJECT_REGISTRY.md`, `object_registry.json`, `LOAD_PROFILES.md`, `START_HERE_FIRST_TIME.md`, `README.md`, `ECOSYSTEM.md`, `PUBLICATION_SCOPE.md` rewritten for the new loading set; the registry now maps each object to its canonical source file name.

### Retired (moved to `ARCHIVE/`)
- `TE_CORE_v5.0.md`, `TE_CORE_v5_1_PATCH.md`, `TE_CORE_v5.1.md`, `TE_BOOTLOADER_v6_0_PROJECT.md`, `TE_BOOTLOADER_v7.1.md`, `TE_MODULE_VERT_v5.0.md`, `TE_MODULE_LENS_v5.0.md`, `TE_MODULE_PPRO_v5.1.md`, `TE_MODULE_SCIMS_v5.0.md`, `TE_OBSERVER v1.0.md`, `TE_OBSERVER v1.0.1 Lyapunov XP.md`, `POST_RELEASE_REMINDERS_v5_3_0.md` (its priority reminder — module-version uplift — is fulfilled by this release), `TRANSLATION_REPORT_FRAMEWORK_EN.md` (June 2026 process record; it referenced the maintainer's private workspace paths).

### Notes
- Major version: the framework set changes as a whole (module uplift, Protocols and VERI added, legacy editions retired from the root). OCT corpus and datasets are unchanged.
- The domain frameworks `TE_MODULE_LEXX` (agreements) and `TE_CASEWORK` (documentary audit and investigation) are published with their runtimes in `ordinative_sciences_framework/FRAMEWORKS/`, where the framework files carry the canonical `_EN` names that the runtimes verify by hash. This mirror keeps its historical file-naming convention.
- Line endings: this repository normalises text files to LF (`.gitattributes`); the canonical corpus is CRLF. Content is identical; byte-level hashes are those of the Theory repository, which stores `FRAMEWORKS/` byte-exact.
- Register (2026-09-24): `README.md`, `START_HERE_FIRST_TIME.md`, `INDEX.md`, `LOAD_PROFILES.md`, `OBJECT_REGISTRY.md`, `PUBLICATION_SCOPE.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md` and this entry state facts in the positive form; the sections «What This Repository Is Not», «Exclusions» and «Do Not Confuse This Project With» are folded into the positive sections and into `PUBLICATION_SCOPE.md`.

## [5.4.1] - 2026-06-21

### Fixed
- OCT book internal cross-references now resolve. The OST guide is cited under its actual repository filename `TE_OST_v2.1.md` (was the legacy slug `Ordinative_Set_Theory_OST_A_Concise_Guide_For_AI_v2_1.md`, 34 occurrences across the consolidated bibliography, the per-chapter reference lists, and the single-file manuscript).
- `Ghioni_2026_Reaction_Diffusion_Civilizational_Dynamics_v1_2.md` reclassified from an internal-corpus reference to a forthcoming external citation (the work is not part of this repository).

### Added
- `OST_Case_Study_Standing_Waves_Spinning_Fluid_v1_0.md` — the worked OST case study cited by the OCT book, now bundled so the internal reference resolves.

## [5.4.0] - 2026-06-21

### Added
- `TE_OST_v2.1.md` — Ordinative Set Theory, the Tier-0 foundation of the Ordinative Sciences notation (`𝓘 = ⟨Σ, R, Φ⟩`), as a concise operational guide for AI.
- `TE_OST_Extension_Teleodynamics_v1.1.md` — advanced OST extension: Teleodynamics and the Causal Inversion Principle.
- `TE_SYMBOL_CANON_v1.0.md` — locked (ratified 2026-06-11) cross-volume notational governance register for the programme (tier precedence OST → TE Vol 1 → PA/SA/OCT). Master copy.
- `TE_BOOTLOADER_v7.1.md` — new bootloader revision adding §2.5 Pre-Output Functional Verification Pass (Φ-test) as a constitutive identity-level check. Previous `TE_BOOTLOADER_v6_0_PROJECT.md` retained for history.

### Updated
- `TE_CORE_v5.1.md` — refreshed to the Symbol Canon v1.0 aligned edition (`ℐ → 𝓘` throughout, SHACK binary-state label convention documented, cross-reference to `TE_SYMBOL_CANON_v1.0.md`). No ontology/axiom/glossary/protocol content changed.
- `TE_MODULE_SVP_v5_1.md` — refreshed to the Symbol Canon aligned edition.
- `INDEX.md` — Core Framework section now lists the OST corpus and Symbol Canon, and points to `TE_BOOTLOADER_v7.1.md` as current.

### Notes
- This release synchronizes the public mirror with the 2026-06-18 in-vault framework batch. The Symbol Canon is now the authoritative notation reference for this repository.

## [5.3.2] - 2026-05-06

### Updated
- `ECOSYSTEM.md` extended from 3-pillar to 4-pillar architecture to include the new `te-ordinative-algebras-en` repository (SA + PA frameworks).
- `README.md` "Part of a Larger Ecosystem" table updated from three-part to four-part, with row added for `te-ordinative-algebras-en`.

### Notes
- The new repository [`te-ordinative-algebras-en`](https://github.com/anckhalion/te-ordinative-algebras-en) was published on 2026-05-06 with initial release `v1.0.0`. It contains the Semantic Algebra (SA) and Proportional Algebra (PA) corpora plus a Python reference engine for PA. PA Theorem 9.1 establishes that SA is mathematically a restriction of PA to the decoherent space `D`; the two are presented as distinct frameworks bundled in one repository for cross-reference convenience.

## [5.3.1] - 2026-05-03

### Updated
- Hardened runtime compliance logic in `OCT/validation/runtime/check_gate_compliance.py`:
  - checks instantiated theorem sheets (not template presence only),
  - requires explicit `PASS` gate decision,
  - validates role separation,
  - validates prereg seal payload structure and hash re-computability,
  - checks prereg timestamp precedence against trajectory logs when available.
- Strengthened prereg and runtime schemas:
  - `OCT/validation/runtime/OCT_PREREG_SEAL_SCHEMA_v0_1.json`
  - `OCT/validation/runtime/OCT_APPEND_ONLY_TRAJECTORY_SCHEMA_v0_1.json`
- Strengthened governance policy and cycle specs:
  - `OCT/validation/OCT_EX_ANTE_PROXY_GATE_POLICY_v0_1.md`
  - `OCT/validation/CYCLE_5_2026-05-01/CYCLE_5_A01_PROCESS_LEVEL_SPEC_v0_1.md`
  - `OCT/validation/CYCLE_5_2026-05-01/CYCLE_5_D03_LOCKED_TAXONOMY_SPEC_v0_1.md`
  - `OCT/validation/CYCLE_5_2026-05-01/CYCLE_5_EXECUTION_AND_REJECT_RULES_v0_1.md`
  - `OCT/validation/CYCLE_5_2026-05-01/CYCLE_5_PREREG_SEAL_TEMPLATE_v0_1.md`
- Updated state interpretation artifacts:
  - `OCT/validation/OCT_PUBLICATION_PROGRESS_TRACKER_v0_1.md`
  - `OCT/OCT_BOOK/OCT_FOUNDATIONAL_BOOK_CHAPTER_17_v1_0.md`

### Notes
- `compliant=true` is now reserved for substantive gate compliance; template-only presence is no longer sufficient.
- Historical Cycle 3-4 outputs remain preserved but are not sufficient for theorem promotion under ex-ante gate policy.

## [5.3.0] - 2026-05-01

### Added
- OCT v5.3 governance package for theorem validation hardening:
  - `OCT/validation/OCT_EX_ANTE_PROXY_GATE_POLICY_v0_1.md`
  - `OCT/validation/templates/OCT_PROXY_PREVALIDATION_SHEET_v0_1.md`
  - `OCT/validation/OCT_CLAIM_TYPE_ANTIPATTERN_CHECKLIST_v0_1.md`
- External review corpus integrated into official OCT validation artifacts:
  - `OCT/validation/external_reviews_2026-05-01/anti_patterns_validation.md`
  - `OCT/validation/external_reviews_2026-05-01/a01_gate_design.md`
- Cycle 5 theorem refactor specification set:
  - `OCT/validation/CYCLE_5_2026-05-01/`
- Runtime minimum compliance package:
  - `OCT/validation/runtime/OCT_APPEND_ONLY_TRAJECTORY_SCHEMA_v0_1.json`
  - `OCT/validation/runtime/OCT_PREREG_SEAL_SCHEMA_v0_1.json`
  - `OCT/validation/runtime/check_gate_compliance.py`
  - `OCT/validation/runtime/compliance_report_v0_1.json`

### Updated
- `OCT/validation/DECISION_MATRIX_FINAL_UNIFIED_v0_1.md` now anchors `revise` rationale to Chapter 8 Definition 8.12 constraints.
- `OCT/validation/OCT_VALIDATION_CYCLES_PLAN_v0_1.md` updated with Cycle 5 hardening lane.
- `OCT/validation/OCT_PUBLICATION_PROGRESS_TRACKER_v0_1.md` and `OCT/validation/OCT_UPDATE_PLAN_v5_3.md` aligned to phases 1-4 minimum completion.
- OCT navigation and chapter references aligned to v5.3 artifacts:
  - `OCT/README.md`
  - `OCT/START_HERE_OCT.md`
  - `OCT/OCT_BOOK/OCT_FOUNDATIONAL_BOOK_CHAPTER_17_v1_0.md`

### Notes
- Phase 3 is specification-complete; execution of Cycle 5 benchmark runs remains pending.
- Runtime compliance check currently reports `compliant=true` for required gate artifacts.

## [5.2.0] - 2026-04-29

### Added
- `OCT/OCT_BOOK/` with the current 17-chapter OCT foundational book track and consolidated bibliography.
- `OCT/OCT_FULL/` with the single-file full manuscript (`OCT_FOUNDATIONAL_BOOK_FULL_v1_0.md`).
- `OCT/OCT_BOOK_LATEX/` with Overleaf-ready LaTeX sources.

### Updated
- Reader navigation updated to point to the current OCT manuscript path:
  - `README.md`
  - `INDEX.md`
  - `START_HERE_FIRST_TIME.md`
  - `SUPER_SIMPLE_FAQ.md`
  - `OCT/README.md`
  - `OCT/START_HERE_OCT.md`
- `.gitignore` updated to exclude `not-to-release` paths and LaTeX build artifacts.

### Notes
- Legacy OCT preprint candidate files remain in place for historical traceability.

## [5.1.0] - 2026-03-08

### Added
- Canonical core release file: `TE_CORE_v5.1.md`
- GitHub publication files:
  - `README.md`
  - `INDEX.md`
  - `CONTRIBUTING.md`
  - `CODE_OF_CONDUCT.md`
  - `SECURITY.md`
  - `.github` templates
  - `.gitignore`
  - `.gitattributes`

### Updated
- Core alignment with Bootloader v6.0 reflected in `TE_CORE_v5.1.md`

### Notes
- `TE_CORE_v5.0.md` remains available as legacy reference.
- `TE_CORE_v5_1_PATCH.md` remains available as patch provenance.
