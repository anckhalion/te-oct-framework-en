# Capitolo 13 - Benchmark, disegno sperimentale, replicabilità multi-dominio

Metadati:
- Versione: v1.0
- Data: 2026-04-22
- Stato: draft completo
- Autore: Fabio Ghioni
- Allineato a: TE_CORE v5.1 / OST v2.1 / OCT baseline v1.0 candidate
- Dipendenze: Capitolo 12 (protocollo PV-8), OCT_VALIDATION_PROTOCOL_v0_1, report Cycle 2-4
- Target parole capitolo: 2.800

---

## 1. Problema

Il Capitolo 12 ha definito la grammatica metodologica della validazione OCT. Ma un protocollo, da solo, non garantisce prova robusta: serve un disegno benchmark che produca evidenza comparabile nel tempo, nei team e nei domini.

Nel lavoro ordinativo il rischio principale e doppio:

1. benchmark troppo facili, che confermano qualsiasi ipotesi già favorita;
2. benchmark non comparabili, che impediscono di distinguere progresso reale da variazione accidentale.

Per questo il problema del capitolo e preciso:

**come costruire un sistema benchmark multi-dominio che renda misurabile la differenza tra performance locale e validazione trasferibile, senza collassare la teoria in una pura ottimizzazione numerica?**

### 1.1 Dal protocollo all'infrastruttura

Il protocollo (Capitolo 12) risponde a "come decidere". Il benchmark design risponde a "su cosa decidere". La tenuta scientifica richiede entrambi.

Senza infrastruttura benchmark:

1. i claim restano narrativi;
2. le repliche sono episodiche;
3. la decisione `validated` resta fragile.

Con infrastruttura benchmark:

1. i claim sono testati in condizioni comparabili;
2. le repliche indipendenti diventano obbligatorie, non opzionali;
3. la curva di evidenza può essere monitorata per versione.

### 1.2 Scope della milestone `v1.4`

Il Capitolo 13 ha funzione ponte tra metodo e governance:

1. implementa la PV-8 in benchmark reali;
2. definisce la nozione operativa di indipendenza benchmark;
3. prepara il Capitolo 14 su audit trail, gate e versioning epistemico.

---

## 2. Tesi del capitolo

La tesi e articolata in dieci enunciati.

1. Un claim OCT e robusto solo se supera benchmark indipendenti per costruzione, non solo per nome.
2. L'indipendenza benchmark richiede separazione di dati, seed policy, tuning e log namespace.
3. La replicabilità multi-dominio e criterio strutturale, non supplemento statistico.
4. Le metriche canoniche (`Coh`, `Phi`, `Delta`) devono convivere con metriche specifiche per task.
5. La stratificazione dei casi e necessaria per evitare conferme trainate da sottogruppi facili.
6. L'analisi di sensibilità e parte del test principale, non appendice facoltativa.
7. Il fallimento parziale e informazione scientifica e va pubblicato con stessa disciplina dei successi.
8. Ogni benchmark deve includere policy di replay e criteri di rerun tracciati.
9. Un pacchetto benchmark senza manifest e hash non e considerato riproducibile oltre livello `R1`.
10. Il disegno proposto e sufficiente per sostenere la governance epistemica del Capitolo 14.

---

## 3. Definizioni canoniche

### Definizione 13.1 (Benchmark indipendente)

Due benchmark `B_i`, `B_j` sono indipendenti se valgono simultaneamente:

1. `D_i ∩ D_j` trascurabile rispetto a soglia preregistrata;
2. seed policy distinta;
3. assenza di tuning trasversale post-freeze;
4. log namespace separato e auditabile;
5. shift di distribuzione dichiarato e verificabile.

### Definizione 13.2 (Asse di dominio)

Un asse di dominio `A_k` e una famiglia coerente di contesti osservativi `Omega` che condividono:

1. tipo di oggetti/morfismi osservati;
2. regime di rumore dominante;
3. criteri semantici di errore.

Esempi operativi per OCT:

1. `A_struct`: strutture compositive e diagrammatiche;
2. `A_pipeline`: processi multi-step di trasformazione;
3. `A_social`: dinamiche narrative longitudinali.

### Definizione 13.3 (Pacchetto benchmark minimo)

`PB_min := <Manifest, Dataset, Script, Config, Hash, Report, DecisionTable>`.

Un benchmark e considerato pubblicabile solo se il pacchetto minimo e completo.

### Definizione 13.4 (Replicabilità multi-dominio)

Un claim e multi-dominio replicabile se la conferma si osserva in almeno due assi `A_k` con contesti non equivalenti banalmente.

### Definizione 13.5 (Stress strutturale)

Stress strutturale: perturbazione controllata che aumenta difficolta compositiva mantenendo il significato del claim.

### Definizione 13.6 (Indice di trasferibilità)

Per claim `C`:

`T_C := mean_k(score_k) - penalty_var`

con:

1. `score_k` performance ordinativa su asse `A_k`;
2. `penalty_var` penalità per variabilità eccessiva cross-dominio.

`T_C` alto indica robustezza trasferibile; `T_C` basso indica risultato locale.

---

## 4. Sviluppo formale

### 4.1 Architettura benchmark in tre livelli

Proponiamo un'architettura a tre livelli.

1. **Livello L1 (core test)**: verifica diretta del claim su benchmark principale.
2. **Livello L2 (indipendenza)**: replica su benchmark #2 con shift esplicito.
3. **Livello L3 (stress/audit)**: sensibilità a soglie, ablation, replay indipendente.

La regola e semplice:

1. L1 senza L2 produce solo evidenza preliminare;
2. L1+L2 senza L3 produce evidenza promettente ma incompleta;
3. L1+L2+L3 e condizione standard per decisione forte.

### 4.2 Disegno degli assi di dominio

Il framework OCT ha già evidenziato tre famiglie di test rilevanti:

1. D02 (commutatività non produttiva) su asse strutturale;
2. A01 (stabilità pipeline IA) su asse operativo-procedurale;
3. D03 (perdita ontologica forgetting) su asse misto strutturale-operativo.

Questa triade e utile perché copre:

1. differenza puramente compositiva;
2. utilità pratica su pipeline reali;
3. perdita di struttura sotto trasformazioni canoniche.

Il capitolo impone che ogni nuova campagna espliciti a priori quale asse copre e quale resta non coperto.

### 4.3 Criteri operativi di indipendenza

L'indipendenza non può essere dichiarata genericamente. Va verificata con checklist.

Checklist minima:

1. `NO` riuso campioni dal benchmark precedente oltre soglia consentita;
2. split dati congelato prima del run;
3. separazione delle seed rispetto al ciclo precedente;
4. divieto di tuning post-freeze;
5. motivazione obbligatoria per rerun con hash log.

Questi criteri sono coerenti con il manifest Cycle 3 e con la policy di execution lock già adottata.

### 4.4 Stratificazione campionaria e copertura

Ogni benchmark deve esplicitare stratificazione su tre assi:

1. complessità strutturale;
2. livello di rumore;
3. ambiguità contestuale.

Se uno strato e sottocampionato, il claim non può essere generalizzato. In pratica:

1. risultati aggregati senza breakdown di strato sono considerati incompleti;
2. la decisione può al massimo restare in `revise`.

### 4.5 Piano statistico minimo

Senza imporre un unico paradigma statistico, fissiamo cinque obblighi minimi:

1. ipotesi nulla/alternativa dichiarate;
2. soglia `alpha` preregistrata;
3. misura di effetto oltre al p-value;
4. intervalli di confidenza o stima di incertezza equivalente;
5. criterio di successo aggregato multi-contesto.

Il capitolo privilegia inferenza trasparente rispetto a ottimizzazione retorica di singole metriche.

### 4.6 Potenza e numerosità campionaria

La numerosità non può essere scelta solo per convenienza computazionale. Deve essere giustificata da:

1. variabilità attesa;
2. effetto minimo di interesse;
3. livello di confidenza richiesto per decisione.

Se la potenza e insufficiente, un esito "non significativo" non autorizza rigetto del claim; autorizza solo revisione del disegno.

### 4.7 Multi-contesto e regola 2/3

In continuità con i cicli già eseguiti, adottiamo una regola pragmatica:

1. conferma minima in almeno `2/3` contesti preregistrati;
2. il terzo contesto può fallire solo con analisi causale esplicita.

La regola evita due estremi:

1. rigidità eccessiva (richiedere successo perfetto in ogni micro-variante);
2. permissività eccessiva (accettare successo in un solo contesto favorevole).

### 4.8 Instrumentation e audit trail

La replicabilità dipende più dai log che dalle intenzioni. Ogni run deve produrre:

1. manifest versione dati e script;
2. checksum artefatti;
3. parametri runtime;
4. output metrici raw e aggregati;
5. decision trace leggibile.

Senza questa catena, il risultato resta al massimo `R1` e non supporta validazione forte.

### 4.9 Tassonomia degli errori

Per evitare diagnosi vaghe introduciamo una tassonomia minima degli errori benchmark:

1. `E_data`: incoerenza o leakage nei dati;
2. `E_model`: instabilità del mapping o della pipeline;
3. `E_metric`: mismatch tra metrica e significato del claim;
4. `E_context`: trasferimento improprio tra domini;
5. `E_decision`: applicazione incoerente della matrice decisionale.

Ogni errore va classificato in severità (`low`, `medium`, `high`) e associato ad azione correttiva.

### 4.10 Policy di rerun e freezing

Il rerun e lecito solo se:

1. motivazione tecnica documentata;
2. stessa preregistrazione o nuova preregistrazione versionata;
3. dichiarazione esplicita di cosa cambia e cosa resta invariato.

Il freezing conclude una fase sperimentale e blocca la retro-modifica opportunistica dei criteri.

### 4.11 Disegno per pubblicazione aperta

Un benchmark scientificamente utile e anche pubblicabile in forma verificabile.

Pacchetto raccomandato:

1. repository operativo (GitHub) con script e manifest;
2. snapshot DOI (Zenodo) della release validata;
3. workspace progettuale (OSF) con preregistrazioni e materiale intermedio;
4. eventuale mirror dataset (Hugging Face) con dataset card metodologica.

La chiave non e moltiplicare piattaforme, ma preservare coerenza di versione tra piattaforme.

### 4.12 Condizione di sufficienza del capitolo

Il capitolo e metodologicamente sufficiente se produce tre risultati:

1. definizione operativa di benchmark indipendente;
2. schema di replicabilità multi-dominio con criteri espliciti;
3. pipeline pubblicabile e auditabile end-to-end.

Questa condizione e soddisfatta dalle definizioni 13.1-13.6 e dai blocchi 4.1-4.11.

### 4.13 Indice di qualità benchmark `Q_B`

Per confrontare campagne diverse introduciamo un indicatore sintetico:

`Q_B := a*Ind + b*Rep + c*Trace + d*Stress - e*Leak`

dove:

1. `Ind` misura l'indipendenza effettiva tra benchmark;
2. `Rep` misura il tasso di repliche riuscite;
3. `Trace` misura la completezza dell'audit trail;
4. `Stress` misura copertura e severità dei test di sensibilità;
5. `Leak` penalizza leakage dati e tuning opportunistico.

Vincoli operativi:

1. coefficienti `a,b,c,d,e >= 0`;
2. `a+b+c+d+e = 1`;
3. soglia minima preregistrata per rilascio esterno.

`Q_B` non sostituisce la decisione teorica sul claim, ma decide la prontezza metodologica del pacchetto benchmark.

### 4.14 Protocollo di replica indipendente

Per dichiarare una replica realmente indipendente proponiamo il seguente protocollo minimo:

1. team esecutore differente da quello del benchmark originario;
2. ambiente ricostruito da zero usando solo artefatti pubblici;
3. verifica hash di dataset/script prima del run;
4. esecuzione senza modifica dei criteri decisionali preregistrati;
5. report finale con confronto puntuale tra esito originario e replica.

La replica indipendente non e una formalità: e il passaggio che trasforma un risultato interno in conoscenza affidabile per la comunità.

---

## 5. Proposizioni e teoremi locali

### Proposizione 13.1 (Insufficienza del benchmark nominalmente diverso)

Enunciato:
Due benchmark con nomi differenti ma senza separazione di dati/seed/tuning non forniscono evidenza indipendente.

Intuizione:
l'indipendenza e proprietà del processo, non dell'etichetta.

Stato: `validated`.

### Proposizione 13.2 (Necessità della stratificazione)

Enunciato:
Senza stratificazione esplicita, la performance aggregata può sovrastimare la robustezza di un claim.

Intuizione:
la media può nascondere collassi locali ad alta rilevanza teorica.

Stato: `validated`.

### Proposizione 13.3 (Valore informativo del fallimento)

Enunciato:
Nel contesto OCT, un fallimento tracciato e classificato aumenta informazione metodologica più di un successo non auditabile.

Intuizione:
il fallimento ben localizzato orienta revisione teorica e disegno successivo.

Stato: `in_review`.

### Teorema 13.4 (Sufficienza operativa del disegno L1-L2-L3)

Ipotesi:
1. benchmark L1 con preregistrazione completa;
2. benchmark L2 indipendente secondo Def. 13.1;
3. stress/audit L3 con report riproducibile.

Tesi:
Il claim testato dispone di evidenza metodologicamente sufficiente per decisione `validated/revise/reject` non arbitraria.

Proof sketch:
1. L1 fornisce test diretto del claim;
2. L2 limita overfitting al benchmark iniziale;
3. L3 misura robustezza a perturbazioni e integrità della catena di prova.

Conseguenze:
fornisce standard minimo per promozione di stato in catalogo teorematico OCT.

Stato: `in_proof`.

### Teorema 13.5 (Necessità della replicabilità multi-dominio)

Ipotesi:
1. claim confermato solo su un asse di dominio;
2. assenza di repliche su asse indipendente;
3. elevata variabilità potenziale tra contesti.

Tesi:
La conferma mono-dominio non e sufficiente per inferenza generale in OCT.

Proof sketch:
1. la semantica ordinativa dipende da `Omega`;
2. cambi di dominio alterano distribuzioni e vincoli compositivi;
3. senza replica multi-asse non si distingue effetto teorico da compatibilità locale.

Conseguenze:
legittima la regola di replicazione minima su assi multipli.

Stato: `in_proof`.

---

## 6. Implicazioni operative

### 6.1 Per il Capitolo 14 (governance epistemica)

Il capitolo consegna a `v1.4` tre oggetti che il Capitolo 14 dovra governare:

1. versioni benchmark e relativi freeze;
2. audit trail dei rerun;
3. criteri di accettazione legati a livelli di riproducibilità.

### 6.2 Per il programma di validazione teoremi

La struttura L1-L2-L3 permette di ordinare i teoremi in priorità:

1. teoremi ad alto impatto con percorso completo immediato;
2. teoremi esplorativi con L1 rapido e ingresso in coda L2/L3;
3. teoremi in conflitto con focus su stress e ablation prima del rilascio.

### 6.3 Per pubblicazione e revisione esterna

Un revisore esterno deve poter rispondere a tre domande senza ambiguità:

1. che cosa e stato testato;
2. come e stato testato;
3. perché la decisione finale e giustificata.

Il capitolo offre una struttura che rende queste risposte ispezionabili.

### 6.4 Per roadmap 2026-2030

La replicabilità multi-dominio e il criterio che separa:

1. risultati locali da risultati fondativi;
2. prototipi interni da standard scientifici pubblicabili.

Quindi la roadmap non dovrebbe contare solo "numero di teoremi testati", ma "numero di teoremi con L1-L2-L3 completo".

### 6.5 Per onboarding di nuovi laboratori

Un laboratorio esterno può entrare nel programma OCT senza conoscere tutta la storia del progetto, se riceve un kit standardizzato:

1. guida iniziale con lessico minimo condiviso;
2. pacchetto `PB_min` di un claim campione;
3. checklist di replica indipendente;
4. template report con sezione errori obbligatoria.

Questo riduce la barriera d'ingresso e aumenta la probabilità di validazioni indipendenti reali.

---

## 7. Limiti e non-claim

Limiti espliciti:

1. il capitolo definisce una baseline metodologica, non l'unica possibile;
2. alcuni domini richiedono metriche ausiliarie altamente specializzate;
3. la regola 2/3 e pragmatica, non dogmatica, e può richiedere adattamento motivato.

Failure mode riconosciuti:

1. benchmark formalmente indipendenti ma semanticamente ridondanti;
2. stress test costruiti troppo deboli per mettere in crisi il claim;
3. rerun usati per "cercare" un esito desiderato;
4. scarsa documentazione dei casi falliti.

Contromisure raccomandate:

1. revisione indipendente del manifest prima dell'esecuzione;
2. quota minima di casi "difficili" in ogni strato;
3. obbligo di pubblicazione dei fallimenti di severità `high`;
4. audit periodico su coerenza tra preregistrazione e report finale.

Box C - Non-claim

Questo capitolo non implica:
1. che ogni claim debba superare tutti i domini possibili;
2. che la significatività statistica da sola determini la validità teorica;
3. che un benchmark ben progettato sostituisca la necessità di formalizzazione matematica.

---

## 8. Claim Ledger (S0-S3)

| ID | Claim | Tipo | Evidenza | Stato |
|---|---|---|---|---|
| C13.1 | L'indipendenza benchmark richiede separazione di dati, seed, tuning e log | metodologico | S1 | validated |
| C13.2 | La stratificazione e necessaria per evitare sovrastima della robustezza | statistico-metodologico | S1 | validated |
| C13.3 | Il disegno L1-L2-L3 e sufficiente come baseline per decisioni non arbitrarie | metodologico-formale | S2 | in_proof |
| C13.4 | La replicabilità multi-dominio e condizione necessaria per inferenza generale OCT | epistemico | S2 | in_proof |
| C13.5 | La pubblicazione dei fallimenti migliora la qualità cumulativa del programma | operativo | S1 | in_review |
| C13.6 | Il pacchetto benchmark minimo `PB_min` supporta rilascio multi-piattaforma coerente | infrastrutturale | S1 | in_review |

---

## 9. Bridge al Capitolo 14

Il Capitolo 13 ha stabilito come progettare benchmark indipendenti e replicabili, e come trasformare il protocollo in infrastruttura sperimentale.

Il Capitolo 14 completera la milestone `v1.4` introducendo la governance epistemica:

1. regole di versioning dei claim;
2. audit trail decisionale;
3. quality gate per release pubbliche;
4. politica di manutenzione del corpus teorematico.

In breve: il Capitolo 13 costruisce la macchina sperimentale; il Capitolo 14 ne definisce la costituzione operativa.

---

## Riferimenti

Riferimenti di framework interno:

1. Ghioni, F. (2026). `TE_CORE_v5.1.md`.
2. Ghioni, F. (2026). `Ordinative_Set_Theory_OST_A_Concise_Guide_For_AI_v2_1.md`.
3. `OCT_VALIDATION_PROTOCOL_v0_1.md`.
4. `OCT_Theory_and_Theorems/validation/CYCLE_3_2026-04-18/BENCHMARK_MANIFEST_cycle3_v0_1.md`.
5. `OCT_Theory_and_Theorems/validation/CYCLE_4_2026-04-19/CYCLE_4_REPORT.md`.
6. `OCT_FOUNDATIONAL_BOOK_CHAPTER_12_v1_0.md`.

Riferimenti primari:

1. Popper, K. (1959). *The Logic of Scientific Discovery*.
2. Lakatos, I. (1978). *The Methodology of Scientific Research Programmes*.
3. Nosek, B. et al. (2018). *The preregistration revolution*.
4. Goodman, S., Fanelli, D., Ioannidis, J. (2016). *What does research reproducibility mean?*.


