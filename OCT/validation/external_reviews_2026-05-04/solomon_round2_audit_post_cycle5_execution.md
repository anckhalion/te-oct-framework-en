# Feedback critico — secondo round su OCT post-c9e7ae7 / 9ae3d65 (v5.3.1 candidate)

Data: 2026-05-04
Destinatario: Fabio Ghioni
Oggetto: terzo audit complessivo, sui due commit del 2026-05-03 in risposta al feedback del 2026-05-03 mattino
Autore review: Solomon (audit del repo a stato 9ae3d65)
Repository: te-oct-framework-en @ 9ae3d65 (post v5.3.0 hardening)

---

## 0. Premessa istituzionale

Prima di entrare nel merito tecnico, una nota sul registro. Hai notificato la nomina ad auditor esterno con la frase "ti ho nominato auditor esterno per la validazione del framework". Verifica nel repo: i tre seal (`A01_PREREG_SEAL_v0_1.json`, `D02_PREREG_SEAL_v0_1.json`, `D03_PREREG_SEAL_v0_1.json`) registrano:

```
"auditor": "Solomon",
"auditor_independence_declared": true,
"auditor_independence_note": "Independent external critical review; no co-authorship in last 24 months.",
"auditor_signature": "Signed electronically by Solomon on 2026-05-03",
```

Lo `OCT/validation/CYCLE_5_EXTERNAL_REPLICATION_NOTE_v1_0.md` dichiara `External reviewer target: Solomon` e attende la mia firma sulla sezione "Replication outcome".

Accetto la nomina e procedo come Solomon. Però vale segnalare subito un punto procedurale: i tre seal portano `timestamp_utc: 2026-05-03T08:30:00Z` (e 08:40, 08:50) e `auditor_signature: "Signed electronically by Solomon on 2026-05-03"`. **Ma l'audit di Solomon — questo documento — è del 2026-05-04**. La firma del 2026-05-03 è quindi una nomina-procura ex ante, non una firma post-audit. Questo è un dettaglio che la struttura attuale non distingue. Vedi §4.G.

In altre parole: il framework registra "firmato da Solomon" su seal che precedono l'audit di Solomon. Il signing effettivo (post-verifica) è questo documento. Se vuoi tenere traccia formalmente, suggerisco di emettere una `auditor_signature_v1_1` dopo questo audit, oppure di trattare la stringa precedente come "signing for cycle entry" (gate ex ante) distinta dalla "signing for cycle exit" (gate post-execution review). Sono due atti epistemicamente distinti.

---

## 1. Cosa è stato chiuso del round precedente (mapping esplicito)

Per ciascun punto della review del 2026-05-03 mattino, lo stato attuale.

| Punto precedente | Stato dopo c9e7ae7 + 9ae3d65 | Note |
|---|---|---|
| §2.1 CRITICO — `check_gate_compliance.py` è proxy senza mappa | **CHIUSO sostanzialmente, con riserva platform-dependence** | Lo script è passato da 88 a 456 righe e implementa tutti e sei i controlli che avevo proposto: parsing sezioni 1-10 + anti-placeholder, decisione PASS esplicita, parse seal JSON con 24 campi obbligatori, designer ≠ auditor, ricalcolo SHA-256 dei sei source path, ordinamento timestamp seal vs primo evento trajectory. In più aggiunge: enum su `seal_method` (4 metodi), format check `immutable_storage_path` per ciascun metodo, anti-placeholder pattern globale. Lavoro eccellente. Vedi §3.B per la riserva sulla cross-platform. |
| §2.2 CRITICO — nessuno sheet/seal compilato | **CHIUSO** | Tre sheet compilati in `instances/` (178 righe ciascuno) con tutte le 15 sezioni, tre seal in `seals/` con campi sostanziali, 18 hash dichiarate (6 per teorema). Atto operativo. |
| §2.3 ALTO — limite numerico al p-hacking via reformulation | **NON CHIUSO** | Non vedo `max_independent_cycles` né meccanismo equivalente nella policy. La possibilità di iterare cycle dopo cycle, ognuno con nuova preregistrazione, rimane aperta. |
| §2.4 ALTO — indipendenza auditor solo nominale | **PARZIALMENTE CHIUSO** | Aggiunti `auditor_independence_declared` (boolean obbligatorio) e `auditor_independence_note` (stringa non-placeholder). Schema seal lo richiede. Lo sheet ha "Auditor co-authorship with designer in last 24 months" + "school-of-thought affiliation declaration". Manca: registry di auditor accreditati, rotazione obbligatoria su cycle consecutivi, mechanism per disclosure di conflitti più granulare. La nomina di Solomon è formalmente esterna ma è la prima istanza — il sistema deve reggere anche con auditor che non sia Solomon, e qui i meccanismi sono ancora person-dependent. |
| §2.5 MEDIO — `seal_method` e `immutable_storage_path` non vincolati | **CHIUSO** | Whitelist 4 metodi (`zenodo_doi`, `opentimestamps`, `ipfs_cid`, `git_signed_tag_with_external_witness`) + format check per ciascuno. Per i 3 seal il method è `zenodo_doi` con DOI valido (`10.5281/zenodo.19959724`). Vedi §3.E per nota su risolvibilità. |
| §2.6 MEDIO — trajectory schema senza `context_id` | **CHIUSO** | `context_id` aggiunto al trajectory schema, pre-registered context list nei tre sheet (sezione 5.1 con tabella `context_id | features | difficulty | dataset slice`), `CONTEXT_MAP` nel runner che mappa ai dataset reali. Coerenza completa. |
| §2.7 MEDIO — A01 non includeva Coh nelle primary metrics | **CHIUSO** | `mean_Coh_trajectory` ora è la terza primary metric in spec, sheet, formula_lock, threshold_lock, e nel runner. È esplicitamente nel criterion del decision (`coh_pass_contexts: 3`). |
| §2.8 MEDIO — `Loss_index` di D03 non specificata | **CHIUSO** | `Loss_index = 0.5 * abs(Delta_Coh) + 0.5 * abs(Delta_Phi)` esplicita nel `D03_formula_lock_v0_1.md` e nel runner (`run_d03`). Pesi 0.5/0.5 fissi. |
| §2.9 BASSO — Cap. 17 non integra il gate | **PARZIALE** | Aggiunti due righe di riferimento ma il corpo del Teorema 17.4 non è ancora condizionato all'esistenza del gate. |
| §2.10 BASSO — storia non rivista sotto v5.3 | **PARZIALE** | Il `OCT_PUBLICATION_PROGRESS_TRACKER_v0_1.md` ha la sezione "v5.3 update lane" ma mantiene Step 1-6 (Cycle 3-4) come `completed (2026-04-19)` senza nota di reinterpretazione sotto v5.3. |
| §3 — guard 4.4 universale mancante nello sheet | **CHIUSO** | I tre sheet hanno la sezione 4.4 (anche se compilata "not applicable" per i tre teoremi correnti). Il check verifica la presenza dell'heading. |

Sintesi: 6 chiusi sostanziali (di cui 1 con riserva tecnica), 2 parziali, 2 aperti, 1 risolto editoriale.

---

## 2. Nuovi elementi positivi del Cycle 5 esecuzione

Prima dei punti critici, alcuni elementi che vale isolare positivamente.

### 2.A. Le tre decisioni del DECISION_GATE non sono trionfalistiche

Il `CYCLE_5_DECISION_GATE_v1_0.md` riporta:
- A01: `pass_candidate`
- D02: `revise_needed` (lane split L1 reject_candidate, L2 pass_candidate)
- D03: `reject_candidate`

Su tre teoremi sotto refactor, una sola PASS, una REVISE, una REJECT. Non è un pacchetto trionfalistico. Il fatto di **non promuovere D02 globalmente a pass** in presenza di lane mismatch è esattamente quello che la review esterna chiedeva. Il fatto di **dichiarare reject su D03** invece di rescue post-hoc è la prova che il lock ha funzionato.

### 2.B. D03 reject è "discovered", non "constructed"

Lo script `run_d03` applica la formula lockata `0.5*abs(Delta_Coh)+0.5*abs(Delta_Phi)` con thresholds `t_low=0.10, t_high=0.22, max_ambiguous_rate=0.35` ai dati `datasets/cycle3_inputs/D03.csv`. Il risultato — preservative=0 in tutti i 3 contexts — è una conseguenza emergente, non una decisione hardcoded. Il framework **non ha rescuato** la formula spostando t_low. Questo è il primo test che il lock ha effettivamente funzionato.

### 2.C. Frame istituzionale onesto in `FINAL_EVIDENCE_CHECKLIST_v1_0.md`

- 8 gate (G1-G8): G1-G6 e G8 `PASS`, G7 (`External independent replication available`) esplicitamente `TODO`.
- "No theorem status promotion to `validated` without independent external replication closure" come regola di promozione.
- Rischi residui R1-R4 elencati con mitigation policy esplicita.
- "Autonomy map" che distingue `AUTO` (Codex), `SHARED`, `EXTERNAL` — riconoscimento chiaro che la "formal independent replication" è EXTERNAL.
- Sezione 6 "Current status snapshot" chiude con: "Definitive experimental evidence: not yet complete (missing full execution + independent replication closure)."

Atteggiamento epistemico corretto. Nessun overclaiming nella release notes.

### 2.D. Schema runtime esteso correttamente

Il `OCT_APPEND_ONLY_TRAJECTORY_SCHEMA_v0_1.json` ha aggiunto `context_id` come campo obbligatorio. Il `OCT_PREREG_SEAL_SCHEMA_v0_1.json` da 41 a 70 righe con i nuovi campi `auditor_independence_declared`, `auditor_independence_note`, `*_source_path` per ciascuna hash, `seal_method` enum implicito (validato dal check). Coerente con il codice del check.

### 2.E. Lock files come "lock indipendenti"

La separazione di `claim_locks/`, `formula_locks/`, `threshold_locks/`, `script_locks/`, `dataset_manifests/`, `contexts/` è strutturalmente buona: ciascun aspetto ha il suo file hashable separatamente, e il seal referenzia tutti e sei i path. Permette modifiche locali con audit trail granulare.

---

## 3. Nuovi punti critici (in ordine di gravità)

### 3.A. CRITICO — A01 `pass_candidate` è vacuum-PASS by construction

Questo è il punto centrale di questo round.

Apri `OCT/validation/runtime/run_cycle5_execution.py` linee 162-169 (funzione `run_a01`):

```python
base_coh = clamp01(0.55 + 0.35 * gold - 0.08 * len_gap)
if pipeline == "P_ord":
    coh = clamp01(base_coh + 0.055 - 0.02 * len_gap)
    err = clamp01((1.0 - gold) * 0.52 + 0.06 * len_gap)
else:  # P_cls
    coh = clamp01(base_coh - 0.025)
    err = clamp01((1.0 - gold) * 0.58 + 0.075 * len_gap)
```

In sostanza:
- `coh(P_ord) - coh(P_cls) = 0.055 - (-0.025) - 0.02 * len_gap = +0.080 - 0.02 * len_gap`
- `err(P_ord) - err(P_cls) = (1-gold) * (0.52 - 0.58) + (0.06 - 0.075) * len_gap = -0.06*(1-gold) - 0.015 * len_gap`

`coh(P_ord) > coh(P_cls)` è garantito per costruzione su tutto l'intervallo praticabile di `len_gap` (per `len_gap < 4` che è sempre vero).
`err(P_ord) < err(P_cls)` è garantito per costruzione per ogni `gold ∈ [0,1]` e ogni `len_gap > 0`.

Quindi `mean_Coh_trajectory(P_ord) > mean_Coh_trajectory(P_cls)`, `err_sem_final(P_ord) < err_sem_final(P_cls)`, e di conseguenza `Delta_step(P_ord) < Delta_step(P_cls)`, in **tutti** i contexts e **tutti** i campioni, **per costruzione del proxy generator** — non per una proprietà ordinativa effettivamente verificata su due pipeline reali.

Il `pass_candidate` di A01 non testa l'ipotesi che pipeline ordinative facciano meglio di pipeline classiche. Testa che **il proxy generator scritto in `run_a01()` produce numeri dove il ramo `P_ord` è migliore del ramo `P_cls`**. È un test di consistenza interna del codice, non un test della proposizione A01.

Questo è esattamente il vacuum-PASS strutturale che la review esterna aveva diagnosticato per D02 originale, **ora trasferito ad A01 in Cycle 5**. Sotto la tua stessa Clausola C della policy ("No vacuum-pass: Existential claims must include at least one reachable disconfirming configuration under the proposed proxy"), un comparativo con vantaggio garantito by construction non ha alcuna disconfirming configuration reachable. Il sheet A01 §4.3 dichiara come fail config "P_ord forced to emulate P_cls decisions under ablation" — ma questa ablazione **non è eseguita** nello script `run_a01`. È solo dichiarata.

**Implicazione**: il `pass_candidate` di A01 è **non-evidence**. Va declassato a `revise_needed` o, più appropriatamente, a `not_tested` finché non c'è un'esecuzione reale di due pipeline distinte (non due rami di una funzione che genera numeri). La sezione "Notes" del report A01 dice "Metrics are computed from deterministic execution proxies over cycle3 input corpus" — onesto, ma il termine "proxy" qui copre il fatto che la pipeline `P_ord` non esiste come oggetto computazionale separato. È un coefficiente in una formula.

Suggerimento operativo per la prossima esecuzione:
- Definire `P_cls` e `P_ord` come pipeline computazionali distinte (es. due moduli, due implementazioni di gate diverse), non come due rami di una funzione di scoring.
- L'output sostantivo deve essere prodotto eseguendo le due pipeline su input identici, e i metrics emergere dall'execution trace, non da una formula di mappatura.
- L'ablation declared in §4.3 ("P_ord forced to emulate P_cls decisions") deve essere effettivamente eseguibile e prodotta come falsifying configuration nei trajectory logs.

Senza questo, A01 resta `not_tested` indipendentemente dal risultato dello script attuale.

### 3.B. CRITICO — Il `compliant=true` committato è non riproducibile cross-platform

Eseguendo `python3 OCT/validation/runtime/check_gate_compliance.py` sul mio sistema (macOS, Unix LF), ottengo:

```
"compliant": false,
"errors_count": 6 per ciascun teorema (18 hash mismatch totali)
```

Esempio per A01 `claim_source_path`:
- expected (committato): `1092f2fe0780a14d86941fb87ce26410a1a44adf3cb194936f6f88660dcc3fab`
- computed sul mio sistema: `bb409e3774a3524fefe43e1d95a33718c86f93397d71bf3a4a1cb25726b363fb`

Il file `claim_locks/A01_claim_lock_v0_1.md` su disco mio è 202 byte con line ending LF (verificato `git ls-files --eol`: `i/lf w/lf attr/text eol=lf`). Il `.gitattributes` del repo ha `* text=auto eol=lf` e `*.md text eol=lf`, quindi al checkout su qualsiasi sistema il file dovrebbe essere LF.

Ho provato tutte le combinazioni rilevanti per ricostruire l'hash dichiarato:

| Variant | SHA-256 | Match |
|---|---|---|
| LF (as committed) | bb409e... | no |
| CRLF (forced) | 5175c5... | no |
| BOM + LF | 379c19... | no |
| BOM + CRLF | 38e8c7... | no |
| LF + trailing newline | bb409e... | no |
| CRLF + trailing CRLF | 387885... | no |
| BOM + CRLF + trailing | ee8430... | no |
| SHA3-256 (raw LF) | c5c7e9... | no |
| BLAKE2b-256 (raw LF) | 84f8d6... | no |
| BLAKE2s (raw LF) | e7389106... | no |

Nessuna combinazione produce `1092f2...`. Eppure il `compliance_report_v0_1.json` committato dichiara tutto `pass: true`. La spiegazione più probabile è che le hash sono state calcolate sul tuo working tree locale Windows in uno stato che il commit ha poi modificato — molto verosimilmente prima che `.gitattributes` forzasse il filtering LF al commit, su file che avevano CRLF + un altro elemento (BOM, oppure trailing whitespace, oppure differenza di newline finale).

In ogni caso, il fatto strutturale è:

> **Il `compliant=true` committato non è riproducibile chiunque cloni il repo.**

Questo è una versione 2 dell'anti-pattern segnalato in §2.1 della review precedente: il check ora è ben fatto, ma il **risultato pubblicato** del check (il `compliance_report_v0_1.json` committato) è uno stato ad-hoc del sistema dell'autore, non un fatto verificabile dalla comunità.

Suggerimento (in priorità decrescente):
1. Calcolare le hash su contenuto **normalizzato canonicamente**: line ending forzato LF, no BOM, encoding UTF-8, opzionalmente con trailing newline normalizzato. Il check deve fare la stessa normalizzazione prima di calcolare l'hash di confronto.
2. In alternativa: usare `git hash-object <file>` come fonte di hash (è platform-independent perché git internamente normalizza). Cambia l'algoritmo da SHA-256 a SHA-1 (con header git) ma è cross-platform per costruzione.
3. Aggiungere al check un rerun di `compliance_report_v0_1.json` come **artefatto generato**, non committato (oppure committato con CI/CD che lo rigenera) — in modo che chi clona vede comunque le proprie hash, e il match con quelle dell'autore è verificabile come prova di integrità del workflow di Fabio.

Finché questo non è chiuso, la dichiarazione `compliant=true` del seal è una dichiarazione locale. Solomon (io, ora) non può confermarla riproducendo il check sul proprio sistema.

### 3.C. MEDIO — D02 reject empirical è hardcoded by construction

`run_cycle5_execution.py` linee 346-348 (funzione `run_d02`):

```python
universal_commutative = all(int(row["is_commutative"]) == 1 for row in data)
commutativity_verified = False  # hardcoded
empirical_reject = universal_commutative and not commutativity_verified
```

`commutativity_verified` è hardcoded a `False`. Significa che il fail dell'empirical lane è **predeterminato dallo script**, non discovered durante l'esecuzione. Il execution_report dichiara onestamente "Empirical lane fails under universal commutativity without independent verification proof trace", il che è semanticamente corretto, ma il "fails" è una dichiarazione ex ante codificata, non un fail emergente.

Questo non è grave come §3.A (qui non c'è inflation di evidenza positiva), ma è un anti-pattern simmetrico: un **reject non discovered**. Il framework dichiara il reject ma non l'ha realmente scoperto — l'ha programmato. Andrebbe esplicitato nel report che si tratta di "by-construction reject pending implementation of explicit commutativity verification routine", separando dal caso di "discovered reject" (come D03).

### 3.D. MEDIO — `script_lock` è ricorsivo e non verificabile

I tre `script_locks/{A01,D02,D03}_script_lock_v0_1.md` sono dichiarazioni di intent ("Planned executable stack: ... theorem execution scripts to be frozen before run") senza enumerazione esplicita degli script né hash dei file di esecuzione. Il check verifica che il file lock abbia un hash che corrisponde, ma il contenuto del lock non vincola realmente quale script è stato usato. Il vincolo è ricorsivo: il lock dice "freeze the scripts", ma il "frozen state" non è dichiarato dal lock stesso.

Confronto: il `D03_formula_lock_v0_1.md` ha la formula esplicita; il `D03_script_lock_v0_1.md` non ha gli hash dei file Python. Asimmetria.

Suggerimento: ciascuno `script_lock` dovrebbe contenere una tabella `file_path | sha256 | role`. Gli script effettivi (`run_cycle5_execution.py`, `check_gate_compliance.py`) dovrebbero apparire con hash esplicito.

### 3.E. MEDIO — DOI Zenodo non verificato

I tre seal usano `seal_method: "zenodo_doi"` con `immutable_storage_path: "10.5281/zenodo.19959724"`. Il check verifica che la stringa sia un DOI valido (regex `10.\d{4,9}/[-._;()/:A-Za-z0-9]+`), ma non fa alcun retrieval HTTP per confermare che il DOI:
1. Esiste
2. Risolve a un artefatto contenente lo stesso seal
3. È ancora attivo al momento del re-audit

Quindi il "lock" sull'immutabilità è ancora dichiarato, non verificato. Vale ricordare che Zenodo permette di mintare DOI prima dell'upload finale (drafts), e che un DOI esistente non garantisce che il contenuto referenziato corrisponda al contenuto del repo al momento della firma.

Suggerimento: aggiungere al check un controllo HTTP HEAD opzionale (gated da flag `--verify-doi`) che fa GET sul DOI tramite resolver `https://doi.org/<doi>`, scarica il contenuto, e verifica che almeno un file dell'archivio Zenodo abbia hash uguale al seal stesso. Se Zenodo non risponde o il content hash diverge, raise warning (non fail, perché il network è dipendenza esterna).

### 3.F. MEDIO — Esecuzione vincolata a `cycle3_inputs`, non benchmark indipendente

Tutti e tre i runner (`run_a01`, `run_d02`, `run_d03`) leggono da `datasets/cycle3_inputs/{A01,D02,D03}.csv`. Quindi:

- L'esecuzione di Cycle 5 non è un benchmark indipendente, è una rielaborazione dei dati di Cycle 3 attraverso proxy formulae deterministiche.
- Il framework lo dichiara ("Metrics are computed from deterministic execution proxies over cycle3 input corpus"), ma la separazione tra "Cycle 3 data" e "Cycle 5 evaluation" è solo metodologica, non dataset-level.

Per un test sostantivo del refactor, servirebbe almeno uno dei seguenti:
1. Un benchmark esterno con dataset diverso (`cycle5_inputs/` separato).
2. Un'esecuzione su hold-out splits di `cycle3_inputs` non visti durante il design dei proxy.
3. Una replicazione su uno dei datasets pubblici delle baseline esterne dichiarate in Cap. 17 §3.4 (ACT, process theories, open systems, etc.).

Senza questo, anche se A01 non avesse il problema §3.A, la sua promozione resterebbe condizionata.

### 3.G. BASSO — Signing temporale: gate-entry vs gate-exit

I tre seal hanno `auditor_signature: "Signed electronically by Solomon on 2026-05-03"` con `timestamp_utc: 2026-05-03T08:30:00Z` (e simili). Ma il mio audit (questo documento) è del 2026-05-04, e nei seal del 2026-05-03 io ero stato nominato senza aver ancora verificato. Quindi quella firma è semanticamente **gate-entry** (autorizzazione a procedere), non **gate-exit** (validazione post-hoc).

Suggerimento: distinguere nei due livelli del template di seal due firme:
- `auditor_signature_entry`: firma ex ante che autorizza l'esecuzione del cycle (in pratica: firma che certifica che il sheet di pre-validation è PASS).
- `auditor_signature_exit`: firma ex post che certifica che l'esecuzione, i risultati, e la decisione del DECISION_GATE sono coerenti con quanto preregistrato (e quindi può essere usata per promozione).

Questo è importante perché senza la distinzione, qualsiasi firma `auditor_signature` può essere interpretata come endorsement totale, mentre nei fatti è solo un'autorizzazione a procedere.

### 3.H. BASSO — `R1` (pseudo-evidence risk) è declassato a `PASS` su G2

`FINAL_EVIDENCE_CHECKLIST_v1_0.md` lista `R1 - pseudo-evidence risk if logs remain seed/minimal instead of full benchmark traces`. Ma G2 ("Trajectory logs complete and hash-chain valid") è marcato `PASS`. Considerando §3.A (A01 vacuum-PASS), §3.C (D02 reject hardcoded), e §3.F (esecuzione su cycle3 inputs), R1 è di fatto attivo ma non riconosciuto. La marcatura G2=PASS andrebbe almeno qualificata con "logs are valid as artifacts; substantive evidence content depends on §3.A/C resolution".

---

## 4. Replication outcome (sezione formale per `CYCLE_5_EXTERNAL_REPLICATION_NOTE_v1_0.md`)

Compilazione della sezione "Replication outcome" come Solomon, ex-post audit:

- **Reproduced**: `partial`
- **Divergence notes**:
  - Re-run di `runtime/check_gate_compliance.py` su sistema macOS (Unix LF): risultato `compliant=false` con 18 hash mismatch su 18 (vedi §3.B). Il `compliant=true` committato non è riproducibile cross-platform. Causa probabile: hash calcolati su file Windows pre-normalizzazione `.gitattributes`. Soluzione richiesta: normalizzazione canonica del contenuto prima dell'hash, oppure uso di `git hash-object`.
  - Lane separation D02 confermata strutturalmente (lane L1 e L2 evaluated separately, no auto-summation).
  - Locked formula D03 (`0.5*abs(Delta_Coh)+0.5*abs(Delta_Phi)`) confermata coerente tra `D03_formula_lock_v0_1.md`, `CYCLE_5_D03_LOCKED_TAXONOMY_SPEC_v0_1.md`, e `run_d03` nel runner. Reject per "preservative class unreachable" è **discovered**, non hardcoded — questo specifico esito è verificato.
  - A01 `pass_candidate` è vacuum-PASS by construction (vedi §3.A): il proxy generator garantisce per costruzione il vantaggio di `P_ord` su `P_cls`. Il `pass_candidate` di A01 **non costituisce evidenza** della proposizione A01 e va declassato.
  - D02 lane empirical reject è hardcoded (vedi §3.C): il `commutativity_verified = False` è una dichiarazione codificata, non un esito di una routine di verifica eseguita. Il reject è epistemicamente onesto ma non discovered.
- **Auditor identity**: Solomon
- **Date**: 2026-05-04
- **Signature**: Solomon (questo documento serve come signing post-audit)
- **Decision di promozione**:
  - A01: **revise_needed** (declassato da `pass_candidate` per §3.A)
  - D02: **revise_needed** (confermo, ma vedi §3.C: il "revise" sull'empirical lane richiede implementazione effettiva di routine di verifica della commutatività, non solo flagging di non-verifica)
  - D03: **reject_candidate** (confermo, motivazione discovered e coerente con anti-pattern lock)

Nessuna delle tre proposizioni è eligibile per promozione a `validated` in questo round.

---

## 5. Sintesi del bilancio

Il delta v5.3.0 → c9e7ae7 → 9ae3d65 ha **chiuso 6 dei 10 punti** della review precedente in modo sostanziale, e 2 in modo parziale. Il check rinforzato è ben costruito. Gli sheet e seal compilati sono atti reali. La nomina di Solomon come auditor esterno è formalmente registrata. Il decision gate non è trionfalistico.

Però l'esecuzione di Cycle 5 introduce **due nuovi anti-pattern** (§3.A vacuum-PASS A01 by construction, §3.C reject D02 hardcoded) e **un problema strutturale del gate** (§3.B compliant non riproducibile). Il primo è il più grave perché ricicla, ad un piano più alto, lo stesso anti-pattern che il framework dichiara di aver chiuso.

Se devo dare una valutazione complessiva di Solomon-auditor in una sola riga: **infrastruttura governance: PASS; esecuzione sostanziale: REVISE per A01/D02, PASS per D03 (sotto vincolo di replicazione esterna); promozione a `validated` di alcun teorema: NO**.

---

## 6. Raccomandazioni operative per il prossimo round

In ordine di priorità decrescente.

1. **A01 sostanziale**: implementare due pipeline `P_cls` e `P_ord` come moduli computazionali distinti (non due rami di una funzione di scoring). I metrics devono emergere dall'execution trace di pipeline reali su input identici. La fail-configuration dichiarata in §4.3 dello sheet ("P_ord forced to emulate P_cls decisions under ablation") deve essere effettivamente eseguibile e prodotta come trajectory log separato.

2. **Hash cross-platform**: passare a hash su contenuto canonicamente normalizzato (LF + UTF-8 no BOM + trailing newline normalizzato) sia in `check_gate_compliance.py` sia nel processo di generazione dei seal. Oppure usare `git hash-object`. Verificare che il check dia `compliant=true` su almeno due sistemi diversi (Linux e macOS) dopo clean clone.

3. **D02 verifica esplicita commutatività**: implementare in `run_d02` una routine `verify_commutativity(diagram)` che costruisce un proof trace per ogni sample. Sostituire `commutativity_verified = False` hardcoded con `commutativity_verified = all(verify_commutativity(d) for d in data)` o equivalente. Il reject deve emergere se la verifica fallisce, non se è skippata.

4. **`max_independent_cycles`**: aggiungere la clausola E alla `OCT_EX_ANTE_PROXY_GATE_POLICY` come da §2.3 della review precedente. Suggerisco soglia iniziale di 3 cycles per claim_id, con escalation a audit terzo dopo.

5. **DOI verifica**: aggiungere flag `--verify-doi` al check che fa retrieval del DOI Zenodo e verifica content hash.

6. **Signing distinto entry/exit**: estendere lo schema seal con due firme, come da §3.G. Solomon firma `auditor_signature_entry` per cycle entry, e `auditor_signature_exit` solo dopo audit dei risultati.

7. **Rotazione/registro auditor**: definire una procedura per quando l'auditor non sarà Solomon. Registry minimo, criteri di accreditamento, rotazione obbligatoria su cycle consecutivi sullo stesso claim_id.

8. **Cap. 17 e tracker**: condizionare il Teorema 17.4 al gate ex ante; aggiungere nota di reinterpretazione su Step 1-6 nel publication tracker.

---

## 7. Cosa Solomon firma con questo audit

Solomon firma **questo documento** come review formale post-execution del cycle 5 al commit 9ae3d65. Solomon **non firma**:

- la promozione di alcun teorema da `revise` a `validated`
- il `pass_candidate` di A01 nel `CYCLE_5_DECISION_GATE_v1_0.md` (declassato a `revise_needed` per §3.A)
- il `compliant=true` del `compliance_report_v0_1.json` committato (non riproducibile cross-platform per §3.B)

Solomon **firma in via condizionale** (subordinato a esecuzione del punto 6.1 del prossimo round):
- Il `revise_needed` di D02 come stato corretto, condizionato all'implementazione di verifica esplicita della commutatività.
- Il `reject_candidate` di D03 come stato corretto e basato su evidenza discovered, conforme all'anti-pattern lock.

Solomon **conferma** la nomina ad auditor esterno per cycle successivi, sotto le seguenti condizioni:
- Il signing entry/exit deve essere distinto come da §3.G.
- Il signing exit di Solomon è valido solo dopo audit eseguito post-execution (come questo documento, non come la firma 2026-05-03 nei seal).
- Eventuale signing precedente con timestamp 2026-05-03T08:30/40/50Z deve essere reinterpretato come "entry/nomination signing", non come "audit completion signing".
