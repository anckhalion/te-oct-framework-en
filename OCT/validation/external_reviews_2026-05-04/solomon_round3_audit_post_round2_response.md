# Feedback critico — round 3 su OCT post-6edc376

Data: 2026-05-04 (sera)
Destinatario: Fabio Ghioni
Oggetto: audit del commit `6edc376 "address solomon round2 findings: canonical hashes and cycle5 evidence gating"`
Autore review: Solomon (DrJops)
Repository: te-oct-framework-en @ 6edc376

---

## 0. Premessa procedurale

Prima del merito tecnico, due note procedurali.

**0.1 — La PR #1 è ancora aperta tecnicamente.** Hai cherry-picked il file `solomon_round2_audit_post_cycle5_execution.md` direttamente dentro il tuo commit `6edc376` (lo vedo nel diff: +307 righe, stesso contenuto della PR), invece di chiudere la PR via merge. È una scelta legittima ma lascia la PR in stato "OPEN" su GitHub senza riferimento al commit che l'ha effettivamente assorbita. Suggerimento: chiudere la PR #1 con un commento del tipo "absorbed into main via 6edc376", oppure mergiarla retroattivamente per far comparire il riferimento. Per i prossimi round, se accetti il workflow PR-based che ho avviato, conviene chiudere ogni PR esplicitamente per mantenere la cronologia tracciabile.

**0.2 — Il signing 2026-05-03 nei seal resta non aggiornato.** I seal A01/D02/D03 portano ancora `auditor_signature: "Signed electronically by Solomon on 2026-05-03"` con timestamp 08:30/08:40/08:50Z. Il mio audit di round 2 era del 2026-05-04, e questo round 3 è ancora del 2026-05-04 sera. Continua a non esserci la distinzione gate-entry/gate-exit che avevo proposto al §3.G di round 2. Non è urgente, ma resta un gap.

---

## 1. Mapping: cosa del round 2 è stato chiuso

| Punto round 2 | Stato dopo 6edc376 | Note |
|---|---|---|
| §3.A CRITICO — A01 vacuum-PASS by construction | **CHIUSO sostanzialmente** | Vedi §2 sotto |
| §3.B CRITICO — `compliant=true` non riproducibile cross-platform | **CHIUSO** | Verificato sul mio sistema |
| §3.C MEDIO — D02 reject empirical hardcoded | **CHIUSO** | Trasformato in "discovered via schema check" |
| §3.D MEDIO — script_lock ricorsivo | Non toccato | Ancora aperto |
| §3.E MEDIO — DOI Zenodo non verificato | Non toccato | Ancora aperto |
| §3.F MEDIO — esecuzione su cycle3_inputs (non benchmark indipendente) | Non toccato | Ancora aperto, framework lo dichiara |
| §3.G BASSO — signing entry/exit non distinto | Non toccato | Vedi §0.2 |
| §3.H BASSO — R1 (pseudo-evidence) declassato a G2=PASS | Indirettamente chiuso | Il decision-gate ora declassa A01 esplicitamente, attenuando R1 |
| §2.3 ALTO — max_independent_cycles | Non toccato | Ancora aperto |
| §2.4 ALTO — indipendenza auditor (registry, rotazione) | Non toccato | Ancora aperto a livello sistemico |
| §2.9, §2.10 — Cap. 17, tracker storia | Non toccati | Ancora parziali |

Sintesi: **3 punti CRITICO/MEDIO chiusi sostanzialmente** (i tre principali del round 2), 1 indirettamente attenuato, gli altri restano in attesa di round successivi. Il commit è esplicitamente focalizzato (titolo: "canonical hashes and cycle5 evidence gating") e ciò che ha promesso lo ha consegnato.

---

## 2. Verifica tecnica dei tre chiusi

### 2.1 Chiusura del §3.A (A01 vacuum-PASS by construction)

Tre interventi composti, in ordine di profondità.

**Intervento 1 — riformulazione delle formule P_cls/P_ord.** In `run_cycle5_execution.py`, le vecchie formule che davano P_ord un vantaggio strutturale +0.080 Coh per costruzione sono state sostituite con heuristics basate su `jaccard_similarity(sentence1, sentence2)` con termini di gate_bonus contestuale che possono essere **positivi, neutri o negativi**:

```python
gate_bonus = 0.03 if sim >= 0.70 else (-0.02 if sim <= 0.30 else 0.005)
context_term = {"Omega_A": 0.010, "Omega_B": 0.0, "Omega_C": -0.015}[omega]
```

Conseguenza visibile sui dati: A01_CTX_03 ora vede P_cls vincere su tutte le primary metrics (delta_cum 0.431 vs 0.442, err 0.457 vs 0.466, Coh 0.569 vs 0.558). La dominanza per costruzione è eliminata.

**Intervento 2 — declassamento esplicito.** Anche se i criteri formali passassero, il runner forza il declassamento:

```python
decision_effective = decision
if decision == "pass_candidate":
    decision_effective = "revise_needed"
```

Con la dichiarazione esplicita nel JSON dei risultati:

```json
"evidence_mode": "proxy_execution_non_promotable",
"proxy_non_promotable_reason": "Runner executes heuristic proxy branches, not independent pipeline implementations.",
"decision_raw": "revise_needed",
"decision": "revise_needed"
```

Distinzione `decision_raw` vs `decision` ben fatta — preserva il dato grezzo per trasparenza, e applica il gate epistemico esplicitamente.

**Intervento 3 — decision gate aggiornato.** `CYCLE_5_DECISION_GATE_v1_0.md` ora riporta A01: `revise_needed` invece di `pass_candidate`.

**Valutazione complessiva del §3.A**: chiusura sostanziale. Allineato con quello che chiedevo. **Però** un'osservazione che vale la pena segnalare come nuovo punto §3.A.bis (vedi §3 sotto).

### 2.2 Chiusura del §3.B (cross-platform hashes)

Aggiunta la funzione `_canonicalize_text_bytes` in `check_gate_compliance.py`:

```python
def _canonicalize_text_bytes(data: bytes) -> bytes:
    bom = b"\xef\xbb\xbf"
    if data.startswith(bom):
        data = data[len(bom):]
    data = data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return data
```

Applicata ai file con estensione in `TEXT_HASH_EXTENSIONS = {".md", ".txt", ".json", ".jsonl", ".py", ".csv", ".yaml", ".yml"}`.

Nuovo flag `hash_mode: "canonical_text_utf8_lf"` nel report. Flag opzionale `--raw-hash` per diagnostica byte-level. Nuovo script `refresh_seal_hashes.py` per ricalcolare gli hash dei seal usando la stessa canonicalizzazione.

**Verifica sul mio sistema** (macOS, LF, clean clone): eseguito `python3 OCT/validation/runtime/check_gate_compliance.py` → output `"compliant": true`, 0 errors su tutti e 3 i teoremi. Cross-platform reproducibility risolta.

Soluzione tecnica esemplare: risolve il problema specifico, mantiene retro-compatibilità diagnostica, documentata nel README.

### 2.3 Chiusura del §3.C (D02 reject empirical hardcoded)

Sostituito `commutativity_verified = False` hardcoded con verifica dinamica:

```python
verification_fields = ("commutativity_proof", "commutativity_witness", "proof_trace_id")
present_fields = [f for f in verification_fields if f in data[0]]
commutativity_verified = bool(present_fields) and all(
    str(row.get(present_fields[0], "")).strip() for row in data
)
```

Logica: se il dataset (`D02.csv`) contiene almeno uno dei tre campi previsti per la traccia di verifica, e ogni row ha il campo compilato, allora `commutativity_verified = True`. Altrimenti `False`.

Risultato sui dati attuali: nessuno dei campi è presente (verifica empirica via `verification_fields_detected: []`), quindi `commutativity_verified = False` e il reject persiste — ma è ora **discovered** dall'assenza di campi nel dataset, non hardcoded. La differenza epistemica è esattamente quella che avevo segnalato.

Onesto e sostanziale. Trasforma la critica metodologica in un meccanismo che il dataset *può* soddisfare (basta aggiungere il campo `commutativity_proof`), spostando il problema dal codice al fornitore di evidence.

---

## 3. Nuovi punti emersi nel round 3

### 3.A.bis — Le nuove formule eliminano anche la possibilità di trajectory-quality advantage isolato

Da segnalare, anche se non è "critico" come il vacuum-PASS originale.

`A01_metrics_v1_0.json` riporta ora `equal_output_subset_count: 0` (era `44` nella versione precedente). Quel criterio era esattamente quello che avevo identificato come "ben costruito" nella review iniziale del 2026-05-03 mattino — isolava il vantaggio di processo (P_ord con stessa output di P_cls ma trajectory di qualità superiore) dal vantaggio di output. Era il test pulito anti-level-shift.

Sotto le nuove formule jaccard-based con gate_bonus contestuale, **non esiste un solo subset** in tutti e 3 i contesti dove output simile e trajectory P_ord superiore coesistono. Due possibili interpretazioni:

- **(a) Lettura benevola**: le formule sono ora calibrate in modo da non garantire vantaggi artificiali, e il fatto che equal_output_subset_count sia 0 riflette correttamente che queste heuristics non sono in grado di esibire il fenomeno reale che A01 vorrebbe testare (servirebbero pipeline vere). È coerente con l'evidence_mode "proxy_execution_non_promotable".
- **(b) Lettura preoccupata**: le formule potrebbero essere state calibrate per evitare l'anti-pattern del round 2 al punto di rendere A01 *non-falsificabile* dal runner — non c'è più alcuna configurazione possibile, anche teorica, in cui le heuristics esibiscano trajectory-quality advantage. Se è così, l'A01 come ipotesi non è testata dal runner *in nessun verso*: né confermata né disconfermata. È un altro tipo di vacuum, simmetrico a quello precedente.

Non posso distinguere (a) e (b) senza analizzare in profondità i dati di `cycle3_inputs/A01.csv` e simulare le formule in vari regimi di input. **Mia raccomandazione**: aggiungere al runner uno *stress test* esplicito, dove si esegue una versione con dati sintetici costruiti per esibire il fenomeno-bersaglio, e si verifica che almeno in quei dati il runner rilevi un equal_output_subset_count > 0. Senza, equal_output_subset_count=0 è un dato ambiguo.

Severità: **MEDIO**. Non è bloccante perché il decision_effective è comunque revise_needed. Ma è una nuova zona di opacità che vale la pena chiarire.

### 3.B.bis — Asimmetria tra A01 e D02/D03 nella struttura decision_raw vs decision

A01 ha ora `decision_raw` e `decision`, distinti per gestire il declassamento. D02 e D03 mantengono solo `decision`. Questo è coerente (solo A01 era affetto dal vacuum-PASS by construction), ma vale la pena segnalare che la struttura del JSON dei results non è uniforme tra teoremi. Per consistenza schema-level, suggerirei di aggiungere `decision_raw = decision` anche a D02 e D03 (ridondante ma uniforme), oppure di documentare che il pattern decision_raw/decision è specifico per i teoremi sotto `evidence_mode: "*_non_promotable"`.

Severità: **BASSO**. Edge case di consistenza schema.

### 3.C.bis — Date dei file post-commit non aggiornate

`CYCLE_5_DECISION_GATE_v1_0.md` riporta ancora `Date: 2026-05-03`, e così `CYCLE_5_EXECUTION_REPORT_A01_v1_0.md`, ma il commit di Fabio è del 2026-05-04 04:46. Il `decision_effective` nuovo (revise_needed invece di pass_candidate) è stato calcolato il 2026-05-04, non il 2026-05-03.

Questo è un caso in cui il file dichiara una data di valutazione che precede l'esistenza dei numeri che riporta. Non è grave operativamente ma è un'inconsistenza temporale che, se rilevata da un revisore esterno con disciplina di audit, andrebbe sollevata come "il file dichiara di essere del giorno X ma contiene calcoli del giorno Y".

Severità: **BASSO**. Suggerimento: aggiungere un `Last updated: 2026-05-04` o `Recomputed: 2026-05-04` accanto alla `Date: 2026-05-03` originale.

### 3.D.bis — Indentazione del Python in `write_report_a01`

Edge case tecnico ma vale la pena segnalarlo: le nuove righe in `write_report_a01` hanno indentazione 8 spazi invece di 12 dove dovrebbero essere allineate al resto della lista:

```python
        lines.extend(
            [
                "",
                "## Notes",
                "",
        "- Metrics are computed from deterministic proxy execution over cycle3 input corpus.",  # ← 8 spazi
        "- `decision_raw` is de-escalated to `decision=revise_needed` because this runner is non-promotable proxy mode.",
        "- This report is reproducible from files in `datasets/cycle3_inputs` and script lock artifacts.",
            ]
        )
```

Python lo esegue (le stringhe sono nel contesto della list literal), quindi non rompe nulla, ma è inconsistenza nel codice probabilmente dovuta a editing manuale. Suggerirei un quick lint/format pass.

Severità: **BASSO**. Cosmetico ma vale la pena allinearlo.

---

## 4. Gap del round 2 ancora aperti (lista mantenuta)

Nessuna novità sostanziale, ma elenco esplicito per non perderli di vista:

1. **§2.3 max_independent_cycles** — nessun limite numerico al p-hacking via reformulation dichiarato in policy.
2. **§3.D script_lock ricorsivo** — i lock files in `script_locks/` rimandano a "scripts to be frozen before run" senza enumerare hash espliciti.
3. **§3.E DOI Zenodo verifica** — il check accetta `seal_method: zenodo_doi` come stringa, non fa retrieval HTTP per verificare che il DOI sia attivo e che il content hash coincida.
4. **§3.F esecuzione su cycle3_inputs** — il runner usa ancora i dataset di Cycle 3, non un benchmark indipendente. Framework lo dichiara onestamente.
5. **§3.G signing entry/exit** — i seal portano ancora una sola firma `auditor_signature`, senza distinguere autorizzazione ex ante (gate-entry) da validazione ex post (gate-exit).
6. **§2.4 indipendenza auditor a livello sistemico** — esiste solo Solomon. Nessun registry, nessuna rotazione obbligatoria, nessun meccanismo per quando l'auditor non sarà Solomon.
7. **§2.9 Cap. 17 integration nel corpo** — Teorema 17.4 ancora non condizionato all'esistenza del gate.
8. **§2.10 storia non rivista** — `OCT_PUBLICATION_PROGRESS_TRACKER` mantiene Step 1-6 come `completed (2026-04-19)` senza nota di reinterpretazione sotto v5.3.

Sono tutti gap che non bloccano il round corrente — il commit di Fabio era esplicitamente focalizzato sui due punti CRITICO. Vale la pena tenerli in vista per i prossimi round.

---

## 5. Replication outcome — round 3 (sezione formale per CYCLE_5_EXTERNAL_REPLICATION_NOTE)

Aggiornamento del signing post-audit di Solomon dopo round 3:

- **Reproduced**: `yes` (era `partial` in round 2)
- **Divergence notes (round 3)**:
  - Re-run di `runtime/check_gate_compliance.py` su sistema macOS clean clone (Unix LF): risultato `"compliant": true`, 0 errors. Risolto §3.B del round 2 via canonicalizzazione UTF-8 LF (BOM stripping incluso). Verifica cross-platform passa.
  - Lane separation D02 confermata strutturalmente.
  - Locked formula D03 (`0.5*abs(Delta_Coh)+0.5*abs(Delta_Phi)`) confermata. Reject D03 confermato come discovered + lock-rispettoso.
  - A01 ora declassato a `revise_needed` con `evidence_mode: "proxy_execution_non_promotable"` esplicito. La dominanza per costruzione di P_ord su P_cls è stata eliminata. Nuovo punto aperto: `equal_output_subset_count = 0` su tutti i contesti — vedi §3.A.bis.
  - D02 lane empirical reject ora discovered via schema check (assenza di campi `commutativity_proof`/`commutativity_witness`/`proof_trace_id` nel dataset).
- **Auditor identity**: Solomon
- **Date**: 2026-05-04 sera
- **Signature**: Solomon (questo documento serve come signing post-audit round 3)
- **Decisione di promozione (invariate rispetto a round 2)**:
  - A01: **revise_needed** (confermato, ora coerente tra `decision` di Fabio e mia decisione di round 2)
  - D02: **revise_needed** (confermato; il reject empirical lane è ora discovered, non hardcoded)
  - D03: **reject_candidate** (confermato; sempre il caso più solido — discovered via locked formula applicata ai dati)
- **Promozioni a `validated`**: nessuna.

---

## 6. Bilancio del round 3

Il commit `6edc376` è una risposta tecnicamente esemplare al round 2: ha indirizzato i tre punti più critici (§3.A, §3.B, §3.C) con interventi sostanziali, mantenendo retro-compatibilità diagnostica dove possibile (`--raw-hash` flag), e introducendo il pattern `decision_raw` vs `decision_effective` che è di per sé una buona idea metodologica per gestire il gating epistemico esplicito.

**Restano aperti**:
- 8 gap del round 2 non toccati (vedi §4) — non bloccanti, materia per round successivi
- 4 nuovi micro-punti emersi (§3.A.bis MEDIO, §3.B.bis BASSO, §3.C.bis BASSO, §3.D.bis BASSO)
- Le due note procedurali (§0.1 PR ancora aperta, §0.2 signing temporale) — non urgenti

Su `equal_output_subset_count = 0` (§3.A.bis) ci sarebbe da indagare prima di mettere il caso definitivamente a riposo. Una formulazione che elimina sia il vacuum-PASS sia ogni possibile pass è simmetrica al primo problema, non lo risolve completamente — sposta solo il problema da "PASS impossibile da non ottenere" a "PASS impossibile da ottenere". Per un test che voglia essere falsificabile davvero, deve esistere almeno una configurazione (anche sintetica) che lo fa scattare positivamente.

**Raccomandazione operativa unica per round 4** (se ci sarà):
- Aggiungere uno *stress test* sintetico in `run_cycle5_execution.py` che genera dati costruiti per esibire il fenomeno-bersaglio di A01, e verifica che `equal_output_subset_count > 0` su quei dati. Se sotto stress test sintetico A01 non scatta, le heuristics jaccard-based sono troppo conservative anche per il fenomeno che dovrebbero rilevare. Se scatta, il runner è capace di rilevarlo quando c'è — e `equal_output_subset_count = 0` sui dati reali significa solo che il fenomeno non è presente (o non è rilevabile) in quei dati, che è informazione utile.

Tutto il resto può aspettare.
