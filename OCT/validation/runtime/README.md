# OCT Validation Runtime Artifacts

Date: 2026-05-01  
Purpose: minimal operational layer for v5.3 governance

## Contents

1. `OCT_APPEND_ONLY_TRAJECTORY_SCHEMA_v0_1.json`
   - canonical append-only event schema for process-level traces.
2. `OCT_PREREG_SEAL_SCHEMA_v0_1.json`
   - canonical preregistration seal schema (hash/timestamp/immutability fields).
3. `check_gate_compliance.py`
   - lightweight audit script checking required v5.3 gate artifacts.

## Usage

Run from repository root:

```powershell
python OCT/validation/runtime/check_gate_compliance.py
```

Optional explicit path:

```powershell
python OCT/validation/runtime/check_gate_compliance.py --validation-root OCT/validation
```

## Notes

This runtime package is intentionally minimal and policy-driven.  
It does not replace theorem-specific benchmark code; it enforces governance prerequisites before execution.

