# Capitolo 12 - Protocollo scientifico OCT: metrica, osservazione, decisione

Metadati:
- Versione: v1.0
- Data: 2026-04-22
- Stato: draft completo
- Autore: Fabio Ghioni
- Allineato a: TE_CORE v5.1 / OST v2.1 / OCT baseline v1.0 candidate
- Target parole capitolo: 2.700

---

## 1. Problema

Con i capitoli precedenti abbiamo costruito un impianto teorico completo:

1. fondazione ontologica e assiomatica;
2. teoremi fondativi, differenziali e applicativi;
3. estensione del corpus classico fino alle strutture avanzate;
4. grammatica di controesempi, limiti e falsificabilità.

Manca però il passaggio che decide se la teoria può diventare pratica scientifica condivisa: un protocollo unico che dica **come** osservare, **cosa** misurare e **quando** decidere.

Senza protocollo:

1. i risultati restano locali e difficili da confrontare;
2. le decisioni di validazione diventano opache;
3. i passaggi `in_proof -> validated` rischiano arbitrarietà.

Con protocollo:

1. ogni test diventa replicabile;
2. ogni decisione è tracciabile;
3. la teoria può essere auditata da team indipendenti.

Il problema del capitolo è quindi:

**come formalizzare una procedura standard che unisca metrica ordinativa, osservazione contestuale e decisione epistemica senza ridurre OCT a sola statistica né a sola deduzione formale?**

### 1.1 Perché questo capitolo apre la milestone `v1.4`

La milestone `v1.4` è il passaggio da “teoria estesa” a “metodo scientifico operativo”:

1. Capitolo 12: protocollo;
2. Capitolo 13: benchmark e replicabilità;
3. Capitolo 14: governance epistemica.

Il Capitolo 12 è la base perché definisce il linguaggio procedurale comune usato nei due capitoli successivi.

### 1.2 Vincolo metodologico

Il protocollo OCT deve mantenere una tripla coerenza:

1. coerenza matematica (con O1-O7 e i teoremi F/D/A);
2. coerenza sperimentale (misure replicabili);
3. coerenza decisionale (regole esplicite di accettazione/revisione/rigetto).

---

## 2. Tesi del capitolo

La tesi è articolata in nove enunciati.

1. Un risultato OCT è scientificamente forte solo se combina prova formale e protocollo di osservazione replicabile.
2. La triade metrica canonica (`Coh`, `Phi`, `Delta`) è necessaria ma non sufficiente: servono metriche ausiliarie dominio-specifiche.
3. Ogni esperimento deve essere indicizzato da un contesto `Omega` dichiarato e versionato.
4. La pre-registrazione dei criteri decisionali riduce bias di conferma.
5. La validazione richiede benchmark indipendenti e multi-contesto.
6. I criteri di decisione devono distinguere `validated`, `revise`, `reject`.
7. Il protocollo deve prevedere pubblicazione di fallimenti significativi, non solo esiti positivi.
8. Il passaggio di stato di un teorema è legittimo solo con evidenza tracciata.
9. Il protocollo proposto è sufficiente per sostenere il disegno benchmark del Capitolo 13.

---

## 3. Definizioni canoniche

### Definizione 12.1 (Unità di validazione)

Unità minima di validazione:

`U_val := <Claim, Omega, Dataset, Pipeline, Metriche, Criteri, Log, Esito>`.

### Definizione 12.2 (Contesto osservativo registrato)

`Omega_reg` è il contesto osservativo con:

1. variabili rilevanti;
2. ipotesi di dominio;
3. condizioni di perturbazione ammesse;
4. versione del protocollo.

### Definizione 12.3 (Metriche canoniche e ausiliarie)

Metriche canoniche:

1. `Coh_Omega(D) in [0,1]`;
2. `Phi_Omega(D)` (normalizzata quando necessario);
3. `Delta_Omega(D)=1-Coh_Omega(D)`.

Metriche ausiliarie (esempi):

1. `Err_sem` per qualità semantica;
2. `Err_struct` per fedeltà strutturale;
3. `Var_Omega` per stabilità cross-contesto.

### Definizione 12.4 (Pre-registrazione)

La pre-registrazione è la dichiarazione ex ante di:

1. criteri di conferma;
2. criteri di falsificazione;
3. soglie e test statistici;
4. regole di decisione.

### Definizione 12.5 (Decisione epistemica)

Esito finale di un test:

1. `validated`: evidenza sufficiente e replicata;
2. `revise`: evidenza mista o insufficiente;
3. `reject`: controevidenza robusta nel dominio dichiarato.

### Definizione 12.6 (Tracciabilità completa)

Un risultato è tracciabile se include:

1. configurazione di esecuzione;
2. dati/versione;
3. codice o procedura;
4. output e log;
5. motivazione della decisione.

### Definizione 12.7 (Indice di evidenza composta)

Dato un claim `C` e un contesto `Omega`, definiamo l'indice di evidenza composta:

`IEC(C,Omega) := w1*Coh + w2*Phi_norm + w3*(1-Delta) + w4*Rep + w5*Trace`

con:

1. `w_i >= 0` e `sum_i w_i = 1`;
2. `Phi_norm` normalizzata nel dominio del benchmark;
3. `Rep` indice di replicabilità inter-benchmark;
4. `Trace` indice di completezza di tracciabilità.

L'`IEC` non sostituisce la valutazione teorica, ma fornisce una sintesi comparabile tra esperimenti.

### Definizione 12.8 (Budget d'incertezza)

Per ogni unità `U_val` definiamo un budget d'incertezza:

`B_unc := <u_data, u_model, u_measure, u_context, u_decision>`

dove ogni termine quantifica la componente di incertezza legata a:

1. qualità e copertura dei dati;
2. specificazione del modello/pipeline;
3. errore o variabilità di misura;
4. trasferibilità tra contesti;
5. discrezionalità residua in decisione.

Un claim non può essere promosso a `validated` se `B_unc` supera la soglia preregistrata.

---

## 4. Sviluppo formale

### 4.1 Architettura del protocollo in tre strati

Il protocollo OCT è organizzato in tre strati:

1. **Strato Metrico**: cosa misurare (`Coh/Phi/Delta` + ausiliarie);
2. **Strato Osservativo**: in quale `Omega` e con quali perturbazioni;
3. **Strato Decisionale**: come passare da misura a stato teorico.

La separazione evita confusioni:

1. buone metriche con cattivo contesto;
2. buon contesto con regole decisionali opache;
3. decisioni forti su evidenza debole.

### 4.2 Pipeline minima di validazione (PV-8)

Proponiamo una pipeline in otto passi.

1. dichiarare claim e teorema target;
2. registrare `Omega_reg`;
3. fissare dataset/versione e baseline;
4. pre-registrare criteri di conferma/falsificazione;
5. eseguire esperimento e raccogliere metriche;
6. ripetere su benchmark indipendente;
7. consolidare risultati multi-contesto;
8. assegnare esito (`validated`/`revise`/`reject`) con motivazione.

La PV-8 è il nucleo operativo del capitolo.

### 4.3 Regole di evidenza minima

Per promuovere un claim a `validated` proponiamo quattro condizioni minime:

1. conferma su almeno due benchmark indipendenti;
2. replicazione su almeno due contesti `Omega` non equivalenti banalmente;
3. coerenza tra metrica canonica e metrica ausiliaria rilevante;
4. assenza di controesempio forte non risolto nel dominio dichiarato.

Se una condizione manca:

1. default su `revise` (non su `validated`).

### 4.4 Trattamento dei risultati discordanti

È frequente ottenere risultati misti tra benchmark o contesti. In OCT non si risolve con media semplice.

Regola proposta:

1. identificare la fonte di divergenza (dati, mapping, soglia, pipeline);
2. classificare divergenza come:
   - rumore controllabile;
   - instabilità strutturale;
   - controevidenza sostanziale.
3. decidere esito in funzione della classe di divergenza.

Questa regola impedisce sia ottimismo ingiustificato sia rigetto prematuro.

### 4.5 Matrice decisionale standard

Per ogni unità `U_val`:

1. **D-Valid**: criteri soddisfatti, replicazione robusta;
2. **D-Revise**: evidenza parziale o conflittuale;
3. **D-Reject**: fallimento robusto nel dominio dichiarato.

Ogni decisione deve includere:

1. claim colpito;
2. evidenze principali;
3. limiti residui;
4. azione successiva.

### 4.6 Collegamento con la falsificabilità (Capitolo 11)

Il protocollo incorpora i principi K1-K7:

1. riproducibilità e tracciabilità;
2. localizzazione del fallimento;
3. decisione finale non arbitraria.

In questo modo, la falsificabilità non resta solo principio teorico: diventa procedura eseguibile.

### 4.7 Controllo di qualità del protocollo

Ogni campagna sperimentale dovrebbe produrre un report QA con:

1. completezza metadati;
2. qualità log;
3. copertura benchmark;
4. coerenza tra decisione e criteri pre-registrati.

Se il QA è insufficiente:

1. il risultato non può passare a `validated`.

### 4.8 Versionamento del protocollo

Il protocollo deve essere versionato (`P_v1`, `P_v2`, ...). Ogni versione deve dichiarare:

1. cosa cambia nelle metriche;
2. cosa cambia nei criteri decisionali;
3. quali risultati pregressi vanno rivalutati.

Questo previene inconsistenze storiche nei passaggi di stato.

### 4.9 Protocollo e apertura dei dati

Per quanto possibile, la validazione deve favorire:

1. pubblicazione di dataset/manifest;
2. pubblicazione dei log principali;
3. pubblicazione degli errori significativi.

La trasparenza non è accessorio etico: è condizione tecnica di replicabilità.

### 4.10 Condizione di non-ridondanza del capitolo

Il capitolo è non ridondante se mostra che:

1. senza protocollo la stessa teoria può produrre esiti incompatibili;
2. con protocollo gli esiti diventano confrontabili e decidibili.

Questa condizione è soddisfatta dall’integrazione tra PV-8, regole di evidenza minima e matrice decisionale.

### 4.11 Operatore decisionale ordinativo `D_OCT`

Per rendere la decisione riproducibile introduciamo un operatore esplicito:

`D_OCT(U_val) -> {validated, revise, reject}`.

Input minimi:

1. indicatori canonici e ausiliari;
2. esito repliche indipendenti;
3. `B_unc` e `IEC`;
4. presenza/assenza di controesempi forti.

Regola orientativa:

1. `validated` se tutte le condizioni minime sono soddisfatte, `IEC >= tau_val` e `B_unc <= beta_val`;
2. `revise` se evidenza intermedia, conflittuale o incertezza oltre soglia di validazione;
3. `reject` se controevidenza robusta o violazioni strutturali persistenti.

L'operatore non elimina il giudizio scientifico, ma ne impone la struttura argomentativa.

### 4.12 Budget d'incertezza e analisi di sensibilità

Ogni campagna deve includere almeno tre verifiche:

1. **sensibilità dati**: variazione controllata del campione/stratificazione;
2. **sensibilità soglie**: stress su `tau_val`, `beta_val`, soglie ausiliarie;
3. **sensibilità contesto**: cambio di `Omega` mantenendo claim invariato.

Se l'esito cambia in modo non spiegato rispetto a piccole perturbazioni, il claim va in `revise` fino a chiarimento.

### 4.13 Schema minimo di preregistrazione

Per evitare preregistrazioni deboli proponiamo uno schema minimo obbligatorio.

Campi obbligatori:

1. claim e dominio di validità dichiarato;
2. dataset, fonti, criteri di inclusione/esclusione;
3. pipeline esecutiva e versioni software;
4. metriche canoniche e metriche ausiliarie;
5. soglie decisionali (`tau_val`, `tau_rev`, `beta_val`);
6. test di robustezza previsti;
7. criteri espliciti di falsificazione;
8. politica di gestione risultati inattesi.

Senza questi campi, l'unita non e idonea a validazione conclusiva.

### 4.14 Livelli di riproducibilità degli artefatti

Definiamo quattro livelli progressivi:

1. `R0` - descrizione narrativa non eseguibile;
2. `R1` - script disponibili ma ambiente non congelato;
3. `R2` - script + ambiente + manifest dati con hash;
4. `R3` - replay indipendente riuscito su infrastruttura esterna.

Per claims con impatto teorico alto, il livello minimo raccomandato e `R2`; per promozione critica e preferibile `R3`.

---

## 5. Proposizioni e teoremi locali

### Proposizione 12.1 (Necessità della pre-registrazione)

Enunciato:
Senza pre-registrazione dei criteri decisionali, la validazione OCT è esposta a bias di conferma non controllati.

Intuizione:
la decisione ex post può essere adattata al risultato osservato.

Stato: `validated`.

### Proposizione 12.2 (Insufficienza del benchmark singolo)

Enunciato:
Un singolo benchmark non è condizione sufficiente per promuovere un claim a `validated`.

Intuizione:
la robustezza richiede indipendenza minima delle evidenze.

Stato: `validated`.

### Teorema 12.3 (Sufficienza operativa della pipeline PV-8)

Ipotesi:
1. esecuzione completa dei passi PV-8;
2. tracciabilità completa;
3. decisione conforme alla matrice standard.

Tesi:
La decisione epistemica risultante è auditabile e non arbitraria.

Proof sketch:
1. PV-8 rende esplicite tutte le dipendenze dell’esperimento;
2. tracciabilità completa rende verificabile il processo;
3. la matrice decisionale vincola la scelta finale.

Conseguenze:
fornisce base operativa per passaggio di stato dei teoremi.

Stato: `in_proof`.

### Teorema 12.4 (Compatibilità tra rigore formale e rigore sperimentale)

Ipotesi:
1. claim formalmente ben specificato;
2. protocollo PV-8 applicato;
3. evidenza multi-benchmark coerente.

Tesi:
È possibile mantenere simultaneamente rigore matematico e rigore sperimentale nel ciclo OCT.

Proof sketch:
1. il formalismo definisce cosa testare;
2. il protocollo definisce come testare;
3. la decisione tracciata definisce quando accettare o rivedere.

Conseguenze:
evita la falsa alternativa tra “teoria pura” e “solo empiria”.

Stato: `in_proof`.

### Proposizione 12.5 (Monotonia informativa della tracciabilità)

Enunciato:
A parita di esito metrico, unita con livello di tracciabilità superiore (`Trace`) produce decisioni più auditabili e meno controvertibili.

Intuizione:
la trasparenza riduce ambiguità interpretative e facilità la replica indipendente.

Stato: `validated`.

### Proposizione 12.6 (Necessità del budget d'incertezza)

Enunciato:
Senza quantificazione esplicita del budget d'incertezza (`B_unc`), la distinzione tra `revise` e `validated` resta metodologicamente fragile.

Intuizione:
la stessa metrica può apparire forte o debole a seconda della varianza nascosta non esplicitata.

Stato: `in_review`.

### Teorema 12.7 (Consistenza procedurale dell'operatore `D_OCT`)

Ipotesi:
1. preregistrazione completa;
2. regole decisionali fissate ex ante;
3. applicazione uniforme su benchmark indipendenti.

Tesi:
L'operatore `D_OCT` e consistente nel senso procedurale: a parita di input e regole, produce decisioni replicabili tra valutatori.

Proof sketch:
1. la preregistrazione blocca il perimetro decisionale;
2. la codifica degli input riduce ambiguità semantiche;
3. la matrice decisionale limita la discrezionalità ex post.

Conseguenze:
fornisce base per audit inter-team e comparazione temporale delle decisioni.

Stato: `in_proof`.

---

## 6. Implicazioni operative

### 6.1 Per progettazione benchmark (Capitolo 13)

Il Capitolo 13 dovrà derivare direttamente da PV-8:

1. benchmark primari e secondari;
2. manifest dati/versioni;
3. criteri di conferma/falsificazione pre-registrati.

### 6.2 Per governance epistemica (Capitolo 14)

Il Capitolo 14 userà:

1. matrice decisionale standard;
2. regole di versionamento protocollo;
3. policy di pubblicazione dei fallimenti.

### 6.3 Per team di ricerca multipli

Il protocollo consente collaborazione distribuita con linguaggio comune:

1. stesso schema di report;
2. stessi stati decisionali;
3. stessa mappa di responsabilità metodologica.

### 6.4 Per pubblicazione tecnica

Ogni release dovrebbe includere:

1. versione protocollo usata;
2. claim valutati;
3. esiti e motivazioni;
4. limiti aperti.

Questo migliora la leggibilità esterna e riduce ambiguità interpretative.

### 6.5 Per continuità del manoscritto

Il protocollo funziona da “strato comune” tra teoria (capitoli 1-11) e applicazioni/benchmark (capitoli 13-16).  
Senza questo strato, il libro rischierebbe frammentazione in blocchi non comunicanti.

### 6.6 Per pacchetto pubblicazione multi-piattaforma

Il protocollo del Capitolo 12 consente una pubblicazione coordinata su canali diversi senza perdita di significato metodologico.

Mappatura operativa consigliata:

1. GitHub: versione eseguibile (documenti, script, manifest, changelog);
2. Zenodo: snapshot citabile con DOI di release;
3. OSF: progetto di ricerca con artefatti, preregistrazioni e versioni intermedie;
4. Hugging Face: eventuali dataset mirror e card metodologiche per benchmark ripetibili.

La coerenza tra piattaforme si ottiene mantenendo identico:

1. identificatore di versione del protocollo;
2. manifest dei dataset con hash;
3. decision table usata per `validated/revise/reject`.

### 6.7 Per lettori non specialisti

Un protocollo esplicito e anche una funzione pedagogica: rende leggibile il passaggio da teoria ad evidenza.

Per una fruizione "a prova di bambino", ogni report dovrebbe includere:

1. obiettivo in linguaggio naturale;
2. cosa e stato misurato e perché;
3. esito finale e motivo della scelta;
4. cosa manca ancora per aumentare la confidenza.

Questo non semplifica la teoria, ma semplifica il suo accesso.

---

## 7. Limiti e non-claim

Limiti espliciti:

1. il capitolo definisce un protocollo minimo, non esaustivo per tutti i domini;
2. alcune metriche ausiliarie richiedono specifica per caso d’uso;
3. la robustezza statistica dipende dalla qualità dei dataset disponibili.

Failure mode riconosciuti:

1. pre-registrazione incompleta o retroattiva;
2. benchmark non indipendenti presentati come indipendenti;
3. decisioni non allineate ai criteri dichiarati;
4. omissione di fallimenti significativi nei report pubblici.

Contromisure prioritarie:

1. checklist di preregistrazione bloccante prima dell'esecuzione;
2. revisione incrociata minima a due valutatori per la decisione finale;
3. audit trimestrale dei livelli `R0-R3` sugli artefatti pubblici;
4. registro pubblico delle revisioni che motivi ogni cambio di stato dei claim.

Box C - Non-claim

Questo capitolo non implica:
1. che il protocollo garantisca automaticamente risultati positivi;
2. che ogni claim in `in_proof` debba diventare `validated`;
3. che la standardizzazione metodologica sostituisca l’innovazione teorica.

---

## 8. Claim Ledger (S0-S3)

| ID | Claim | Tipo | Evidenza | Stato |
|---|---|---|---|---|
| C12.1 | La pipeline PV-8 è sufficiente come baseline operativa di validazione OCT | metodologico | S2 | in_review |
| C12.2 | La pre-registrazione riduce bias decisionali in modo significativo | epistemico | S1 | validated |
| C12.3 | Multi-benchmark e multi-contesto sono necessari per promozione a `validated` | metodologico | S1 | validated |
| C12.4 | La matrice decisionale standard migliora tracciabilità e auditabilità | metodologico | S1 | in_review |
| C12.5 | Il protocollo unifica rigore formale e rigore sperimentale | metateorico | S2 | in_proof |
| C12.6 | La pubblicazione dei fallimenti è condizione tecnica di replicabilità | epistemico-operativo | S1 | validated |
| C12.7 | L'operatore `D_OCT` rende replicabile la decisione a parita di input/regole | metodologico-formale | S2 | in_proof |
| C12.8 | Il budget d'incertezza e necessario per distinguere validazione da revisione | metodologico | S1 | in_review |
| C12.9 | I livelli `R0-R3` migliorano la comparabilità di riproducibilità tra studi | operativo | S1 | validated |

---

## 9. Bridge al Capitolo 13

Il Capitolo 12 ha definito la procedura standard di validazione:

1. metrica canonica e ausiliaria;
2. osservazione contestuale registrata;
3. decisione epistemica tracciata.

Il Capitolo 13 tradurrà questa procedura in disegno benchmark completo:

1. selezione e stratificazione dataset;
2. benchmark indipendenti e replicabilità multi-dominio;
3. criteri quantitativi di conferma/falsificazione per i blocchi F/D/A.

In sintesi: il Capitolo 12 definisce il metodo; il Capitolo 13 ne implementa l’infrastruttura sperimentale.

---

## Riferimenti

Riferimenti di framework interno:

1. Ghioni, F. (2026). `TE_CORE_v5.1.md`.
2. Ghioni, F. (2026). `Ordinative_Set_Theory_OST_A_Concise_Guide_For_AI_v2_1.md`.
3. `OCT_VALIDATION_PROTOCOL_v0_1.md`.
4. `OCT_FOUNDATIONAL_BOOK_CHAPTER_11_v1_0.md`.
5. `OCT_FOUNDATIONAL_BOOK_CHAPTER_10_v1_0.md`.

Riferimenti primari:

1. Popper, K. (1959). *The Logic of Scientific Discovery*.
2. Lakatos, I. (1978). *The Methodology of Scientific Research Programmes*.
3. Nosek, B. et al. (2018). *The preregistration revolution*.

