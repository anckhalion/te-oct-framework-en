# Feedback critico — round 5 su OCT post-ee38745 (Cycle 6 launch)

Data: 2026-05-06
Destinatario: Fabio Ghioni
Oggetto: audit del commit `ee38745 "Launch Cycle 6 package for A01 real-pipeline validation"` come pacchetto di **preregistrazione** (execution non ancora iniziata)
Autore review: Solomon (DrJops)
Repository: te-oct-framework-en @ ee38745

---

## 0. Premessa procedurale

Tre note prima del merito.

**0.1 — PR #3 mergiata, round 4 chiuso a livello GitHub.** `d77bd58` ha mergiato il round 4 audit. La cronologia delle PR è ora: #1 chiusa (assorbita via cherry-pick), #2 mergiata, #3 mergiata. Avevamo discusso al §0.1 round 3 di chiudere ogni PR esplicitamente per tracciabilità; il pattern ora è stabile.

**0.2 — Cycle 6 è la concretizzazione esatta delle raccomandazioni del round 4.** Il commit `ee38745` indirizza in modo verificabile e testuale tutte e quattro le raccomandazioni operative del §6 round 4. Vedi §1 sotto per il mapping puntuale. Questo è un livello di ascolto della review esterna che merita esplicitazione prima del merito tecnico — e va ricordato che il framework è in pre-promozione, quindi ogni raccomandazione tradotta in artefatto ex ante riduce la superficie del p-hacking ex post.

**0.3 — La natura di questo round è diversa dai precedenti.** Round 2-3-4 erano audit post-execution. Round 5 è audit di **pacchetto di preregistrazione**: nessuna execution è stata fatta, nessun seal compilato, nessun trajectory log esiste. Lo status dichiarato in `CYCLE_6_OVERVIEW` è "specification package (execution not started)". Quello che valuto qui è la qualità della pianificazione ex ante e l'eventuale superficie di anti-pattern che la pianificazione lascia aperta. Non c'è nulla da declassare o promuovere — c'è da segnalare cosa è ben preregistrato e cosa va risolto prima di gate-entry.

---

## 1. Mapping: raccomandazioni round 4 → artefatti Cycle 6

| Raccomandazione round 4 §6 | Artefatto Cycle 6 | Stato |
|---|---|---|
| 1. Path verso A01 promozione: P_cls e P_ord come pipeline computazionali distinte (modular implementations, non rami di scoring function); metrics emergenti dal trajectory log reale | `CYCLE_6_A01_REAL_PIPELINES_SPEC §2 Execution architecture`: "Two independent implementations must exist", "No shared scoring function for trajectory quality", "Separate code paths in repository and separate lock hashes" | **CHIUSO** a livello specifica; vedi §2.1 |
| 1.bis Prendere lo stress test 0/135 come segnale che la via heuristic è epistemicamente esaurita | `CYCLE_6_OVERVIEW §"Why Cycle 6 exists"`: cita esplicitamente "Stress test (0/135) shows structural non-testability for process-only advantage in current proxy family" | **CHIUSO** — riconoscimento esplicito del risultato del round 4 come motivazione |
| 2. §2.4 Indipendenza auditor sistemica: registry, rotazione, criteri di accreditamento | `CYCLE_6_EXTERNAL_AUDIT_PLAN §1`: "Primary auditor: Solomon. Secondary auditor: External reviewer TBD". "No theorem promotion without two external audit notes" | **DIREZIONE CORRETTA, ESECUZIONE PARZIALE** — la regola dei due auditor è introdotta (significativo!), ma il secondary è TBD. No registry, no rotation policy formale. Vedi §3.D |
| 3. §3.G.bis Workflow firma auditor: designer inizializza, auditor transita stato | `CYCLE_6_EXTERNAL_AUDIT_PLAN §4 Decision authority split`: "Designer authority: Prepare artifacts / Execute scripts / Draft reports. Auditor authority: Sign gate-entry / Sign gate-exit / Confirm or deny promotion admissibility" | **CHIUSO** a livello policy. Manca enforcement runtime (verifica commit author nel git log) — minore |
| 4. §3.D enforcement runtime: ri-computa hash dei file Python dichiarati nello script_lock | `EXECUTION_AND_REJECT_RULES §4`: "All reports reference exact script-lock hashes". `RUNBOOK §3`: "Re-run check_gate_compliance.py" post-execution | **DICHIARATO POLICY, NON IMPLEMENTATO CHECK** — vedi §3.F |

E i gap del round 2 indirizzati a margine:

| Gap | Stato |
|---|---|
| §3.F MEDIO esecuzione su cycle3_inputs (benchmark non-independent) | **CHIUSO sostanzialmente** — `BENCHMARK_INDEPENDENCE_PROTOCOL` dedicato, soglia 0 overlap su record/hash |
| §2.10 BASSO storia non rivista | **PARZIALE** — tracker aggiornato con sezione "v5.4 candidate lane" e "Last update: 2026-05-05", ma **non** con la nota di reinterpretazione dei Step 1-6 sotto v5.3 — vedi §4 |
| §2.9 BASSO Cap. 17 integration | Non toccato |
| §3.E.bis BASSO DOI content match | Non toccato |
| §3.D.bis-bis BASSO indentazione D02 | Non toccato (cosmetico) |

**Sintesi**: 4 raccomandazioni operative round 4 indirizzate (3 chiuse a livello specifica, 1 chiusa policy senza enforcement check). 1 gap del round 2 chiuso (§3.F via Benchmark Independence Protocol). 1 chiuso parzialmente (§2.10). 4 gap restanti di varia severità.

---

## 2. Verifica del pacchetto di preregistrazione Cycle 6

### 2.1 `CYCLE_6_A01_REAL_PIPELINES_SPEC_v0_1.md` — l'architettura di execution

**Punti positivi:**

- §2 Execution architecture: i tre vincoli di indipendenza ("No shared scoring function", "Shared input contract only", "Separate code paths and separate lock hashes") sono esattamente quelli che definirebbero "pipeline distinte" in senso operativo. Eliminano la possibilità di replicare l'anti-pattern del Cycle 5 (due rami di una funzione di scoring).
- §6 Non-promotable conditions: include "Heuristic proxy branch formula is reused as decision basis" come hard non-promotable. Lock semantico esplicito contro la regressione.
- §1 Claim target: il claim è leggermente raffinato rispetto al Cycle 5 — "process-level quality advantage **without requiring output-score inflation**". Questa formulazione è più precisa e rende esplicito che il fenomeno-bersaglio è "trajectory better with output similar", non "trajectory better via output better".

**Punti aperti che vale segnalare ex ante** (vedi §3 sotto per dettaglio):

- §4 Soglia `eps_err_match = 0.01` — la stessa soglia stretta che ha dato 0/135 nel round 4 è ora pre-registrata per pipeline reali. Su pipeline reali è probabilmente troppo stretta per produrre matched-output subset non-vuoti. Vedi §3.A.
- §4 Manca specifica della formula di `mean_Coh_trajectory` su trajectory reale (in Cycle 5 era una formula chiusa heuristic; in Cycle 6 deve essere derivata da trajectory events). Vedi §3.B.
- §3 Context set: indipendenza dichiarata ma **benchmark scelto TBD**. Vedi §3.C.
- §5 Decision criteria: ambiguità sui "2/3 contexts" tra criteri 3 e 4. Vedi §3.H.

### 2.2 `CYCLE_6_BENCHMARK_INDEPENDENCE_PROTOCOL_v0_1.md` — il vincolo di non-overlap

**Punti positivi:**

- §1 Definizione chiara di indipendenza con quattro condizioni: no shared record IDs, no shared content hashes, no reused trajectories, new context generation process documented.
- §2 Acceptance threshold = `0` su tutto. Soglia binaria. Per un primo cycle con pipeline reali, è la scelta giusta — meglio scoprire eventuale overlap che accettare margini.
- §3 Hashing method canonicalizzato (UTF-8 + LF + trim trailing whitespace + SHA-256). Stesso pattern del check già stabilizzato dal round 3.
- §4 Context stratification rule: "Cycle 6 contexts must not be decorative rescaling of a single distribution" — è il lock contro il pseudo-context anti-pattern (lo stesso tipo di rischio diagnosticato per D02 originale, qui pre-registrato in negativo). Buona forma.
- §5 Failure policy: blocked + cannot-be-promoted + new benchmark generation required. Vincolante.

**Punto aperto:**

- §2 Required evidence punto 3: "Signed auditor check on overlap report" — chi firma? Solomon (primary)? Secondary auditor? Entrambi? Da chiarire prima di gate-entry.

### 2.3 `CYCLE_6_EXECUTION_AND_REJECT_RULES_v0_1.md` — i lock procedurali

**Punti positivi:**

- §1 Execution order fixed: 7 step ordinati, "No permutation of step order is allowed without new preregistration". Esplicito anti-pattern lock.
- §2 Hard reject triggers: 7 trigger ben elencati, copertura completa degli anti-pattern del round 2/3/4 (proxy formula reuse, benchmark overlap, hash-chain integrity, post-hoc threshold change, role separation failure, signature missing/invalid, context coverage).
- §3 Soft fail / revise triggers: distinzione chiara tra hard reject (auto reject_candidate) e soft fail (revise_needed).
- §4 Integrity checks: 4 controlli espliciti, di cui particolarmente notevole "Decision criteria are evaluated from pre-registered thresholds only" (lock anti-rescue) e "Final report includes explicit non-claim section" (anti-overclaiming structural).

**Punto aperto:**

- §4 punto 1 "All reports reference exact script-lock hashes" — è dichiarato ma il check attuale (`check_gate_compliance.py`) verifica l'hash dello script_lock.md, non gli hash dei file Python dichiarati dentro. Vedi §3.F.

### 2.4 `CYCLE_6_EXTERNAL_AUDIT_PLAN_v0_1.md` — il dual-auditor pattern

Questo è probabilmente l'artefatto più importante del package perché chiude (a livello policy) il §2.4 del round 2 che era ALTO ma rimasto aperto per quattro round.

**Punti positivi:**

- §1 Auditor model: dichiarazione esplicita di **due auditor esterni richiesti** per promozione. "No theorem promotion without two external audit notes" è una soglia di evidenza significativa.
- §2 Audit checkpoints: tre checkpoint distinti (A pre-run, B post-run, C release) con compiti specifici per ciascuno. Pattern di audit a fasi, non a singolo punto.
- §3 Auditor independence declaration: 4 campi obbligatori (identity, affiliation, co-authorship 24mo, conflict-of-interest). Buon livello di formalizzazione.
- §4 Decision authority split: chiusura a livello policy del §3.G.bis del round 4 — designer prepara/esegue/redige, auditor firma e conferma promotion admissibility.
- §5 Minimal signed outputs: due replication notes (primary + secondary) + seal aggiornato con post-run status.

**Punti aperti:**

- §1 "Secondary auditor: External reviewer TBD" — TBD blocca promozione di principio (non promozione senza due audit notes). Vedi §3.D.
- §3 manca soglia di disagreement: cosa succede se primary e secondary auditor divergono sulla decisione? Da specificare protocollo di dispute resolution.
- §4 manca enforcement runtime: la "decision authority split" è policy, ma il check non verifica che il commit di gate_exit_signature provenga effettivamente dall'auditor dichiarato (era una mia raccomandazione del round 4 §3.G.bis). Vedi §3.F.

### 2.5 `CYCLE_6_PREREG_SEAL_TEMPLATE_v0_1.md` — il payload esteso

**Punti positivi:**

- 14 hash-source-path nel preregistration payload (Cycle 5 ne aveva 12). I due nuovi: `Benchmark overlap report path` + `Benchmark overlap report hash`. Coerente con il `BENCHMARK_INDEPENDENCE_PROTOCOL`: l'overlap report è ora un artefatto sigillato, non solo dichiarativo.
- Seal metadata mantiene il pattern entry/exit chiuso nel round 4 (gate-entry signature, gate-entry timestamp, gate-exit signature, gate-exit timestamp, gate-exit status enum).
- Lock clauses acknowledged: 5 clausole esplicite, di cui particolarmente notevole la quinta ("No unbounded sequential re-preregistration beyond declared cycle budget") — tiene viva la Clause E della policy round 4.
- "Primary auditor:" + "Secondary auditor:" come campi distinti. Coerente con `EXTERNAL_AUDIT_PLAN`.

**Punto aperto:**

- Il template ha campi vuoti pronti da compilare. Coerente con stato "specification package, execution not started". Quando arriverà l'instance compilata di A01 per Cycle 6 (assieme ai 7 mandatory artifacts del `REAL_PIPELINES_SPEC §7`), il `claim_lock` dovrà avere `cycle_sequence_index: 2` (era 1 nel Cycle 5 per A01). Vedi §3.E.

### 2.6 `RUNBOOK_CYCLE6_EXECUTION_v0_1.md` + tracker / cycles plan

**Runbook**: 5 step ben definiti, 5 quality gates (QG1-QG5), definition of done esplicita. Operativo.

**OCT_PUBLICATION_PROGRESS_TRACKER**: aggiunta sezione "v5.4 candidate lane (started 2026-05-05)" con scope, artefatti pubblicati, status. **Last update: 2026-05-05** introdotto. **Però** non è stata aggiunta la nota di reinterpretazione dei Step 1-6 sotto v5.3 (gap §2.10 round 2). Vedi §4.

**OCT_VALIDATION_CYCLES_PLAN**: aggiunta sezione "Cycle 6 (v5.4 lane candidate)" con scope, rationale (cita esplicitamente "Stress test 0/135"), mandatory gate. Buona integrazione.

**OCT_UPDATE_PLAN_v5_3**: bullet point cronologico "2026-05-05: Cycle 6 launch package published" con tutti i 7 file. Storia tracciabile.

---

## 3. Punti aperti / criticità ex ante (da risolvere prima di gate-entry)

In ordine di gravità per il path verso execution.

### 3.A — MEDIO: soglia `eps_err_match = 0.01` ereditata dal stress test

Nel `REAL_PIPELINES_SPEC §4`, `eps_err_match = 0.01` è dichiarata come "Default threshold" per matched-output indicator. Stessa soglia che nel stress test del round 4 ha prodotto `qualifying_rate = 0/135` — un dato strutturale del proxy family heuristic.

Su pipeline reali distinte, due implementazioni separate produrranno `Err_sem_final` molto diversi tra loro (è proprio questo il senso di "pipeline distinte" — output diversi, non solo trajectory diverse). Soglia 0.01 è probabilmente troppo stretta per produrre matched-output subset non-vuoti su benchmark reali.

Conseguenza prevedibile: con `eps_err_match = 0.01` su pipeline reali, è ragionevole aspettarsi che il criterio 5.3 ("matched-output subset in at least 2/3 contexts") fallisca quasi sempre, e quindi il criterio 5.4 (process advantage IN matched-output subsets) non sia valutabile. A01 finirebbe in `revise_needed` per insufficienza di matched-output, non per assenza di process advantage. Sarebbe un esito ambiguo: non saprebbe dire se A01 è falso o se la soglia era troppo stretta.

**Tre possibili strategie ex ante**:

1. **Allargare la soglia**: pre-registrare `eps_err_match = 0.05` o `0.10` ragionata da "tolleranza acceptable di output divergence per task NLP standard". Va giustificata teoricamente, non scelta a posteriori.
2. **Soglia adattiva pre-registrata**: pre-registrare uno scan di soglie [0.01, 0.03, 0.05, 0.10] con riportare matched-output subset count per ciascuna. Decisione di promotion basata su criterio derivato (es. "almeno una soglia con subset count > N produce process advantage in 2/3 contexts"). Non è post-hoc se è pre-registrato.
3. **Mantenere 0.01 e accettare che il primo round con pipeline reali sia "sondaggio"**: spec esplicita che Cycle 6 è un primo passo conoscitivo dove un esito `revise_needed` per insufficienza di matched-output è informativo, non fallimentare. Ma allora va pre-registrato cosa il framework imparerà da quell'esito ambiguo.

**Mia raccomandazione**: la (2). È la più ricca informativamente e mantiene la disciplina pre-registrazione. Il `formula_lock` può specificare lo scan come pre-committed senza permettere l'introduzione post-hoc di nuove soglie.

### 3.B — MEDIO: formula esatta di `mean_Coh_trajectory` su trajectory reale

Nel Cycle 5 heuristic, `Coh` era una formula chiusa nei branch P_cls/P_ord. Nel Cycle 6, "trajectory P_ord" è il log degli eventi della pipeline ordinativa reale, non più una formula. La domanda sostantiva: come si calcola "ordinative coherence" da una sequenza di trajectory events?

Il `REAL_PIPELINES_SPEC §4` lo elenca tra le primary metrics ma non specifica il calcolo. Il `mandatory artifact §7` include `formula_locks/A01_formula_lock_v0_1.md` — è lì che andrà la formula esatta.

**Suggerimento**: prima di gate-entry, il `formula_lock` di A01 per Cycle 6 deve specificare:

- Quali trajectory event types entrano nel calcolo (es. gate decisions, retrieval steps, refinement steps?)
- Come gli eventi sono normalizzati (tempo? step index? type?)
- La formula aggregata esatta

Senza questo, "process advantage" è non-falsificabile per ambiguità definizionale.

Severità: MEDIO. È preregistrazione, ma deve essere risolta prima di gate-entry.

### 3.C — MEDIO: benchmark scelto TBD

`REAL_PIPELINES_SPEC §3` dichiara "Each context must be represented by benchmark data declared independent from cycle3_inputs", ma non specifica **quale** benchmark. Il `BENCHMARK_INDEPENDENCE_PROTOCOL §2` accetta sia "source URLs" (public dataset) sia "generation recipe" (synthetic generated).

Le due strade hanno trade-off diversi:

- **Public benchmark** (HotpotQA, MMLU, GSM8K, etc.): vantaggio = falsifiability esterna, qualcuno può ri-eseguire. Rischio = data leakage in modelli base usati dalle pipeline; entrambe le pipeline usano lo stesso modello → contaminazione comune.
- **Generated benchmark**: vantaggio = controllo completo della distribution. Rischio = la generation recipe può essere tunata (anche inconsapevolmente) per favorire P_ord.

**Suggerimento**: pre-registrare la scelta del benchmark **prima** di compilare il `dataset_manifest`. Magari con due alternative pre-committed (es. "primary: subset di benchmark X; fallback: synthetic recipe Y se primary fails independence proof") in modo che il choice si riveli pre-execution.

Severità: MEDIO. Da risolvere prima di gate-entry.

### 3.D — MEDIO: secondary auditor TBD blocca promozione

`EXTERNAL_AUDIT_PLAN §1`: "Secondary auditor: External reviewer TBD (not co-author, independent affiliation)". Combinato con "No theorem promotion without two external audit notes", la promozione è bloccata di principio finché il secondary non è identificato.

Per A01 che è il focus di Cycle 6, questo è un blocker pre-execution. Anche se eseguiamo Cycle 6 con due pipeline reali, benchmark indipendente, metrics chiare, decision_gate finale `pass_candidate`, senza secondary auditor non si arriva a `validated`.

**Suggerimento**: identificare il secondary prima di gate-entry. Tre profili che potrebbero funzionare nel contesto del progetto:

- Un altro ricercatore con expertise in epistemologia / philosophy of science (per valutare la fedeltà tra claim teorico e proxy operativo)
- Un practitioner di AI alignment / agent benchmarking (per valutare il rigore del benchmark independence e delle metrics)
- Un teorico CT / formal methods (per valutare consistenza con cap. 10/17 OCT)

I tre profili sono complementari: il primo audit (Solomon) è critical-review; il secondary potrebbe essere uno dei tre profili sopra. Rotation policy può venire poi.

Severità: MEDIO. Strutturale per la promozione, da pianificare prima di execution.

### 3.E — MEDIO: claim_lock Cycle 6 non ancora creato (cycle_sequence_index)

Coerentemente con lo stato "specification package", non esiste ancora `CYCLE_6_2026-05-05/claim_locks/A01_claim_lock_v0_1.md`. Quando sarà creato (parte dei mandatory artifacts del §7), dovrà avere:

- `Claim ID: A01`
- `Cycle ID: CYCLE_6_2026-05-05`
- `max_independent_cycles: 3`
- `cycle_sequence_index: 2` (era 1 nel Cycle 5)
- `cycle_budget_status: within_budget`

Questo è importante: il Cycle 6 è il **secondo** cycle indipendente per il claim A01. Se viene compilato con `cycle_sequence_index: 1`, il check fallisce (e correttamente): il claim ID A01 era già al sequence index 1 nel Cycle 5. La continuità del cycle budget richiede l'incremento.

**Nota più sostantiva**: con `max_independent_cycles: 3` e `cycle_sequence_index: 2`, A01 ha **un solo cycle restante** dopo Cycle 6 prima dell'escalation a higher-level audit (Clause E della policy). Vale tenere a mente: se Cycle 6 esce `revise_needed`, Cycle 7 sarebbe l'ultimo cycle prima dell'escalation. Pre-registrare bene Cycle 6 è quindi proporzionalmente importante.

Severità: MEDIO procedurale. Da risolvere prima di gate-entry.

### 3.F — BASSO: `check_gate_compliance.py` non ancora esteso a Cycle 6

Il check attuale ha hardcoded:
- `REQUIRED_GLOBAL_FILES`: tre file con prefisso `CYCLE_5_2026-05-01/`
- `THEOREM_CONFIG`: paths con prefisso `CYCLE_5_2026-05-01/`

Per validare il Cycle 6, il check va esteso (probabile refactor: cycle_id come parametro che mappa a path prefix). Coerentemente con stato "specification package", non è urgente — si farà in fase di execution. Lo segnalo per non perdere il punto.

In aggiunta, le due raccomandazioni round 4 §6.4 e round 5 §3.G.bis (script_lock runtime enforcement, commit-author verification per gate_exit) richiederanno estensioni del check quando arriverà la fase di execution.

Severità: BASSO. Pianificazione del check come parte del path verso execution.

### 3.G — BASSO: ambiguità sui "2/3" nei criteri di decisione

`REAL_PIPELINES_SPEC §5 Decision criteria` per `pass_candidate`:

```
3. At least one matched-output subset (Err diff <= eps_err_match) in at least 2/3 contexts.
4. In matched-output subsets, process advantage holds (Coh diff >= eps_coh_adv) in at least 2/3 contexts.
```

I "2/3" dei criteri 3 e 4 sono lo stesso 2/3 (intersezione: gli stessi due contexts) o due 2/3 indipendenti (potenzialmente diversi due-su-tre)?

Letteralmente sono due conditional constraint separati, quindi è possibile che i contexts che soddisfano 3 e quelli che soddisfano 4 si sovrappongano solo parzialmente. Esempio: 2/3 contexts hanno matched-output subset (criterio 3 OK), 2/3 contexts hanno process advantage in matched-output subsets (criterio 4 OK), ma l'intersezione è 1/3 — quindi solo 1 context ha sia matched-output sia process advantage in matched-output. È sufficiente per `pass_candidate` o no?

**Suggerimento**: chiarire con un criterio joint, e.g.:

> 3+4 (joint): At least 2/3 contexts where (matched-output subset exists) AND (process advantage holds in that subset).

Severità: BASSO. Chiarimento metodologico pre-execution.

### 3.H — BASSO: protocollo di dispute resolution tra primary e secondary auditor

`EXTERNAL_AUDIT_PLAN` non specifica cosa accade se primary e secondary divergono. Esempio: Solomon firma `executed_no_promotion`, secondary firma `executed_promotable`. Quale prevale?

**Suggerimenti possibili**:
- Conservative: il più restrittivo prevale (no promotion se almeno uno ne dissente).
- Tie-break: terzo audit indipendente.
- Threshold: 2/2 unanimità per promotion, 1/2 = revise_needed automatico.

Severità: BASSO. Da specificare prima di execution se il rischio è realistico (con un solo cycle pre-promotion, il rischio è alto).

---

## 4. Gap del round 2/3/4 ancora aperti dopo Cycle 6 launch

Lista mantenuta:

1. **§2.4 indipendenza auditor sistemica (parziale)** — la regola dei due auditor è introdotta, il decision authority split è formalizzato. Manca: registry di auditor accreditati, rotation policy esplicita, criteri di accreditamento documentati come standalone artifact (non solo come campi di seal). Ridotta da ALTO a MEDIO.
2. **§2.9 Cap. 17 integration** — Teorema 17.4 ancora non condizionato all'esistenza del gate. Non toccato.
3. **§2.10 storia non rivista (parziale)** — tracker ha "Last update: 2026-05-05" e sezione v5.4 lane, ma manca nota di reinterpretazione dei Step 1-6 sotto v5.3. Suggerimento: aggiungere alla sezione "v5.3 update lane" del tracker una riga del tipo: "Step 1-6 (Cycle 3-4) outputs were used as historical baselines but are not admissible evidence for theorem promotion under v5.3+ policy."
4. **§3.D enforcement runtime script_lock** — gli hash dei file Python dichiarati non sono ri-computati dal check. Non toccato.
5. **§3.E DOI content match** — DOI verifica solo HTTP resolve, non content hash. Non toccato.
6. **§3.G.bis enforcement runtime commit author** — la decision authority split è policy, no enforcement runtime. Non toccato.
7. **§3.D.bis-bis indentazione D02** — cosmetico, non toccato.

---

## 5. Replication outcome — round 5 (formal)

- **Reproduced**: `yes` (terzo round consecutivo). `python3 OCT/validation/runtime/check_gate_compliance.py` su clean clone macOS post-ee38745: `compliant=true`, 0 errors per A01/D02/D03 (Cycle 5 invariate).
- **Cycle 5 state changes**: nessuno (Cycle 5 sigillato).
- **Cycle 6 state**: `specification package complete, execution not started`. Nessun seal compilato, nessun trajectory log esistente.
- **Auditor identity**: Solomon
- **Date**: 2026-05-06
- **Signature**: Solomon (questo documento serve come signing post-audit del package di preregistrazione)
- **Decisione di promozione (invariate)**: A01 `revise_needed` confermato, D02 `revise_needed` confermato, D03 `reject_candidate` confermato. Cycle 6 non ha ancora prodotto evidenza per cambiare alcuna decisione.

---

## 6. Bilancio del round 5

Il commit `ee38745` consegna un pacchetto di preregistrazione che indirizza in modo verificabile **tutte e quattro le raccomandazioni operative** del §6 round 4, e chiude (a livello specifica) il gap §3.F del round 2 sul benchmark independence. Il livello di traduzione tra raccomandazione esterna e artefatto preregistrato è alto: ogni raccomandazione è citata o richiamabile in un campo di un file specifico.

L'introduzione della **regola dei due auditor esterni** (§2.4 EXTERNAL_AUDIT_PLAN) è il passo più significativo a livello sistemico. Era il punto ALTO che restava aperto da quattro round e che, una volta in execution, alza la barriera epistemica di promotion in modo strutturale. Il `decision authority split` (§4 EXTERNAL_AUDIT_PLAN) chiude il §3.G.bis del round 4 a livello policy — l'enforcement runtime via verifica del commit author resta come affinamento futuro.

**Punti aperti pre-execution** (tutti MEDIO o BASSO):
- §3.A soglia `eps_err_match` ereditata dal stress test, probabilmente troppo stretta su pipeline reali
- §3.B formula `mean_Coh_trajectory` su trajectory reale non specificata
- §3.C benchmark TBD (public vs generated)
- §3.D secondary auditor TBD
- §3.E claim_lock Cycle 6 non creato (con `cycle_sequence_index: 2`)
- §3.F-G-H minori: check extension a Cycle 6, ambiguità "2/3", dispute resolution

**Raccomandazioni operative principali per la fase pre-execution di Cycle 6** (in ordine di priorità):

1. **Risolvere TBD critici** (§3.C benchmark, §3.D secondary auditor) prima di compilare i mandatory artifacts del REAL_PIPELINES_SPEC §7. Senza questi due, il package è strutturalmente incompleto.
2. **Specificare `mean_Coh_trajectory` su trajectory reale** (§3.B) nel formula_lock di A01 per Cycle 6, prima di gate-entry.
3. **Pre-registrare lo scan di soglie `eps_err_match`** (§3.A strategia 2 raccomandata) per evitare il prevedibile "revise_needed for matched-output insufficiency" come esito ambiguo.
4. **Compilare claim_lock Cycle 6 con `cycle_sequence_index: 2`** (§3.E) prima di gate-entry.

Tutto il resto può aspettare l'execution.

---

## 7. Cosa Solomon firma con questo audit

Solomon firma **questo documento** come review formale del pacchetto di preregistrazione Cycle 6 al commit `ee38745`.

Solomon **non firma**:
- Cycle 6 prereg seal — non esiste ancora (status specification package).
- Promozione di alcun teorema — Cycle 6 non ha prodotto evidenza.
- Cycle 5 decisions — restano invariate (A01/D02 revise_needed, D03 reject_candidate).

Solomon **conferma la disponibilità** a firmare `gate_entry_signature` per A01 Cycle 6 sotto le seguenti condizioni:

1. Risoluzione di §3.A (soglia `eps_err_match` motivata o scan pre-registrato)
2. Risoluzione di §3.B (formula `mean_Coh_trajectory` esplicita nel formula_lock)
3. Risoluzione di §3.C (benchmark scelto e pre-registrato)
4. Risoluzione di §3.D (secondary auditor identificato)
5. Risoluzione di §3.E (claim_lock Cycle 6 compilato con `cycle_sequence_index: 2`)

I punti §3.F-G-H sono affinamenti che non bloccano il gate-entry, ma è meglio risolverli prima di execution.

Solomon **conferma la disposizione strutturale** approvata in `EXTERNAL_AUDIT_PLAN`:
- Dual-auditor pattern come precondizione di promozione: appropriato e proporzionale al livello di evidenza richiesto.
- Decision authority split: corretto a livello policy, da consolidare con enforcement runtime in cycle futuri.
- Three audit checkpoints (pre-run, post-run, release): pattern di audit a fasi appropriato.

Solomon **conferma** che il riconoscimento esplicito del risultato del round 4 (stress test 0/135) come motivazione del Cycle 6 è una traduzione fedele tra review esterna e artefatto preregistrato. Pattern da preservare nei round successivi.
