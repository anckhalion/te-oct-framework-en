import csv
import json
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
INP = ROOT / "datasets" / "cycle3_inputs" / "D03.csv"
OUT_DIR = ROOT / "datasets" / "cycle4_outputs"
OUT_DIR.mkdir(parents=True, exist_ok=True)
OMEGAS = ["Omega_A", "Omega_B", "Omega_C"]


def eval_thresholds(rows, low, high):
    by_omega = defaultdict(Counter)
    total = Counter()
    for row in rows:
        lu = float(row["loss_u"])
        if lu <= low:
            cls = "preservativo"
        elif lu >= high:
            cls = "degenerativo"
        else:
            cls = "ambiguo"
        by_omega[row["omega"]][cls] += 1
        total[cls] += 1

    n = sum(total.values())
    amb_rate = (total["ambiguo"] / n) if n else 0.0
    coexist = True
    omega_rows = {}
    for om in OMEGAS:
        c = by_omega[om]
        om_n = sum(c.values())
        p = c["preservativo"] / om_n if om_n else 0.0
        d = c["degenerativo"] / om_n if om_n else 0.0
        a = c["ambiguo"] / om_n if om_n else 0.0
        omega_rows[om] = {"preservativo": p, "degenerativo": d, "ambiguo": a}
        if c["preservativo"] == 0 or c["degenerativo"] == 0:
            coexist = False
    return {
        "low": low,
        "high": high,
        "ambiguous_rate": amb_rate,
        "coexist_all_contexts": coexist,
        "total_preservativo": total["preservativo"],
        "total_degenerativo": total["degenerativo"],
        "total_ambiguo": total["ambiguo"],
        "omega": omega_rows,
    }


def main():
    with INP.open("r", encoding="utf-8", errors="ignore") as f:
        rows = list(csv.DictReader(f))

    results = []
    lows = [0.272, 0.274, 0.276, 0.278]
    highs = [0.284, 0.286, 0.288]
    for low in lows:
        for high in highs:
            if low >= high:
                continue
            results.append(eval_thresholds(rows, low, high))

    out_json = OUT_DIR / "d03_threshold_stress.json"
    out_json.write_text(json.dumps(results, indent=2), encoding="utf-8")

    out_csv = OUT_DIR / "d03_threshold_stress.csv"
    with out_csv.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(
            f,
            fieldnames=[
                "low",
                "high",
                "ambiguous_rate",
                "coexist_all_contexts",
                "total_preservativo",
                "total_degenerativo",
                "total_ambiguo",
                "Omega_A_preservativo",
                "Omega_A_degenerativo",
                "Omega_A_ambiguo",
                "Omega_B_preservativo",
                "Omega_B_degenerativo",
                "Omega_B_ambiguo",
                "Omega_C_preservativo",
                "Omega_C_degenerativo",
                "Omega_C_ambiguo",
            ],
        )
        w.writeheader()
        for r in results:
            row = {
                "low": r["low"],
                "high": r["high"],
                "ambiguous_rate": r["ambiguous_rate"],
                "coexist_all_contexts": r["coexist_all_contexts"],
                "total_preservativo": r["total_preservativo"],
                "total_degenerativo": r["total_degenerativo"],
                "total_ambiguo": r["total_ambiguo"],
                "Omega_A_preservativo": r["omega"]["Omega_A"]["preservativo"],
                "Omega_A_degenerativo": r["omega"]["Omega_A"]["degenerativo"],
                "Omega_A_ambiguo": r["omega"]["Omega_A"]["ambiguo"],
                "Omega_B_preservativo": r["omega"]["Omega_B"]["preservativo"],
                "Omega_B_degenerativo": r["omega"]["Omega_B"]["degenerativo"],
                "Omega_B_ambiguo": r["omega"]["Omega_B"]["ambiguo"],
                "Omega_C_preservativo": r["omega"]["Omega_C"]["preservativo"],
                "Omega_C_degenerativo": r["omega"]["Omega_C"]["degenerativo"],
                "Omega_C_ambiguo": r["omega"]["Omega_C"]["ambiguo"],
            }
            w.writerow(row)

    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
