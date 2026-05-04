#!/usr/bin/env python3
"""Substantive compliance check for OCT v5.3/v5.3.1 gate artifacts."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime
from pathlib import Path


REQUIRED_GLOBAL_FILES = [
    "OCT_EX_ANTE_PROXY_GATE_POLICY_v0_1.md",
    "OCT_CLAIM_TYPE_ANTIPATTERN_CHECKLIST_v0_1.md",
    "templates/OCT_PROXY_PREVALIDATION_SHEET_v0_1.md",
    "CYCLE_5_2026-05-01/CYCLE_5_OVERVIEW_v0_1.md",
    "CYCLE_5_2026-05-01/CYCLE_5_EXECUTION_AND_REJECT_RULES_v0_1.md",
    "CYCLE_5_2026-05-01/CYCLE_5_PREREG_SEAL_TEMPLATE_v0_1.md",
    "runtime/OCT_PREREG_SEAL_SCHEMA_v0_1.json",
    "runtime/OCT_APPEND_ONLY_TRAJECTORY_SCHEMA_v0_1.json",
]

THEOREM_CONFIG = {
    "A01": {
        "spec": "CYCLE_5_2026-05-01/CYCLE_5_A01_PROCESS_LEVEL_SPEC_v0_1.md",
        "sheet": "CYCLE_5_2026-05-01/instances/A01_OCT_PROXY_PREVALIDATION_SHEET_v0_1.md",
        "seal": "CYCLE_5_2026-05-01/seals/A01_PREREG_SEAL_v0_1.json",
        "trajectory": "CYCLE_5_2026-05-01/trajectory/A01_trajectory_events.jsonl",
    },
    "D03": {
        "spec": "CYCLE_5_2026-05-01/CYCLE_5_D03_LOCKED_TAXONOMY_SPEC_v0_1.md",
        "sheet": "CYCLE_5_2026-05-01/instances/D03_OCT_PROXY_PREVALIDATION_SHEET_v0_1.md",
        "seal": "CYCLE_5_2026-05-01/seals/D03_PREREG_SEAL_v0_1.json",
        "trajectory": "CYCLE_5_2026-05-01/trajectory/D03_trajectory_events.jsonl",
    },
    "D02": {
        "spec": "CYCLE_5_2026-05-01/CYCLE_5_D02_EVIDENCE_CLASS_SPEC_v0_1.md",
        "sheet": "CYCLE_5_2026-05-01/instances/D02_OCT_PROXY_PREVALIDATION_SHEET_v0_1.md",
        "seal": "CYCLE_5_2026-05-01/seals/D02_PREREG_SEAL_v0_1.json",
        "trajectory": "CYCLE_5_2026-05-01/trajectory/D02_trajectory_events.jsonl",
    },
}

SHEET_REQUIRED_HEADINGS = [
    "## 1) Claim logical type",
    "## 2) Claim statement and falsifier statement",
    "## 3) Concept-to-observable mapping table",
    "## 4) Anti-pattern prevention checks (mandatory)",
    "### 4.1 Comparative claim guard (level-shift test)",
    "### 4.2 Taxonomic claim guard (post-hoc rescue lock)",
    "### 4.3 Existential claim guard (vacuum-pass test)",
    "### 4.4 Universal claim guard (trivial confirmation lock)",
    "## 5) Falsifiability reachability test",
    "### 5.1 Pre-registered context list (mandatory when using multi-context criteria)",
    "## 6) Validity space coverage declaration (Coh/Phi/Delta)",
    "## 7) Evidence class declaration",
    "## 8) Role separation confirmation",
    "## 9) Preregistration seal",
    "## 10) Gate decision",
]

SHEET_REQUIRED_LABELS = [
    "Date:",
    "Prepared by (proxy designer):",
    "Audited by (independent auditor):",
    "Theorem ID:",
    "Cycle ID candidate:",
    "Status:",
    "Decision:",
    "Signer (auditor):",
]

SEAL_HASH_FIELDS = [
    ("claim_source_path", "claim_hash"),
    ("thresholds_source_path", "thresholds_hash"),
    ("formula_source_path", "formula_hash"),
    ("dataset_manifest_path", "dataset_manifest_hash"),
    ("script_version_source_path", "script_version_hash"),
    ("contexts_source_path", "contexts_hash"),
]

PLACEHOLDER_PATTERN = re.compile(
    r"\b(todo|tbd|pending|placeholder|n/a|to be assigned|none)\b",
    re.IGNORECASE,
)

DOI_PATTERN = re.compile(r"^10\.\d{4,9}/[-._;()/:A-Za-z0-9]+$")
SHA256_PATTERN = re.compile(r"^[A-Fa-f0-9]{64}$")
SEAL_METHOD_RULES = {
    "zenodo_doi": lambda value: bool(DOI_PATTERN.fullmatch(value)),
    "opentimestamps": lambda value: value.endswith(".ots")
    or ".ots" in value
    or value.startswith("https://"),
    "ipfs_cid": lambda value: value.startswith("ipfs://"),
    "git_signed_tag_with_external_witness": lambda value: value.startswith("https://")
    or value.startswith("http://"),
}

TEXT_HASH_EXTENSIONS = {
    ".md",
    ".txt",
    ".json",
    ".jsonl",
    ".py",
    ".csv",
    ".yaml",
    ".yml",
}


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _extract_label_value(text: str, label: str) -> str:
    pattern = re.compile(rf"^{re.escape(label)}\s*(.*)$", re.MULTILINE)
    match = pattern.search(text)
    return match.group(1).strip() if match else ""


def _is_non_placeholder(value: str) -> bool:
    return bool(value.strip()) and not PLACEHOLDER_PATTERN.search(value.strip())


def _parse_iso_datetime(value: str) -> datetime | None:
    raw = value.strip()
    if not raw:
        return None
    if raw.endswith("Z"):
        raw = raw[:-1] + "+00:00"
    try:
        return datetime.fromisoformat(raw)
    except ValueError:
        return None


def _canonicalize_text_bytes(data: bytes) -> bytes:
    bom = b"\xef\xbb\xbf"
    if data.startswith(bom):
        data = data[len(bom) :]
    data = data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return data


def _sha256_file(path: Path, canonicalize_text: bool) -> str:
    digest = hashlib.sha256()
    data = path.read_bytes()
    if canonicalize_text and path.suffix.lower() in TEXT_HASH_EXTENSIONS:
        data = _canonicalize_text_bytes(data)
    digest.update(data)
    return digest.hexdigest()


def _resolve_artifact_path(validation_root: Path, raw_path: str) -> Path:
    candidate = Path(raw_path)
    return candidate if candidate.is_absolute() else (validation_root / candidate).resolve()


def _load_json(path: Path) -> dict | list:
    return json.loads(path.read_text(encoding="utf-8"))


def _read_trajectory_first_timestamp(path: Path) -> datetime | None:
    if not path.exists():
        return None

    suffix = path.suffix.lower()
    try:
        if suffix == ".jsonl":
            first_ts = None
            for line in path.read_text(encoding="utf-8").splitlines():
                stripped = line.strip()
                if not stripped:
                    continue
                event = json.loads(stripped)
                ts = _parse_iso_datetime(str(event.get("timestamp_utc", "")))
                if ts is None:
                    continue
                if first_ts is None or ts < first_ts:
                    first_ts = ts
            return first_ts
        if suffix == ".json":
            data = _load_json(path)
            if isinstance(data, list):
                timestamps = [
                    _parse_iso_datetime(str(event.get("timestamp_utc", "")))
                    for event in data
                    if isinstance(event, dict)
                ]
                timestamps = [ts for ts in timestamps if ts is not None]
                return min(timestamps) if timestamps else None
    except (OSError, json.JSONDecodeError):
        return None
    return None


def _check_sheet(sheet_path: Path, theorem_id: str) -> dict:
    result = {
        "path": str(sheet_path),
        "exists": sheet_path.exists(),
        "pass": False,
        "errors": [],
        "warnings": [],
    }
    if not sheet_path.exists():
        result["errors"].append("Missing instantiated pre-validation sheet.")
        return result

    text = _read_text(sheet_path)
    for heading in SHEET_REQUIRED_HEADINGS:
        if heading not in text:
            result["errors"].append(f"Missing section heading: {heading}")

    labels = {label: _extract_label_value(text, label) for label in SHEET_REQUIRED_LABELS}
    for label, value in labels.items():
        if not _is_non_placeholder(value):
            result["errors"].append(f"Missing or placeholder value for `{label}`")

    sheet_theorem = labels.get("Theorem ID:", "")
    if sheet_theorem and sheet_theorem != theorem_id:
        result["errors"].append(
            f"Theorem mismatch in sheet: expected `{theorem_id}`, found `{sheet_theorem}`."
        )

    designer = labels.get("Prepared by (proxy designer):", "")
    auditor = labels.get("Audited by (independent auditor):", "")
    if designer and auditor and designer.strip() == auditor.strip():
        result["errors"].append("Role separation failed: designer equals auditor.")

    decision_value = labels.get("Decision:", "")
    if decision_value.upper() != "PASS":
        result["errors"].append(
            f"Gate decision is `{decision_value or 'empty'}`; expected `PASS`."
        )

    signer_value = labels.get("Signer (auditor):", "")
    if signer_value and auditor and signer_value.strip() != auditor.strip():
        result["warnings"].append(
            "Signer differs from declared auditor; verify delegated signing policy."
        )

    result["pass"] = len(result["errors"]) == 0
    return result


def _check_seal(
    validation_root: Path,
    seal_path: Path,
    theorem_id: str,
    expected_cycle_id: str,
    trajectory_path: Path,
    canonicalize_hashes: bool,
) -> dict:
    result = {
        "path": str(seal_path),
        "exists": seal_path.exists(),
        "pass": False,
        "errors": [],
        "warnings": [],
    }
    if not seal_path.exists():
        result["errors"].append("Missing preregistration seal JSON.")
        return result

    try:
        payload = _load_json(seal_path)
    except (json.JSONDecodeError, OSError) as exc:
        result["errors"].append(f"Cannot parse seal JSON: {exc}")
        return result

    if not isinstance(payload, dict):
        result["errors"].append("Seal payload must be a JSON object.")
        return result

    required_fields = {
        "cycle_id",
        "theorem_id",
        "spec_file",
        "designer",
        "auditor",
        "auditor_independence_declared",
        "auditor_independence_note",
        "claim_source_path",
        "claim_hash",
        "thresholds_source_path",
        "thresholds_hash",
        "formula_source_path",
        "formula_hash",
        "dataset_manifest_path",
        "dataset_manifest_hash",
        "script_version_source_path",
        "script_version_hash",
        "contexts_source_path",
        "contexts_hash",
        "timestamp_utc",
        "seal_method",
        "immutable_storage_path",
        "auditor_signature",
        "lock_acknowledged",
    }
    missing_fields = sorted(field for field in required_fields if field not in payload)
    if missing_fields:
        result["errors"].append(f"Seal missing required fields: {', '.join(missing_fields)}")
        return result

    if payload.get("theorem_id") != theorem_id:
        result["errors"].append(
            f"Seal theorem mismatch: expected `{theorem_id}`, found `{payload.get('theorem_id')}`."
        )

    if payload.get("cycle_id") != expected_cycle_id:
        result["errors"].append(
            f"Seal cycle mismatch: expected `{expected_cycle_id}`, found `{payload.get('cycle_id')}`."
        )

    designer = str(payload.get("designer", "")).strip()
    auditor = str(payload.get("auditor", "")).strip()
    if not _is_non_placeholder(designer):
        result["errors"].append("Seal field `designer` is empty or placeholder.")
    if not _is_non_placeholder(auditor):
        result["errors"].append("Seal field `auditor` is empty or placeholder.")
    if designer and auditor and designer == auditor:
        result["errors"].append("Role separation failed in seal: designer equals auditor.")

    if payload.get("auditor_independence_declared") is not True:
        result["errors"].append("`auditor_independence_declared` must be true.")
    if not _is_non_placeholder(str(payload.get("auditor_independence_note", ""))):
        result["errors"].append("Missing substantive `auditor_independence_note`.")

    if not _is_non_placeholder(str(payload.get("auditor_signature", ""))):
        result["errors"].append("Missing substantive auditor signature.")

    if payload.get("lock_acknowledged") is not True:
        result["errors"].append("`lock_acknowledged` must be true.")

    seal_method = str(payload.get("seal_method", "")).strip()
    immutable_path = str(payload.get("immutable_storage_path", "")).strip()
    rule = SEAL_METHOD_RULES.get(seal_method)
    if rule is None:
        result["errors"].append(
            f"Invalid `seal_method` `{seal_method}`. Allowed: {', '.join(SEAL_METHOD_RULES)}."
        )
    elif not rule(immutable_path):
        result["errors"].append(
            f"`immutable_storage_path` is not valid for `seal_method={seal_method}`."
        )

    for source_key, hash_key in SEAL_HASH_FIELDS:
        source_raw = str(payload.get(source_key, "")).strip()
        hash_value = str(payload.get(hash_key, "")).strip()

        if not _is_non_placeholder(source_raw):
            result["errors"].append(f"Missing source path `{source_key}`.")
            continue
        if not SHA256_PATTERN.fullmatch(hash_value):
            result["errors"].append(f"Invalid SHA-256 value in `{hash_key}`.")
            continue

        source_path = _resolve_artifact_path(validation_root, source_raw)
        if not source_path.exists() or not source_path.is_file():
            result["errors"].append(f"Referenced source path not found: `{source_raw}`")
            continue

        computed = _sha256_file(source_path, canonicalize_text=canonicalize_hashes)
        if computed.lower() != hash_value.lower():
            result["errors"].append(
                f"Hash mismatch for `{source_key}`: expected `{hash_value}`, computed `{computed}`."
            )

    seal_dt = _parse_iso_datetime(str(payload.get("timestamp_utc", "")))
    if seal_dt is None:
        result["errors"].append("Invalid `timestamp_utc` in seal.")
    else:
        first_event_dt = _read_trajectory_first_timestamp(trajectory_path)
        if first_event_dt is not None and seal_dt >= first_event_dt:
            result["errors"].append(
                "Seal timestamp must be strictly earlier than first trajectory event timestamp."
            )
        elif first_event_dt is None:
            result["warnings"].append(
                "No trajectory event log found yet; timestamp precedence check skipped."
            )

    result["pass"] = len(result["errors"]) == 0
    return result


def run_check(validation_root: Path, cycle_id: str, canonicalize_hashes: bool) -> dict:
    missing_global = []
    present_global = []

    for rel in REQUIRED_GLOBAL_FILES:
        path = validation_root / rel
        if path.exists():
            present_global.append(rel)
        else:
            missing_global.append(rel)

    theorem_status = {}
    for theorem_id, cfg in THEOREM_CONFIG.items():
        spec_path = validation_root / cfg["spec"]
        sheet_path = validation_root / cfg["sheet"]
        seal_path = validation_root / cfg["seal"]
        trajectory_path = validation_root / cfg["trajectory"]

        spec_exists = spec_path.exists()
        if spec_exists:
            present_global.append(cfg["spec"])
        else:
            missing_global.append(cfg["spec"])

        sheet_result = _check_sheet(sheet_path, theorem_id)
        seal_result = _check_seal(
            validation_root,
            seal_path,
            theorem_id,
            cycle_id,
            trajectory_path,
            canonicalize_hashes=canonicalize_hashes,
        )

        theorem_errors = []
        theorem_errors.extend(sheet_result["errors"])
        theorem_errors.extend(seal_result["errors"])

        theorem_status[theorem_id] = {
            "spec_path": cfg["spec"],
            "spec_exists": spec_exists,
            "sheet_check": sheet_result,
            "seal_check": seal_result,
            "errors_count": len(theorem_errors),
            "warnings_count": len(sheet_result["warnings"]) + len(seal_result["warnings"]),
        }

    compliant = (len(missing_global) == 0) and all(
        status["errors_count"] == 0 and status["spec_exists"] for status in theorem_status.values()
    )

    return {
        "validation_root": str(validation_root),
        "cycle_id": cycle_id,
        "hash_mode": "canonical_text_utf8_lf" if canonicalize_hashes else "raw_bytes",
        "compliant": compliant,
        "global_missing_count": len(missing_global),
        "global_missing": sorted(set(missing_global)),
        "global_present_count": len(sorted(set(present_global))),
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
        "--cycle-id",
        default="CYCLE_5_2026-05-01",
        help="Cycle identifier expected in theorem seals.",
    )
    parser.add_argument(
        "--write-report",
        default="OCT/validation/runtime/compliance_report_v0_1.json",
        help="Output JSON report path",
    )
    parser.add_argument(
        "--raw-hash",
        action="store_true",
        help="Use raw-byte hash mode instead of canonical text hash mode.",
    )
    args = parser.parse_args()

    validation_root = Path(args.validation_root).resolve()
    report = run_check(validation_root, args.cycle_id, canonicalize_hashes=not args.raw_hash)

    out_path = Path(args.write_report).resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    print(json.dumps(report, indent=2))
    return 0 if report["compliant"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
