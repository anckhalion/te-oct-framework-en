# Changelog

All notable changes to this repository should be documented in this file.

The format is inspired by Keep a Changelog and semantic versioning principles for documentation releases.

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
