# Capitolo 15 - Case study fisico: standing waves e controfase strutturale

Metadati:
- Versione: v1.0
- Data: 2026-04-22
- Stato: draft completo
- Autore: Fabio Ghioni
- Allineato a: TE_CORE v5.1 / OST v2.1 / OCT baseline v1.0 candidate
- Dipendenze: Capitoli 12-14, case study OST standing waves (v1.0)
- Target parole capitolo: 2.200

---

## 1. Problema

Dopo i capitoli metodologici, il testo fondativo OCT deve mostrare una prova di lavoro su un dominio fisico in cui:

1. il fenomeno sia osservabile, riproducibile e formalizzabile;
2. la differenza tra lettura estensionale e lettura ordinativa sia non banale;
3. la nozione di controfase non resti una metafora, ma assuma forma misurabile.

Il caso delle standing waves in fluido rotante soddisfa queste condizioni. La letteratura classica sullo scattering Aharonov-Bohm idrodinamico mostra già la dipendenza topologica della risposta dal campo di circolazione. Il lavoro sperimentale del 2026 su standing waves e singolo vortice aggiunge un passaggio chiave: la transizione da difetti locali vicino al core a linee nodali globali quantizzate, in contro-rotazione rispetto al vortice.

Il problema del capitolo e quindi preciso:

**come leggere questo risultato come caso studio OCT, distinguendo chiaramente cosa e dato fisico consolidato, cosa e mappatura ordinativa, e cosa resta ipotesi da consolidare nei cicli successivi?**

### 1.1 Rilevanza per l'opera fondativa

Il capitolo ha quattro funzioni strategiche:

1. dimostrare che il lessico ordinativo può interpretare un fenomeno fisico non progettato da OCT;
2. mostrare che la struttura `⟨Sigma, R, Phi⟩` ha potere esplicativo anche in sistemi classici controllati;
3. offrire un esempio didattico ad alta intuibilità per il lettore non specialistico;
4. preparare il passaggio al caso sistemico-sociale (Capitolo 16) evitando salto analogico troppo brusco.

### 1.2 Vincolo epistemico

Per evitare overclaiming, questo capitolo adotta tre regole:

1. i dati sperimentali restano attribuiti al dominio fisico originario;
2. la lettura OCT e esplicitata come traduzione strutturale, non come "appropriazione" del risultato;
3. ogni estensione inter-dominio viene etichettata con stato di evidenza coerente (`S0-S3`).

---

## 2. Tesi del capitolo

La tesi e articolata in nove enunciati.

1. Il sistema standing-wave + vortice e un candidato robusto per formalizzazione ordinativa in quanto separa chiaramente componenti (`Sigma`), relazioni (`R`) e risposta (`Phi`).
2. La sostituzione strutturale che porta alla doppia periodicità angolare mostra non-additività ordinativa: piccolo cambio in `R`, grande cambio in `Phi`.
3. Le linee nodali globali quantizzate sono interpretabili come controfase strutturale e non come semplice cancellazione locale.
4. La quantizzazione del numero di linee nodali da parametro continuo supporta la tesi di quantizzazione topologica emergente.
5. La contro-rotazione sistematica delle linee nodali rispetto al vortice e un marker osservabile di opposizione coerente all'attrattore.
6. Il caso dimostra una forma fisica di inversione causale teleodinamica: stessa causa locale, envelope di effetto differente in base alla configurazione globale.
7. La lettura OCT non sostituisce il modello fisico, ma ne espande la trasferibilità concettuale.
8. Il caso e sufficiente come benchmark qualitativo per claims metodologici del libro, non ancora per claims quantitativi universali cross-dominio.
9. La struttura del caso fornisce template operativo per la scrittura dei case study successivi.

---

## 3. Definizioni canoniche del caso

### Definizione 15.1 (Sistema fisico ordinativo)

Nel contesto del case study definiamo:

`I_sw := <Sigma_sw, R_sw, Phi_sw>`

con:

1. `Sigma_sw` = {fluido, vortice irrotazionale, onde contro-propaganti};
2. `R_sw` = vincoli dinamici e topologici della configurazione standing-wave;
3. `Phi_sw` = pattern nodale emergente osservabile.

### Definizione 15.2 (Parametro topologico di scattering)

Sia `alpha` il parametro adimensionale che lega circolazione, lunghezza d'onda e velocità di gruppo. `alpha` governa la struttura globale del pattern nodale.

### Definizione 15.3 (Controfase strutturale nel dominio fisico)

Una configurazione e in controfase strutturale quando:

1. emerge un insieme nodale non locale;
2. i settori separati dal nodo mostrano opposizione di fase;
3. la risposta complessiva si oppone in verso all'attrattore che la organizza.

### Definizione 15.4 (Indice di globalità nodale)

Definiamo indice di globalità:

`G_n := L_n / L_dom`

con `L_n` lunghezza media delle linee nodali osservate e `L_dom` scala lineare del dominio utile. `G_n` alto indica risposta sistemica non confinata al core.

### Definizione 15.5 (Delta configurativo)

`Delta_R := R_sw - R_travel`

dove `R_travel` indica la relazione corrispondente al caso a onda viaggiante singola. Il caso mostra che `Delta_R` piccolo in apparenza può produrre salto qualitativo in `Phi`.

### Definizione 15.6 (Inversione causale locale-globale)

In questo capitolo c'e inversione causale quando la stessa sorgente locale (vortice) esprime effetti confinati o globali a seconda della configurazione relazionale del campo.

---

## 4. Sviluppo formale del case study

### 4.1 Dalla lettura estensionale alla lettura ordinativa

La lettura estensionale standard descrive componenti e equazioni del sistema, ottenendo predizioni corrette sul pattern osservato. La lettura ordinativa aggiunge una domanda diversa:

1. quale trasformazione in `R` produce il salto di regime in `Phi`?
2. quali invarianti restano stabili nella transizione?
3. quali proprietà della risposta sono trasferibili a sistemi non fluidodinamici?

Il vantaggio non e rifare la fisica, ma esplicitarne la grammatica di configurazione.

### 4.2 Non-additività strutturale

Nel confronto tra regime travelling-wave e regime standing-wave il sistema mostra una non-additività tipica:

1. non otteniamo due copie specchiate del pattern locale;
2. otteniamo una topologia nuova a scala di dominio.

In linguaggio OCT:

1. stessa famiglia di oggetti fisici;
2. mutazione compatta delle relazioni;
3. biforcazione della risposta di categoria (locale vs globale).

Questo e uno dei passaggi più forti del capitolo: la distinzione tra "somma di effetti" e "riorganizzazione di campo".

### 4.3 Quantizzazione topologica da sorgente continua

Il parametro di circolazione e continuo, ma il numero di linee nodali osservabili e discreto e legato a intervalli integer-like di `|alpha|`.

Interpretazione ordinativa:

1. la discretizzazione non viene imposta dalla sorgente;
2. emerge dal vincolo topologico della configurazione;
3. il conteggio nodale e quindi proprietà di `R`, non di una quantizzazione microscopica primaria della sorgente.

Implicazione per OCT: la categoria di output può essere discreta anche quando la categoria dei controlli sperimentali e continua.

### 4.4 Controfase come forma, non come assenza

Un punto pedagogico cruciale: la linea nodale non e "vuoto". E una forma strutturante che organizza il campo in settori con opposizione di fase.

Per questo la controfase nel caso fisico soddisfa tre criteri:

1. necessità strutturale (non artificio post hoc);
2. orientamento opposto all'attrattore;
3. funzione ordinativa globale del pattern.

In termini del libro, questo caso rende operativa la definizione TE di controfase strutturale, altrimenti percepita dal lettore come lessico astratto.

### 4.5 Inversione causale teleodinamica

Lo stesso vortice, con parametro di intensita comparabile, produce:

1. effetto locale nel caso classico;
2. effetto globale nel caso standing-wave.

L'invariante non e il raggio d'azione, ma la sorgente. Cambia la configurazione del campo che "ospita" la sorgente. Questo e precisamente il pattern di inversione causale discusso nella teleodinamica ordinativa.

### 4.6 Mappatura con protocollo del Capitolo 12

Per mantenere coerenza metodologica, il case study viene letto con la pipeline PV-8:

1. claim: esistenza di controfase strutturale globale quantizzata;
2. contesto: dominio idrodinamico shallow-water con vortice irrotazionale;
3. evidenza: report sperimentale e formulazione analitica coerente;
4. decisione: claims metodologici in stato `validated` o `in_review` secondo portata.

Questo impedisce che il capitolo diventi solo "narrazione elegante" senza disciplina decisionale.

### 4.7 Indicatori minimi per replicazione OCT-oriented

Proponiamo un micro-set di indicatori per eventuali repliche future:

1. `N_nodes` (conteggio linee nodali);
2. `G_n` (globalità nodale);
3. `Omega_rel` (verso di rotazione relativo nodo-vortice);
4. `S_phase` (salto di fase inter-settori);
5. robustezza a variazioni moderate dei parametri geometrici.

Se almeno quattro indicatori su cinque sono confermati in benchmark indipendente, il claim C15.2 può avanzare di stato.

### 4.8 Condizione di sufficienza del capitolo

Il capitolo e considerato sufficiente se dimostra insieme:

1. mappatura rigorosa `fisica -> OST/OCT`;
2. assenza di overclaim inter-dominio;
3. utilità metodologica per il case study successivo.

Questa condizione e soddisfatta da definizioni 15.1-15.6, analisi 4.1-4.7 e ledger claims in sezione 8.

---

## 5. Proposizioni e teoremi locali

### Proposizione 15.1 (Non-additività configurativa osservabile)

Enunciato:
Nel caso standing-wave + vortice, la risposta globale non e riducibile a sovrapposizione lineare dei pattern locali del caso a onda singola.

Intuizione:
il passaggio di relazione topologica cambia classe di risposta.

Stato: `validated`.

### Proposizione 15.2 (Controfase strutturale fisicamente ancorata)

Enunciato:
Le linee nodali quantizzate in contro-rotazione costituiscono una realizzazione fisica coerente della controfase strutturale.

Intuizione:
la controfase e una forma organizzativa che emerge per vincolo, non un'assenza passiva.

Stato: `in_review`.

### Proposizione 15.3 (Quantizzazione emergente da relazione)

Enunciato:
Un output discreto può emergere da controllo continuo quando la topologia relazionale impone vincoli di conteggio.

Intuizione:
la discretizzazione e una proprietà del sistema configurato, non necessariamente della sorgente elementare.

Stato: `validated`.

### Teorema 15.4 (Compatibilità tra formalismo fisico e formalismo ordinativo)

Ipotesi:
1. descrizione sperimentale/analitica consistente del fenomeno;
2. mappatura esplicita `Sigma, R, Phi`;
3. criteri di decisione metodologica tracciati.

Tesi:
Il caso standing-wave e compatibile con una lettura ordinativa forte senza perdita di rigore fisico.

Proof sketch:
1. il formalismo fisico resta intatto;
2. la mappatura ordinativa agisce come livello strutturale aggiuntivo;
3. i claim sono graduati per evidenza e non per retorica.

Conseguenze:
abilità l'uso del caso come ponte disciplinare in un testo fondativo OCT.

Stato: `in_proof`.

### Teorema 15.5 (Marker minimo di controfase globale)

Ipotesi:
1. nodi estesi con `G_n` sopra soglia;
2. opposizione di fase inter-settori;
3. verso di rotazione opposto all'attrattore.

Tesi:
La risposta può essere classificata come controfase strutturale globale nel lessico OCT.

Proof sketch:
1. i tre marker coprono estensione, dinamica e semantica di fase;
2. l'assenza di uno dei marker riduce il claim a pattern locale o ambiguo;
3. la compresenza dei tre marker soddisfa la definizione 15.3.

Conseguenze:
fornisce criterio operativo per confronto con altri domini.

Stato: `in_proof`.

---

## 6. Implicazioni operative

### 6.1 Per il Capitolo 16

Il caso fisico prepara il lettore a una traslazione controllata verso sistemi sociali complessi:

1. stesso schema `sorgente -> relazione -> risposta`;
2. stessa attenzione alla differenza tra locale e globale;
3. stessa disciplina su non-confondere analogia con identità strutturale.

### 6.2 Per OCT come teoria generale

Il case study fornisce un benchmark narrativamente forte e metodologicamente pulito per tre idee chiave:

1. non-additività ordinativa;
2. controfase strutturale;
3. quantizzazione emergente topologica.

### 6.3 Per pubblicazione e peer dialog

Questo capitolo e progettato per essere leggibile anche da revisori esterni non già allineati al lessico TE/OCT, perché:

1. ancora i passaggi a un esperimento pubblico e replicabile;
2. separa chiaramente dati, interpretazione, estensione;
3. rende falsificabili i claims metodologici principali.

### 6.4 Per didattica e onboarding

Tra tutti i casi possibili, questo e probabilmente il più didattico per introdurre OCT a nuovi ricercatori:

1. fenomenologia visiva forte;
2. matematica gestibile;
3. ponte diretto tra fisica classica e linguaggio ordinativo.

---

## 7. Limiti e non-claim

Limiti espliciti:

1. il capitolo non sostituisce la trattazione fisica specialistica del paper originale;
2. la mappatura inter-dominio non implica universalità automatica;
3. alcuni indicatori operativi proposti richiedono campagna replicativa dedicata per consolidamento.

Failure mode riconosciuti:

1. abuso analogico: trasferire troppo dal caso fisico al caso sociale;
2. riduzione simbolica: usare "controfase" come metafora senza marker misurabili;
3. semplificazione eccessiva della dipendenza da contesto sperimentale.

Contromisure:

1. mantenere separazione netta tra stato dei dati fisici e stato dei claims OCT;
2. usare sempre ledger `S0-S3` nei passaggi di estensione;
3. ancorare ogni estensione a un criterio di falsificabilità esplicito.

Box C - Non-claim

Questo capitolo non implica:
1. che ogni pattern nodale sia controfase strutturale;
2. che il caso standing-wave validi di per se tutto OCT;
3. che la relazione con domini sociali sia diretta senza mediazione metodologica.

---

## 8. Claim Ledger (S0-S3)

| ID | Claim | Tipo | Evidenza | Stato |
|---|---|---|---|---|
| C15.1 | Il caso standing-wave realizza non-additività ordinativa osservabile | metodologico | S1 | validated |
| C15.2 | Le linee nodali contro-rotanti sono classificabili come controfase strutturale | metateorico | S2 | in_review |
| C15.3 | La quantizzazione nodale da parametro continuo e un esempio di quantizzazione topologica emergente | teorico-operativo | S1 | validated |
| C15.4 | Il caso mostra una forma di inversione causale locale-globale coerente con teleodinamica OST | metateorico | S2 | in_proof |
| C15.5 | Il set indicatori (`N_nodes`, `G_n`, `Omega_rel`, `S_phase`) e sufficiente come baseline di replica OCT-oriented | protocollo | S1 | in_review |
| C15.6 | Il caso e benchmark didattico robusto per introduzione a OCT | editoriale-scientifico | S1 | validated |

---

## 9. Bridge al Capitolo 16

Il Capitolo 15 ha mostrato OCT su un sistema fisico controllato, dove la trasformazione di relazione produce un salto di risposta globale osservabile.

Il Capitolo 16 usera la stessa grammatica su un dominio ad alta complessità storica: le dinamiche reaction-diffusion dei sistemi civilizzazionali. Il passaggio e deliberato:

1. dal laboratorio fisico alla dinamica socio-storica;
2. da controfase in campo ondoso a controfase in architetture istituzionali;
3. da quantizzazione topologica locale a biforcazioni multi-scala di sistema.

In sintesi: dopo aver verificato la forma in fisica, testiamo la forma nella storia.

---

## Riferimenti

Riferimenti di framework interno:

1. Ghioni, F. (2026). `TE_CORE_v5.1.md`.
2. Ghioni, F. (2026). `Ordinative_Set_Theory_OST_A_Concise_Guide_For_AI_v2_1.md`.
3. `OCT_FOUNDATIONAL_BOOK_CHAPTER_12_v1_0.md`.
4. `OCT_FOUNDATIONAL_BOOK_CHAPTER_13_v1_0.md`.
5. `OCT_FOUNDATIONAL_BOOK_CHAPTER_14_v1_0.md`.
6. `OST_Case_Study_Standing_Waves_Spinning_Fluid_v1_0.md`.

Riferimenti primari:

1. Singh, R.; Ronning, J.; Liu, L.; Angheluta, L.; Concha, A.; Bandi, M. (2026). *Communications Physics* 9:123.
2. Berry, M. V. et al. (1980). Hydrodynamic analogue of Aharonov-Bohm scattering.
3. Aharonov, Y.; Bohm, D. (1959). Significance of electromagnetic potentials.

