# Capitolo 4 - Oggetti, morfismi, composizione, identità in estensione OCT

Metadati:
- Versione: v1.0
- Data: 2026-04-21
- Stato: draft completo
- Autore: Fabio Ghioni
- Allineato a: TE_CORE v5.1 / OST v2.1 / OCT baseline v1.0 candidate
- Target parole capitolo: 3.100

---

## 1. Problema

Con i Capitoli 1-3 abbiamo costruito:

1. la motivazione epistemica dell’estensione ordinativa;
2. la base ontologica della singolarità;
3. il kernel assiomatico O1-O7.

Con i Capitoli 8-11 abbiamo consolidato:

1. lo spazio di validità `S_Omega`;
2. il blocco teorematico fondativo e differenziale;
3. la grammatica di controesempi, limiti e falsificabilità.

Ora inizia la fase `v1.3`: espansione sistematica del corpus categoriale classico in quadro OCT. Il primo passo è apparentemente semplice ma in realtà decisivo: ridefinire **oggetti, morfismi, composizione e identità** in forma compatibile con il classico ma dotata di selettività ordinativa.

Il problema specifico del capitolo è:

**come preservare la potenza della sintassi categoriale classica evitando, allo stesso tempo, che entità formalmente lecite ma ordinativamente sterili o degenerative vengano trattate come equivalenti?**

La difficoltà emerge su due fronti:

1. se l’estensione è troppo debole, non aggiunge discriminazione reale;
2. se l’estensione è troppo invasiva, rompe la continuità con la teoria classica.

La strategia adottata qui è conservativa-selettiva:

1. conservativa sul piano strutturale;
2. selettiva sul piano ordinativo.

In altre parole:

1. non cambiamo il significato classico di composizione e identità;
2. introduciamo un livello di ammissibilità che decide quando la stessa struttura è operativamente reale in `Omega`.

### 1.1 Perché questo capitolo viene dopo la fase 8-11

Ordine non lineare ma intenzionale:

1. prima abbiamo fissato lo spazio di validità e i teoremi;
2. ora torniamo alla micro-struttura classica con criteri già stabilizzati.

Il vantaggio è metodologico:

1. le definizioni qui introdotte non sono “promesse”, ma già agganciate a metriche e criteri di fallimento;
2. ogni scelta locale su oggetto/morfismo/composizione/identità può essere testata contro il quadro critico del Capitolo 11.

### 1.2 Obiettivo tecnico del capitolo

L’obiettivo non è riscrivere da zero la teoria degli oggetti e dei morfismi, ma esplicitare:

1. qual è il corrispettivo OCT di ogni nozione classica;
2. quali condizioni aggiuntive servono per ammissibilità ordinativa;
3. quali errori di inferenza sono evitati dalla riformulazione.

---

## 2. Tesi del capitolo

La tesi del capitolo è articolata in otto enunciati.

1. L’oggetto ordinativo è una singolarizzazione contestuale di un oggetto classico, non una sostituzione antagonista.
2. Il morfismo ordinativo è un morfismo classico ben tipizzato più vincolo di ammissibilità `Coh/Phi`.
3. La composizione ordinativa è chiusa solo condizionatamente (gate sulla composta).
4. L’identità ordinativa richiede neutralità non-degenerativa, non sola tautologia sintattica.
5. La struttura classica è preservata dal funtore di oblio, ma non vale il viceversa in generale.
6. Le quattro nozioni classiche restano formalmente intatte e vengono rafforzate da criteri operativi.
7. La distinzione tra validità locale e validità composita è obbligatoria in OCT.
8. Il capitolo prepara direttamente limiti/colimiti/equivalenze del Capitolo 5.

---

## 3. Definizioni canoniche

### Definizione 4.1 (Oggetto ordinativo)

Dato un oggetto classico `A`, definiamo l’oggetto ordinativo in `Omega`:

`A_Omega := S_Omega(A) = <A, R_Omega(A), H_t(A), Pi_Omega(A)>`.

Commento:

1. `A` resta il supporto strutturale;
2. `R_Omega`, `H_t`, `Pi_Omega` introducono la specificazione relazionale-funzionale minima.

### Definizione 4.2 (Morfismo ordinativamente ammissibile)

Per `f: A_Omega -> B_Omega`:

`Adm_Omega(f) := Syn(f) and Coh_Omega(f) >= tau_f and Phi_Omega(f) != 0`.

Commento:

1. `Syn(f)` è requisito necessario;
2. `Coh/Phi` sono requisiti selettivi.

### Definizione 4.3 (Composizione ordinativa)

Per `f: A_Omega->B_Omega`, `g: B_Omega->C_Omega`:

`g ∘_Omega f` è ammessa se:

1. `g∘f` è definita in senso classico;
2. `Adm_Omega(f)` e `Adm_Omega(g)`;
3. `Adm_Omega(g∘f)`.

### Definizione 4.4 (Identità ordinativa)

`id_A^Omega: A_Omega -> A_Omega` è identità ordinativa se:

1. coincide con identità classica sul supporto `A`;
2. non induce degradazione oltre soglia su coerenza/funzione in auto-applicazione.

### Definizione 4.5 (Classe di composizione sterile)

Una composizione è sterile se:

1. è sintatticamente lecita;
2. mantiene coerenza sopra soglia;
3. ma `Phi_Omega=0`.

Questa classe è distinta dalla degenerazione pura (`Coh<tau`).

### Definizione 4.6 (Funtore di oblio ordinativo)

`U_Omega: OrdCat_Omega -> Cat_class`

rimuove il layer ordinativo mantenendo oggetti, morfismi e leggi classiche.

---

## 4. Sviluppo formale

### 4.1 Oggetti: dal nodo astratto al nodo tipizzato

Nel quadro classico, un oggetto è identificato dal suo ruolo in una rete di morfismi. Questa impostazione resta valida in OCT, ma viene resa operativa con un vincolo contestuale.

Passaggio:

1. classico: `A`;
2. ordinativo: `A_Omega = <A,R,H,Pi>`.

Questa estensione non altera le leggi classiche. Introduce però una differenza cruciale:

1. due oggetti possono essere formalmente equivalenti in un livello astratto;
2. ma divergere ordinativamente per profilo relazionale, storia e funzione emergente.

Errore evitato:

1. assumere che identità simbolica o equivalenza strutturale basti per identità operativa.

### 4.2 Morfismi: tipizzazione più generatività

In category theory classica, la validità del morfismo è primariamente tipologica. In OCT questo resta il primo filtro, ma non l’ultimo.

Schema:

1. filtro 1: `Syn(f)` (classico);
2. filtro 2: `Coh_Omega(f)>=tau_f`;
3. filtro 3: `Phi_Omega(f)!=0`.

Ne segue una distinzione esplicita:

1. morfismi leciti ma sterili;
2. morfismi leciti ma degenerativi;
3. morfismi ordinativamente ammissibili.

Questa tripartizione migliora la diagnosi locale e prepara la composizione controllata.

### 4.3 Composizione: chiusura condizionata

La legge classica `g∘f` resta intatta. Quello che cambia è la nozione di “chiusura utile”.

In OCT:

1. non basta che `f` e `g` siano ammissibili singolarmente;
2. serve test ordinativo sulla composta.

Questo evita inferenze lineari errate:

1. “due passi validi implicano sempre traiettoria valida”.

Controesempio tipico:

1. `f` preserva coerenza locale;
2. `g` preserva coerenza locale;
3. `g∘f` amplifica incompatibilità latenti e cade sotto soglia.

Conclusione:

1. la composizione ordinativa è una legge con gate, non solo una concatenazione.

### 4.4 Identità: neutralità condizionata

Nel classico, `id_A` è neutra per definizione strutturale. In OCT la neutralità è anche una proprietà misurabile.

Richiesta minima:

1. auto-applicazione non produce deriva sistematica su `Coh/Phi`.

Perché è necessario:

1. in sistemi dinamici reali, un’operazione formalmente neutra può attivare costi nascosti, attriti di sincronizzazione o perdita funzionale.

Errore evitato:

1. confondere neutralità simbolica con neutralità operativa.

### 4.5 Composizione locale vs composizione globale

Distinzione obbligatoria:

1. validità locale: test su singolo morfismo;
2. validità globale: test su catena compositiva.

In OCT entrambe sono necessarie:

1. la sola validità locale non garantisce tenuta globale;
2. la sola validità globale senza tracciamento locale rende opaca la diagnosi di fallimento.

Questa distinzione è fondamentale per pipeline modulari e sistemi multi-stadio.

### 4.6 Oggetti e morfismi come coppia inseparabile

Nel quadro ordinativo, non ha senso valutare un oggetto senza dinamica morfismica, né un morfismo senza contesto oggettuale singolarizzato.

Principio operativo:

1. `A_Omega` determina condizioni di ammissibilità dei morfismi uscenti/entranti;
2. l’insieme dei morfismi ammissibili retro-definisce lo stato operativo di `A_Omega`.

Ne deriva una co-definizione dinamica:

1. oggetti e morfismi sono analiticamente distinguibili ma operativamente co-determinati.

### 4.7 Stabilità di composizione in vicinato contestuale

Per prevenire fragilità da fitting locale, la composizione va valutata anche su `N_epsilon(Omega)`.

Richiesta minima:

1. `Adm_Omega(g∘f)` deve restare stabile entro perturbazioni ammesse.

In assenza di questa condizione:

1. si ottengono composizioni “formalmente vincenti” ma non replicabili.

### 4.8 Relazione con la matrice A/B/C/D

Oggetti e morfismi in OCT possono essere classificati tramite la matrice standard:

1. A: ammissibile pieno;
2. B: lecito ma sterile;
3. C: lecito ma degenerativo;
4. D: non lecito sintatticamente.

Nel Capitolo 4 questa matrice è utile per:

1. qualificare rapidamente lo stato di un morfismo;
2. spiegare perché una composizione viene accettata o rifiutata.

### 4.9 Recupero classico come controllo di coerenza

Il capitolo conserva esplicitamente la riduzione classica:

1. se il layer ordinativo è disattivato, restano oggetti/morfismi/composizione/identità classici.

Questo punto impedisce due letture sbagliate:

1. OCT come negazione del classico;
2. OCT come lessico alternativo senza nuove regole.

### 4.10 Mappa errori tipici evitati dal capitolo

Errori classici in applicazione ingenua:

1. “tipizzato quindi valido”;
2. “composto quindi robusto”;
3. “identità quindi neutro in ogni senso”;
4. “equivalenza locale quindi equivalenza globale”.

Il capitolo fornisce, per ciascun errore, un criterio di controllo operativo.

### 4.11 Composizione lunga e accumulo di rischio ordinativo

Una catena compositiva lunga `f_n ∘ ... ∘ f_1` introduce un problema che il controllo locale non risolve da solo: l’accumulo di rischio.

Anche quando ogni `f_i` soddisfa il gate locale, il sistema può mostrare:

1. drift progressivo di coerenza;
2. compressione della funzione emergente;
3. amplificazione di perdite marginali in punti di interfaccia.

Per questo proponiamo un criterio di monitoraggio a due scale:

1. **scala locale**: `Adm_Omega(f_i)` per ogni passo;
2. **scala cumulativa**: `Adm_Omega(F_k)` per ogni prefisso `F_k = f_k ∘ ... ∘ f_1`.

Il vantaggio è diagnostico:

1. si individua il punto in cui la catena passa da robusta a fragile;
2. si evita di attribuire il collasso solo all’ultimo morfismo osservato.

Questa analisi è particolarmente importante per pipeline IA multi-step e trasformazioni semantiche iterabili.

### 4.12 Criterio di margine compositivo

Oltre al gate binario (ammesso/non ammesso), introduciamo un margine compositivo:

`m_comp(F_k) := Coh_Omega(F_k) - tau_chain`.

Uso operativo:

1. `m_comp >> 0`: catena robusta;
2. `m_comp > 0` ma piccolo: catena fragile, da monitorare;
3. `m_comp <= 0`: catena degenerativa.

Il margine permette decisioni più fini:

1. non tutte le composizioni ammesse hanno la stessa affidabilità;
2. il valore di margine guida priorità di revisione e strategie di riprogettazione.

In assenza di margine, si rischia una logica “on/off” che non cattura la dinamica di prossimità al collasso.

### 4.13 Interfacce tra morfismi: punto critico nascosto

Molti fallimenti globali non nascono dal singolo morfismo, ma dalla giunzione tra morfismi consecutivi. In termini pratici, la compatibilità tipologica non garantisce compatibilità ordinativa di interfaccia.

Definiamo quindi il concetto di **interfaccia ordinativa** tra `f` e `g`:

1. allineamento semantico delle uscite/ingressi;
2. assenza di perdita sistematica di coerenza al passaggio;
3. mantenimento della funzione emergente in transizione.

Un criterio minimo è:

`Int_Omega(g,f) = true` se il passaggio `B_f -> B_g` non introduce delta critico su `Coh` o annullamento su `Phi`.

Conseguenze operative:

1. debug mirato su confini di modulo;
2. migliore separazione tra errore “di modulo” ed errore “di integrazione”.

### 4.14 Tipologia dei fallimenti su oggetti e morfismi

Per rendere il capitolo utilizzabile nei cicli di validazione, proponiamo una tipologia minima dei fallimenti.

1. **F-Obj1 (Oggetto sottospecificato)**  
   `A_Omega` non ha profilo relazionale sufficiente per test affidabile.

2. **F-Mor1 (Morfismo sterile)**  
   `Syn` e `Coh` validi, ma `Phi=0`.

3. **F-Mor2 (Morfismo degenerativo)**  
   `Syn` valido, ma `Coh<tau`.

4. **F-Comp1 (Composta fragile)**  
   passi locali validi, composta al bordo di soglia.

5. **F-Comp2 (Composta collassata)**  
   composta in classe degenerativa.

6. **F-Id1 (Identità non neutra)**  
   auto-applicazione con drift ordinativo misurabile.

Questa tipologia ha tre vantaggi:

1. uniforma il lessico nei report di test;
2. collega direttamente tipo di fallimento e strategia di correzione;
3. riduce conflitti interpretativi tra team.

### 4.15 Criterio minimo di accettazione per modulo compositivo

Proponiamo una regola di accettazione pratica per moduli OCT-based:

un modulo può essere dichiarato “ordinativamente affidabile” solo se soddisfa contemporaneamente:

1. assenza di fallimenti F-Mor2 su suite primaria;
2. frequenza F-Mor1 sotto soglia dichiarata;
3. nessun caso F-Comp2 su scenari di carico nominale;
4. margine compositivo medio positivo sopra valore minimo dichiarato;
5. log completo delle interfacce critiche.

Questa regola non pretende universalità assoluta, ma fornisce un baseline replicabile per sviluppo e pubblicazione tecnica.

---

## 5. Proposizioni e teoremi locali

### Proposizione 4.1 (Conservazione sintattica degli oggetti)

Enunciato:
La singolarizzazione `S_Omega` non distrugge la tipizzazione classica dell’oggetto.

Intuizione:
`A_Omega` contiene `A` come supporto strutturale, con estensione relazionale-funzionale.

Stato: `validated`.

### Proposizione 4.2 (Necessità del gate morfismico)

Enunciato:
Esistono morfismi `Syn(f)` veri ma `Adm_Omega(f)` falsi.

Intuizione:
controesempi con `Phi=0` o `Coh<tau` rendono il gate indispensabile.

Stato: `validated`.

### Teorema 4.3 (Chiusura condizionata della composizione)

Ipotesi:
1. `Adm_Omega(f)` e `Adm_Omega(g)`;
2. composizione classica definita;
3. `Adm_Omega(g∘f)` verificata.

Tesi:
`g∘_Omega f` è composizione ordinativa valida.

Proof sketch:
1. la definibilità classica garantisce coerenza sintattica;
2. il gate sulla composta garantisce non-degenerazione e non-sterilità;
3. dunque la composta è ammessa in `OrdCat_Omega`.

Conseguenze:
stabilisce il meccanismo operativo per catene compositive affidabili.

Stato: `in_proof`.

### Teorema 4.4 (Neutralità ordinativa condizionata dell’identità)

Ipotesi:
1. `id_A` classica su `A`;
2. test ordinativo su auto-applicazione in `Omega`;
3. assenza di degradazione oltre soglia.

Tesi:
`id_A^Omega` è neutra in senso ordinativo.

Proof sketch:
1. la neutralità sintattica è data;
2. la neutralità ordinativa richiede stabilità su `Coh/Phi`;
3. soddisfatte entrambe, l’identità è pienamente neutra.

Conseguenze:
evita uso improprio dell’identità in domini dinamici ad attrito.

Stato: `in_proof`.

### Proposizione 4.5 (Non equivalenza locale-globale)

Enunciato:
Validità ordinativa locale dei morfismi non implica validità ordinativa globale della catena.

Intuizione:
la composta può introdurre incompatibilità emergenti non visibili localmente.

Stato: `validated`.

### Teorema 4.6 (Accumulo non lineare del rischio compositivo)

Ipotesi:
1. catena compositiva `F_n = f_n ∘ ... ∘ f_1` con `Adm_Omega(f_i)` veri;
2. esiste almeno un sottoinsieme di interfacce con `Int_Omega` debole;
3. il contributo di rischio di interfaccia è non nullo e persistente.

Tesi:
La validità locale uniforme non garantisce, in generale, margine compositivo globale stabile.

Proof sketch:
1. ogni `f_i` può rispettare il gate locale;
2. le interfacce deboli introducono perdite incrementali;
3. le perdite possono accumularsi oltre il bordo di sicurezza della catena;
4. ne segue che il margine globale può diventare fragile o negativo.

Conseguenze:
1. giustifica monitoraggio su prefissi compositivi;
2. fonda la necessità di metriche di interfaccia oltre le metriche di modulo.

Stato: `in_proof`.

---

## 6. Implicazioni operative

### 6.1 Per implementazione di pipeline compositive

Ogni pipeline OCT dovrebbe verificare:

1. gate locale su ogni morfismo;
2. gate globale su composte critiche;
3. classificazione A/B/C/D per diagnosticare i fallimenti.

### 6.2 Per la documentazione di progetto

È utile che ogni modulo espliciti:

1. oggetti singolarizzati coinvolti;
2. morfismi ammessi e non ammessi;
3. ragione del rifiuto (sterilità vs degenerazione).

Questo rende tracciabile il comportamento del sistema e accelera revisione.

### 6.3 Per la validazione empirica

I test dovrebbero includere:

1. casi positivi di composizione robusta;
2. casi negativi di composizione fragile;
3. stress su identità in presenza di perturbazioni leggere.

### 6.4 Per il passaggio al Capitolo 5

Limiti, colimiti, equivalenze e isomorfismi del Capitolo 5 useranno direttamente le nozioni qui fissate:

1. oggetto ordinativo;
2. morfismo ammissibile;
3. composizione con gate;
4. identità non-degenerativa.

### 6.5 Per la governance editoriale

Ogni nuova versione dovrebbe mantenere coerenza su questi quattro blocchi. Se cambia uno, devono essere riesaminati anche gli altri per evitare incoerenze interne nel manoscritto.

Inoltre, è consigliabile mantenere un changelog locale per oggetti, morfismi, composizioni e identità, così da collegare ogni modifica teorica a effetti misurabili sui benchmark.

---

## 7. Limiti e non-claim

Limiti espliciti:

1. il capitolo non chiude ancora la formalizzazione completa dei casi enriched/2-categoriali;
2. la scelta delle soglie resta dominio-dipendente;
3. la neutralità ordinativa dell’identità richiede protocolli di misura robusti;
4. la distinzione locale-globale è formalizzata in versione minima, da estendere.

Failure mode riconosciuti:

1. sovra-ottimizzare i gate su dati specifici;
2. confondere casi sterili con casi degenerativi;
3. applicare il gate globale senza diagnosi locale;
4. dichiarare neutralità identitaria senza test ordinativo.

Box C - Non-claim

Questo capitolo non implica:
1. che ogni struttura classica debba essere automaticamente reinterpretata in OCT;
2. che il gate ordinativo elimini la necessità di prove matematiche classiche;
3. che l’ammissibilità ordinativa locale sia sufficiente per garantire robustezza sistemica.

---

## 8. Claim Ledger (S0-S3)

| ID | Claim | Tipo | Evidenza | Stato |
|---|---|---|---|---|
| C4.1 | L’oggetto ordinativo conserva il supporto classico e aggiunge specificazione relazionale-funzionale | formale | S2 | in_review |
| C4.2 | Il morfismo ordinativo richiede gate `Syn+Coh+Phi` | formale | S1 | validated |
| C4.3 | La composizione ordinativa è chiusa in modo condizionato e non automatico | formale | S2 | in_proof |
| C4.4 | L’identità ordinativa richiede neutralità non-degenerativa verificata | formale | S2 | in_proof |
| C4.5 | La validità locale non implica validità globale | formale-operativo | S1 | validated |
| C4.6 | La matrice A/B/C/D migliora la diagnosi operativa su oggetti e morfismi | metodologico | S1 | in_review |

---

## 9. Bridge al Capitolo 5

Il Capitolo 4 ha stabilito la grammatica micro-strutturale dell’estensione OCT:

1. cosa sono gli oggetti in forma singolarizzata;
2. cosa rende un morfismo ammissibile;
3. quando una composizione è realmente valida;
4. cosa significa identità in senso non-degenerativo.

Il Capitolo 5 userà questa base per affrontare il livello successivo:

1. isomorfismi ed equivalenze;
2. limiti e colimiti;
3. selettività ordinativa delle costruzioni universali.

In sintesi: il Capitolo 4 fissa i mattoni; il Capitolo 5 valuterà la stabilità delle architetture costruite con quei mattoni.

---

## Riferimenti

Riferimenti di framework interno:

1. Ghioni, F. (2026). `TE_CORE_v5.1.md`.
2. Ghioni, F. (2026). `Ordinative_Set_Theory_OST_A_Concise_Guide_For_AI_v2_1.md`.
3. `OCT_FOUNDATIONAL_BOOK_CHAPTER_03_v1_0.md`.
4. `OCT_FOUNDATIONAL_BOOK_CHAPTER_08_v1_0.md`.
5. `OCT_FOUNDATIONAL_BOOK_CHAPTER_09_v1_0.md`.
6. `OCT_FOUNDATIONAL_BOOK_CHAPTER_11_v1_0.md`.

Riferimenti primari:

1. Eilenberg, S., Mac Lane, S. (1945). *General Theory of Natural Equivalences*.
2. Mac Lane, S. (1998). *Categories for the Working Mathematician*.
3. Riehl, E. (2016). *Category Theory in Context*.
4. Spivak, D. (2014). *Category Theory for the Sciences*.
