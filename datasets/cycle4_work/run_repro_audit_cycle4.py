import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PY = sys.executable


def run_script(rel_path: str):
    p = ROOT / rel_path
    cp = subprocess.run([PY, str(p)], cwd=ROOT, capture_output=True, text=True)
    return {
        "script": rel_path,
        "returncode": cp.returncode,
        "stdout_tail": cp.stdout[-8000:],
        "stderr_tail": cp.stderr[-4000:],
    }


def load_json(rel_path: str):
    return json.loads((ROOT / rel_path).read_text(encoding="utf-8"))


def main():
    runs = []
    runs.append(run_script("datasets/cycle3_work/build_cycle3_inputs.py"))
    runs.append(run_script("datasets/cycle3_work/run_cycle3_metrics.py"))
    runs.append(run_script("datasets/cycle4_work/run_d03_revision_cycle4.py"))
    runs.append(run_script("datasets/cycle4_work/run_d03_threshold_stress.py"))

    checks = []
    ok = True
    for r in runs:
        passed = r["returncode"] == 0
        checks.append({"name": f"run::{r['script']}", "passed": passed})
        ok = ok and passed

    run_summary = load_json("datasets/cycle3_inputs/run_summary.json")
    cycle3_metrics = load_json("datasets/cycle3_inputs/cycle3_metrics.json")
    d03_rev = load_json("datasets/cycle4_outputs/d03_cycle4_revision_metrics.json")
    d03_stress = load_json("datasets/cycle4_outputs/d03_threshold_stress.json")

    checks.extend(
        [
            {"name": "rows::D02==180", "passed": run_summary["D02"]["rows"] == 180},
            {"name": "rows::A01==320", "passed": run_summary["A01"]["rows"] == 320},
            {"name": "rows::D03==260", "passed": run_summary["D03"]["rows"] == 260},
            {"name": "A01::criteria_delta_pass", "passed": bool(cycle3_metrics["A01"]["criteria_pass_delta"])},
            {"name": "A01::criteria_err_pass", "passed": bool(cycle3_metrics["A01"]["criteria_pass_err"])},
            {
                "name": "D03::S1_coexist_true",
                "passed": bool(d03_rev["S1_primary_fixed_band"]["coexisting_regimes_all_contexts"]),
            },
            {
                "name": "D03::S1_ambiguous_lt_0.20",
                "passed": float(d03_rev["S1_primary_fixed_band"]["ambiguous_rate"]) < 0.20,
            },
            {
                "name": "D03::stress_has_valid_config",
                "passed": any(
                    (item["coexist_all_contexts"] and item["ambiguous_rate"] < 0.20)
                    for item in d03_stress
                ),
            },
        ]
    )

    for c in checks:
        ok = ok and bool(c["passed"])

    out = {
        "status": "PASS" if ok else "FAIL",
        "checks": checks,
        "runs": runs,
    }

    out_path = ROOT / "datasets" / "cycle4_outputs" / "audit_cycle4_repro_v0_1.json"
    out_path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
