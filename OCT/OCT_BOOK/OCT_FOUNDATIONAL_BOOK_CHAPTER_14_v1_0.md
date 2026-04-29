# Capitolo 14 - Governance epistemica: versioning, audit trail, quality gates

Metadati:
- Versione: v1.0
- Data: 2026-04-22
- Stato: draft completo
- Autore: Fabio Ghioni
- Allineato a: TE_CORE v5.1 / OST v2.1 / OCT baseline v1.0 candidate
- Dipendenze: Capitoli 12-13, decision matrix unificata, tracker pubblicazione
- Target parole capitolo: 2.500

---

## 1. Problema

Una teoria può avere buone definizioni e buoni benchmark, ma fallire comunque come programma scientifico se non possiede una governance epistemica esplicita.

Nel contesto OCT, il rischio non e solo tecnico. E istituzionale:

1. stati dei claim aggiornati in modo incoerente tra file diversi;
2. release pubbliche prive di tracciabilità decisionale;
3. conflitti tra risultati locali e narrativa generale del progetto.

Per questo il problema del capitolo e netto:

**quale sistema di regole permette di governare nel tempo il passaggio dei claim tra `draft`, `in_proof`, `validated/revise/reject`, mantenendo trasparenza, reversibilità controllata e responsabilità editoriale?**

### 1.1 Perché la governance e parte della teoria

In OCT la validità non e solo proprietà logica di una formula: e proprietà processuale di una catena evidenziale.

Di conseguenza:

1. senza governance, la teoria non scala oltre il laboratorio originario;
2. senza audit trail, la validazione non e verificabile retrospettivamente;
3. senza quality gate, la pubblicazione rischia di confondere stato ipotetico e stato consolidato.

### 1.2 Ruolo nella milestone `v1.4`

Con questo capitolo si chiude il blocco metodologico.

1. Capitolo 12: protocollo di decisione;
2. Capitolo 13: infrastruttura benchmark;
3. Capitolo 14: costituzione operativa del corpus.

Dopo questo punto il libro può passare ai case study (Capitoli 15-16) senza perdere rigore di stato.

---

## 2. Tesi del capitolo

La tesi e articolata in dieci enunciati.

1. Ogni claim OCT deve avere doppio stato: formale e decisionale.
2. Lo stato decisionale e valido solo se ancorato a evidenza tracciata e versionata.
3. I quality gate devono essere pubblici, finiti e verificabili ex post.
4. Ogni cambio di stato deve essere reversibile solo tramite procedura esplicita.
5. Le deviazioni dal protocollo sono ammesse solo con eccezione registrata.
6. L'audit trail e parte del risultato scientifico, non metadato accessorio.
7. Il versioning epistemico deve distinguere evoluzione teorica da evoluzione empirica.
8. La pubblicazione multi-piattaforma richiede sincronizzazione di stato e identificatori.
9. Le decisioni `revise` non sono fallimenti: sono meccanismi di controllo della deriva.
10. Il sistema proposto e sufficiente per governare la fase case-study e la transizione a preprint stabile.

---

## 3. Definizioni canoniche

### Definizione 14.1 (Stato formale)

Stato formale di un claim nel programma teorematico:

`S_form in {draft, in_proof, validated}`.

### Definizione 14.2 (Stato decisionale)

Stato decisionale basato su evidenza operativa:

`S_dec in {validated, revise, reject}`.

`S_dec` non sostituisce `S_form`, ma lo qualifica per uso editoriale e pubblicazione.

### Definizione 14.3 (Record di stato)

Un record minimo di stato e:

`R_state := <ClaimID, S_form, S_dec, EvidenceRef, DecisionDate, Version, Signatures>`.

### Definizione 14.4 (Quality Gate)

Un quality gate `G_k` e una condizione booleana preregistrata che deve risultare `PASS` per autorizzare un tipo specifico di rilascio.

### Definizione 14.5 (Eccezione governance)

Eccezione governance: deviazione motivata da procedura standard, registrata con:

1. motivo;
2. rischio introdotto;
3. mitigazione;
4. data di scadenza dell'eccezione.

### Definizione 14.6 (Audit trail epistemico)

Catena ordinata di evidenze e decisioni che permette di ricostruire integralmente:

1. quali dati sono stati usati;
2. quali criteri erano attivi;
3. perché uno stato e cambiato.

---

## 4. Sviluppo formale

### 4.1 Architettura governance a quattro strati

La governance proposta e composta da quattro strati coordinati.

1. **Strato G1 - Semantico**: definizioni, notazione, perimetro del claim.
2. **Strato G2 - Evidenziale**: benchmark, metriche, report, repliche.
3. **Strato G3 - Decisionale**: matrice `validated/revise/reject`.
4. **Strato G4 - Rilascio**: gate, versioning, pubblicazione.

Un errore in un singolo strato può invalidare il rilascio anche se gli altri tre sono coerenti.

### 4.2 Doppio stato e regole di coerenza

Definiamo regole minime di coerenza tra `S_form` e `S_dec`.

1. se `S_form = draft`, allora `S_dec` non può essere `validated`;
2. se `S_dec = reject`, il claim non può essere promosso senza nuova evidenza versionata;
3. se `S_dec = revise`, il claim resta pubblicabile solo con etichetta esplicita di provvisorieta;
4. promozione a `S_form = validated` richiede allineamento con decisione non conflittuale e gate di rilascio superati.

Queste regole evitano inversioni narrative del tipo "teorema consolidato" con evidenza ancora in revisione.

### 4.3 Versioning epistemico

Il versioning deve distinguere almeno tre dimensioni:

1. `V_theory`: cambi nella formalizzazione/assiomatica;
2. `V_evidence`: cambi nei benchmark, dataset o analisi;
3. `V_release`: confezionamento editoriale/pubblicazione.

Regola:

1. una modifica in `V_evidence` senza modifica teorica non autorizza riscrittura implicita di claim;
2. una modifica in `V_theory` richiede rivalutazione esplicita delle evidenze collegate;
3. ogni release pubblica deve dichiarare la tripla versione (`V_theory`, `V_evidence`, `V_release`).

### 4.4 Quality gate standard `G0-G6`

Proponiamo sette gate minimi.

1. `G0` - completezza metadati (`PASS/FAIL`);
2. `G1` - integrità artefatti (manifest + hash);
3. `G2` - preregistrazione e criteri decisionali bloccati;
4. `G3` - evidenza benchmark indipendente minima;
5. `G4` - audit trail leggibile e ripercorribile;
6. `G5` - coerenza tra stato formale e decisionale;
7. `G6` - checklist pubblicazione multi-piattaforma allineata.

Policy:

1. `FAIL` su `G0-G2` blocca qualsiasi release;
2. `FAIL` su `G3-G5` blocca release "claim-strong" e consente solo release di lavoro;
3. `FAIL` su `G6` consente rilascio locale ma non rilascio ufficiale.

### 4.5 Procedura di cambio stato (PCS-6)

Ogni cambio stato deve seguire sei passi.

1. proposta di cambio con motivazione;
2. verifica automatica gate disponibili;
3. revisione umana indipendente minima;
4. emissione decisione e firma;
5. aggiornamento record `R_state`;
6. pubblicazione del changelog decisionale.

La PCS-6 rende il cambio di stato una procedura, non un atto implicito.

### 4.6 Gestione eccezioni e debito epistemico

Le eccezioni non vanno eliminate, vanno governate.

Per ogni eccezione registriamo:

1. grado di rischio (`low/medium/high`);
2. scadenza entro cui rientrare in procedura standard;
3. owner responsabile del rientro;
4. impatto su gate e release ammesse.

L'accumulo di eccezioni oltre soglia definisce debito epistemico e obbliga una release dedicata di consolidamento.

### 4.7 Audit trail minimo pubblicabile

Ogni rilascio claim-sensitive deve includere:

1. decision matrix corrente;
2. stato teoremi allineato;
3. riferimenti ai report benchmark rilevanti;
4. log sintetico dei cambi di stato;
5. elenco eccezioni aperte e chiuse.

Senza questo bundle, un revisore esterno non può verificare la storia decisionale.

### 4.8 Governance multi-piattaforma

Per GitHub, Zenodo, OSF, Hugging Face il principio e uno: **stesso stato, stessa versione, stesso claim ledger**.

Sincronizzazioni obbligatorie:

1. ID versione release;
2. checksum dei pacchetti dati;
3. decision table di riferimento;
4. timestamp di emissione.

Divergenze tra piattaforme sono trattate come incidenti di governance.

### 4.9 Politica di comunicazione dello stato

Ogni documento pubblico che cita un claim deve riportare etichetta di stato nel punto d'uso.

Formato raccomandato:

`ClaimID [S_form / S_dec / EvidenceLevel]`.

Esempio:

`D03 [in_proof / revise / S2]`.

Questo riduce ambiguità per lettori nuovi e impedisce overclaiming involontario.

### 4.10 Condizione di sufficienza del capitolo

La governance e sufficiente se garantisce contemporaneamente:

1. tracciabilità completa dei cambi stato;
2. regole di blocco rilascio verificabili;
3. allineamento stabile tra teoria, evidenza e pubblicazione.

La condizione e soddisfatta dall'integrazione di G1-G4 con PCS-6, gate `G0-G6` e policy multi-piattaforma.

### 4.11 Indicatori di salute della governance (KPI-E)

Per monitorare se la governance funziona nel tempo proponiamo cinque indicatori periodici:

1. `K1_time_to_decision`: tempo medio tra chiusura benchmark e decisione ufficiale;
2. `K2_trace_completeness`: percentuale record con audit trail completo;
3. `K3_exception_debt`: numero eccezioni aperte oltre scadenza;
4. `K4_sync_gap`: discrepanze di stato tra piattaforme pubbliche;
5. `K5_revise_stagnation`: claim in `revise` senza piano attivo di uscita.

Uso operativo:

1. soglie KPI fissate trimestralmente;
2. superamento soglia produce azione correttiva obbligatoria;
3. trend peggiorativo su due finestre consecutive blocca release non critiche.

Questo blocco evita che la governance resti un disegno statico e la trasforma in sistema vivo, misurabile e migliorabile.

### 4.12 Registro delle decisioni contestate

Una governance matura deve prevedere anche disaccordo strutturato.  
Per questo ogni contestazione formale a una decisione va registrata in un log dedicato con:

1. decisione contestata e riferimento al record `R_state`;
2. motivo tecnico della contestazione;
3. evidenza addizionale proposta;
4. esito della revisione (conferma, modifica, sospensione).

Il registro non indebolisce l'autorità del processo: la rende verificabile e correggibile.

---

## 5. Proposizioni e teoremi locali

### Proposizione 14.1 (Necessità del doppio stato)

Enunciato:
Un singolo stato non distingue adeguatamente maturità formale e maturità evidenziale del claim.

Intuizione:
la stessa formula può essere formalmente elegante ma sperimentalmente ancora instabile.

Stato: `validated`.

### Proposizione 14.2 (Funzione anti-deriva dei gate)

Enunciato:
Un sistema di gate pubblici riduce la probabilità di promozioni opportunistiche di stato.

Intuizione:
vincoli espliciti rendono costoso ignorare evidenze negative o incomplete.

Stato: `validated`.

### Proposizione 14.3 (Valore epistemico delle eccezioni tracciate)

Enunciato:
Eccezioni registrate e temporalmente limitate migliorano l'affidabilità complessiva rispetto a eccezioni implicite non documentate.

Intuizione:
la trasparenza dell'anomalia e preferibile alla sua invisibilità.

Stato: `in_review`.

### Teorema 14.4 (Consistenza procedurale della PCS-6)

Ipotesi:
1. applicazione completa della procedura PCS-6;
2. quality gate valutati prima della decisione;
3. aggiornamento record di stato obbligatorio.

Tesi:
La governance produce cambi di stato auditabili e confrontabili nel tempo.

Proof sketch:
1. la procedura serializza decisione e responsabilità;
2. i gate impongono condizioni minime verificabili;
3. il record standardizzato abilità confronto storico.

Conseguenze:
rende possibile una storia epistemica computabile del corpus OCT.

Stato: `in_proof`.

### Teorema 14.5 (Sufficienza dei gate `G0-G6` per rilascio claim-sensitive)

Ipotesi:
1. tutti i gate `G0-G6` in `PASS`;
2. allineamento tra ledger, decision matrix e stato teoremi;
3. assenza di eccezioni `high` scadute.

Tesi:
Il rilascio e metodologicamente idoneo a disseminazione scientifica pubblica.

Proof sketch:
1. `G0-G2` garantiscono base tecnica minima;
2. `G3-G5` garantiscono coerenza evidenziale e semantica;
3. `G6` garantisce consistenza cross-piattaforma.

Conseguenze:
fornisce criterio operativo unificato per pubblicazione OCT.

Stato: `in_proof`.

---

## 6. Implicazioni operative

### 6.1 Per chiusura milestone `v1.4`

Con il Capitolo 14 la milestone metodologica e chiusa quando:

1. Capitolo 12 (protocollo) e completo;
2. Capitolo 13 (benchmark design) e completo;
3. Capitolo 14 (governance) e completo e coerente con gli artefatti di validazione.

### 6.2 Per i case study (Capitoli 15-16)

Ogni case study dovra essere scritto con vincolo di stato esplicito:

1. quali claim usa;
2. in quale stato sono;
3. quali parti sono ipotesi operative e quali sono evidenze consolidate.

### 6.3 Per gestione editoriale

La governance permette un editing "forte" senza alterare significato epistemico:

1. si può migliorare il testo;
2. non si può migliorare lo stato senza nuova evidenza.

### 6.4 Per revisori e comunità scientifica

Un revisore esterno può ricostruire l'intera catena decisionale senza accesso privato al team, se il bundle governance e completo.

Questa proprietà e essenziale per credibilità internazionale del programma OCT.

### 6.5 Per ritmo operativo del team

La governance non deve solo \"controllare\"; deve anche dare ritmo alla ricerca.

Cadenza consigliata:

1. review settimanale dei gate per i claim attivi;
2. review mensile del debito epistemico;
3. review trimestrale dei KPI-E e delle policy eccezioni;
4. retrospettiva semestrale su versioning e coerenza multi-piattaforma.

Questa cadenza rende sostenibile il programma su orizzonte pluriennale senza accumulare disordine metodologico.

---

## 7. Limiti e non-claim

Limiti espliciti:

1. il modello di governance e baseline operativa, non costituzione definitiva;
2. alcuni domini ad alta sensibilità possono richiedere gate aggiuntivi;
3. la procedura non elimina il conflitto interpretativo, ma lo rende tracciabile.

Failure mode riconosciuti:

1. proliferazione di eccezioni non chiuse;
2. aggiornamento parziale dei record tra piattaforme;
3. uso improprio dello stato `revise` come zona grigia permanente;
4. eccesso di burocrazia che rallenta la ricerca viva.

Contromisure raccomandate:

1. revisione periodica del debito epistemico;
2. allineamento automatico dei ledger principali;
3. policy di scadenza massima per claim in `revise` senza piano;
4. semplificazione continua dei template senza perdere auditabilità.

Box C - Non-claim

Questo capitolo non implica:
1. che la governance sostituisca il valore creativo della teoria;
2. che ogni decisione governance sia incontestabile;
3. che un claim in `revise` sia scientificamente irrilevante.

---

## 8. Claim Ledger (S0-S3)

| ID | Claim | Tipo | Evidenza | Stato |
|---|---|---|---|---|
| C14.1 | Il doppio stato (`S_form`, `S_dec`) e necessario per evitare ambiguità epistemiche | governance-metateorica | S1 | validated |
| C14.2 | I gate `G0-G6` riducono la deriva decisionale in rilascio | metodologico-operativo | S1 | validated |
| C14.3 | La PCS-6 rende auditabili i cambi di stato | procedurale | S2 | in_proof |
| C14.4 | La sincronizzazione multi-piattaforma e condizione di credibilità esterna | infrastrutturale | S1 | in_review |
| C14.5 | La gestione esplicita delle eccezioni riduce il rischio epistemico cumulativo | governance-rischio | S1 | in_review |
| C14.6 | Il pacchetto governance e sufficiente per supportare la fase case-study | metaprogramma | S2 | in_proof |

---

## 9. Bridge al Capitolo 15

Con il Capitolo 14 il quadro metodologico dell'opera e completo:

1. protocollo di validazione (Cap. 12);
2. benchmark design e replicabilità (Cap. 13);
3. governance di stato e rilascio (Cap. 14).

Il Capitolo 15 entra nel primo caso studio fisico (standing waves e controfase strutturale), usando integralmente questa architettura come base di lettura e valutazione.

In sintesi: da qui in avanti l'opera non espone solo teoria OCT, ma mostra OCT in azione con disciplina scientifica esplicita.

---

## Riferimenti

Riferimenti di framework interno:

1. Ghioni, F. (2026). `TE_CORE_v5.1.md`.
2. Ghioni, F. (2026). `Ordinative_Set_Theory_OST_A_Concise_Guide_For_AI_v2_1.md`.
3. `OCT_FOUNDATIONAL_BOOK_CHAPTER_12_v1_0.md`.
4. `OCT_FOUNDATIONAL_BOOK_CHAPTER_13_v1_0.md`.
5. `OCT_Theory_and_Theorems/validation/DECISION_MATRIX_FINAL_UNIFIED_v0_1.md`.
6. `OCT_Theory_and_Theorems/validation/OCT_THEOREM_STATUS_ALIGNMENT_v1_0_candidate_v0_1.md`.
7. `OCT_Theory_and_Theorems/validation/OCT_PUBLICATION_PROGRESS_TRACKER_v0_1.md`.

Riferimenti primari:

1. Popper, K. (1959). *The Logic of Scientific Discovery*.
2. Lakatos, I. (1978). *The Methodology of Scientific Research Programmes*.
3. Merton, R. K. (1973). *The Sociology of Science*.
4. Goodman, S., Fanelli, D., Ioannidis, J. (2016). *What does research reproducibility mean?*.

