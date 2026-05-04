#!/usr/bin/env python3
"""Refresh Cycle 5 seal hash fields using canonical UTF-8 LF text hashing."""

from __future__ import annotations

import json
import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
VALIDATION_ROOT = ROOT / "OCT" / "validation"
SEAL_DIR = VALIDATION_ROOT / "CYCLE_5_2026-05-01" / "seals"

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

HASH_FIELDS = [
    ("claim_source_path", "claim_hash"),
    ("thresholds_source_path", "thresholds_hash"),
    ("formula_source_path", "formula_hash"),
    ("dataset_manifest_path", "dataset_manifest_hash"),
    ("script_version_source_path", "script_version_hash"),
    ("contexts_source_path", "contexts_hash"),
]


def canonicalize_text_bytes(data: bytes) -> bytes:
    bom = b"\xef\xbb\xbf"
    if data.startswith(bom):
        data = data[len(bom) :]
    data = data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return data


def file_hash(path: Path) -> str:
    data = path.read_bytes()
    if path.suffix.lower() in TEXT_HASH_EXTENSIONS:
        data = canonicalize_text_bytes(data)
    return hashlib.sha256(data).hexdigest()


def main() -> int:
    seal_files = sorted(SEAL_DIR.glob("*_PREREG_SEAL_v0_1.json"))
    if not seal_files:
        print("No seal files found.")
        return 1

    for seal_path in seal_files:
        payload = json.loads(seal_path.read_text(encoding="utf-8"))
        for source_key, hash_key in HASH_FIELDS:
            source_rel = payload[source_key]
            source_path = (VALIDATION_ROOT / source_rel).resolve()
            payload[hash_key] = file_hash(source_path)

        seal_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        print(f"Updated {seal_path.name}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
