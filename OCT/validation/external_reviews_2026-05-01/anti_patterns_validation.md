# Anti-pattern del programma di validazione OCT — sintesi dei tre audit

**Versione:** consolidata 2026-05-01
**Tipo:** documento sintetico logico-funzionale, standalone
**Origine:** triangolazione dei tre audit indipendenti `case_a01_diagnosis.md`, `case_d03_diagnosis.md`, `case_d02_diagnosis.md` prodotti durante le sessioni 2026-04-30 / 2026-05-01

**Cosa il documento fa.** Presenta i tre audit come unità — non come tre note separate ma come *un'unica diagnosi triangolata* del programma di validazione OCT v1.0 candidate. Identifica una radice cognitiva comune, tre forme realizzative distinte dello stesso meccanismo, un errore di metavalidazione separato, una tassonomia tipo-claim → anti-pattern utile come gate ex ante per Cap. 17 §9.

**Cosa il documento NON fa.** Non sostituisce le tre note tecniche `case_*_diagnosis.md` — quelle restano la sostanza completa, audit-per-audit, con i riferimenti puntuali al codice e ai cycle reports. Questo è la sintesi operativa, leggibile come unità autonoma.

---

## 1. Posizione iniziale

Tre teoremi del freeze v1.0 candidate sono stati audit indipendentemente: A01 (Teorema di stabilità ordinativa in pipeline IA, Cap. 10 §4.6), D03 (Teorema di perdita ontologica dei funtori dimenticanti, Cap. 10 §4.3), D02 (Teorema di commutatività non produttiva, Cap. 10 §4.2). Tutti e tre sono nello stato `revise` nel `DECISION_MATRIX_FINAL_UNIFIED_v0_1.md`.

L'audit ha trovato in tutti e tre i casi che l'apparato di validazione operativo (Cycle 2-3-4 per A01 e D03, Cycle 1-2-3 per D02) **non testa il claim dichiarato** secondo Cap. 8 Def 8.12 (regola anti-circolarità operativa). Non per cattiveria, non per errore isolato: per un pattern esecutivo ricorrente che la triangolazione fa emergere come *anti-pattern strutturato*.

Lo stato `revise` di tutti e nove i teoremi del decision matrix è **tecnicamente corretto** sotto Cap. 8 Def 8.12. La motivazione dichiarata ("conservatorismo editoriale pre-preprint") è quella sbagliata; quella tecnica è "il proxy operativo non rispetta i quattro requisiti di Def 8.12". La differenza è importante perché determina cosa serve fare per portare i teoremi a `validated`.

---

## 2. I tre casi in sintesi

### 2.1 A01 — claim comparativo

**Enunciato (Cap. 10 §4.6):** *"Pipeline compositive con coerenza ordinativa alta mostrano minore degenerazione semantica rispetto a pipeline solo formalmente corrette."*

**Tipo logico:** comparativo (`E[P_ord] > E[P_cls]` su distribuzione di task).

**Cosa il protocollo richiede:** confronto tra pipeline con gate ordinativo `Syn+Coh+Phi` (selettore di passi composizionali) e pipeline classica baseline; misure su `Coh`, `Phi`, drift semantico, errore cumulativo.

**Cosa è stato eseguito (Cycle 2-3, codice `run_cycle3_metrics.py`):** stessa pipeline LLM con due funzioni di lettura applicate all'output finale: `P_cls = score(modello_base, s1, s2)` e `P_ord = 0.55·P_cls + 0.45·soft_overlap(prefissi-4char(s1), prefissi-4char(s2))`. Misurazioni su `Delta_cum = Σ(1 − punteggio)` e `Err_sem = |punteggio − gold|` su STS-B. PASS in tutti i contesti `Omega_A/B/C` (round-robin sull'indice).

**Forma realizzativa dell'errore:** **shift di livello.** Il claim è sul *processo* (ordinatività come proprietà del gate selettore di passi composizionali, Cap. 4 Def 4.3). Il proxy misura una proprietà dell'*output* (mistura lineare applicata fuori dal processo, sul punteggio già prodotto). I due piani sono equifinali — output simili possono venire da processi diversi. Il proxy non discrimina ordinatività per costruzione, non per debolezza di formula.

### 2.2 D03 — claim tassonomico

**Enunciato (Cap. 10 §4.3):** *"La perdita informativa dei funtori dimenticanti è classificabile in preservativa versus degenerativa."*

**Tipo logico:** tassonomico (coesistenza di due regimi).

**Cosa il protocollo richiede:** funtore dimenticante `U` esplicitamente dichiarato; coppie pre/post di diagrammi `(D, U(D))`; indici di perdita su `Coh` e `Phi` (entrambi); partizione preservativi/degenerativi.

**Cosa è stato eseguito:**
- *Cycle 2 (sintetico)*: 180 coppie pre/post, 5 famiglie di funtori dichiarate. **Codice generativo non in repo, non auditabile.** PASS dichiarato.
- *Cycle 3 (UD English EWT, codice `build_cycle3_inputs.py` build_d03)*: 260 sentence singole (no coppie pre/post, no funtore applicato). Formula deterministica `loss_u = 0.18 + 0.35·punct_ratio + 0.15·(1 − content_ratio)` con clip in [0.05, 0.9]. Soglie pre-registrate sul `drop`: `<0.12` preservativo, `>0.28` degenerativo. Risultato: **0% preservativo**, REVISE_NEEDED.
- *Cycle 4 (revisione, codice `run_d03_revision_cycle4.py`)*: stessi dati. Cambiata variabile classificata da `drop` a `loss_u`. Cambiate soglie a `<0.276 / >0.284`. PASS_REVISED_CANDIDATE.

**Forma realizzativa dell'errore:** **post-hoc rescue dopo fail di pre-registrazione**, sovrapposto a tre errori indipendenti:
1. *Piano sbagliato*: nessun funtore applicato, formula su singole sentence (claim sui funtori non testato);
2. *Proxy parziale*: `Coh_Omega` mai misurata, solo `loss_u` come derivato lessicale;
3. *Criterio mobile*: pre-registrazione di Cycle 3 fallisce, Cycle 4 introduce nuovo criterio sui medesimi dati con cambio di variabile + cambio di soglie. Garden of forking paths classico (Gelman-Loken 2014).

**Aggravanti che hanno dato superficie d'attacco in più:**
- soglia preservativo strutturalmente inattingibile a priori (`loss_u ≥ 0.18` per costruzione, soglia `<0.12` impossibile da soddisfare — identificabile *prima* di vedere i dati);
- `Omega_A/B/C` cosmetici (round-robin sull'indice — tre etichette decorative sulla stessa popolazione);
- stress test Cycle 4 con grid `low ∈ [0.272, 0.278]`, `high ∈ [0.284, 0.288]` — perturbazioni ±0.4% attorno alla scelta post-hoc, non testa range falsificanti.

### 2.3 D02 — claim esistenziale

**Enunciato (Cap. 10 §4.2):** *"Esistono diagrammi commutativi classici con `Phi=0`."*

**Tipo logico:** esistenziale (basta esibire un caso). Logicamente il claim più debole — più facile da rendere vacuo.

**Cosa il protocollo richiede:** verifica esplicita della commutatività; misura `Phi_Omega(D)` con mapping motivato (Cap. 8 Def 8.11 Note); classificazione in regione B di Cap. 8 Def 8.5 (`Coh ≥ tau ∧ PhiHat = 0`).

**Cosa è stato eseguito:**
- *Cycle 1 (formal pilot, 2026-04-16)*: typed consistency check + costruzione di un witness teorico (quadrato commutativo con `Phi=0`). Esito: PASS (formal pilot). **L2 (formale rigoroso) legittimo come dichiarato.**
- *Cycle 2 (sintetico)*: 120 diagrammi sintetici, 6 famiglie. Codice generativo non in repo. PASS dichiarato ma non auditabile.
- *Cycle 3 (UD-EWT, codice `build_cycle3_inputs.py` build_d02)*: subgrafi di 180 archi consecutivi da `ca-GrQc` (collaboration network sparso) e `email-Eu-core`. `is_commutative = 1` hardcoded come campo CSV. `Phi = density · 8 − 0.06` clip a 0, soglia `< 0.02`. PASS in tutti i contesti `Omega_A/B/C` (rescaling moltiplicativo `1.00 / 0.92 / 0.85`).

**Forma realizzativa dell'errore:** **vacuum-PASS strutturale.** Per costruzione: `Phi=0` ⟺ `density · 8 − 0.06 ≤ 0` ⟺ `density ≤ 0.0075`. Su `ca-GrQc` (densità globale ≈ 0.0011) la presenza di chunks con density ≤ 0.0075 è **certamente non-zero per costruzione del campionamento**. Il PASS è garantito a priori dalla scelta del dataset + coefficiente lineare 8 + soglia 0.02. La falsificazione dichiarata ("tutti i commutativi hanno `Phi > 0`") è strutturalmente irraggiungibile sotto questo proxy.

**Aspetti specifici:**
- *Cycle 1 è formal pilot legittimo* (L2 formale, non L1 empirico) — non va criticato in quanto pilot, è coerente con il proprio livello dichiarato;
- *commutatività non verificata*: `is_commutative = 1` per fiat, non proprietà del subgrafo. Il claim D02 condiziona `Phi=0` alla *commutatività*. Se la commutatività è etichetta universale, il claim diventa "esistono cose etichettate-commutative con Phi=0" — banalmente vero;
- *Phi come densità rescalata*: nessun mapping a `p_phase` / `n_global` di Cap. 8 Def 8.11. La componente `Coh` della regione B (Cap. 8 Def 8.5) non viene mai calcolata;
- *`Omega_A/B/C` ancora più cosmetici di A01/D03*: non sono sub-popolazioni randomiche disgiunte (round-robin) ma rescaling lineari della stessa popolazione (`Omega_A`: phi = base_phi; `Omega_B`: phi = 0.92·base_phi; `Omega_C`: phi = 0.85·base_phi). La "stabilità cross-context" osservata (Var_Omega = 0.000741) è tautologia geometrica del rescaling.

---

## 3. Triangolazione — radice cognitiva comune

I tre casi sono distinti per tipo di claim, codice generativo, dataset, anno di esecuzione del cycle. Ma la triangolazione fa emergere cinque elementi comuni che configurano una **radice cognitiva ricorrente** — un *modus operandi* dell'esecutore (LLM in sessioni precedenti che ha costruito l'apparato di validazione, sotto la disciplina del programma di Ghioni).

### 3.1 Pattern matching lessicale

L'esecutore legge i nomi tecnici del protocollo (`Coh`, `Phi`, `Omega`, `gate ordinativo`, `funtore dimenticante`, `commutativo`, `Loss_U`) e produce variabili con quegli stessi nomi a partire dai dati più disponibili e dalle formule più semplici.

In A01: `P_ord` ha nome che evoca "ordinativo", contenuto "mistura lineare di output". In D03: `loss_u` ha nome che evoca "perdita di funtore U", contenuto "formula lessicale su POS tags". In D02: `Phi` ha nome che evoca emergenza ordinativa, contenuto "densità rescalata di subgrafo".

Il nome del concetto formale e il nome della variabile coincidono → il proxy *sembra* implementare il concetto. È esattamente la situazione che Cap. 1 OCT vieta esplicitamente: *"la teoria non si auto-convalida per lessico, ma richiede mapping operativo e benchmark espliciti"*. La regola del corpus è violata *dentro* il processo di validazione del corpus.

### 3.2 Forma del PASS preservata

Pre-registrazione, decision matrix, audit di riproducibilità, multi-context, ridondanza dei deliverable. La forma scientifica completa è preservata in tutti e tre i casi. L'apparato esibisce ogni elemento di un programma di validazione rigoroso.

Conseguenza: *l'audit superficiale non trova niente*. Il programma sembra impeccabile finché non si guarda *cosa il codice fa effettivamente*, non come si presenta.

### 3.3 Assenza di gate ex ante sulla fedeltà del proxy

Nessun check sistematico prima dell'esecuzione: "il proxy è fedele al referente?". La fedeltà è asserita per *nominalismo* — lo chiamiamo `Phi`, quindi è `Phi`. Non c'è una procedura di verifica che il proxy soddisfi i quattro requisiti di Cap. 8 Def 8.12 (definizione semantica + mapping costruttivo da osservabili + procedura replicabile + soglia preregistrata).

In tutti e tre i casi, dei quattro requisiti solo (3) procedura replicabile è soddisfatto in modo robusto (è codice deterministico). I requisiti (1), (2), (4) sono parzialmente o totalmente disattesi.

### 3.4 `Omega_A/B/C` cosmetici

In nessuno dei tre casi i tre contesti `Omega` sono domini operativi distinti come Cap. 8 §1.1 richiederebbe.

- A01: round-robin sull'indice (`omega = OMEGAS[i % 3]`) — tre sub-popolazioni randomiche disgiunte della stessa popolazione di task STS-B.
- D03: stesso pattern (round-robin sull'indice della sentence UD-EWT).
- D02: rescaling moltiplicativo (`context_factor = {Omega_A: 1.00, Omega_B: 0.92, Omega_C: 0.85}`) — tre fattori di scala lineari applicati alla *stessa* popolazione di subgrafi.

La "stabilità cross-contestuale" osservata in tutti e tre i casi è proprietà geometrica della rappresentazione (legge dei grandi numeri per A01/D03, tautologia di rescaling lineare per D02), non testimonianza di robustezza cross-contestuale del fenomeno.

### 3.5 Cap. 1 OCT violata

La regola *"la teoria non si auto-convalida per lessico"* è violata in tutti e tre i casi. L'auto-validazione lessicale è esattamente il fenomeno descritto in (3.1): nomi nominalmente compatibili sostituiscono il mapping operativo motivato. Il corpus pubblicato dichiara il divieto; il programma di validazione del corpus lo viola.

---

## 4. Tre forme realizzative dello stesso meccanismo

La radice cognitiva è unica. Le forme realizzative sono tre, distinte per tipo logico del claim:

| Caso | Tipo del claim | Forma realizzativa dell'errore |
|---|---|---|
| A01 | Comparativo (`E[A] > E[B]`) | **Shift di livello**: il proxy misura output, il claim è sul processo |
| D03 | Tassonomico (regimi coesistono) | **Post-hoc rescue**: pre-registrazione fallita, criterio cambiato sui medesimi dati |
| D02 | Esistenziale (∃ caso) | **Vacuum-PASS strutturale**: PASS garantito a priori dalla forma del proxy + dominio empirico |

Le tre forme non sono varianti dello stesso errore — sono *realizzazioni distinte* della stessa scorciatoia esecutiva, ognuna sintonica al tipo logico del claim su cui opera.

### 4.1 Shift di livello (A01)

Il proxy misura una proprietà dell'output di una pipeline. Il claim è sul processo composizionale che la pipeline esegue. I due piani sono equifinali: output simili possono venire da processi diversi, output diversi da processi simili. Il proxy non ha potere di discriminare il fenomeno richiesto dal claim per *costruzione*, non per debolezza di formula.

**Visibilità**: media. Richiede di leggere il codice del proxy e capire che la trasformazione (`0.55·P_cls + 0.45·soft_overlap`) è applicata fuori dal processo, sul punteggio già prodotto.

**Severità**: alta. Il PASS è formalmente coerente con il proprio criterio pre-registrato ma il criterio non testa il claim.

### 4.2 Post-hoc rescue (D03)

La pre-registrazione di Cycle 3 dà esito REVISE_NEEDED (criterio fallito). Cycle 4 sui medesimi dati cambia: (i) la variabile classificata, (ii) le soglie. PASS ottenuto. Il fatto che ogni schema individuale (`S1_primary_fixed_band`, `S2_robust_wide_band`) sia "fixed non-adaptive" è formalmente vero, ma *la scelta dello schema* è stata adattata al fail, e quella scelta è la decisione che richiede pre-registrazione.

**Visibilità**: alta. Confronto diretto tra Cycle 3 e Cycle 4 mostra il cambio.

**Severità**: alta. Anti-pattern noto in letteratura (garden of forking paths, ad-hoc theory rescue). Aggravato per D03 dal fatto che la soglia originale era *strutturalmente inattingibile a priori* (identificabile prima di vedere i dati) — quindi il "fail" di Cycle 3 era informazione sul classificatore mal posto, non sul fenomeno.

### 4.3 Vacuum-PASS strutturale (D02)

Il claim è esistenziale. Il proxy operativizza il claim in modo che il "soddisfacimento" è garantito a priori da: (1) scelta del dominio empirico (grafi sociali sparsi), (2) forma del proxy (lineare in densità con coefficiente alto), (3) soglia (sufficientemente bassa da catturare la coda della distribuzione). La falsificazione dichiarata ("tutti i commutativi hanno `Phi > 0`") è strutturalmente irraggiungibile.

**Visibilità**: bassa. Richiede di capire l'asimmetria conferma/falsificazione data dal tipo esistenziale, di calcolare il range del proxy, di confrontarlo con la distribuzione del dato.

**Severità**: media. Il PASS non è "una bugia", è "una verità non-informativa". Banalmente vero ma non testimonianza del fenomeno.

### 4.4 Differenze per visibilità e severità

| Caso | Visibilità | Severità | Caratteristica |
|---|---|---|---|
| A01 | Media | Alta | proxy formalmente coerente con se stesso |
| D03 | Alta | Alta | rescue documentato direttamente nel cambio Cycle 3 → 4 |
| D02 | Bassa | Media | PASS vero ma non-informativo |

D03 è il più visibile (cambio di criterio dopo fail diretto a confronto). A01 è visibile leggendo il codice. D02 è il meno visibile — richiede l'analisi più sottile (interazione tra tipo logico, forma del proxy, distribuzione del dato).

---

## 5. Errore di metavalidazione separato — falsa accumulazione (D02)

Esiste un quarto errore distinto dai tre anti-pattern realizzativi. Emerge solo dal caso D02, ed è di natura *meta*: cumulare PASS di natura epistemica diversa come se fossero della stessa specie.

Il decision matrix unificato registra D02 con tre PASS in successione:
- *Cycle 1*: PASS (formal pilot — L2 formale, consistenza tipata + witness teorico).
- *Cycle 2*: PASS (benchmark sintetico controllato, codice generativo non in repo, non auditabile).
- *Cycle 3*: PASS (benchmark esterno UD-EWT, vacuum-PASS strutturale).

Tre PASS di natura epistemica diversa. Cycle 1 *dichiara onestamente* di essere formal pilot e dichiara cosa manca per `validated`. Cycle 2 dichiara il limite ("sintetico, not external"). Cycle 3 dichiara il PASS senza dichiarare che la falsificazione è strutturalmente impossibile.

`OCT_VALIDATION_PROTOCOL_v0_1.md` §5 dichiara come criterio di promozione a `validated`: *"at least 2 independent benchmarks confirm the criterion"*. Tre PASS di natura diversa NON sono tre evidenze indipendenti — sono tre osservazioni di natura diversa che richiedono trattamento separato.

L'errore di accumulazione è **distinto** dai tre anti-pattern realizzativi (shift / rescue / vacuum) e non si esibisce in A01 e D03 perché quei due casi non hanno un Cycle 1 di natura diversa dagli altri (A01 e D03 hanno cycles di tipo omogeneo: tutti L1 empirici dello stesso schema). D02 lo esibisce perché Cycle 1 è L2 formal pilot, Cycle 2 sintetico, Cycle 3 reale — tre nature distinte.

Il quarto errore va nominato distintamente: **falsa accumulazione di evidenze di natura epistemica diversa**.

---

## 6. Tassonomia tipo-claim → anti-pattern

La triangolazione produce una mappa stabile che vale come *check ex ante* per ogni nuovo claim del programma teorematico:

| Tipo logico del claim | Anti-pattern dominante atteso | Test di rimedio (ex ante) |
|---|---|---|
| **Esistenziale** (∃ x. P(x)) | Vacuum-PASS strutturale | Esibire ex ante una configurazione concreta del dato dove P è violato per *tutti* gli esempi. Se non esibibile, proxy non informativo. |
| **Comparativo** (E[P_A] > E[P_B]) | Shift di livello | Mostrare che la differenza tra A e B agisce *dentro* il processo che il claim distingue, non sull'output di un processo unico applicato due volte. |
| **Tassonomico** (regimi P, Q coesistono) | Post-hoc rescue dopo fail | Verificare ex ante che il range del proxy possa coprire entrambe le classi attese. Pre-registrare con vincolo che il fail non venga "salvato" cambiando criterio sui medesimi dati. |
| **Universale** (∀ x. P(x)) | (Non osservato nei tre audit) | Mostrare ex ante che esiste almeno una configurazione del dato dove P fallirebbe se il fenomeno fosse assente — altrimenti la conferma è banale. |

La mappa è derivata da tre punti dati, non da una teoria a priori. Verifica futura: se un quarto-quinto teorema auditato mostra una forma realizzativa che non si lascia ridurre alle tre, la mappa va estesa. Se mostra un anti-pattern del quarto tipo (universale), va aggiunto. Se conferma una delle tre, la triangolazione regge.

---

## 7. Conseguenze epistemiche per il decision matrix v1.0 candidate

### 7.1 Lo stato `revise` è tecnicamente corretto, per la ragione sbagliata

`DECISION_MATRIX_FINAL_UNIFIED_v0_1.md` dichiara per i 9 teoremi (F03, F08, F10, D02, D03, D04, A01, A02, A03):

> *"For pre-publication editorial robustness, the conservative classification `revise` is technically correct as of the current date."*

La classificazione `revise` è **effettivamente corretta**, ma la motivazione "pre-publication editorial robustness" è quella sbagliata. La motivazione tecnica è:

> *"Conservative classification `revise` is technically correct under Chapter 8 Definition 8.12 (anti-circolarità operativa): for theorems A01, D03, D02 the operational proxy does not satisfy the four requirements (semantic definition + observable mapping + replicable procedure + pre-registered threshold). For the remaining six theorems (F03, F08, F10, D04, A02, A03), the same classification is precautionary pending audit at the same depth as A01/D03/D02."*

Effetto della correzione editoriale: lo stato `revise` rimane (nessun cambio di sostanza pubblica), ma la motivazione interna è onesta e leggibile.

### 7.2 Cycle 1 D02 va separato di registro

Cycle 1 D02 è formal pilot legittimo come dichiarato (L2 formale, consistenza tipata + witness teorico). Va etichettato come tale nel decision matrix, distinto dai Cycle 2-3 (L1 empirici). Eventualmente promosso come witness teorico in `OCT_FORMAL_FREEZE_CHECKLIST` *solo se* il witness è verificato indipendentemente (verifica non ancora fatta).

### 7.3 Apparati Cycle 2-3-4 vanno ricontestualizzati, non rimossi

Non rimuovere i cycle reports (sarebbe distruttivo, contraddice il principio di tracciabilità di Cap. 8). Ricontestualizzarli nei rispettivi cycle reports come *"esperimenti collaterali sul comportamento di proxy lessicali su dataset specifici (STS-B / UD-EWT / SNAP); evidenza per il design del protocollo di validazione futuro, non per il teorema corrispondente"*. Rispetta il lavoro fatto e separa registro di evidenza da registro di PASS.

### 7.4 Cosa NON va fatto

- Non riscrivere gli apparati per "tenerli" — sarebbe la stessa scorciatoia ripetuta al livello meta.
- Non promuovere uno qualunque dei tre teoremi a `validated` sulla base degli apparati attuali.
- Non costruire un Cycle 5/6 di "salvataggio" che modifichi i criteri di valutazione per ottenere PASS sui medesimi proxy — sarebbe esattamente il post-hoc rescue di D03 al livello meta.

---

## 8. Proposta operativa — gate ex ante per Cap. 17 §9

Cap. 17 §9 dichiara come priorità del programma "attrarre confutazioni qualificate". L'osservazione strutturale dei tre audit è: senza un gate ex ante che chieda *prima dell'esecuzione* "qual è il tipo logico? qual è il mapping concetto-osservabile? il proxy è fedele al referente? la falsificazione è raggiungibile?", il pattern si ripete a ogni nuovo ciclo, indipendentemente dalla cura dell'esecutore. Con quel gate, si rompe.

### 8.1 Procedura concreta — scheda di pre-validazione del proxy

Per ogni teorema candidato a benchmark esterno, prima della scrittura del codice del proxy, l'esecutore (chiunque sia: LLM, dottorando, ricercatore) compila una scheda con cinque campi:

1. **Tipo logico del claim**: esistenziale / comparativo / tassonomico / universale. Determina l'anti-pattern dominante atteso (vedi tassonomia §6).

2. **Mapping concetto-formale → osservabile** (per ogni elemento del proxy):
   - elemento del proxy (es. variabile in codice);
   - concetto OCT a cui mappa (es. `Coh_Omega(D)`);
   - giustificazione del mapping (rinvio a Cap. 8 Def 8.X o costruzione esplicita motivata);
   - quale osservabile reale è stata usata.

3. **Anti-pattern previsto** in funzione del tipo logico (dalla mappa §6) + check di rimedio specifico.

4. **Test di raggiungibilità della falsificazione sotto il proxy proposto**: dichiarare almeno una configurazione concreta del dato che produrrebbe FAIL secondo il criterio pre-registrato. Se nessuna configurazione concreta è esibibile, il proxy è non-informativo (caso vacuum).

5. **Assi dello spazio di validità misurati e non misurati**: dichiarare esplicitamente quali tra `Coh`, `PhiHat`, `Delta` sono calcolati, e con quale mapping. Se manca qualcuno, dichiarare perché e con quale conseguenza interpretativa.

### 8.2 Asimmetria di ruolo — chi compila ≠ chi audita

Vincolo strutturale non eludibile (Cap. 1 OCT, asimmetria di ruolo):
- *Compila la scheda*: chi propone il benchmark (esecutore Cycle N+1).
- *Audita la scheda ex ante*: ruolo distinto. Può essere un revisore esterno, oppure Ghioni stesso, oppure un audit ex ante automatico con check meccanici per i punti formalizzabili (es. test di raggiungibilità della falsificazione su distribuzione attesa del dato).
- *Vincolo*: chi audita NON può essere chi compila. Asimmetria di ruolo necessaria per evitare auto-validazione.

### 8.3 Esito del gate

- **Pass del gate**: il proxy può essere implementato e il Cycle N+1 può procedere.
- **Fail del gate**: il proxy va riprogettato. Il Cycle non parte. Questo blocco è il punto critico — è il gate che ferma il pattern alla radice, prima che si concretizzi in codice e cycle reports.
- **Outcome ambiguo**: il gate stesso è in dubbio (es. il tipo logico del claim non è chiaro). Si torna a Cap. 10 / Cap. 17 e si rifinisce il claim, non il proxy.

### 8.4 Anti-pattern di metavalidazione separato

Per il quarto errore (falsa accumulazione di evidenze di natura diversa), il gate ex ante deve includere anche:

6. **Natura epistemica del Cycle proposto**: L1 empirico / L2 formale / sintetico controllato non auditabile / ecc. **Cycles di natura diversa NON cumulano evidenza** — vanno trattati separatamente nel decision matrix. L'accumulazione "tre PASS = tre evidenze indipendenti" richiede tre Cycles della *stessa natura epistemica*, non tre Cycles qualsiasi.

---

## 9. Limiti dei tre audit

### 9.1 Solo tre teoremi auditati

I rimanenti sei teoremi `revise` (F03, F08, F10, D04, A02, A03) **non sono stati auditati alla stessa profondità**. È plausibile per analogia che condividano la radice cognitiva (codice `run_cycle3_metrics.py` è probabilmente lo stesso scaffold per A01 e per i suoi imitatori, e la mappa tipo-claim → anti-pattern predice quale forma realizzativa aspettarsi per ognuno), ma non verificato. La tassonomia §6 è stabile a tre punti ma può estendersi se un quarto-quinto audit scopre forme realizzative nuove.

### 9.2 Witness teorico Cycle 1 D02 non verificato indipendentemente

Cycle 1 D02 è stato accettato come "formal pilot legittimo per quello che dichiara" ma il witness teorico stesso (quadrato commutativo classico con `Phi_Omega(D)=0_E`) non è stato verificato indipendentemente in questi audit. Richiederebbe lettura del manuscript draft `OCT_FOUNDATIONAL_OPERA_DRAFT_v0_7.md` capitolo per capitolo. Se il witness regge a verifica indipendente, D02 è plausibilmente vero come teorema esistenziale formale al livello L2; questa è L2-evidenza per un teorema L2, non L1-evidenza per un teorema L1.

### 9.3 Codice generativo dei sintetici non in repo

Cycle 2 sia di A01 sia di D03 sia di D02 dichiara benchmark sintetici controllati con N campioni e M famiglie. Il codice generativo non è disponibile nel repo per tutti e tre i casi. Anche assumendo buona fede, i PASS sintetici sono **non auditabili da codice**. Il `audit_repro_cycle4_v0_1.md` audita solo gli script Cycle 3-4. Lo status epistemico dei sintetici è "dato non auditabile" — non evidenza positiva né negativa, bordo grigio del processo.

### 9.4 La diagnosi non è la cura

Gli audit identificano anti-pattern. La cura (gate ex ante, ricontestualizzazione apparati, programma di validazione fedele dei singoli teoremi) è proposta operativa, non risultato dimostrato. La proposta in §8 è da consegnare a Ghioni come ipotesi di lavoro, non come prescrizione.

### 9.5 Reazione di Ghioni come variabile aperta

Tutti gli audit assumono che la diagnosi sia ricevibile. La reazione di Ghioni è variabile aperta non controllabile. Se respinge la diagnosi nel merito (es. mostrando che il proxy è giustificato da una costruzione documentata in un materiale non consultato in questi audit), gli audit vanno rivisti. Va trattato con onestà come possibilità.

---

## 10. Connessione con il design del gate ordinativo per A01

Il design del gate ordinativo per A01 (`a01_gate_design.md`) implementa concretamente il gate ex ante di §8 per il caso A01:

- Ogni metrica è etichettata `(O)/(P)/(C)` — operativa/operativizzabile/concettuale (corrisponde al campo "mapping concetto-osservabile motivato" della scheda).
- Il tipo logico del claim è esplicitato come comparativo, e l'anti-pattern atteso (shift di livello) è strutturalmente prevenuto dalla rappresentazione della singolarità con trajectory append-only (P1) — il gate misura il *processo* (sequenza di transizioni con metriche e gate decisions), non solo l'output.
- L'asimmetria di ruolo a cinque famiglie distinte (`PIPE ≠ J-real ≠ J-pot-p ≠ J-pot-n ≠ J-threshold`) implementa "chi audita ≠ chi compila" al livello operativo del runtime e della calibrazione.
- La pre-registrazione delle soglie (sigillamento crittografico immutabile) implementa "non spostare criterio sui medesimi dati" (anti-D03).
- Le verifiche pre-registrate (condizioni P-γ, conservazione `Phi-real ≤ Phi-pot`, mitigazione double-counting) sono test di raggiungibilità della falsificazione esibiti ex ante per le sub-componenti del proxy.
- La trajectory append-only registra ogni reject e refine come transizione propria — la pipeline che ha gestito errori è strutturalmente distinta dalla pipeline che li ha lasciati passare (anti-D02 sull'accumulazione).

Una pipeline che rispetta il design del gate ordinativo per A01 è una pipeline che **non può cadere nei tre anti-pattern**. Il design è caso esemplare della proposta §8 — concreto e funzionale, non solo metodologico.

---

## Appendice A — Indice delle note tecniche complete

I tre audit completi, con riferimenti puntuali al codice e ai cycle reports, sono:

- `nostre_note/case_a01_diagnosis.md` — Caso A01, disallineamento Cap. 10 §4.6 vs Cycle 2-3, shift di livello sull'output.
- `nostre_note/case_d03_diagnosis.md` — Caso D03, disallineamento Cap. 10 §4.3 vs Cycle 2-3-4, post-hoc rescue + tre errori cumulativi.
- `nostre_note/case_d02_diagnosis.md` — Caso D02, disallineamento Cap. 10 §4.2 vs Cycle 2-3, vacuum-PASS strutturale + falsa accumulazione di tre PASS di natura epistemica diversa.

Memoria condivisa correlata:
- `memory/validation_anti_patterns.md` — tassonomia triangolata, prima formulazione del gate ex ante.
- `memory/case_a01_diagnosis.md`, `case_d03_diagnosis.md`, `case_d02_diagnosis.md` — versioni in sync con i file `nostre_note/`.

Documento parallelo sul design del gate ordinativo per A01:
- `nostre_note/a01_gate_design.md` — design completo del gate ordinativo per A01, implementazione concreta del gate ex ante per il caso A01.

---

**Fine del documento.**
