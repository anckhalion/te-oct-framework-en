# OCT Validation Runtime Artifacts

Date: 2026-05-01  
Purpose: minimal operational layer for v5.3 governance

## Contents

1. `OCT_APPEND_ONLY_TRAJECTORY_SCHEMA_v0_1.json`
   - canonical append-only event schema for process-level traces.
2. `OCT_PREREG_SEAL_SCHEMA_v0_1.json`
   - canonical preregistration seal schema (hash/timestamp/immutability fields).
3. `check_gate_compliance.py`
   - substantive audit script for theorem-level gate compliance:
     - instantiated pre-validation sheets,
     - explicit `PASS` decision,
     - role separation checks,
     - prereg seal integrity and hash re-check,
     - timestamp precedence vs trajectory logs.
   - default hash mode: canonical text hashing (UTF-8, BOM stripped, LF line endings) for cross-platform reproducibility.
   - optional `--raw-hash` mode for byte-level diagnostics.
4. `run_cycle5_execution.py`
   - deterministic cycle5 proxy execution runner generating full trajectory logs, results, and reports.
5. `refresh_seal_hashes.py`
   - recomputes seal hash fields in canonical hash mode.

## Usage

Run from repository root:

```powershell
python OCT/validation/runtime/check_gate_compliance.py
```

Optional explicit path:

```powershell
python OCT/validation/runtime/check_gate_compliance.py --validation-root OCT/validation
```

Raw-byte diagnostic run:

```powershell
python OCT/validation/runtime/check_gate_compliance.py --raw-hash
```

## Notes

This runtime package is governance-driven.  
It does not replace theorem-specific benchmark code; it enforces pre-run admissibility constraints before execution.
