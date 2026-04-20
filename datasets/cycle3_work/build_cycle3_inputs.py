import csv
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
WORK = ROOT / "datasets" / "cycle3_work"
OUT = ROOT / "datasets" / "cycle3_inputs"
OUT.mkdir(parents=True, exist_ok=True)

OMEGAS = ["Omega_A", "Omega_B", "Omega_C"]


def read_edge_list(path: Path):
    edges = []
    with path.open("r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split()
            if len(parts) < 2:
                continue
            try:
                u = int(parts[0])
                v = int(parts[1])
            except ValueError:
                continue
            if u == v:
                continue
            if u > v:
                u, v = v, u
            edges.append((u, v))
    return edges


def build_d02():
    src1 = WORK / "D02" / "ca-GrQc.txt"
    src2 = WORK / "D02" / "email-Eu-core.txt"
    edges_1 = read_edge_list(src1)
    edges_2 = read_edge_list(src2)

    chunk_size = 180
    stride = 120
    base_samples = []

    def sample_from(edges, source_label, target_n):
        idx = 0
        while len([x for x in base_samples if x["source"] == source_label]) < target_n:
            start = idx * stride
            end = start + chunk_size
            if end > len(edges):
                break
            chunk = edges[start:end]
            nodes = set()
            for u, v in chunk:
                nodes.add(u)
                nodes.add(v)
            n_nodes = len(nodes)
            m_edges = len(chunk)
            if n_nodes < 2:
                idx += 1
                continue
            density = m_edges / (n_nodes * (n_nodes - 1) / 2)
            # Proxy phi from structural productivity: sparse chunks can be commutative but non-productive.
            base_phi = max(0.0, density * 8.0 - 0.06)
            base_phi = round(min(base_phi, 1.0), 6)
            base_samples.append(
                {
                    "base_id": f"{source_label}_{idx:03d}",
                    "source": source_label,
                    "n_nodes": n_nodes,
                    "m_edges": m_edges,
                    "density": density,
                    "base_phi": base_phi,
                    "is_commutative": 1,
                }
            )
            idx += 1

    sample_from(edges_1, "ca-GrQc", 30)
    sample_from(edges_2, "email-Eu-core", 30)

    if len(base_samples) < 60:
        raise RuntimeError(f"Insufficient base samples for D02: {len(base_samples)}")

    context_factor = {"Omega_A": 1.00, "Omega_B": 0.92, "Omega_C": 0.85}
    rows = []
    for sample in base_samples[:60]:
        for omega in OMEGAS:
            phi = sample["base_phi"] * context_factor[omega]
            if phi < 0.02:
                phi = 0.0
            phi = round(phi, 6)
            rows.append(
                {
                    "diagram_id": f"{sample['base_id']}_{omega}",
                    "base_id": sample["base_id"],
                    "source": sample["source"],
                    "omega": omega,
                    "is_commutative": sample["is_commutative"],
                    "n_nodes": sample["n_nodes"],
                    "m_edges": sample["m_edges"],
                    "density": round(sample["density"], 6),
                    "phi": phi,
                }
            )

    out_path = OUT / "D02.csv"
    with out_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(
            f,
            fieldnames=[
                "diagram_id",
                "base_id",
                "source",
                "omega",
                "is_commutative",
                "n_nodes",
                "m_edges",
                "density",
                "phi",
            ],
        )
        w.writeheader()
        w.writerows(rows)
    return rows


def iter_stsb_rows(tsv_path, split_name):
    with tsv_path.open("r", encoding="utf-8", errors="ignore") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            s1 = (row.get("sentence1") or "").strip()
            s2 = (row.get("sentence2") or "").strip()
            score_raw = row.get("score")
            if not s1 or not s2 or not score_raw:
                continue
            try:
                score = float(score_raw)
            except ValueError:
                continue
            yield {
                "split": split_name,
                "source1": row.get("source1", "none"),
                "source2": row.get("source2", "none"),
                "sentence1": s1,
                "sentence2": s2,
                "score": score,
            }


def build_a01():
    base = WORK / "A01" / "STS-B" / "STS-B"
    pools = []
    pools.extend(iter_stsb_rows(base / "test.tsv", "test"))
    pools.extend(iter_stsb_rows(base / "dev.tsv", "dev"))
    pools.extend(iter_stsb_rows(base / "train.tsv", "train"))
    rows = []
    for i, r in enumerate(pools[:320]):
        omega = OMEGAS[i % 3]
        rows.append(
            {
                "task_id": f"A01_{i+1:04d}",
                "split": r["split"],
                "omega": omega,
                "source1": r["source1"],
                "source2": r["source2"],
                "sentence1": r["sentence1"],
                "sentence2": r["sentence2"],
                "gold_score": round(r["score"], 3),
                "gold_score_norm": round(r["score"] / 5.0, 6),
            }
        )
    out_path = OUT / "A01.csv"
    with out_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(
            f,
            fieldnames=[
                "task_id",
                "split",
                "omega",
                "source1",
                "source2",
                "sentence1",
                "sentence2",
                "gold_score",
                "gold_score_norm",
            ],
        )
        w.writeheader()
        w.writerows(rows)
    return rows


def parse_conllu_sentences(path: Path):
    sent_tokens = []
    sent_id = None
    text = None
    with path.open("r", encoding="utf-8", errors="ignore") as f:
        for raw in f:
            line = raw.rstrip("\n")
            if line.startswith("# sent_id ="):
                sent_id = line.split("=", 1)[1].strip()
            elif line.startswith("# text ="):
                text = line.split("=", 1)[1].strip()
            elif not line.strip():
                if sent_tokens:
                    yield sent_id or "unknown", text or "", sent_tokens
                sent_tokens = []
                sent_id = None
                text = None
            elif line.startswith("#"):
                continue
            else:
                cols = line.split("\t")
                if len(cols) < 8:
                    continue
                tok_id = cols[0]
                if "-" in tok_id or "." in tok_id:
                    continue
                sent_tokens.append(
                    {
                        "id": tok_id,
                        "form": cols[1],
                        "upos": cols[3],
                        "head": cols[6],
                        "deprel": cols[7],
                    }
                )
    if sent_tokens:
        yield sent_id or "unknown", text or "", sent_tokens


def build_d03():
    conllu = WORK / "D03" / "UD_English-EWT-r2.17" / "en_ewt-ud-train.conllu"
    rows = []
    content_tags = {"NOUN", "VERB", "ADJ", "ADV", "PROPN"}
    punct_tag = {"PUNCT"}
    for i, (sent_id, text, toks) in enumerate(parse_conllu_sentences(conllu)):
        if len(rows) >= 260:
            break
        tok_count = len(toks)
        if tok_count == 0:
            continue
        content_count = sum(1 for t in toks if t["upos"] in content_tags)
        punct_count = sum(1 for t in toks if t["upos"] in punct_tag)
        dep_edges = sum(1 for t in toks if t["head"] not in {"0", "_"})

        phi_pre = 0.7 * (content_count / tok_count) + 0.3 * min(1.0, dep_edges / 25.0)
        punct_ratio = punct_count / tok_count
        loss_u = min(0.9, max(0.05, 0.18 + 0.35 * punct_ratio + 0.15 * (1 - (content_count / tok_count))))
        phi_post = max(0.0, phi_pre - loss_u)
        drop = phi_pre - phi_post
        if drop < 0.12:
            cls = "preservativo"
        elif drop > 0.28:
            cls = "degenerativo"
        else:
            cls = "ambiguo"

        omega = OMEGAS[i % 3]
        rows.append(
            {
                "pair_id": f"D03_{i+1:04d}",
                "omega": omega,
                "sentence_id": sent_id,
                "text": text,
                "tok_count": tok_count,
                "content_tok_count": content_count,
                "phi_pre": round(phi_pre, 6),
                "phi_post": round(phi_post, 6),
                "loss_u": round(loss_u, 6),
                "class": cls,
            }
        )

    out_path = OUT / "D03.csv"
    with out_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(
            f,
            fieldnames=[
                "pair_id",
                "omega",
                "sentence_id",
                "text",
                "tok_count",
                "content_tok_count",
                "phi_pre",
                "phi_post",
                "loss_u",
                "class",
            ],
        )
        w.writeheader()
        w.writerows(rows)
    return rows


def compute_d02_metrics(rows):
    by_omega = {o: [] for o in OMEGAS}
    by_base = {}
    for r in rows:
        by_omega[r["omega"]].append(r)
        by_base.setdefault(r["base_id"], {})[r["omega"]] = r["phi"]

    summary = {}
    for o, vals in by_omega.items():
        n = len(vals)
        zero_n = sum(1 for v in vals if float(v["phi"]) == 0.0)
        pos_n = n - zero_n
        summary[o] = {
            "n": n,
            "phi_zero_quota": zero_n / n if n else 0.0,
            "phi_positive_quota": pos_n / n if n else 0.0,
        }

    all_zero = 0
    for _base, omap in by_base.items():
        if all(float(omap.get(o, 0.0)) == 0.0 for o in OMEGAS):
            all_zero += 1
    inter_all_zero = all_zero / len(by_base) if by_base else 0.0

    quotas = [summary[o]["phi_zero_quota"] for o in OMEGAS]
    mean = sum(quotas) / len(quotas)
    var = sum((q - mean) ** 2 for q in quotas) / len(quotas)
    return summary, inter_all_zero, var


def write_metadata():
    meta = {
        "dataset_version": "cycle3_real_mix_v1",
        "seeds": [101, 202, 303],
        "pipeline_version_cls": "cls_proxy_v1",
        "pipeline_version_ord": "ord_proxy_v1",
        "omega_contexts": OMEGAS,
    }
    (OUT / "metadata.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")


def main():
    d02_rows = build_d02()
    a01_rows = build_a01()
    d03_rows = build_d03()
    write_metadata()
    d02_summary, d02_intersection, d02_var = compute_d02_metrics(d02_rows)

    run = {
        "D02": {
            "rows": len(d02_rows),
            "summary_by_omega": d02_summary,
            "intersection_phi_zero_all_omegas": d02_intersection,
            "var_phi_zero_quota": d02_var,
        },
        "A01": {"rows": len(a01_rows)},
        "D03": {"rows": len(d03_rows)},
    }
    (OUT / "run_summary.json").write_text(json.dumps(run, indent=2), encoding="utf-8")
    print(json.dumps(run, indent=2))


if __name__ == "__main__":
    main()
