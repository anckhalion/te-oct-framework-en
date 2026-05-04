# Feedback critico — round 4 su OCT post-85a3ced

Data: 2026-05-05
Destinatario: Fabio Ghioni
Oggetto: audit dei due commit di sostanza del 2026-05-04 sera (`7a27c29` stress test A01 + `85a3ced` cycle budgets / entry-exit signatures / strict DOI)
Autore review: Solomon (DrJops)
Repository: te-oct-framework-en @ 85a3ced

---

## 0. Premessa procedurale

Tre note prima del merito tecnico.

**0.1 — PR #2 mergiata correttamente.** `dc40194` ha mergiato la PR del round 3 senza squash, conservando i due commit di Solomon (`9d1d9e6` audit + signing). La cronologia GitHub è ora tracciabile: PR #1 chiusa esplicitamente (assorbita via cherry-pick del round 2), PR #2 mergiata, PR #3 in apertura come parte di questo round. La nota procedurale del §0.1 round 3 è chiusa.

**0.2 — Le due firme entry/exit nei seal sono ora distinte.** I tre seal A01/D02/D03 portano `gate_entry_signature` (Solomon, 2026-05-03) e `gate_exit_signature` (Solomon, 2026-05-04) come campi separati con timestamp distinti. La nota §0.2 round 3 sul signing temporale 2026-05-03 è risolta strutturalmente — vedi §2.2 sotto. Resta un edge-case di workflow procedurale che apro come §3.G.bis nuovo.

**0.3 — Hash cross-platform regge a un secondo passaggio.** Re-eseguito `python3 OCT/validation/runtime/check_gate_compliance.py` su clean clone macOS post-85a3ced: `"compliant": true`, 0 errors per ciascuno dei tre teoremi, anche con i nuovi campi entry/exit obbligatori e il claim budget validation in linea. La canonicalizzazione UTF-8 LF + BOM stripping ha tenuto attraverso due commit successivi che hanno toccato 4 dei 6 file hashati (claim_lock per cycle budget, sheet per heading 1.1, seal per entry/exit, script_lock per hash espliciti). Buon segnale: la pipeline di re-hashing via `refresh_seal_hashes.py` è effettivamente usata.

---

## 1. Mapping: cosa del round 2/3 è stato chiuso

| Punto | Round | Severità | Stato dopo 85a3ced | Note |
|---|---|---|---|---|
| §2.3 max_independent_cycles | round 2 | ALTO | **CHIUSO** | Vedi §2.1 |
| §3.G signing entry/exit | round 2 | BASSO | **CHIUSO** | Vedi §2.2 |
| §3.E DOI verifica | round 2 | MEDIO | **CHIUSO step 1, parziale step 2** | Vedi §2.3 |
| §3.A.bis stress test A01 | round 3 | MEDIO | **CHIUSO sostanzialmente, con risultato di portata** | Vedi §2.4 |
| §3.D script_lock ricorsivo | round 2 | MEDIO | **CHIUSO declarative, parziale enforcement** | Bonus inaspettato — vedi §2.5 |
| §3.B.bis schema decision_raw | round 3 | BASSO | **CHIUSO** | D02/D03 ora hanno `decision_raw` parallelo a A01 |
| §3.C.bis date dei file | round 3 | BASSO | **CHIUSO** | `RUN_DATE = datetime.now(timezone.utc).date().isoformat()` dinamico in tutti i write_report |
| §3.D.bis indentazione A01 | round 3 | BASSO | **CHIUSO A01, re-introdotto in D02** | Vedi §3.C |
| §3.F esecuzione su cycle3_inputs | round 2 | MEDIO | Non toccato | Ancora aperto |
| §2.4 indipendenza auditor sistemica | round 2 | ALTO | Non toccato | Ancora aperto |
| §2.9 Cap. 17 integration nel corpo | round 2 | BASSO | Non toccato | Ancora aperto |
| §2.10 storia non rivista nel tracker | round 2 | BASSO | Non toccato | Ancora aperto |

Sintesi: **4 punti dichiarati nel commit message tutti chiusi** (di cui 1 con risultato sostantivo non-banale, vedi §2.4), **3 punti del round 3 chiusi a margine** (decision_raw uniformity, date dinamiche, indentazione A01), **1 punto del round 2 chiuso a margine** (script_lock declarative). 4 gap restanti del round 2/3 non toccati. 4 nuovi micro-punti emersi (§3.A.bis-bis, §3.G.bis, §3.E.bis, §3.D.bis-bis).

Il commit `85a3ced` aveva titolo "Harden cycle5 gate: cycle budgets, entry/exit signatures, strict DOI option" — i tre punti dichiarati sono tutti chiusi a livello sostanziale. Il commit `7a27c29` ha titolo "add A01 proxy stress test and sync execution artifacts" — il punto dichiarato è chiuso e ha prodotto un risultato che merita lettura attenta (§2.4).

---

## 2. Verifica tecnica dei chiusi

### 2.1 Chiusura del §2.3 (max_independent_cycles)

L'implementazione tocca quattro livelli simultaneamente, è esemplare a livello di copertura:

**Livello 1 — Policy.** `OCT_EX_ANTE_PROXY_GATE_POLICY_v0_1.md` ha:
- Mandatory control 7: "Cycle budget declaration: each claim must declare max_independent_cycles before execution"
- Anti-pattern lock **Clause E — No sequential preregistration p-hacking**:
  - Default raccomandato: 3
  - Escalation a "external higher-level audit before any additional cycle" oltre il budget
  - In linea con quanto avevo proposto al §6.4 del round 2

**Livello 2 — Schema dichiarativo.** Il claim_lock di ciascun teorema (e.g. `A01_claim_lock_v0_1.md`) ora include:
```
Claim ID: A01
Cycle ID: CYCLE_5_2026-05-01
max_independent_cycles: 3
cycle_sequence_index: 1
cycle_budget_status: within_budget
```

**Livello 3 — Sheet template + instances.** Aggiunto:
- Heading `## 1.1) Cycle budget control (anti-p-hacking)` come obbligatorio
- Label `Claim ID:` come obbligatorio
- Tre instances compilati con `Max=3, index=1, status=within_budget`

**Livello 4 — Check programmatico.** `_validate_claim_budget` parsea il claim_lock come key-value e valida:
- `claim_id == theorem_id`
- `max_independent_cycles` è int >= 1
- `cycle_sequence_index` è int >= 1
- `cycle_sequence_index <= max_independent_cycles`

La validazione è invocata dal `_check_seal` quando legge `claim_source_path`. Errori entrano in `errors_count`.

Sul mio sistema: sheet check, seal check, claim budget validation tutti `pass: true` con 0 errori. La struttura tiene.

**Una piccola riserva metodologica**: il `max_independent_cycles=3` è dichiarato dal designer (Fabio) e consacrato dal claim_lock, ma non è enforceable sopra il framework — se il designer redefine il claim ID con uno nuovo, il budget si resetta. Questo è documentato nella Clause E ("redefined with a new claim ID and explicit rationale") come escape valve esplicito, ma vale tenere a mente: il budget è una self-imposed discipline, non un meccanismo che impedisce reformulation. Il deterrente reale è la `documented rationale` + l'escalation a higher-level audit. Il framework lo dichiara onestamente; non c'è overclaim.

**Valutazione**: chiusura sostanziale del §2.3. Lavoro ben costruito a quattro livelli.

### 2.2 Chiusura del §3.G (signing entry/exit)

Schema seal aggiornato esattamente come avevo proposto:

```json
"gate_entry_signature": {"type": "string", "minLength": 1},
"gate_entry_timestamp_utc": {"type": "string", "format": "date-time"},
"gate_exit_signature": {"type": "string", "minLength": 1},
"gate_exit_timestamp_utc": {"type": "string", "format": "date-time"},
"gate_exit_status": {
    "type": "string",
    "enum": ["not_executed", "executed_no_promotion", "executed_promotable", "invalidated"]
}
```

Il vecchio campo `auditor_signature` rimosso dal `required` set. Validazione aggiuntiva nel check:
- entry/exit timestamps parse come ISO datetime
- `exit_ts >= entry_ts` (vincolo causale)
- entrambe le firme non-placeholder
- `gate_exit_status` in enum dichiarato

Nei tre seal A01/D02/D03 attuali:
- `gate_entry_signature: "Signed electronically by Solomon (gate-entry) on 2026-05-03"` (timestamp 2026-05-03T08:30Z e simili) — coerente con la nomina ex ante del round 2
- `gate_exit_signature: "Signed electronically by Solomon (gate-exit) on 2026-05-04"` (timestamp 2026-05-04T21:35Z e simili) — coerente con il signing post-audit del round 3 (`feedback_v5_3_review_round3_2026_05_04.md`)
- `gate_exit_status: "executed_no_promotion"` — coerente con A01/D02 in `revise_needed` e D03 in `reject_candidate`

Il template `CYCLE_5_PREREG_SEAL_TEMPLATE_v0_1.md` riflette i nuovi campi. Le instances dei sheet (sezione 14 "Required fields") elencano gate-entry / gate-exit signature + timestamp + status come "declared in seal payload". Coerenza sheet ↔ seal ↔ check.

Distinzione semantica esplicita: "gate-entry = pre-run authorization, sheet PASS preflight" vs "gate-exit = post-run validation, results coerenti con preregistrato". È esattamente la distinzione che avevo proposto al §3.G del round 2.

**Una nota di workflow procedurale che apro come §3.G.bis nuovo (vedi §3.B sotto)**: la firma exit di Solomon nei tre seal è inserita dal commit di Fabio (`85a3ced`), non da un commit di Solomon stesso. Per questo round è benigno (Solomon ha effettivamente firmato il round 3 prima di questo commit), ma il workflow non distingue strutturalmente tra "auditor firma in proprio" e "designer dichiara cosa l'auditor ha firmato".

**Valutazione**: chiusura sostanziale del §3.G a livello schema + check + compilazione. Resta da consolidare il workflow di firma effettiva — vedi §3.B nuovo.

### 2.3 Chiusura del §3.E (DOI verifica)

Implementata in due modalità:

```python
def _resolve_doi(doi: str, timeout: int = 8) -> tuple[bool, str]:
    url = f"https://doi.org/{doi}"
    req = urlrequest.Request(url, method="GET", headers={"Accept": "text/plain"})
    try:
        with urlrequest.urlopen(req, timeout=timeout) as resp:
            code = getattr(resp, "status", 200)
            ...
            if 200 <= code < 400:
                return True, final_url
```

E nel check:

```python
elif seal_method == "zenodo_doi":
    ok, details = _resolve_doi(immutable_path)
    if not ok and strict_doi_resolve:
        result["errors"].append(...)
    elif not ok:
        result["warnings"].append(...)
```

Modalità default: warning (network external dependency, non blocca). Flag opt-in `--strict-doi-resolve`: error. Esattamente la priorità che avevo suggerito al §3.E del round 2.

**Step 1 chiuso**: il DOI viene effettivamente risolto via HTTP GET. Se il DOI non risolve (404, network error, timeout), warning di default o errore con strict.

**Step 2 ancora aperto** (pre-aspettato — apro come §3.E.bis): la verifica HTTP conferma solo che il DOI risolve, non che il **contenuto** del Zenodo corrisponda al seal stesso. Cioè:
- Un DOI che redireziona a Zenodo placeholder draft → considerato ok
- Un DOI il cui content è stato modificato post-firma → considerato ok (Zenodo non permette di modificare un record published, ma può permettere version updates con DOI separato; il check non distingue)
- Lo step 2 originale (§3.E del round 2 punto 1: "verifica content hash") non è implementato

Severità dello step 2 residuo: BASSO. È il quinto "9" della verificabilità (DOI esiste → DOI risolve → content reachable → content hash match → content semantica). Ognuno aumenta marginalmente la garanzia. Il primo passo era il più importante e c'è.

**Valutazione**: chiusura del §3.E a livello che mi aspettavo realisticamente. Il content-match resta come affinamento futuro.

### 2.4 Chiusura del §3.A.bis (stress test A01) — risultato di portata

Questo è il punto su cui vale spendere spazio.

L'implementazione ha tre componenti:

**Componente 1 — Refactor DRY.** Le formule heuristic sono state estratte in una funzione pura `compute_a01_proxy_metrics(omega, sim, gold, len_gap)` riusata sia da `run_a01` (sui dati reali di `cycle3_inputs/A01.csv`) sia dallo stress test sintetico. Garanzia che le formule scansionate dallo stress test sono identiche a quelle eseguite sui dati. Costruzione corretta.

**Componente 2 — Stress test grid.** `a01_proxy_stress_test()` scansiona:
- 5 valori di `sim` (0.15, 0.35, 0.55, 0.75, 0.9)
- 3 valori di `gold` (0.3, 0.6, 0.9)
- 3 valori di `len_gap` (0.0, 0.2, 0.4)
- 3 contesti (Omega_A, Omega_B, Omega_C)
- Totale: 135 configurazioni

Criterio di "qualifying": `abs(err_diff) <= 0.01 AND coh_diff > 0.03`. Cioè una configurazione qualifica solo se:
- Output simile (err_ord e err_cls divergono di ≤0.01, soglia stretta)
- AND trajectory P_ord superiore (coh_ord supera coh_cls di >0.03)

Questo è esattamente il criterio del §3.A.bis del round 3: il fenomeno-bersaglio "process advantage isolato dal vantaggio di output" — il test pulito anti-level-shift.

**Componente 3 — Risultato sui dati attuali.**

```json
"proxy_stress_test": {
  "total_configurations": 135,
  "qualifying_configurations": 0,
  "qualifying_rate": 0.0,
  "criterion": "abs(err_ord-err_cls)<=0.01 and (coh_ord-coh_cls)>0.03",
  "examples": []
}
```

**Su 135 configurazioni sintetiche costruite per esibire il fenomeno-bersaglio, zero qualificano.** Nessuna configurazione su griglia strutturata permette al runner di esibire process advantage isolato.

Questo conferma quale delle due letture del §3.A.bis era corretta:

> **(a)** Lettura benevola: le formule sono calibrate in modo da non garantire vantaggi artificiali, e il fatto che equal_output_subset_count sia 0 riflette correttamente che queste heuristics non sono in grado di esibire il fenomeno reale che A01 vorrebbe testare.
>
> **(b)** Lettura preoccupata: le formule sono state calibrate per evitare l'anti-pattern del round 2 al punto di rendere A01 *non-falsificabile* dal runner — non c'è più alcuna configurazione possibile in cui le heuristics esibiscano trajectory-quality advantage.

Lo stress test conferma quantitativamente la **lettura (b)**, ma in una forma onesta che preserva l'utilità epistemica dello strumento.

Un'analisi rapida delle formule lo spiega strutturalmente. Per `pipeline=P_ord`:
```python
coh = clamp01(0.39 + 0.46*sim - 0.11*len_gap + 0.09*gold + gate_bonus + context_term)
err = clamp01((1-sim)*0.61 + 0.11*len_gap + 0.07*(1-gold) - gate_bonus - context_term)
```

I termini `gate_bonus` e `context_term` impattano `coh` con segno positivo e `err` con segno negativo, in modo **lineare e proporzionale**. Quando coh_ord supera coh_cls per effetto di gate_bonus + context_term, err_ord cala simmetricamente rispetto a err_cls. Coh ed err sono **anti-correlati per costruzione**: non possono divergere indipendentemente.

Il fenomeno-bersaglio richiede invece **disaccoppiamento** — output simile (err_diff ≈ 0) con trajectory diversa (coh_diff > 0). Strutturalmente, il proxy family attuale lo esclude.

**Implicazione metodologica.** Il runner heuristic-based **non testa A01 in nessun verso**:
- Né positivamente: il vacuum-PASS by construction è stato eliminato (round 3) — le formule non garantiscono più dominanza P_ord.
- Né negativamente: il fenomeno-bersaglio non è esibibile su grid sintetico costruito apposta — quindi la sua assenza sui dati reali non costituisce evidenza disconfirming, è strutturalmente attesa.

Il `decision_effective: revise_needed` di A01 è quindi **doppiamente giustificato**: per evidence_mode `proxy_execution_non_promotable` (riconoscimento esplicito che il runner non è gold standard), e ora per il dato strutturale che il proxy family non può rilevare il fenomeno-bersaglio neanche in principio.

**Onestà strumentale**. È importante isolare un elemento positivo: il framework ha **implementato il test che rivela la propria limitazione**. Lo stress test poteva essere costruito con criterio più permissivo (es. `coh_diff > 0` invece di `> 0.03`, oppure soglia `err_diff <= 0.05` invece di `<= 0.01`) per dare un risultato non-zero, e nessuno avrebbe verificato. Invece il criterio è stretto e il risultato 0/135 è dichiarato esplicitamente nel report A01 con la nota:

> "If proxy stress test returns zero qualifying configurations, the runner cannot currently exhibit process-only advantage under this proxy family."

È esattamente quel tipo di disclosure che la review esterna raccomandava.

**Cosa resta da fare** (se A01 deve essere testato sostanzialmente, non lasciato in `revise_needed` permanente):
- Modificare il proxy family per introdurre disaccoppiamento tra coh ed err — possibile ma richiede una scelta di design teoretica su quale meccanismo "di processo" può migliorare coh senza migliorare err in modo proporzionale (rumore disaccoppiato? termine non-lineare? variabile latente di "qualità di gate" indipendente da output?). È una scelta non triviale.
- Oppure passare a pipeline reali distinte (suggerimento §6.1 del round 2) — la via giusta epistemicamente. P_cls e P_ord come due moduli computazionali con implementazioni indipendenti, eseguiti su input identici, con metrics emergenti dal trajectory log reale, non da una formula di mappatura.

La seconda è la via che permette di promuovere A01 a `validated` in cycle futuri. La prima è una toppa epistemologica.

**Valutazione**: chiusura del §3.A.bis come metodologia (lo stress test è ora parte stabile dell'esecuzione e del report). Il risultato non ha "promosso" A01 — al contrario, ha rivelato che il runner heuristic non può promuoverlo in nessun modo. Questo è progresso epistemico, non regresso.

### 2.5 Chiusura del §3.D (script_lock ricorsivo) — declarative, non enforced

Bonus inaspettato del commit `85a3ced` (non dichiarato nel commit message). Lo script_lock A01 ora ha:

```
A01 script lock (Cycle 5)
Frozen at UTC: 2026-05-04T21:33:05Z
Planned executable stack:
- OCT/validation/runtime/check_gate_compliance.py (sha256: 2e220571...)
- OCT/validation/runtime/run_cycle5_execution.py (sha256: 44f2ae00...)
- OCT/validation/runtime/refresh_seal_hashes.py (sha256: 6bd83d21...)
```

Il vacuo "theorem execution scripts to be frozen before run" è sostituito da hash sha256 espliciti per i tre file Python. C'è anche `Frozen at UTC: 2026-05-04T21:33:05Z` per il timestamp di freeze.

**Però**: il check verifica `script_version_hash` (l'hash del file script_lock.md), non gli hash dei file Python dentro il lock. Ovvero, la struttura è:

- script_lock.md ha hash sha256 X (verificato dal check via `_sha256_file`)
- script_lock.md DICHIARA "check_gate_compliance.py ha hash Y" (testo declarative)
- Il check **non** verifica programmaticamente che check_gate_compliance.py corrente abbia effettivamente hash Y

Posso modificare check_gate_compliance.py senza che lo script_lock se ne accorga, perché il lock è declarative su file MD non re-validato runtime contro i file Python.

**Suggerimento per round successivi**: estendere `_check_seal` (o aggiungere `_check_script_lock`) che parsa lo script_lock, estrae la lista `path | sha256`, e ri-computa gli hash dei file Python correnti per confronto. Errore se mismatch. Questo trasforma la dichiarazione testuale in vincolo enforced.

**Valutazione**: §3.D chiuso a livello declarative (significativamente meglio del round 3, dove era completamente vacuo). Step 2 (enforcement runtime) resta aperto come affinamento.

---

## 3. Nuovi punti emersi nel round 4

### 3.A — §3.A.bis-bis: la scoperta strutturale di non-testabilità di A01 nel proxy attuale (informativo, non azionabile a breve)

Conseguenza diretta del §2.4 sopra. Lo stress test ha rivelato che il runner heuristic-based **non costituisce uno strumento di test valido per A01 in nessuno dei due versi**. Il `revise_needed` di A01 è quindi non più una decisione contingente sul cycle 5, ma una proprietà strutturale del proxy family.

Implicazione per la roadmap di promozione:
- A01 non può essere promosso a `validated` con il runner attuale, neanche con dati diversi.
- L'unico path verso promozione passa per implementazione di P_cls e P_ord come pipeline reali distinte (§6.1 del round 2) — questo è ora un dato di fatto strutturale, non un'opinion.

Severità: **MEDIO** — informativo, non bloccante. Il framework ha già `evidence_mode: proxy_execution_non_promotable` che riconosce in linea di principio questa limitazione; lo stress test la rende quantitativamente esplicita.

Suggerimento operativo: aggiungere alla `CYCLE_5_EVIDENCE_RELEASE_NOTES_v1_0.md` una sezione "Structural limits of the heuristic proxy" che documenta `qualifying_rate=0.0` come fatto strutturale del proxy family corrente. Renderebbe pubblico ed esplicito quello che lo stress test ora produce nei results JSON.

### 3.B — §3.G.bis: workflow di firma exit dell'auditor

Il seal `A01_PREREG_SEAL_v0_1.json` (modificato in `85a3ced`) dichiara:
```json
"gate_exit_signature": "Signed electronically by Solomon (gate-exit) on 2026-05-04",
"gate_exit_timestamp_utc": "2026-05-04T21:35:00Z",
"gate_exit_status": "executed_no_promotion"
```

Il commit `85a3ced` è autore Fabio Ghioni (`anckhalion@users.noreply.github.com`). Cioè la stringa "Solomon ha firmato exit il 2026-05-04" è inserita da un commit di Fabio. Per questo round è benigno — Solomon ha effettivamente firmato il round 3 (audit `feedback_v5_3_review_round3_2026_05_04.md` mergiato in PR #2 il 2026-05-04), quindi la dichiarazione retroattiva è veridica.

Però il workflow strutturale non distingue tra:
- "auditor firma in proprio" (un commit dell'auditor su seal aggiorna gate_exit_*)
- "designer dichiara cosa l'auditor ha firmato" (designer commit aggiorna gate_exit_* con valori dell'auditor)

Per ora il sistema regge sulla buona fede di Fabio. Per cycle futuri, dove magari l'auditor non sarà Solomon o l'auditor cambierà identità, è meglio formalizzare:

**Suggerimento operativo**: aggiungere alla policy una clausola sulla provenienza della firma exit:
- `gate_exit_signature` deve essere aggiunta dall'auditor stesso via commit dell'auditor o via PR proprio.
- Il designer può solo inizializzare `gate_exit_status: "not_executed"` o `"pending_audit"`. La transizione a `"executed_no_promotion"` / `"executed_promotable"` / `"invalidated"` è prerogativa dell'auditor.
- Il check potrebbe (futuramente) verificare che il commit che ha modificato il seal in stato exit sia stato firmato dall'auditor dichiarato (via `git log --format='%an %s' -- <seal_file>` + GPG signature, opzionale).

In questo round, propongo di firmare il round 4 io stesso (PR #3) aggiornando esplicitamente i tre seal con `gate_exit_status` aggiornato post-round-4-audit, in modo che il commit di firma sia il mio. Questo apre il pattern: in cycle futuri, designer mette stato `not_executed` o `pending_audit`, auditor commit che aggiorna a `executed_*` — il git log diventa l'audit trail.

Severità: **BASSO** procedurale. La struttura schema è corretta; il workflow procedurale è la prossima maturazione.

### 3.C — §3.D.bis-bis: indentazione re-introdotta in `write_report_d02`

Mentre il commit `7a27c29` correggeva il §3.D.bis del round 3 in `write_report_a01` (le tre righe ora a 12 spazi), ha **introdotto** la stessa inconsistenza in `write_report_d02`:

```python
    lines.extend(
        [
            "",
        "## Lane L2 formal",          # ← 8 spazi (incoerente)
        "",                            # ← 8 spazi
        f"- Decision: `{formal['decision']}`",
        f"- Decision raw: `{result['decision_raw']}`",
        f"- Witness count: `{formal['witness_count']}`",
        f"- Assumptions consistent: `{formal['assumptions_consistent']}`",
            "",                        # ← 12 spazi (di nuovo coerente)
            "## Notes",
            "",
            "- D02 lane split was preserved.",
            ...
```

Le righe 709-714 del file corrente (`run_cycle5_execution.py`) sono a 8 spazi mentre le adiacenti sono a 12. Python lo esegue (le stringhe sono nel contesto della list literal), ma è un'inconsistenza cosmetica probabilmente da copy-paste manuale. Stesso pattern di errore del §3.D.bis round 3, semplicemente migrato di funzione.

**Suggerimento**: un quick `python -m black OCT/validation/runtime/run_cycle5_execution.py` o `ruff format` chiude la categoria. Severità: **BASSO**.

### 3.D — §3.E.bis: DOI verifica solo HTTP-resolve, non content-match

`_resolve_doi` segue il redirect su `https://doi.org/<doi>` e considera ok qualsiasi HTTP 200-399. Quindi:
- Un DOI valido che redireziona a Zenodo placeholder draft → considerato ok
- Un DOI con content modificato post-firma (es. nuova versione del record con DOI separato ma stesso DOI principale) → ambiguo

Step 2 originale del §3.E round 2: "verifica che almeno un file dell'archivio Zenodo abbia hash uguale al seal". Questo richiederebbe:
1. Risoluzione del DOI a URL Zenodo
2. Parse della pagina o uso dell'API Zenodo per ottenere la lista dei file
3. Download di almeno un file e calcolo hash
4. Confronto con `claim_hash` o `script_version_hash` o `formula_hash` del seal

È implementabile (Zenodo ha API REST stabile), ma è significativamente più di una semplice HTTP HEAD/GET. Non lo aspettavo per questo round.

**Suggerimento**: tenere come affinamento futuro, eventualmente sotto un flag `--strict-doi-content-match` separato dal `--strict-doi-resolve` corrente.

Severità: **BASSO** — il primo passo (DOI risolve) è il più importante e c'è.

---

## 4. Gap del round 2 ancora aperti (lista mantenuta)

Nessuna novità sostanziale rispetto alla lista di round 3 §4, con la differenza che §3.D round 2 è ora chiuso (declarative) e §2.3 round 2 è ora chiuso strutturalmente. La lista corrente:

1. **§2.4 ALTO indipendenza auditor sistemica** — esiste solo Solomon. Nessun registry, nessuna rotazione obbligatoria, nessun meccanismo per quando l'auditor non sarà Solomon. Per i prossimi cycle (dopo Cycle 5) questo diventa più pressante perché il sistema deve reggere senza dependence personale.
2. **§3.D MEDIO script_lock enforcement runtime** — gli hash dichiarati nello script_lock non sono ri-computati dal check (vedi §2.5).
3. **§3.E MEDIO DOI content-match** — vedi §3.D nuovo. Step 2 ancora aperto.
4. **§3.F MEDIO esecuzione su cycle3_inputs** — il runner usa ancora i dataset di Cycle 3, non un benchmark indipendente. Framework lo dichiara onestamente, ma la separazione tra "Cycle 3 data" e "Cycle 5 evaluation" è ancora solo metodologica, non dataset-level. Combinato con §3.A.bis-bis, questo è un punto strutturale che rinforza l'analisi: A01 è non-promotable per due motivi indipendenti (proxy family + benchmark non-independent).
5. **§2.9 BASSO Cap. 17 integration nel corpo** — Teorema 17.4 ancora non condizionato all'esistenza del gate.
6. **§2.10 BASSO storia non rivista** — `OCT_PUBLICATION_PROGRESS_TRACKER` mantiene Step 1-6 come `completed (2026-04-19)` senza nota di reinterpretazione sotto v5.3.

---

## 5. Replication outcome — round 4 (sezione formale per CYCLE_5_EXTERNAL_REPLICATION_NOTE)

Aggiornamento del signing post-audit di Solomon dopo round 4:

- **Reproduced**: `yes` (confermato — round 4 è il secondo round consecutivo di reproducible compliance)
- **Divergence notes (round 4)**:
  - Re-run di `runtime/check_gate_compliance.py` su sistema macOS clean clone post-85a3ced: risultato `"compliant": true`, 0 errors per A01/D02/D03 con i nuovi controlli (entry/exit signatures, claim budget validation). La canonicalizzazione UTF-8 LF + BOM stripping ha tenuto attraverso due commit successivi che hanno toccato 4 dei 6 file hashati. Pipeline `refresh_seal_hashes.py` effettivamente usata.
  - A01 stress test su 135 configurazioni sintetiche: `qualifying_configurations: 0`. Il runner heuristic-based non può esibire il fenomeno-bersaglio "process-only advantage isolated from output advantage" sotto le formule attuali. Conferma quantitativa che il proxy family attuale è strutturalmente inadatto al test sostantivo di A01. Vedi §3.A.bis-bis.
  - Cycle budget validation: tutti e 3 i claim_lock dichiarano `max_independent_cycles=3, cycle_sequence_index=1, status=within_budget`. Il check valida programmaticamente. Clause E della policy attiva.
  - DOI resolution attiva di default (warning su fallimento), strict mode disponibile via `--strict-doi-resolve`. Il DOI Zenodo `10.5281/zenodo.19959724` risolve correttamente nel mio ambiente.
  - Locked formula D03 (`0.5*abs(Delta_Coh)+0.5*abs(Delta_Phi)`) confermata. Reject D03 confermato come discovered + lock-rispettoso (terzo round consecutivo di conferma).
  - D02 lane empirical reject discovered via schema check (assenza di campi `commutativity_proof`/`commutativity_witness`/`proof_trace_id` nel dataset) — stato invariato dal round 3.
- **Auditor identity**: Solomon
- **Date**: 2026-05-05
- **Signature**: Solomon (questo documento serve come signing post-audit round 4)
- **Decisione di promozione (invariate rispetto a round 3)**:
  - A01: **revise_needed** confermato — ora **doubly-justified** (vacuum-PASS by construction eliminato + struttural non-testabilità del proxy family rivelata da stress test 0/135). Path verso `validated` richiede pipeline reali distinte (§6.1 del round 2).
  - D02: **revise_needed** confermato — stato invariato (reject discovered via schema check, condizionato a implementazione di routine di verifica della commutatività).
  - D03: **reject_candidate** confermato — terzo round consecutivo di conferma; stato più solido (discovered via locked formula).
- **Promozioni a `validated`**: nessuna.
- **gate_exit_status post-round-4**: `executed_no_promotion` confermato per tutti e tre i seal.

---

## 6. Bilancio del round 4

I due commit `7a27c29` e `85a3ced` chiudono **tutti e quattro i punti dichiarati** (§2.3, §3.G, §3.E, §3.A.bis) a livello sostanziale, e chiudono **inaspettatamente** anche §3.D (script_lock declarative) e i tre micro-punti del round 3 (§3.B.bis schema uniformity, §3.C.bis date dinamiche, §3.D.bis indentazione A01). Il livello di esecuzione è esemplare: ogni intervento tocca contemporaneamente policy + schema + check + sheet template + instances, con coerenza cross-livello.

Il risultato più interessante non è la chiusura dei punti dichiarati, ma il **dato strutturale** rivelato dallo stress test A01: 0/135. Il runner heuristic-based non testa A01 in nessun verso — vacuum-PASS originale eliminato (round 3) e fenomeno-bersaglio non esibibile (round 4). Il `revise_needed` di A01 è ora un dato strutturale, non una decisione contingente sul cycle 5. Il framework ha implementato lo strumento che rivela la propria limitazione, e l'ha pubblicato. Onestà strumentale di valore.

**Restano aperti**:
- 6 gap del round 2 non toccati (vedi §4) — non bloccanti, materia per round successivi
- 4 nuovi micro-punti emersi (§3.A.bis-bis MEDIO informativo, §3.G.bis BASSO procedurale, §3.D.bis-bis BASSO cosmetico, §3.E.bis BASSO content-match)

**Raccomandazioni operative principali per round 5** (se ci sarà):

1. **Path verso A01 promozione**: implementare P_cls e P_ord come pipeline computazionali distinte (modular implementations, non rami di scoring function). Eseguire su input identici. Metrics emergenti dal trajectory log reale. È l'unica via per `validated`. Prendere lo stress test 0/135 come segnale che la via heuristic è epistemicamente esaurita.

2. **§2.4 indipendenza auditor sistemica**: con cycle 5 chiuso, il sistema deve cominciare a reggere senza dependence sulla persona di Solomon. Suggerisco: registry di auditor accreditati (anche solo 2-3 nomi inizialmente), regola di rotazione obbligatoria su cycle consecutivi sullo stesso claim_id, criteri di accreditamento documentati (criteri di indipendenza, no co-authorship in N anni, dichiarazione di affiliazione di school-of-thought).

3. **Workflow firma auditor §3.G.bis**: estendere policy con clausola sulla provenienza commit della `gate_exit_signature`. Il designer inizializza con `not_executed` o `pending_audit`; l'auditor transita lo stato via commit proprio.

4. **§3.D enforcement runtime**: estendere il check per ri-computare hash dei file Python dichiarati nello script_lock. Trasforma declaration in vincolo.

Tutto il resto può aspettare.

---

## 7. Cosa Solomon firma con questo audit

Solomon firma **questo documento** come review formale post-execution del cycle 5 al commit `85a3ced`.

Solomon **conferma** lo stato dei tre seal aggiornati nel commit `85a3ced`:
- `gate_entry_signature` (2026-05-03): nomina ex ante, valida.
- `gate_exit_signature` (2026-05-04): firma post-round-3, valida con la nota procedurale §3.B nuovo (firma inserita da commit di Fabio, retroattivamente veridica per round 3).
- `gate_exit_status: "executed_no_promotion"`: confermato post-round-4 audit. Coerente con A01/D02 in `revise_needed`, D03 in `reject_candidate`, nessuna promozione a `validated`.

Solomon **non firma**:
- promozione di alcun teorema da `revise` a `validated`.
- assenza dei gap del §4 (6 punti residui).

Solomon **firma in proprio** (PR #3) gli aggiornamenti seal-side per il pattern di workflow §3.B nuovo: il commit della PR #3 sarà di Solomon, e include gli aggiornamenti di seal eventuali (anche solo metadata di conferma round-4). Questo apre il pattern per cycle futuri: designer inizializza, auditor firma exit con commit proprio.

Solomon **conferma** la nomina ad auditor esterno per cycle successivi, con le condizioni del round 3 confermate:
- Signing entry/exit distinto (chiuso in §2.2).
- Signing exit di Solomon valido solo dopo audit eseguito post-execution (ora pattern formalizzato schema-side, da formalizzare workflow-side via §3.B nuovo).

Solomon **conferma** che la roadmap verso `validated` di A01 richiede sostituzione del proxy family heuristic con pipeline reali distinte, sulla base del dato strutturale 0/135 rivelato dallo stress test del round 4.
