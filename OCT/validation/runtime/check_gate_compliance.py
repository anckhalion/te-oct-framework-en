#!/usr/bin/env python3
"""Minimal compliance check for OCT v5.3 gate artifacts."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


REQUIRED_GLOBAL_FILES = [
    "OCT_EX_ANTE_PROXY_GATE_POLICY_v0_1.md",
    "OCT_CLAIM_TYPE_ANTIPATTERN_CHECKLIST_v0_1.md",
    "templates/OCT_PROXY_PREVALIDATION_SHEET_v0_1.md",
    "CYCLE_5_2026-05-01/CYCLE_5_OVERVIEW_v0_1.md",
    "CYCLE_5_2026-05-01/CYCLE_5_EXECUTION_AND_REJECT_RULES_v0_1.md",
    "CYCLE_5_2026-05-01/CYCLE_5_PREREG_SEAL_TEMPLATE_v0_1.md",
]

REQUIRED_THEOREM_SPECS = {
    "A01": "CYCLE_5_2026-05-01/CYCLE_5_A01_PROCESS_LEVEL_SPEC_v0_1.md",
    "D03": "CYCLE_5_2026-05-01/CYCLE_5_D03_LOCKED_TAXONOMY_SPEC_v0_1.md",
    "D02": "CYCLE_5_2026-05-01/CYCLE_5_D02_EVIDENCE_CLASS_SPEC_v0_1.md",
}


def run_check(validation_root: Path) -> dict:
    missing = []
    present = []

    for rel in REQUIRED_GLOBAL_FILES:
        p = validation_root / rel
        if p.exists():
            present.append(rel)
        else:
            missing.append(rel)

    theorem_status = {}
    for theorem, rel in REQUIRED_THEOREM_SPECS.items():
        p = validation_root / rel
        theorem_status[theorem] = {
            "path": rel,
            "exists": p.exists(),
        }
        if p.exists():
            present.append(rel)
        else:
            missing.append(rel)

    compliant = len(missing) == 0
    return {
        "validation_root": str(validation_root),
        "compliant": compliant,
        "missing_count": len(missing),
        "missing": missing,
        "present_count": len(present),
        "theorem_status": theorem_status,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--validation-root",
        default="OCT/validation",
        help="Path to OCT validation directory",
    )
    parser.add_argument(
        "--write-report",
        default="OCT/validation/runtime/compliance_report_v0_1.json",
        help="Output JSON report path",
    )
    args = parser.parse_args()

    validation_root = Path(args.validation_root).resolve()
    report = run_check(validation_root)

    out_path = Path(args.write_report).resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    print(json.dumps(report, indent=2))
    return 0 if report["compliant"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

