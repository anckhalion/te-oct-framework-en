# CYCLE 6 Benchmark Independence Protocol v0.1

Date: 2026-05-05  
Cycle: `CYCLE_6_2026-05-05`  
Theorem: A01

## 1) Independence definition

A Cycle 6 benchmark is independent from Cycle 3 iff all are true:
1. No shared record identifiers.
2. No shared normalized content hashes.
3. No shared pre-labeled trajectories reused as-is.
4. Context generation process is documented and new.

## 2) Required evidence

1. `A01_dataset_manifest_v0_1.md` with source URLs or generation recipe.
2. `A01_cycle3_overlap_report_v0_1.md` containing:
   - record ID overlap count
   - hash overlap count
   - overlap percentage
3. Signed auditor check on overlap report.

Acceptance threshold:
1. Record overlap count = `0`
2. Hash overlap count = `0`
3. Overlap percentage = `0.0%`

## 3) Hashing method

Canonicalization rules:
1. UTF-8 encoding
2. LF newline normalization
3. Trim trailing whitespace per line
4. SHA-256 digest

## 4) Context stratification rule

Cycle 6 contexts must not be decorative rescaling of a single distribution.
Each context declaration must include:
1. Distinguishing features
2. Expected difficulty
3. Perturbation profile
4. Dataset slice path

## 5) Failure policy

If independence proof fails:
1. Cycle execution status -> `blocked`
2. A01 cannot be promoted
3. New benchmark generation is mandatory before rerun

