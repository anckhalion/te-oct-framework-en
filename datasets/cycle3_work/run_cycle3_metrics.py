import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
INP = ROOT / "datasets" / "cycle3_inputs"
OUT = INP / "cycle3_metrics.json"
OMEGAS = ["Omega_A", "Omega_B", "Omega_C"]


def toks(text):
    return re.findall(r"[a-z0-9']+", text.lower())


def jaccard(a, b):
    sa = set(a)
    sb = set(b)
    if not sa and not sb:
        return 1.0
    if not sa or not sb:
        return 0.0
    return len(sa & sb) / len(sa | sb)


def soft_overlap(a, b):
    if not a or not b:
        return 0.0
    pa = {x[:4] for x in a}
    pb = {x[:4] for x in b}
    return len(pa & pb) / max(len(pa), len(pb))


def run_a01():
    path = INP / "A01.csv"
    by_omega = defaultdict(list)
    with path.open("r", encoding="utf-8", errors="ignore") as f:
        reader = csv.DictReader(f)
        for row in reader:
            a = toks(row["sentence1"])
            b = toks(row["sentence2"])
            gold = float(row["gold_score_norm"])
            cls_pred = jaccard(a, b)
            ord_pred = 0.55 * cls_pred + 0.45 * soft_overlap(a, b)
            delta_cls = 1.0 - cls_pred
            delta_ord = 1.0 - ord_pred
            err_cls = abs(cls_pred - gold)
            err_ord = abs(ord_pred - gold)
            by_omega[row["omega"]].append((delta_ord, delta_cls, err_ord, err_cls))

    summary = {}
    ord_better_delta = True
    ord_better_err = True
    for om in OMEGAS:
        vals = by_omega[om]
        n = len(vals)
        d_ord = sum(v[0] for v in vals) / n
        d_cls = sum(v[1] for v in vals) / n
        e_ord = sum(v[2] for v in vals) / n
        e_cls = sum(v[3] for v in vals) / n
        summary[om] = {
            "n": n,
            "delta_cum_ord": d_ord,
            "delta_cum_cls": d_cls,
            "err_sem_ord": e_ord,
            "err_sem_cls": e_cls,
        }
        ord_better_delta = ord_better_delta and (d_ord < d_cls)
        ord_better_err = ord_better_err and (e_ord < e_cls)

    return {
        "summary_by_omega": summary,
        "criteria_pass_delta": ord_better_delta,
        "criteria_pass_err": ord_better_err,
    }


def run_d03():
    path = INP / "D03.csv"
    by_omega = defaultdict(Counter)
    total = Counter()
    with path.open("r", encoding="utf-8", errors="ignore") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cls = row["class"]
            om = row["omega"]
            by_omega[om][cls] += 1
            total[cls] += 1

    summary = {}
    coexisting_all_contexts = True
    total_rows = sum(total.values())
    ambiguous_rate = (total.get("ambiguo", 0) / total_rows) if total_rows else 0.0
    for om in OMEGAS:
        c = by_omega[om]
        n = sum(c.values())
        if n == 0:
            summary[om] = {"n": 0, "preservativo": 0.0, "degenerativo": 0.0, "ambiguo": 0.0}
            coexisting_all_contexts = False
            continue
        p = c.get("preservativo", 0) / n
        d = c.get("degenerativo", 0) / n
        a = c.get("ambiguo", 0) / n
        summary[om] = {"n": n, "preservativo": p, "degenerativo": d, "ambiguo": a}
        if p <= 0.0 or d <= 0.0:
            coexisting_all_contexts = False

    return {
        "summary_by_omega": summary,
        "total_counts": dict(total),
        "ambiguous_rate": ambiguous_rate,
        "coexisting_regimes_all_contexts": coexisting_all_contexts,
    }


def main():
    results = {"A01": run_a01(), "D03": run_d03()}
    OUT.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
