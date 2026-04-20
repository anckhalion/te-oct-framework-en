import csv
import json
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
INP = ROOT / "datasets" / "cycle3_inputs" / "D03.csv"
OUT_DIR = ROOT / "datasets" / "cycle4_outputs"
OUT_DIR.mkdir(parents=True, exist_ok=True)
OMEGAS = ["Omega_A", "Omega_B", "Omega_C"]


SCHEMES = {
    # Primary preregistered scheme (fixed, non-adaptive): centered around loss_u ~= 0.28.
    "S1_primary_fixed_band": {"low": 0.276, "high": 0.284},
    # Robustness scheme with slightly wider uncertainty band.
    "S2_robust_wide_band": {"low": 0.274, "high": 0.286},
}


def classify(loss_u: float, low: float, high: float):
    if loss_u <= low:
        return "preservativo"
    if loss_u >= high:
        return "degenerativo"
    return "ambiguo"


def evaluate_scheme(rows, low, high):
    by_omega = defaultdict(Counter)
    total = Counter()
    classified_rows = []
    for row in rows:
        lu = float(row["loss_u"])
        cls = classify(lu, low, high)
        om = row["omega"]
        by_omega[om][cls] += 1
        total[cls] += 1
        new_row = dict(row)
        new_row["class_cycle4"] = cls
        classified_rows.append(new_row)

    n = sum(total.values())
    amb_rate = (total["ambiguo"] / n) if n else 0.0
    summary_by_omega = {}
    coexist_all = True
    for om in OMEGAS:
        c = by_omega[om]
        om_n = sum(c.values())
        if om_n == 0:
            summary_by_omega[om] = {
                "n": 0,
                "preservativo": 0.0,
                "degenerativo": 0.0,
                "ambiguo": 0.0,
            }
            coexist_all = False
            continue
        p = c["preservativo"] / om_n
        d = c["degenerativo"] / om_n
        a = c["ambiguo"] / om_n
        summary_by_omega[om] = {"n": om_n, "preservativo": p, "degenerativo": d, "ambiguo": a}
        if c["preservativo"] == 0 or c["degenerativo"] == 0:
            coexist_all = False

    return {
        "total_counts": dict(total),
        "ambiguous_rate": amb_rate,
        "coexisting_regimes_all_contexts": coexist_all,
        "summary_by_omega": summary_by_omega,
        "rows": classified_rows,
    }


def main():
    with INP.open("r", encoding="utf-8", errors="ignore") as f:
        rows = list(csv.DictReader(f))

    all_results = {}
    for name, cfg in SCHEMES.items():
        res = evaluate_scheme(rows, cfg["low"], cfg["high"])
        all_results[name] = {
            "thresholds": cfg,
            "total_counts": res["total_counts"],
            "ambiguous_rate": res["ambiguous_rate"],
            "coexisting_regimes_all_contexts": res["coexisting_regimes_all_contexts"],
            "summary_by_omega": res["summary_by_omega"],
        }
        out_csv = OUT_DIR / f"D03_reclassified_{name}.csv"
        with out_csv.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(
                f,
                fieldnames=list(res["rows"][0].keys()) if res["rows"] else ["pair_id", "omega", "loss_u", "class_cycle4"],
            )
            w.writeheader()
            w.writerows(res["rows"])

    out_json = OUT_DIR / "d03_cycle4_revision_metrics.json"
    out_json.write_text(json.dumps(all_results, indent=2), encoding="utf-8")
    print(json.dumps(all_results, indent=2))


if __name__ == "__main__":
    main()
