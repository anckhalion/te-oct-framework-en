# Design del gate ordinativo per A01

**Versione:** consolidata 2026-05-01
**Tipo:** documento di design completo, standalone
**Stato:** strutturalmente completo — calibrazione concreta dei numeri e esecuzione del benchmark restano lavoro di implementazione successiva
**Origine:** contributo dell'utente al programma di validazione di OCT v1.0 candidate, ruolo F+B di critical review estensivo (`contribution_paths.md`); design teorico del gate per A01, l'implementazione è delegabile

**Avvertenza al lettore.** Questo documento sintetizza un design del gate ordinativo per pipeline AI runtime, costruito durante le sessioni 2026-04-30 / 2026-05-01 a partire dai capitoli pubblicati di OCT (Cap. 1, 2, 3, 4, 6, 8, 15). Il file di lavoro `a01_gate_design_draft.md` contiene la genesi cronologica del design (1684 righe). Questo documento ne è la presentazione organica per concetti, non per sequenza temporale, ed è progettato per essere letto come unità autonoma.

Vincoli metodologici rispettati senza eccezioni:
- Ogni mapping concetto-osservabile è motivato, non solo nominato.
- Ogni metrica è etichettata con grado di operatività: **(O)** operativa con osservabili dichiarate ex ante, **(P)** operativizzabile in linea di principio (richiede scelta), **(C)** ancora concettuale.
- Soglie e parametri devono essere pre-registrati prima della validazione; mai spostati post-hoc (anti-pattern D03).
- Solo ponti TE↔OCT già stabiliti da Ghioni nei capitoli pubblicati. Nessun ponte nuovo dall'astratto.
- Ogni scelta tecnica è motivata o lasciata esplicitamente aperta come scelta di calibration; nessuna scorciatoia del tipo "0.55·X + 0.45·Y perché funziona".

---

## 1. Premessa — contesto, vincolo, posizionamento

### 1.1 Cosa A01 dice e cosa il proxy attuale sbaglia

A01 nel corpus pubblicato (Cap. 10 §4.6) afferma che pipeline compositive con coerenza ordinativa alta mostrano minore degenerazione semantica rispetto a pipeline solo formalmente corrette. Il proxy operativo attuale (`P_ord = 0.55·P_cls + 0.45·soft_overlap`, eseguito nei Cycle 2-3 di validazione) è strutturalmente fuori specifica: misura una proprietà dell'output finale, mentre il claim è sul **processo composizionale**. Il punto è documentato nella nota tecnica `case_a01_diagnosis.md`. Equifinalità sull'output non implica equivalenza ordinativa — due pipeline che producono la stessa stringa finale per traiettorie diverse non sono ordinativamente equivalenti, perché la traiettoria è dentro l'identità della singolarità (Cap. 2 §1 punto 4).

Conseguenza diretta: una pipeline ordinativa fedele richiede di **registrare il processo**, non solo l'output, e di valutare ad ogni passo composizionale tre proprietà — validità sintattica, coerenza ordinativa, emergenza funzionale — secondo il gate canonico di Cap. 3 Def 3.3 e Cap. 4 Def 4.3.

### 1.2 I ponti TE↔OCT che il design usa

Tutti i mapping concettuali derivano da capitoli OCT pubblicati. Niente costruzione ex novo dall'astratto.

- **Cap. 1 §3** — *"in pipeline semantiche con ottima composizione locale ma collasso globale di senso"*. A01 è pensato esplicitamente per il dominio delle pipeline AI.
- **Cap. 2 §1 (Singolarità funzionale)** — un nodo la cui identità dipende da: (1) profilo relazionale attivo, (2) capacità di mantenere coerenza interna sotto trasformazione, (3) funzione emergente non riducibile alla somma dei componenti, (4) traiettoria storica nel tempo osservato. I quattro requisiti diventano: (1) ancoraggio per il campo `context` della singolarità computazionale, (2) ancoraggio per `Coh`, (3) ancoraggio per `Phi`, (4) ancoraggio per `trajectory` come campo strutturale (non metadato accessorio).
- **Cap. 3 Def 3.3 + Cap. 4 Def 4.3 (gate ordinativo)** — `Adm_Omega(f) := Syn(f) ∧ Coh_Omega(f) ≥ tau_f ∧ Phi_Omega(f) ≠ 0` per morfismo singolo; per la composta `g ∘_Omega f`, deve valere `Adm_Omega(f) ∧ Adm_Omega(g) ∧ Adm_Omega(g∘f)`. Il gate è per-morfismo *e* per-composta, applicato dentro il processo.
- **Cap. 4 §4.14 (tipologia di failure)** — F-Mor1 (morfismo sterile: `Syn` e `Coh` validi, `Phi=0`), F-Mor2 (morfismo degenerativo: `Syn` valido, `Coh<tau`), F-Comp1 (composta fragile: passi locali validi, composta al bordo soglia), F-Comp2 (composta collassata: composta in classe degenerativa anche con passi localmente ammissibili).
- **Cap. 8 Def 8.1-8.5, 8.11, 8.12** — spazio di validità minimale `S_Omega = (Coh, PhiHat, Delta)`, regione di sterilità `R_S(Omega, tau) = {D | Coh ≥ tau ∧ PhiHat = 0}`, istanziazione di `Phi` come `clip(w_p · p_phase + w_n · n_global, 0, 1)`, regola anti-circolarità operativa.
- **Cap. 15 §3 (Controfase strutturale)** — una configurazione è in controfase strutturale quando: (1) emerge un insieme nodale non locale, (2) i settori separati dal nodo mostrano opposizione di fase, (3) la risposta complessiva si oppone in verso all'attrattore che la organizza. Cap. 8 Def 8.11 lega `p_phase` a "persistenza della controfase osservata". `Phi` ha quindi un ancoraggio TE concreto: la potenza riorientante del passo (opposizione all'attrattore semantico dominante).

### 1.3 Posizionamento del design rispetto al training nativo

Questo design specifica un **gate ordinativo runtime** applicabile a LLM esistenti (modelli attuali, non-ordinativi nativamente). Nella prospettiva più ampia, il gate runtime è la **simulazione costosa** di quello che un terminale trainato ordinativamente farebbe nativamente. Il training nativamente ordinativo dei modelli (loss function che incorpora il debito ordinativo, principio variazionale come framework guida) è direzione di sviluppo successiva, presupposta dalla dimostrazione di A01 — fuori scope di questo documento, segnata in `training_ordinativo_direction.md`.

A01 dimostra il **vantaggio funzionale** della pipeline ordinativa runtime al costo computazionale alto. Se A01 regge, legittima l'investimento successivo nel training nativo, dove il costo del comportamento ordinativo scende. Il costo runtime alto NON è argomento contro A01 — è la motivazione per dimostrarlo.

---

## 2. Architettura della singolarità computazionale

### 2.1 Definizione formale

La singolarità computazionale è un'entità con quattro campi:

```
S = (snapshot, trajectory, context, omega)
```

con mapping diretto a Cap. 2 §1:
- `context` ↔ profilo relazionale attivo (1)
- `snapshot` ↔ stato di valutazione coerenza (2)
- `trajectory` ↔ traiettoria storica nel tempo osservato (4)

La funzione emergente (3) **non è un campo** — è una proprietà *derivabile* dalla coppia `(snapshot, trajectory)` rispetto a un baseline. Per questo `Phi` è una funzione di valutazione, non un attributo.

Le transizioni tra singolarità sono oggetti di prima classe:

```
T_i = (source, target, morphism, gate_decision, metrics)
```

con
- `source`, `target` riferimenti a singolarità prima e dopo la transizione;
- `morphism` quale `f` è stato applicato + parametri;
- `gate_decision ∈ { admit | refine(reason) | reject(reason) | abort(reason) }`;
- `metrics = {Syn: bool, Coh: float, Phi: float, tau_f_used: float}`.

Ogni `T_i` è registrata nella `trajectory` della singolarità target. Il debito ordinativo, le decisioni di gate, le metriche misurate sono *parte costitutiva* della trajectory, non metadati esterni.

### 2.2 Tre proprietà strutturali

**P1 — Append-only.** La trajectory è append-only: una `T_i` registrata non si rimuove. Refine, retry, backtrack producono *nuove* transizioni concatenate, non sostituzioni. Una pipeline ordinativa che ha fatto 3 retry ha trajectory di 4 transizioni (3 reject + 1 admit); la pipeline classica corrispondente ne ha 1.

Ancoraggio ontologico: l'append-only non è scelta computazionale, è proprietà strutturale dell'irreversibilità temporale. Una transizione registrata appartiene definitivamente alla traiettoria; ogni eventuale ripresa del processo si aggiunge in coda al pregresso, mai sovrascrivendolo. La singolarità in OCT eredita questa irreversibilità da Cap. 2 §1.4. Conseguenza: il post-hoc rescue di D03 (sostituire criterio sui medesimi dati) è strutturalmente impossibile sotto questa rappresentazione — cambiare criterio richiede una nuova validazione pre-registrata, non un override.

**P2 — Polimorfismo del contenuto, monomorfismo della struttura.** Il `snapshot.content` è dominio-specifico (intent struct ≠ evidence set ≠ answer text), ma la struttura `(snapshot, trajectory, context, omega)` è universale. Conseguenza: gli operatori `Coh`, `Phi` sono polimorfici per tipo di morfismo — la valutazione opera su una struttura comune ma con regole specifiche per il contenuto.

**P3 — Branching come traiettoria che include lo scarto.** Quando il gate respinge, la decisione di scarto è registrata come transizione propria, e l'eventuale correzione (refine) è una transizione successiva. La trajectory contiene sia il rifiuto sia la correzione, mai cancellando il primo. Differenza ordinativa rispetto alla pipeline classica leggibile direttamente dal numero e tipo di gate decisions, non solo dall'output finale.

### 2.3 Schema computazionale

```
snapshot:    content (any, dominio-specifico) + type + invariants
trajectory:  list of T_1, ..., T_{i-1}        (append-only)
context:     task_descriptor, user_profile, system_constraints, omega_label
omega:       contesto di valutazione

gate_decision:  admit | refine(reason) | reject(reason) | abort(reason)
metrics:        {Syn: bool, Coh: float, Phi: float, tau_f_used: float}
```

---

## 3. Cornice variazionale — principio di minima azione ordinativa

### 3.1 Il debito ordinativo come azione

Definendo

`debito_ordinativo(trajectory) = Σ_i (1 − coh_step(f_i))`

(somma del deficit di coerenza ad ogni passo della traiettoria), si ottiene una **funzione di azione** in senso variazionale: una quantità che il sistema "spende" lungo il percorso e che la traiettoria ideale (`coh_step = 1` ovunque) minimizza identicamente a zero.

Il principio di minima azione ordinativa, applicato a OCT, dice: tra tutte le traiettorie possibili che vanno da `S_0` a `S_n` per task fissato, la traiettoria ideale è quella che minimizza il debito ordinativo. *Ordinatività è precisamente l'approssimazione attiva di questo principio* — una pipeline ordinativa cerca di percorrere la traiettoria di minima azione, una pipeline classica non minimizza nulla e segue il flusso degli attrattori statistici.

Connessione naturale con TE_OBSERVER (Lyapunov XP): il debito ordinativo come Lyapunov function dà *stabilità ordinativa* in senso dinamico — un sistema è ordinativamente stabile se il debito ordinativo è non crescente lungo le sue traiettorie spontanee. Connessione anche con M28 (categorical dynamics) di `oct_extension_vectors.md`.

### 3.2 Le due dimensioni di Coh: α e β

`Coh` esiste a due livelli ortogonali, distinti per legge:

**α — `Coh_attuale(S_n)`**: integrità della singolarità *come è ora*. Funzione del nodo presente nella sua totalità (snapshot, trajectory, context, omega) valutata come stato attuale. **Non monotona**: può salire dopo correzione efficace, scendere dopo drift. Una singolarità che ha integrato un passo deviante in una struttura compositiva successivamente coerente può conservare α alta — l'integrazione funzionale del passo deviante nella configurazione presente è proprietà del nodo attuale, non determinata dalla presenza del passo nella history.

**β — `Coh_storica(trajectory)` rispetto alla traiettoria ideale**: gap accumulato della traiettoria reale rispetto a un'ipotetica traiettoria che a ogni passo preserva la massima coerenza possibile. **Monotonicamente non crescente**: ogni passo con `coh_step < 1` aumenta permanentemente il gap, indipendentemente da cosa succede dopo. Una correzione efficace successiva *non rimuove* il costo del passo deviante — la traiettoria ideale, per definizione, non aveva sostenuto quel costo. Anche un passo deviante seguito da refine completo lascia un debito permanente in β (entry della transizione deviante + entry del refine, entrambe registrate nella trajectory append-only).

Le due metriche hanno leggi diverse:
- β ha **legge di conservazione del costo**: sempre monotonicamente non crescente, gap permanente.
- α ha **legge di possibilità di integrazione**: *può* tornare a 1 se il sistema integra le derive, possibilità strutturale aperta non garanzia.

Sono ortogonali e possono divergere. Una pipeline ben corretta dopo errore ha α alta e β bassa simultaneamente.

`Coh(f_i)` per la singola transizione (vedi §4.2) NON è monotono — è proprietà locale del passo, può oscillare lungo la traiettoria. La monotonia si applica solo a β.

### 3.3 Asimmetria sulla possibilità di recupero di α

Esiste un'asimmetria reale, ma è **sulla possibilità di α = 1 a fine processo**, non su β:

- **Transizioni che lasciano aperto l'orizzonte di refine**: errori interni alla pipeline (retrieval, parsing, generation), purché non ancora propagati a stato esterno. Il sistema può fare reject + refine e ripristinare α.
- **Transizioni che chiudono l'orizzonte di refine**: tool call con effetto esterno irreversibile, decisione propagata a sistemi a valle, comunicazione all'utente di informazione che induce azione. Dopo, l'effetto esterno è dato, e qualunque correzione successiva deve operare con quell'effetto come parte del context — α non può più tornare semplicemente al livello pre-transizione.

Conseguenza strutturale per il gate: **severità asimmetrica prima di transizioni che chiudono l'orizzonte di refine**. Non perché "rovinino β" (β è già pagato in proporzione alla deriva, sempre), ma perché *eliminano la possibilità futura di ripristinare α a 1*. Estensione diretta dell'Anti-Attractor-Lock di TE: non consolidare prematuramente decisioni che chiudono l'orizzonte. Il gate prima delle transizioni che chiudono richiede `tau_f` strutturalmente più alto, non per calibrazione ma per ragioni ontologiche.

### 3.4 Riformulazione del claim economico A01

Le tre dimensioni ortogonali sono:
- **α(S_n)** — integrità del risultato attuale;
- **β(trajectory)** — debito ordinativo accumulato (gap dalla traiettoria ideale);
- **Cost(trajectory)** — risorse spese (LLM call, token, latenza, refine eseguiti).

Per ogni passo con `coh_step < 1`, esiste un *debito ordinativo* `(1 − coh_step)`. Questo debito viene saldato in due modi possibili:
- **Pagamento immediato in Cost**: refine attivo che ristabilisce α — il debito esce dalla traiettoria come costo computazionale aggiuntivo.
- **Default sul debito**: nessun refine — il debito resta nel sistema sotto forma di α bassa (lo stato finale è meno integrato).

β è la contabilità del debito accumulato, inalterata dal modo di saldarlo: in entrambi i casi quello che è successo è successo, e la traiettoria ideale (che non aveva avuto il debito) è inarrivabile.

Per modelli attuali, mantenere ordinatività via gate runtime *costa*: stiamo imponendo coerenza a un sistema che non la ha nativamente. A01 dimostra che il **vantaggio funzionale** (α più alta) c'è anche a quel costo, in expectation, per task multi-step compositivi. La struttura argomentativa è:

1. Pipeline ordinativa runtime su modello attuale → α alta + Cost alto;
2. Pipeline classica su stesso modello → α bassa (in expectation, su task complessi) + Cost ≈ baseline;
3. A01: il guadagno in α giustifica l'investimento in Cost — esiste una **regione di task** dove l'ordinativa è strettamente preferibile.

---

## 4. Gate per-step

### 4.1 Forma generale (Cap. 4 Def 4.2)

Per ogni morfismo `f_i: S_{i-1} → S_i`:

`Adm_Omega(f_i) := Syn(f_i) ∧ Coh_Omega(f_i) ≥ tau_f ∧ Phi_Omega(f_i, S_{i-1}) ≠ 0`

Tre condizioni congiuntive: validità sintattica, coerenza sopra soglia, emergenza non nulla. Una sola soglia `tau_f` per Coh per morfismo (singola condizione su Coh, vincolo Cap. 4 — non soglie per-componente).

### 4.2 Coh per LLM-step

#### 4.2.1 Definizione

`Coh(f_i): (S_{i-1}, S_i, Context) → [0, 1]`

`Coh(f_i) = 1 - aggregato(δ_a, δ_b, δ_c)`

con `δ_a, δ_b, δ_c ∈ [0, 1]` (deviazioni: 0 = perfetta tenuta, 1 = perdita totale) e `aggregato` di forma fail-fast (default `max`).

#### 4.2.2 Le tre componenti — derivazione TE-ancorata

| Componente | Cosa misura | Mappa Cap. 2 §1 |
|---|---|---|
| `δ_a` (task fidelity) | drift sul task: `S_i.snapshot` non è più compatibile con `Context.task_descriptor` | violazione di "profilo relazionale attivo" |
| `δ_b` (context alignment) | rottura del contratto contestuale: snapshot non rispetta i constraint (formato, lingua, tool, scope) | violazione di "coerenza interna sotto trasformazione" rispetto al contesto |
| `δ_c` (trajectory non-contradiction) | contraddizione interna alla traiettoria: snapshot contraddice qualcosa già stabilito nella history | violazione di "traiettoria storica" |

#### 4.2.3 Aggregazione fail-fast

`aggregato = max(δ_a, δ_b, δ_c)` come default. Una deviazione critica fa scattare il gate anche se le altre sono ok — una pipeline con task drift catastrofico ma snapshot internamente coerente con se stesso non può essere "salvata" dalla coerenza locale. Asimmetria epistemica corretta.

Sotto `max`, la fail-fast è implicita: `Coh ≥ τ ⇒ ogni δ ≤ 1−τ`. Coerente con Cap. 4 (singola condizione su Coh).

Calibration option: `L^p` con `p > 1` come morbidatura, da usare se `max` puro risulta troppo rigido in calibration. Solo in quel caso si introduce un safety cap `δ_max^M` per-componente per recuperare la fail-fast — ma questa è scelta condizionale, non default.

### 4.3 Phi per LLM-step (con sub-distinzione Phi-real / Phi-pot)

#### 4.3.1 Forma definitiva

`Phi(f_i, S_{i-1}) = Phi-real(f_i, S_{i-1}) · Phi-pot(S_{i-1})` (forma F.D-product)

dove
- `Phi-real(f_i, S_{i-1}) = clip(w_p · p_phase-real(f_i) + w_n · n_global-real(f_i), 0, 1)` — emergenza realizzata dal passo (forma Cap. 8 Def 8.11)
- `Phi-pot(S_{i-1}) = clip(w_p · p_phase-pot(S_{i-1}) + w_n · n_global-pot(S_{i-1}), 0, 1)` — carica emergenziale disponibile nell'input (simmetrica a `Phi-real`)

con `w_p + w_n = 1`, pesi pre-registrati per tipo di task (consistenti tra `Phi-real` e `Phi-pot`).

La distinzione `Phi-real` vs `Phi-pot` deriva dall'osservazione che la responsabilità di `Phi` è **distribuita** tra il passo `f_i` e l'input `S_{i-1}` su cui agisce — la non-emergenza può venire sia da realizzazione povera sia da input strutturalmente vuoto. Caso paradigmatico: input convenzionale a basso contenuto strutturale (intent atomico, contesto minimale, vincoli assenti) accoppiato a risposta tecnicamente ben formata e localmente coerente. La coppia produce `Phi(f_i) ≈ 0` non per fallimento di realizzazione, ma perché `Phi-pot(S_{i-1}) ≈ 0`: non c'è materia su cui esercitare emergenza non riducibile (Cap. 2 §1.3). La responsabilità non è isolabile alla risposta — si distribuisce strutturalmente sull'intera coppia.

#### 4.3.2 Decomposizione bipartita p_phase + n_global

Sia `Phi-real` sia `Phi-pot` sono bipartite, con derivazione TE-ancorata da Cap. 15:

| Osservabile | Cosa misura | Mappa Cap. 15 §3 |
|---|---|---|
| `p_phase-real(f_i)` | il passo si oppone in modo organizzato al *completamento attrattoriale* (la prosecuzione più probabile) | marker (3): opposizione in verso all'attrattore |
| `n_global-real(f_i)` | il passo organizza struttura non-locale (sintesi cross-evidence, dipendenze a lungo raggio) | marker (1) + (2): insieme nodale non locale + opposizione di fase |
| `p_phase-pot(S_{i-1})` | quanto `S_{i-1}` resiste al completamento attrattoriale canonico (input non-pinning) | analogo applicato all'input |
| `n_global-pot(S_{i-1})` | quanto `S_{i-1}` ha struttura non-locale disponibile | analogo applicato all'input |

`p_phase` (lato real e pot) è inerentemente **contrastiva**: richiede un baseline (il completamento attrattoriale di default). Senza baseline non c'è opposizione misurabile. `n_global` è **strutturale interna**: si misura sulla sola produzione, cercando proprietà non-locali; richiede una nozione di "località" dichiarata ex ante.

#### 4.3.3 Operativizzazione enumerata stratificata

Per ogni componente, quattro famiglie di candidati operativi, tutti **(P)**, etichettati per tipo di task.

**Per `p_phase-pot`** (analogo per `p_phase-real`):

| Codice | Candidato | Operativizzazione | Asimmetria di ruolo |
|---|---|---|---|
| P-α | Greedy completion entropy | LLM baseline (famiglia diversa) genera distribuzione top-k completamenti di `S_{i-1}`; entropia/perplexity normalizzata | baseline-LLM ≠ pipeline; normalizzazione di scala richiede grounding su sub-set umano |
| P-β | Embedding distance da classe canonica | Costruire ex ante classe `C_canon` di replies-canoniche per task; misurare distanza | classe `C_canon` costruita da etichettatori distinti dalla pipeline; embedding-model distinto |
| P-γ | Distance from baseline-pipeline canonical output | Pipeline in modalità greedy/cold (PIPE-canon) produce baseline; giudice separato misura concentrazione/spread | baseline-producer = PIPE-canon, giudice ≠ pipeline; **condizionato a tre verifiche** (vedi §7.4 P-γ) |
| P-δ | LLM-as-judge eterogeneo on canonicity | Judge model (famiglia diversa) classifica `S_{i-1}` su prevedibilità canonica | judge ≠ pipeline; calibrato su sub-set umano (κ ≥ pre-registrato) |

**Per `n_global-pot`** (analogo per `n_global-real`):

| Codice | Candidato | Operativizzazione | Asimmetria di ruolo |
|---|---|---|---|
| N-α | Profondità semantica | Parse tree depth, AMR graph depth, embedding manifold curvature | parser/extractor distinto dalla pipeline |
| N-β | Latenza dimensionale | Intrinsic dimensionality (PCA, MLE Levina-Bickel, persistent homology) | embedding model distinto |
| N-γ | Densità relazionale del context | Grafo entity-relation (NER + RE); densità, centrality, modularity | extractor distinto |
| N-δ | Symbolic structure (per domini formalizzabili) | Logical form, KB query, ontology references; ricchezza strutturale | tool symbolic distinto; tendente a (O) per domini formalizzati |

**Stratificazione raccomandata per task type** (sequenza di priorità pre-registrata: `formalizzabile > classe canonica nota > n_global degenerato > multi-step > semantico libero`):

| Tipo di task | Candidati primari `p_phase` | Candidati primari `n_global` |
|---|---|---|
| Formalizzabile (logica/matematica/codice) | symbolic pre-screen + P-α | N-δ |
| Classe canonica nota | P-β | N-γ |
| n_global degenerato (risposte brevi, fact-check) | P-α (con bassa pesatura `n_global`) | N-α |
| Multi-step complessa | P-α | N-α |
| Semantico libero | P-α | N-α/N-β |

Un task che ricade in più categorie viene assegnato alla **prima della sequenza** (stratificazione prioritaria, non esaustiva).

#### 4.3.4 Doppio livello di sterilità preservato

La forma F.D-product preserva **due livelli distinti** di sterilità che operano a granularità diverse — *non vanno unificati*:

- **Sterilità interna a Phi-real** (doppio zero pesato di `p_phase-real + n_global-real`): cattura *sterilità dell'azione* — `f_i` non opera né struttura non-locale né opposizione all'attrattore. F-Mor1 classico di Cap. 4 §4.14.
- **Sterilità aggregata a F** (un fattore — `Phi-real` o `Phi-pot` — nullo): cattura *sterilità ontologica* (V1 azione vuota / V1\* input vuoto). `Phi(f_i) = 0` per fattore zero.

Una pipeline con stitching mediocre su input ricco ha `Phi-real` moderata (non zero) — F.D-product produce `Phi(f_i)` basso ma non zero, segnalando *pipeline inefficiente*, non strutturalmente sterile. Solo `Phi-real = 0` esatto produce F.D-product = 0 (F-Mor1 puro). Mantenere i due livelli distinti preserva la tipologia di failure di Cap. 4 §4.14: inefficienza ≠ sterilità ontologica.

#### 4.3.5 Perché F.D-product (non F.D-geomean, non F.E)

La scelta della forma `F` per combinare `Phi-real` e `Phi-pot` deriva da quattro vincoli formali (V1 responsabilità su Phi-realizzata, V1\* responsabilità su Phi-potenziale, V2 sterilità doppio zero, V3 range Cap. 8) e da analisi del comportamento al limite.

Tre forme alternative considerate ed eliminate o riservate:
- **Ratio (Phi-real / Phi-pot)**: eliminata strutturalmente. Misura efficienza di conversione, non emergenza assoluta. Caso degenere "domanda vuota + risposta vuota" dà ratio 1 ma zero emergenza.
- **min(Phi-pot, Phi-real)** (F.E): praticabile, ma sotto conservazione strutturale `Phi-real ≤ Phi-pot` (argomento "f_i non crea emergenza dal nulla") si riduce a `Phi-real` con sterility-gate puro. Lascia `Phi-pot` intermedi non penalizzati — caso paradigmatico: input strutturalmente ricco (alta `n_global-pot` per densità relazionale) ma canonicamente prevedibile (bassa `p_phase-pot` perché la risposta-attrattore di consenso disciplinare è univocamente determinata dall'input), accoppiato a risposta che riproduce la canonica senza opporsi all'attrattore. Sotto F.E la coppia passa con valore moderato; F.D-product la penalizza strutturalmente. F.E delega l'opposizione all'attrattore al refine attivo, esternalizzando dalla metrica.
- **Geomean (√(Phi-real · Phi-pot))**: decadimento al limite V1\* come radice quadrata (più lento) — lascia "scia di ordinatività residua" che il framing TE non autorizza.

F.D-product (`Phi-real · Phi-pot` con `g = identità`) è scelta perché:
1. **Massima internalizzazione di V1\***: la responsabilità sull'input entra direttamente in metrica, non solo nel refine.
2. **Decadimento lineare al limite V1\***: `Phi-pot = 0.1 ⇒ Phi(f_i) ≤ 0.1`. Avvicina V1\* rapidamente, coerente con V1\* come limite ontologico stretto (Cap. 2 §1.3: emergenza richiede materia).
3. **Minima complessità**: nessun sub-parametro (vs F.D-geomean nessuno, F.D-soft-gate richiede θ, F.D-asymmetric richiede a, b).
4. **Forma canonica Cap. 8 Def 8.11**: scalari in [0,1] moltiplicabili direttamente.
5. **Severità sui valori intermedi**: caso "good-good" (`Phi-pot = Phi-real = 0.7 ⇒ Phi = 0.49`) è coerente con TE — ordinatività richiede *eccellenza*, non sufficienza. Calibration di `τ_Phi` ammortizza se serve.

Una pipeline che riceve input "intermedio" (`Phi-pot ≈ 0.4`) e produce risposta canonica (`Phi-real ≈ 0.3`) ottiene `Phi(f_i) = 0.12` — penalizzata aggressivamente per non aver opposto l'attrattore data l'occasione strutturale. F.E lascerebbe passare a 0.3.

#### 4.3.6 Mitigazione del double-counting

Rischio teorico: `Phi-real` e `Phi-pot` condividono la decomposizione `p_phase + n_global` — possibile double-counting di `p_phase` quando si moltiplicano in F.D-product.

Mitigazione strutturale come prima difesa: per task con `n_global` non degenerata, una reply che devia spuriamente da un baseline ha `n_global-real` basso (struttura non organizzata); `Phi-real` complessiva resta moderata; F.D-product non amplifica oltre la materia organizzata effettivamente prodotta.

Limite: per task con `n_global` **strutturalmente bassa** (risposte brevi, fact-check binario, classificazione one-token, dove `p_phase` domina la `Phi-real`), il double-counting può amplificare spurious senza correzione interna. In quei casi serve compensazione esterna: stratificazione di `τ_Phi^M` per tipo di task — `τ_Phi` più alto per task con `n_global` strutturalmente bassa, esplicito e dichiarato (vedi §8.4).

### 4.4 Sub-effetto strutturale: Phi ricorrentemente basso predice chiusura dell'orizzonte di refine

`Phi(f_i) = 0` ricorrente non è solo sintomo locale di sterilità — è predittore strutturale di incapacità futura di refine. Una pipeline che non sa fare struttura non-locale oggi non saprà fare refine non-locale domani, perché il refine richiede capacità di riorganizzazione cross-passo. Il gate F-Mor1 (sterilità per `Phi=0`) ha quindi conseguenze sulle proprietà *future* di α della pipeline, non solo locali.

Conseguenza per il design del gate: i passi più vicini alla chiusura dell'orizzonte di refine pretendono `tau_f` più stretto, perché il falso-ammesso in quei passi costa di più (propagazione asimmetrica, vedi §3.3).

---

## 5. Gate sulla composta — il punto distintivo

### 5.1 La condizione 3 di Cap. 4 Def 4.3

Per la composta `g ∘_Omega f`:
1. `g ∘ f` definita classicamente (continuità con la category theory standard);
2. `Adm_Omega(f) ∧ Adm_Omega(g)` valgono indipendentemente;
3. `Adm_Omega(g ∘ f)` vale per la composta stessa.

La condizione 3 non è ridondante: cattura il caso F-Comp1 di Cap. 4 §4.14 (composta fragile — ogni passo singolarmente ok ma la composta al bordo di soglia) e F-Comp2 (composta collassata in classe degenerativa anche con passi localmente ammissibili).

### 5.2 Cosa significa per la pipeline AI

Per la traiettoria `S_0 → S_1 → ... → S_n`:
- ogni `f_i` deve passare il gate per-step (§4);
- la *traiettoria intera* deve mantenere coerenza globale — `Coh(S_n)` come proprietà del nodo presente (non additiva dei `Coh(f_i)` locali);
- piccole derive locali, ognuna sopra soglia per-step, possono produrre `S_n` internamente al bordo perché la singolarità presente ha accumulato sotto-tensioni.

Operativizzazione candidata **(P)**: `Coh_traiettoria` con soglia globale `tau_global` distinta dalle `tau_f` locali, monotonicamente non crescente lungo la traiettoria (cf. β di §3.2). Una traiettoria è ammessa solo se la perdita cumulativa di coerenza resta sotto `tau_global`.

Questo è il punto strutturale dove una pipeline AI ordinativa si differenzia da una classica anche se ogni LLM-call individuale appare ok. Una proxy che misura solo l'output finale (come quello attuale di A01) non discrimina ordinatività della traiettoria.

---

## 6. Refine attivo R come operatore pre-step separato

### 6.1 Decisione strutturale

R è un morfismo categoriale (Cap. 4 Def 4.3-aderente, esteso): `R: S_{i-1} → S_{i-1}'`, con propria entry in trajectory append-only. È **operatore pre-step separato**, non sub-routine intra-step di `f_i`.

Cinque argomenti per la separazione:
1. **Distinzione concettuale tra refine reattivo e refine attivo**: il primo modifica come `f_i` opera senza modificare `S_{i-1}` (intra-step), il secondo modifica `S_{i-1}` prima che `f_i` venga applicato (separato per natura). Conservare la distinzione richiede separazione strutturale.
2. **Refine attivo agisce a monte del passo critico** — è prevenzione strutturale del falso-ammesso, non correzione a posteriori. Intra-step perderebbe la separazione "a monte".
3. **Trajectory append-only (P1)**: la modifica `S_{i-1} → S_{i-1}'` deve essere visibile per auditability. Intra-step la nasconderebbe.
4. **Asimmetria di ruolo**: R ≠ giudici post-refine. Intra-step renderebbe R parte di PIPE.
5. **Gate proprio per la qualità del refine**: il refine deve passare verifiche di qualità che non hanno corrispondente in `f_i`.

Costo accettato: overhead computazionale (R è morfismo separato) + complessità architetturale. Compensati dalla cattura strutturale.

### 6.2 Tre sub-tipi di R (minimo viable, non esaustivo)

| Codice | Sub-tipo | Operativizzazione |
|---|---|---|
| **R-prompt** | R-prompt-rewrite | riformula `S_{i-1}` testualmente: chiarimenti, ricarica dimensioni, riformulazione del task |
| **R-context** | R-context-augment | espande context portion di `S_{i-1}` con materia rilevante (RAG over deeper sources, query expansion) |
| **R-struct** | R-structural-injection | inietta struttura latente esplicita: estrae ontologia dei concetti, crea grafo semantico, esplicita relazioni |

I tre sono **minimo viable strutturalmente per A01**, non tassonomia esaustiva. Sub-classificazioni più fini sono specializzazioni:
- *R-decomposition* (spezzare in sotto-domande) è specializzazione di R-structural-injection;
- *R-perspective-shift* (ricontestualizzare da prospettive diverse) è specializzazione di R-context-augment.

Sub-classificazioni ulteriori sono riservate a calibration empirica.

### 6.3 Trigger di R

`trigger(S_{i-1}) = AND( Phi-pot(S_{i-1}) < θ_R , criticità(f_i) ≥ θ_C )`

con `θ_R, θ_C` pre-registrati per stratificazione di task. Logica:
- `Phi-pot bassa` AND `criticità bassa`: refine non vale il costo (`Phi-real` basso accettato).
- `Phi-pot bassa` AND `criticità alta`: R attivato per prevenire falso-ammesso strutturale.
- `Phi-pot adeguata`: R non necessario.

Coerente con asimmetria di costo (passi più vicini alla chiusura dell'orizzonte di refine richiedono trigger più sensibile). NON applicato uniformemente — applicato preferenzialmente sui passi dove il falso-ammesso costerebbe di più.

### 6.4 Gate proprio di R

R produce `S_{i-1}'` che passa due gate:

| Gate | Funzione | Respinto se |
|---|---|---|
| **Gate-Coh-R** | `Coh-fidelity(S_{i-1}, S_{i-1}')`: la modifica preserva fidelity al task originale | la modifica cambia il task invece di arricchire l'input |
| **Gate-ΔΦ-pot** | `Phi-pot(S_{i-1}') > Phi-pot(S_{i-1}) + δ_R`: il refine deve incrementare materially la potenzialità | `Phi-pot` post ≈ `Phi-pot` pre, oltre soglia `δ_R` (refine inefficace) |

Aggregazione fail-fast: respinto se uno dei due fallisce. Il gate di `f_i` valuta l'azione (Coh + Phi); il gate di R valuta la modifica (Coh-fidelity + ΔΦ-pot). I due gate sono strutturalmente diversi e non collassano l'uno sull'altro.

### 6.5 Trajectory dopo R

Sequenza con R applicato:
```
S_{i-1} → R-event(S_{i-1}, S_{i-1}', Phi-pot') → f_i-event(S_{i-1}', S_i, Phi-real, Phi(f_i))
```

Append-only registra entrambi gli eventi distinti. `Phi(f_i, S_{i-1}') = Phi-real(f_i, S_{i-1}') · Phi-pot(S_{i-1}')`. Senza R: trajectory standard `S_{i-1} → f_i-event(S_{i-1}, S_i, ...)`.

Trajectory permette di distinguere passi con e senza R nel debito ordinativo `Σ(1 − coh_step)`.

### 6.6 Policy del refine — due livelli complementari

La policy del refine opera a **due livelli distinti e complementari**:

**Livello 1 — Preventivo (pre-`f_i`)**

Trigger §6.3 attivato → R applicato prima di `f_i`. Gestisce il caso "Phi-pot bassa + passo critico" *a monte*, prima che `f_i` venga eseguito. È il caso normale del refine attivo.

**Livello 2 — Post-fallimento (post-`f_i` respinto)**

Se `f_i` viene eseguita (perché trigger non attivato al livello 1) e il gate respinge `f_i`, la decisione opera a tre rami:

1. **Phi-pot adeguata MA Phi-real basso**: refine reattivo — rifare `f_i` con parametri diversi (prompt più ricco, più context) sullo *stesso* `S_{i-1}`. Phi-pot fissata, fallimento di realizzazione.
2. **Phi-pot inadeguata** (rivelata solo dal fallimento): refine attivo retroattivo — applicare R `S_{i-1} → S_{i-1}'`, poi rifare `f_i` su `S_{i-1}'`. Caso "trigger non attivato al livello 1 ma Phi-pot effettivamente bassa" (criticità sottostimata o `Phi-pot` apparente alta vs operativa bassa).
3. **Entrambi falliscono**: respinta finale, escalation (criticità del passo determina cosa significa "escalation" per il task specifico).

I due livelli **non sono alternativi**, sono **complementari**:
- Livello 1 ottimizza per prevenzione (anti-falso-ammesso preventivo).
- Livello 2 fornisce robustezza contro mis-calibration del livello 1.

Una pipeline ordinativa completa implementa entrambi.

---

## 7. Asimmetria di ruolo a cinque famiglie

### 7.1 Componenti del sistema

| Componente | Funzione |
|---|---|
| **PIPE** | pipeline-completa con apparato ordinativo runtime (sotto valutazione) |
| **PIPE-canon** | pipeline-canonica greedy/cold senza apparato ordinativo runtime (per baseline P-γ) |
| **R** | refine attivo (vedi §6) |
| **J-real** | giudice di Phi-real (componenti p_phase-real, n_global-real) |
| **J-pot-p** | giudice di p_phase-pot (P-α/β/γ/δ) |
| **J-pot-n** | giudice di n_global-pot (N-α/β/γ/δ) |
| **J-threshold** | calibratore di soglie τ_Phi, τ_Coh, R_min, parametri di R |
| **HUM** | sub-set umano qualificato — grounding non collassabile |

### 7.2 Vincoli di asimmetria di esecuzione (runtime)

| Coppia | Vincolo | Origine |
|---|---|---|
| PIPE ≠ J-real | famiglia di modelli diversa | Cap. 1 OCT |
| PIPE ≠ J-pot-p | famiglia di modelli diversa | Cap. 1 OCT |
| PIPE ≠ J-pot-n | famiglia di modelli/extractor diverso | Cap. 1 OCT |
| PIPE-canon ≠ J-pot-p (caso P-γ) | la pipeline-canonica produce baseline, il giudice è separato | §7.4 |
| baseline-producer ≠ J-pot-p (caso P-α/P-β) | per p_phase-pot contrastivo: chi produce baseline ≠ chi misura distanza | asimmetria a tre |
| R ≠ J-real, J-pot-p, J-pot-n (post-refine) | il refine modifica `S_{i-1}'`, ma i giudici sono separati da R | §6.4 |
| J-real ≠ J-pot-p ≠ J-pot-n (raccomandato) | i giudici dei tre canali distinti per evitare bias correlati | estensione |

### 7.3 Vincoli di asimmetria di calibrazione

| Coppia | Vincolo |
|---|---|
| J-threshold ≠ PIPE | chi calibra ≠ pipeline sotto valutazione |
| J-threshold ≠ J-real, J-pot-p, J-pot-n | chi calibra ≠ chi giudica nel runtime |
| J-threshold ≠ HUM-builder ma allineato a HUM-grounding | calibratore allinea al sub-set umano (κ ≥ pre-registrato) ma non lo costruisce |
| HUM-builder ≠ pipeline-team | chi costruisce sub-set umano ≠ chi sviluppa la pipeline |
| Pre-registrazione delle soglie | mai spostate dopo aver visto i dati (anti-D03) |

### 7.4 Risoluzione P-γ — lettura (c) condizionata

Se P-γ è il candidato scelto per `p_phase-pot`, va risolta concettualmente la natura di PIPE-canon. Tre letture candidate:

(a) **PIPE-canon è LITERALLY un modo della stessa pipeline LLM** — stessa rete, stessi pesi, solo decoding diverso (greedy vs sampling con apparato ordinativo). Auto-valutazione disguised — viola Q4.

(b) **PIPE-canon è una pipeline distinta** (modello-LLM diverso, scelto come "modello canonico di riferimento"). P-γ collassa essenzialmente a P-α (greedy completion entropy con baseline-LLM eterogeneo).

(c) **PIPE-canon è la pipeline LLM in modo greedy *senza* apparato ordinativo runtime** — stessi pesi del LLM sottostante, ma diverso *livello* (PIPE-canon = "PIPE meno il livello ordinativo runtime"). L'asimmetria di ruolo si applica al livello di apparato ordinativo, non al livello di pesi LLM sottostante.

**Risoluzione**: lettura (c) — l'asimmetria Q4 si applica al livello di apparato ordinativo. P-γ rimane viable, *condizionato* a tre verifiche simultanee:

- **(C1) Nettezza empirica PIPE vs PIPE-canon**: misurare divergenza tra output (es. embedding distance media + varianza). Soglia `ε_C1` pre-registrata; se sotto, P-γ va declassato a P-α.
- **(C2) Effetto qualitativo netto del layer ordinativo runtime**: classificazione degli output su dimensioni qualitative. Se il layer non produce differenza qualitativa identificabile, (c) regredisce a (a).
- **(C3) J-pot-p davvero eterogeneo**: famiglia di modelli strutturalmente diversa da PIPE.

P-γ ammissibile solo se **tutte e tre** le condizioni sono verificate. Senza una qualunque, declassamento a P-α.

### 7.5 Tabella sinottica e cinque famiglie minime

| Livello | Componente | Distinto da: |
|---|---|---|
| Pipeline-completa | PIPE | – (sotto valutazione) |
| Pipeline-canonica | PIPE-canon | livello ordinativo (non pesi LLM) |
| Refine | R | giudici post-refine |
| Giudice Phi-real | J-real | PIPE |
| Giudice p_phase-pot | J-pot-p | PIPE, PIPE-canon (caso P-γ), baseline-producer (P-α/P-β) |
| Giudice n_global-pot | J-pot-n | PIPE |
| Giudici tra loro | J-real, J-pot-p, J-pot-n | tra di loro (raccomandato) |
| Calibratore soglie | J-threshold | PIPE, J-real, J-pot-p, J-pot-n |
| Sub-set umano | HUM | tutto il resto |

**Famiglie minime di modelli/agent distinti**: cinque (PIPE, J-real, J-pot-p, J-pot-n, J-threshold) + grounding HUM.

### 7.6 Bilanciamento operativo: cinque famiglie come standard ideale, riduzioni controllate

L'argomento per cinque famiglie distinte regge: J-pot-p e J-pot-n stesso modello con prompt diversi avrebbero **correlazione di bias intrinseca** (sopravvalutazione/sotto-valutazione semantica condivisa nei domini specifici), invisibile dai dati di calibrazione. Il bias scompare con prompt diversi solo all'apparenza.

Tuttavia il costo materiale è significativo. Bilanciamento operativo:

- **Cinque famiglie come requisito ideale**.
- **Combinazioni controllate ammesse** con due vincoli non eludibili:
  - **(i) correlazione di bias dichiarata nel claim A01**: il claim si formula come "rispetto a giudizio eterogeneo a `N` famiglie distinte" con `N` esplicito (5, 4, 3, ecc.). Trasparenza pubblica.
  - **(ii) stima empirica della correlazione + soglia massima accettabile pre-registrata** (es. `ρ ≤ 0.3`).
- **Mai trattare la riduzione come ottimizzazione invisibile**: anti-pattern parente di D02 (vacuum-PASS) e D03 (post-hoc rescue).

---

## 8. Protocollo di calibrazione

### 8.1 Mappa gerarchica dei parametri

| Livello | Parametri | Riferimento |
|---|---|---|
| Gate `f_i` | `τ_Phi^M` (per morfismo, stratificato) | §4.3 |
| Gate `f_i` interno | `τ_Coh^M` | §4.2 |
| Forma `Phi-real` | `w_p`, `w_n` (per task type) | §4.3.1 |
| Forma `Phi-pot` | `w_p`, `w_n` (per task type, coerenti con `Phi-real`) | §4.3.1 |
| `p_phase-real`/`p_phase-pot` | scelta P-α/β/γ/δ per task type, parametri specifici | §4.3.3 |
| `n_global-real`/`n_global-pot` | scelta N-α/β/γ/δ per task type, parametri specifici | §4.3.3 |
| Trigger R | `θ_R`, `θ_C` | §6.3 |
| Gate R | `τ_Coh-R^M`, `δ_R^M` | §6.4 |
| Famiglie | identità delle cinque famiglie + correlazione `ρ` se riduzioni | §7.5-7.6 |
| Verifiche P-γ | criteri operativi per C1, C2, C3 | §7.4 |

Numero di parametri: dell'ordine di **20-30** per stratificazione di task type, con almeno cinque stratificazioni.

### 8.2 Cinque elementi del protocollo

#### 8.2.1 Set etichettato

| Elemento | Grado |
|---|---|
| Numerosità per tipo di morfismo `N_M`, pre-registrate, non identiche tra tipi | (O) |
| Proporzione minima di casi al bordo, pre-registrata (anti-vacuum-PASS) | (C) |
| Mix sintetici / output pipeline classica reale, pre-registrato | (P) |
| Disgiunzione strutturale dal set di benchmark A01, sigillata con hash | (O) |
| Sub-set umano qualificato 20–30% pre-registrato come grounding non collassabile | (O) |

#### 8.2.2 Asimmetria di ruolo

| Elemento | Grado |
|---|---|
| Tre ruoli separati: pipeline-builder ≠ metric-designer ≠ label-judge | (O) |
| Etichettatura in cieco rispetto al valore di Coh/Phi calcolato | (O) |
| Multi-judge ≥ 3 con voto di maggioranza; terza categoria "al bordo" per disaccordo elevato | (P) |
| LLM-as-judge eterogeneo allineato al sub-set umano sul resto | (O) |
| Soglia di allineamento κ ≥ pre-registrato (es. 0.85; raw concordance sconsigliata su task ternario) | (O) |
| Sotto soglia: LLM-as-judge non si usa per quel morfismo. Alternative: etichettatura umana piena, oppure A01 dichiarato non testabile per quel morfismo nel run corrente | (O) |
| Claim A01 dichiara esplicitamente referente: "umano qualificato + LLM-as-judge eterogeneo allineato a umano sul sub-set", NON "LLM" puro | (O) |
| Cinque famiglie minime (§7.5) o riduzioni controllate dichiarate (§7.6) | (O) |

#### 8.2.3 Forma soglia Cap. 4-aderente

`τ_Coh^M`, `τ_Phi^M`, `τ_Coh-R^M`, `δ_R^M` come soglie singole per morfismo. Fail-fast implicita da `max` interno (vedi §4.2.3). Non soglie per-componente (esclusa da Cap. 4 Def 4.2).

Granularità: `(morfismo)` come default. Stratificazione per `(morfismo, tipo di task)` come estensione operativa.

#### 8.2.4 Costi asimmetrici falso-ammesso ≫ falso-respinto

Asimmetria derivata strutturalmente dal framework variazionale α/β/Cost (§3). Falso-ammesso paga (1) il proprio `(1 − coh)` in β, (2) può attivare F-Comp1/F-Comp2 propagando il danno lungo la traiettoria. Falso-respinto paga Cost del refine + ε-β (se il refine ha `coh ≈ 1`).

Estensione al gate di R e al trigger:
- Falso-ammesso del gate-R (refine inefficace ma passa il gate): `f_i` esegue su `S_{i-1}'` ingannevolmente migliorato → propagazione del falso-ammesso a `f_i`. Costo strutturalmente alto.
- Falso-respinto del trigger-R (R non attivato quando serviva): `f_i` esegue su `S_{i-1}` con Phi-pot inadeguata → fallimento o falso-ammesso di `f_i`. Costo dipendente dalla criticità del passo.
- Falso-ammesso del trigger-R (R applicato quando non serviva): refine inutile + delay computazionale. Costo basso.

`R_min^M` per ciascun gate calibrato sull'asimmetria. Default uniforme (semplice da pre-registrare); stratificato per criticità come estensione (P).

#### 8.2.5 Sigillamento crittografico immutabile

| Elemento | Grado |
|---|---|
| Documento sigillato (timestamp + hash crittografico) prima della produzione del set | (O) |
| Versionamento esplicito: ogni revisione del protocollo è una nuova pre-registrazione, NON un override | (O) |
| Failure mode dichiarato: se A01 fallisce con quelle soglie, il fallimento entra in trajectory append-only del programma di validazione | (O) |

Tutti i parametri pre-registrati e sigillati prima della validazione. Il sigillamento è per-stratificazione di task type.

### 8.3 Verifiche pre-registrate

Tre verifiche da eseguire prima della validazione finale del claim. Ognuna pre-registrata, criteri di fallimento dichiarati.

#### 8.3.1 Condizioni P-γ (C1, C2, C3)

Vedi §7.4. Verifica empirica della nettezza PIPE vs PIPE-canon, dell'effetto qualitativo netto del layer ordinativo, dell'eterogeneità di J-pot-p. Se una qualunque fallisce, P-γ va declassato a P-α per quella stratificazione.

**Mai trattare il fallimento come "soglia da abbassare retroattivamente"** (anti-D03).

#### 8.3.2 Conservazione `Phi-real ≤ Phi-pot`

L'argomento "f_i non crea emergenza dal nulla" predice `Phi-real ≤ Phi-pot` strutturalmente. Verifica empirica: su sub-set umano, calcolare la frazione di passi in cui `Phi-real > Phi-pot`. Pre-registrare soglia accettabile `ε_cons` (es. ≤ 5% come rumore di misura).

Se la violazione supera `ε_cons` sistematicamente:
- F.D-product **rimane valida** (la moltiplicazione è legittima qualunque sia la conservazione).
- L'argomento positivo va riformulato come "tendenza statistica" non "legge strutturale".
- Dichiarazione esplicita nel claim A01.

**Nessun aggiustamento post-hoc dei pesi o delle soglie per "salvare" la conservazione**.

#### 8.3.3 Mitigazione double-counting

Stratificazione `τ_Phi^M` per task type — `τ_Phi` più alto per task con `n_global` strutturalmente bassa (compensazione per la compressione naturale di `Phi(f_i)` quando `p_phase` domina e double-counting può amplificare). Stratificazione esplicita; mitigazione **dichiarata, non occulta**.

### 8.4 Stratificazione completa per task type

| Tipo di task | Candidati `Phi-real` | Candidati `Phi-pot` | `τ_Phi^M` | Trigger R |
|---|---|---|---|---|
| Classe canonica nota | P-β/N-γ | P-β/N-γ | standard | standard |
| Complessa multi-step | P-α/N-α | P-α/N-α | standard | sensibile (più aggressivo) |
| Formalizzabile (logica/matematica/codice) | symbolic+P-α / N-δ | symbolic+P-α / N-δ | standard | calibrato su unicità soluzione |
| Semantico libero (literary/philosophical) | P-α/N-α-β | P-α/N-α-β | standard | meno aggressivo |
| **Risposta breve / fact-check (`n_global` degenerato)** | P-α/N-α (bassa pesatura `n_global`) | come `Phi-real` | **più alto** (mitigazione double-counting) | calibrato su eccezionalità |

**Sequenza di priorità** (pre-registrata): `formalizzabile > classe canonica nota > n_global degenerato > multi-step > semantico libero`. Un task in più categorie va alla **prima della sequenza**.

Sub-osservazione segnata per rifinitura in calibrazione concreta: "n_global degenerato" è epistemicamente diverso dalle altre — è *tipo di rischio* (double-counting amplificato sul lato `p_phase`) più che *tipo di task*. Potrebbe essere trattato come modificatore applicabile a qualunque tipo invece che categoria stand-alone. Trattare ora come categoria stand-alone è scelta conservativa che preserva la stratificazione semplice; rifinitura possibile in implementazione successiva.

### 8.5 Cosa il protocollo NON fissa

Tutti i numeri concreti restano aperti, da fissare in calibrazione effettiva sotto pre-registrazione. Il protocollo fornisce il *quadro*, non i *valori*:

- valori concreti di `N_M`, `R_min` (uniforme o stratificato), soglia di allineamento κ;
- composizione precisa "casi al bordo / casi chiari" del set di calibrazione;
- valori specifici di `τ_Phi`, `τ_Coh`, `θ_R`, `θ_C`, `δ_R`, `ε_C1`, `ε_C2`, `ε_cons`;
- pesi `w_p`, `w_n` per ogni stratificazione;
- scelta del candidato definitivo per `p_phase` e `n_global` per ciascuna stratificazione di task.

La calibrazione concreta richiede sub-set umano + esecuzione del protocollo, ed è lavoro di implementazione successiva, sotto la disciplina qui definita.

---

## 9. Pipeline ordinativa vs pipeline classica

**Pipeline classica `P_cl`** applica `f_1 → f_2 → ... → f_n` senza gate. Accetta ogni output. Il fallimento si manifesta solo come errore osservabile a valle (allucinazione palese, off-topic, rifiuto del verifier).

**Pipeline ordinativa `P_ord`** applica gli stessi morfismi con:
- gate `Adm_Omega` ad ogni step (validità sintattica + Coh ≥ τ + Phi ≠ 0);
- gate sulla composta (la traiettoria mantiene coerenza globale);
- refine attivo R come operatore pre-step su trigger (Livello 1) o post-fallimento (Livello 2);
- decisione al respinto: backtrack / refine / abort ordinativo (la pipeline dichiara "non posso rispondere ordinativamente", non finge PASS).

**Confronto fedele** (questo è il chiodo che il proxy attuale di A01 manca):

Per equifinalità, due pipeline possono produrre output simili da processi molto diversi. Il confronto va misurato sul **processo** — traiettorie + decisioni di gate + drift cumulativo lungo la traiettoria — non sull'output finale. Per ogni task del benchmark:
- registrare la traiettoria intera di entrambe le pipeline;
- misurare `Delta_cum` come perdita di coerenza cumulativa lungo la traiettoria, non come funzione dell'output;
- includere casi dove l'output è equivalente tra le due ma la traiettoria è diversa — solo così la differenza ordinativa è isolabile.

**Tre regimi possibili**:
- pipeline ordinativa che non ha avuto reject: `Coh_traiettoria` massima, Cost ≈ baseline, α alta;
- pipeline ordinativa con reject + refine: `Coh_traiettoria` intermedia (degradata dal reject ma contenuta dal refine), Cost > baseline, α potenzialmente alta;
- pipeline classica con errore non corretto: `Coh_traiettoria` bassa (errore propaga), Cost ≈ baseline, α bassa.

---

## 10. Claim A01-raffinato

### 10.1 Forma del claim

Una pipeline ordinativa `P_ord` per task multi-step compositivi, costituita da:

- sequenza di morfismi `f_i` con gate ordinativo `Phi(f_i, S_{i-1}) = Phi-real(f_i, S_{i-1}) · Phi-pot(S_{i-1})` (F.D-product, §4.3);
- componenti bipartite simmetriche (`Phi-real` e `Phi-pot` come somma pesata `p_phase + n_global`);
- refine attivo R come operatore pre-step separato (§6) con policy a due livelli complementari;
- trajectory append-only auditabile (§2.2) con eventi `R-event` distinti dagli `f_i-event` (§6.5);
- asimmetria stratificata a cinque famiglie distinte (§7.5) o riduzione controllata `N < 5` con correlazione di bias dichiarata e pre-registrata (§7.6);
- calibrazione di tutte le soglie e parametri sotto il protocollo §8 (cinque elementi di §8.2 scalati, sigillamento crittografico immutabile per ogni stratificazione di task type);
- verifiche pre-registrate completate (§8.3): condizioni P-γ (C1+C2+C3), conservazione `Phi-real ≤ Phi-pot`, mitigazione double-counting;

ha **α (integrità del nodo presente, §3.2) strettamente maggiore** rispetto a una pipeline classica `P_cl` (stessi morfismi senza gate ordinativo, senza refine attivo, senza asimmetria stratificata) sul medesimo task multi-step compositivo, **in expectation** sul corpus etichettato di calibrazione, **anche al costo runtime alto** della pipeline ordinativa.

Più precisamente, sotto la disciplina del protocollo §8:

- `α(P_ord) > α(P_cl) + ε_α` (margine pre-registrato, dipendente dalla stratificazione);
- `β(P_ord) < β(P_cl)` (debito ordinativo come gap d'azione: la traiettoria ordinativa si avvicina alla geodetica ordinativa);
- `Cost(P_ord) > Cost(P_cl)` (costo runtime maggiore);
- il vantaggio in α giustifica l'investimento in Cost — esiste una **regione di task** (identificata dalla stratificazione §8.4) dove `P_ord` è strettamente preferibile.

### 10.2 Tre livelli di "elevazione del livello"

Il raffinamento "pipeline ordinativa eleva il livello della conversazione, non solo fa bene il task dato" è misurabile a tre livelli operativi:

**A livello locale (per-passo)**: `Phi(f_i)` cattura il livello di emergenza ordinativa del passo come prodotto di potenzialità input + realizzazione azione. Penalizzazione attiva di canonicità via F.D-product (decadimento lineare al limite V1\*).

**A livello traiettoria (cumulativo)**: debito ordinativo `Σ(1 − coh_step)` (§3.1) come funzione di azione. La traiettoria ordinativa minimizza il debito, avvicinandosi alla geodetica ordinativa.

**A livello refine attivo (input enrichment)**: R aumenta `Phi-pot` su `S_{i-1}'`, alzando il tetto di emergenza realizzabile per il passo successivo. La pipeline non si limita a rispondere al meglio data la materia — *crea condizioni di emergenza* operando attivamente sull'input. È il senso operativo di "elevare il livello": l'apparato ordinativo runtime simula in modo costoso il comportamento di un terminale trainato ordinativamente.

### 10.3 Cinque vincoli per la validità del claim

Il claim A01-raffinato è valido **solo se** sono soddisfatti tutti i seguenti vincoli, non eludibili:

1. **Disciplina del protocollo §8**: cinque elementi (set etichettato + asimmetria + soglia singola + costi asimmetrici + sigillamento) tutti applicati, sigillamento immutabile per ogni stratificazione.
2. **Asimmetria stratificata**: cinque famiglie distinte oppure `N < 5` con correlazione di bias pre-registrata e verificata empiricamente sotto soglia accettabile.
3. **Verifiche pre-registrate completate**: condizioni P-γ (C1+C2+C3), conservazione `Phi-real ≤ Phi-pot` (con dichiarazione esplicita se violata sistematicamente), mitigazione double-counting via stratificazione `τ_Phi` esplicita.
4. **Sub-set umano qualificato**: ordine di decine di migliaia di esempi etichettati con qualità expert-level dominio-dipendente, su tutte le stratificazioni.
5. **Trajectory append-only auditabile**: ogni R-event e f_i-event registrato distintamente per audit del debito ordinativo.

Senza questi vincoli, A01-raffinato collassa al caso D02 (vacuum-PASS, asimmetria collassata) o D03 (post-hoc rescue, parametri spostati post-validazione).

### 10.4 Cosa A01-raffinato NON dice — onestà esplicita

- **NON dice che `P_ord` è sempre preferibile**: la regione di task dove `P_ord` è strettamente preferibile è identificata in calibrazione (stratificazione §8.4); fuori da quella regione il vantaggio non è dimostrato. Il claim è *localmente vero* sulla regione identificata.
- **NON dice che la pipeline ordinativa runtime è la soluzione finale**: il vantaggio funzionale al costo alto è la *motivazione* per il training ordinativo nativo (fuori scope A01). A01 dimostra il vantaggio, non lo ottimizza.
- **NON dice che il refine attivo R è sempre necessario**: R è applicato solo quando trigger §6.3 scatta (Livello 1) o post-fallimento (Livello 2). Task con `Phi-pot` alta + criticità bassa non richiedono R.
- **NON dice che il livello della conversazione si eleva indefinitamente**: la pipeline è auditabile e ha gate; il livello si eleva fino a soglia, oltre la quale il debito ordinativo cresce.
- **NON dice che la conservazione `Phi-real ≤ Phi-pot` è legge strutturale universale**: è argomento verificabile empiricamente in §8.3.2; se violazione sistematica, il claim si riformula come "tendenza statistica" ma F.D-product resta valida.

---

## 11. Limiti onesti del design

### 11.1 È registro di traduzione, non implementazione

Il design fornisce il quadro concettuale, le forme delle metriche, il protocollo di calibrazione. Tutti i numeri concreti, le scelte specifiche di candidati per stratificazione, le calibrazioni effettive sono lavoro di implementazione successiva, sotto la disciplina del protocollo §8. La separazione è coerente con il principio "design vs implementazione".

### 11.2 Caso concreto considerato è una pipeline a 4 step

Pipeline più complesse (multi-agent con branching dinamico, recursion profonda, tool use con feedback loop) richiederanno estensioni del design corrente. L'argomento strutturale è invariante (gate per-passo + gate sulla composta + asimmetria + protocollo), ma il costo materiale cresce con la complessità e la stratificazione per task type va estesa.

### 11.3 I ponti TE↔OCT sono ponti, non istanziazioni formali

Tutti i mapping (`Coh ← coerenza interna sotto trasformazione`, `Phi ← controfase strutturale`, ecc.) sono ponti che usano il registro pubblicato da Ghioni. Non sono validati formalmente come istanziazioni di Cap. 8 Def 8.11 (che è benchmark fisico standing-wave, dominio-specifico). La validazione formale di questa traduzione (mostrare che le operativizzazioni candidate per pipeline AI soddisfano le proprietà che `p_phase` e `n_global` hanno nel benchmark fisico) è essa stessa lavoro aperto.

### 11.4 Gate sulla composta è la parte più aperta operativamente

Concettualmente solido (deriva direttamente da Cap. 4 Def 4.3 condizione 3), ma operativamente richiede `Coh_traiettoria` definita esplicitamente — funzione di decadimento, soglia globale `tau_global`, relazione precisa con i `Coh(f_i)` locali. Il design corrente la lascia come operativizzazione candidata (P), da chiudere in implementazione.

### 11.5 Pre-condizione di realizzabilità del protocollo di calibrazione

La costruzione di un set di calibrazione etichettato (multi-judge, multi-ruolo, sui quattro tipi di morfismo, con casi al bordo, su cinque stratificazioni di task type) ha costo reale di risorse umane qualificate non eludibile. Ordine di grandezza: **migliaia di esempi etichettati expert-level per stratificazione** → totale dell'ordine di **decine di migliaia di esempi** su tutte le stratificazioni.

"Expert-level" è dominio-dipendente: per task tecnici (logica, matematica, codice) richiede qualifiche specifiche (PhD-level + esperienza nel sub-dominio); per task di sintesi semantica libera, expert-level è meno pre-determinato (reviewer accademici, comunità di pratica con track record). La specificazione del livello di etichettatura va fissata per task type al momento della costruzione del sub-set umano, e dichiarata nel protocollo §8.2.5.

Il protocollo §8.2.2 ammette LLM-as-judge eterogeneo solo come moltiplicatore di un sub-set umano (20–30%), non come sostituto. Saltare questa pre-condizione collassa il referente del claim A01 al modello giudice e produce A01-vacuum nel senso di D02. **Questa pre-condizione è ciò che separa A01-raffinato da A01-degenere**.

### 11.6 Cinque famiglie distinte: costo materiale significativo

Cinque famiglie di modelli/agent distinti (PIPE, J-real, J-pot-p, J-pot-n, J-threshold) + sub-set umano è costo materiale. Riduzioni controllate ammesse con dichiarazione esplicita di `N` e correlazione di bias pre-registrata, mai elusione invisibile. Per pipeline multi-step compositive, l'asimmetria si applica per-passo — il costo è per-passo, non di scala per l'intera pipeline.

---

## 12. Direzioni di sviluppo future (fuori scope A01)

### 12.1 Training nativamente ordinativo

L'idea: invece di applicare un gate ordinativo come strato sopra un LLM esistente (gate-and-correct architecture), trainare l'LLM con una loss function che incorpora il debito ordinativo, in modo che il modello produca traiettorie ordinative *di default*, senza bisogno di refine post-hoc.

Tre livelli del lavoro:
1. **Training (primario)**: loss ordinativa che penalizza `coh_step < 1`, premia `Phi > 0` (anti-sterilità), introduce parsimonia computazionale (anti-debito). Principio variazionale di minima azione ordinativa come framework guida.
2. **Inference runtime (guardia di secondo livello)**: anche un LLM ordinativamente trainato non sarà perfetto. Il gate runtime esiste come *guardia*, non come correttore primario.
3. **Evaluation (per chiudere il loop)**: il gate è anche lo strumento per misurare se un LLM è ordinativo.

A01 (sui modelli attuali con gate runtime) è il **presupposto dimostrativo** per giustificare il training ordinativo. Se A01 regge, allora il vantaggio funzionale c'è anche al costo attuale alto del gate runtime → vale la pena investire nel training ordinativo perché in quel regime il costo del comportamento ordinativo scende drasticamente.

Possibile collocazione futura nel programma OCT: nuovo vettore di `oct_extension_vectors.md` ("training ordinativo nativo") o estensione del vettore A.

### 12.2 Pipeline multi-step compositive complesse

A01-raffinato si applica per-passo nelle pipeline complesse (multi-agent, branching). Il costo cresce con la complessità ma l'argomento strutturale è invariante. Estensione naturale a Cap. 4 composizione gates F-Comp1/F-Comp2.

### 12.3 Estensione a domini specifici

La stratificazione §8.4 è un primo passo. Estensioni a domini specifici (peer-review scientifica, dialogo terapeutico, decision-making medico, ecc.) richiedono ri-stratificazione e ri-calibrazione del protocollo §8 con sub-set umano specifico del dominio.

### 12.4 Schema di benchmark fedele per A01

Il design del gate è completo; lo schema di benchmark per A01 fedele resta aperto come lavoro di implementazione. Lo schema deve:
- includere task dove output ordinativo ≈ output classico ma traiettoria distinta (per isolare la differenza di processo);
- registrare la traiettoria intera, non solo l'output;
- includere la dimensione Cost esplicitamente, non solo α/β;
- coprire la stratificazione §8.4;
- rispettare la disgiunzione strutturale set-calibrazione / set-benchmark (§8.2.1) per evitare contaminazione.

### 12.5 Connessione con la tassonomia degli anti-pattern di validazione

Il design del gate ordinativo per A01 è coerente con il gate ex ante proposto in `validation_anti_patterns.md` come rimedio strutturale agli anti-pattern A01-shift-di-livello, D03-post-hoc-rescue, D02-vacuum-PASS. Il design implementa concretamente il gate ex ante per il caso A01: ogni metrica è etichettata (O/P/C), ogni soglia è pre-registrata, l'asimmetria di ruolo è strutturale, le verifiche pre-registrate impediscono il post-hoc rescue. Una pipeline che rispetta questo design è una pipeline che non può cadere nei tre anti-pattern.

---

## Appendice A — Mappa delle sezioni del file di lavoro originale

Il file `a01_gate_design_draft.md` (1684 righe) contiene la genesi cronologica del design. Mappa delle sezioni principali per chi voglia tracciare la derivazione:

- §1-§9 — bozza iniziale del design con sette punti aperti (inclusi gate per-step su pipeline RAG minimal, derivazione dai capitoli OCT, ponti TE↔OCT)
- §10 — Punto 6 chiuso: rappresentazione computazionale della singolarità
- §11 — Punto 1 chiuso: Coh per LLM-step
- §12 — Punto 2 chiuso: Phi per LLM-step (forma originale, prima del raffinamento 2.bis)
- §12bis — Cornice variazionale: principio di minima azione ordinativa
- §13bis — Sub-punto 2.bis decantato: Phi come danza, Phi-potenziale vs Phi-realizzata, refine attivo
- §16 — Punto 3 fase 1 chiuso: protocollo di calibrazione di τ_Coh
- §17 — Savepoint sessione 2026-04-30/05-01
- §18 — Sub-punto 2.bis Q1 enumerazione vincolata (cinque forme F.A-F.E, eliminazioni F.A/F.B/F.C)
- §19 — Sub-punto 2.bis Q2-a + Q2-b: decomposizione bipartita di Phi-pot, operativizzazione enumerata
- §20 — Sub-punto 2.bis Q1-chiudi: scelta F.D-product
- §21 — Sub-punto 2.bis Q4: asimmetria di ruolo a cinque famiglie, risoluzione P-γ
- §22 — Sub-punto 2.bis Q6: architettura del refine attivo R
- §23 — Sub-punto 2.bis Q3 fase 2: protocollo di calibrazione completo
- §24 — Sub-punto 2.bis Q5: claim A01-raffinato come sintesi finale

---

**Fine del documento.**
