# Capitolo 7 - Monoidali, enriched, fibrations, topos e dinamiche categoriali

Metadati:
- Versione: v1.0
- Data: 2026-04-22
- Stato: draft completo
- Autore: Fabio Ghioni
- Allineato a: TE_CORE v5.1 / OST v2.1 / OCT baseline v1.0 candidate
- Target parole capitolo: 3.600

---

## 1. Problema

Con i Capitoli 4-6 abbiamo completato la transizione dai mattoni locali della teoria (oggetti, morfismi, composizione, identità) al livello trasformazionale (funtori, naturali, aggiunzioni, monadi/comonadi). Resta ora il passaggio verso le strutture categoriali avanzate che, nel corpus classico, consentono di modellare sistemi complessi multilivello:

1. categorie monoidali;
2. categorie arricchite;
3. fibrations;
4. topos.

Nel quadro classico queste strutture estendono potenza espressiva e generalità. In OCT dobbiamo aggiungere una condizione ulteriore: la complessità strutturale non deve diventare opacità ordinativa. Una struttura più ricca è utile solo se:

1. resta interpretabile in termini di `Coh/Phi/Delta`;
2. mantiene robustezza sotto variazioni contestuali;
3. non nasconde degenerazioni dietro simmetrie formali.

Il problema del capitolo è quindi:

**come estendere le strutture avanzate della category theory mantenendo insieme rigore classico, selettività ordinativa e tracciabilità operativa?**

La difficoltà è concreta:

1. strutture monoidali possono imporre simmetrie non sostenibili in dominio reale;
2. arricchimenti possono aumentare espressività ma anche amplificare rumore;
3. fibrations possono modellare dipendenze verticali ma introdurre perdita tra base e fibra;
4. topos possono offrire quadro logico interno potente ma non garantire, da soli, validità ordinativa.

Questo capitolo fornisce quindi una grammatica avanzata, ma disciplinata da un principio unico:

1. ogni estensione strutturale deve dichiarare il proprio costo ordinativo.

### 1.1 Perché questo capitolo chiude la milestone `v1.3`

La milestone `v1.3` mira a espandere sistematicamente il corpus classico in chiave OCT (Capitoli 4-7). Il Capitolo 7 è il punto di chiusura perché affronta i costrutti dove la complessità teorica diventa maggiore e dove il rischio di “equivalenza apparente” cresce.

Se il capitolo regge:

1. il ponte verso protocollo, benchmark e governance (`v1.4`) diventa naturale;
2. la teoria può passare da fondazione/estensione a standard operativo.

### 1.2 Obiettivo tecnico

Obiettivo minimo del capitolo:

1. definire criteri ordinativi per monoidali, enriched, fibrations, topos;
2. mostrare casi tipici in cui la struttura classica resta valida ma l’uso ordinativo richiede restrizioni;
3. fissare regole di accettazione per strutture avanzate in scenari reali.

---

## 2. Tesi del capitolo

La tesi è articolata in dieci enunciati.

1. La struttura monoidale classica è necessaria ma non sempre sufficiente in contesti ordinativi asimmetrici.
2. Le categorie arricchite diventano ordinativamente utili solo se l’arricchimento non distrugge margine coerentivo.
3. Le fibrations sono strumenti potenti per stratificare contesti, ma richiedono controllo esplicito del trasporto verticale.
4. Un topos può fornire logica interna forte senza garantire automaticamente realtà ordinativa dei costrutti.
5. Esiste una nozione di “coerenza multilivello” che collega base, fibre e dinamica globale.
6. Le simmetrie e dualità avanzate restano condizionate dal dominio osservativo.
7. La complessità strutturale deve essere accompagnata da criteri di fallimento tracciabili.
8. Le strutture avanzate possono essere classificate con la stessa grammatica A/B/C se si esplicitano i mapping.
9. L’estensione proposta resta compatibile con recupero classico.
10. Il capitolo prepara direttamente il passaggio metodologico dei Capitoli 12-14.

---

## 3. Definizioni canoniche

### Definizione 7.1 (Categoria monoidale ordinativa)

Una categoria monoidale ordinativa è una categoria monoidale classica `(C, tensor, I)` con vincolo aggiuntivo:

1. le operazioni `tensor` su oggetti/morfismi rilevanti non devono produrre caduta sistematica sotto soglia su `Coh`;
2. la composizione monoidale deve preservare `Phi` non nulla su classi operative dichiarate.

### Definizione 7.2 (Simmetria monoidale condizionata)

La simmetria `sigma_{A,B}: A tensor B -> B tensor A` è ordinativamente ammissibile solo se il cambio di ordine non altera in modo critico invarianti ordinativi del dominio.

### Definizione 7.3 (Categoria arricchita ordinativa)

Una categoria arricchita ordinativa è una categoria arricchita classica in cui l’oggetto-hom arricchito incorpora anche indicatori ordinativi minimi (coerenza, emergenza, margine).

### Definizione 7.4 (Fibration ordinativa)

Una fibration ordinativa `p: E->B` è una fibration classica in cui:

1. il sollevamento cartesiano non introduce perdita ordinativa non dichiarata;
2. la relazione base-fibra mantiene coerenza multilivello su classi test.

### Definizione 7.5 (Coerenza multilivello)

Dato un oggetto fibrato, la coerenza multilivello è la compatibilità tra:

1. coerenza nel livello base;
2. coerenza nel livello fibra;
3. coerenza delle mappe di passaggio.

### Definizione 7.6 (Topos ordinativo)

Un topos ordinativo è un topos classico usato in contesto OCT con vincolo che i costrutti logici interni impiegati in inferenze operative siano validati anche in termini ordinativi.

### Definizione 7.7 (Dinamica categoriale ordinativa)

Una dinamica categoriale ordinativa è una evoluzione temporale di strutture/funtori in cui:

1. i passaggi temporali restano formalmente leciti;
2. l’evoluzione non produce deriva sistematica verso sterilità/degenerazione.

### Definizione 7.8 (Costo di complessità strutturale)

Definiamo costo sintetico di complessità:

`Cost_str := c1*Instab + c2*Loss_tr + c3*Opac`

dove `Opac` misura perdita di leggibilità causale del sistema al crescere della stratificazione.

---

## 4. Sviluppo formale

### 4.1 Monoidali: potenza compositiva e asimmetria reale

La struttura monoidale classica permette di modellare composizioni parallele o tensoriali. In OCT questa potenza è preziosa, ma va gestita con prudenza:

1. in domini simmetrici il tensor può preservare bene `Coh/Phi`;
2. in domini direzionali la simmetrizzazione può distruggere informazione funzionale.

Da qui una regola operativa:

1. `tensor` è ammesso sempre formalmente;
2. è ammesso in senso ordinativo solo dopo test di simmetria condizionata.

Errore evitato:

1. imporre simmetria per eleganza algebrica quando il dominio è strutturalmente orientato.

### 4.2 Arricchimento: espressività contro opacità

Arricchire una categoria significa dare struttura più ricca agli hom. In OCT questo può essere vantaggioso perché:

1. rende espliciti gradi di qualità relazionale;
2. consente metriche più fini su trasporto e composizione.

Ma c’è un rischio:

1. over-arricchimento che aumenta parametri e riduce stabilità inferenziale.

Per questo proponiamo un criterio di arricchimento sobrio:

1. introdurre solo componenti che migliorano decisione A/B/C;
2. evitare componenti decorative senza impatto diagnostico.

### 4.3 Fibrations: verticalità controllata

Le fibrations permettono di separare livelli di descrizione (base/fibra). In OCT sono utili per modellare contesti multilivello, ma possono introdurre perdita verticale:

1. informazioni mantenute in fibra ma non nella base;
2. coerenza locale alta in fibra con incoerenza globale in base;
3. trasporto verticale formalmente corretto ma ordinativamente dissipativo.

Serve quindi un controllo bilanciato:

1. test di coerenza interna alle fibre;
2. test di coerenza tra fibre e base;
3. test di stabilità dei lift sotto perturbazione contestuale.

### 4.4 Topos: logica interna e validità ordinativa

Un topos fornisce ambiente logico potente (subobject classifier, exponentials, ecc.). In OCT questo non viene negato. Tuttavia:

1. validità logica interna non equivale automaticamente a validità ordinativa esterna;
2. inferenze interne devono essere collegate a criteri di `Coh/Phi` quando usate per decisioni operative.

Ne segue una distinzione:

1. verità interna al topos;
2. accettabilità ordinativa nel dominio osservato.

Questa distinzione evita che la ricchezza logica mascheri fragilità dinamiche.

### 4.5 Dinamiche categoriali: dal statico al processo

Molte strutture avanzate sono presentate staticamente. In applicazioni reali, però, categorie/funtori cambiano nel tempo. OCT richiede quindi una nozione dinamica:

1. sequenze di strutture `C_t`;
2. transizioni `T_t: C_t -> C_{t+1}`;
3. monitoraggio di deriva su invarianti globali.

Punto chiave:

1. una struttura può essere ordinativamente valida a `t0` e non esserlo a `t1`;
2. la validazione deve quindi includere traiettoria, non solo istanti.

### 4.6 Interazione tra monoidali e arricchimenti

Quando si combinano tensor e arricchimento aumentano le interazioni non lineari:

1. il tensor può amplificare rumore dei valori arricchiti;
2. un arricchimento utile localmente può diventare instabile in composizione tensoriale.

Serve un test combinato:

1. validità di `tensor` su oggetti semplici;
2. validità su oggetti arricchiti;
3. confronto differenziale tra i due regimi.

### 4.7 Interazione tra fibrations e topos

In sistemi complessi è frequente usare logica interna (stile topos) su strutture stratificate (stile fibration). Qui il rischio maggiore è la disconnessione:

1. coerenza logica locale alta;
2. incoerenza di trasporto tra livelli.

Per evitarla proponiamo il principio di allineamento verticale:

1. ogni inferenza interna usata operativamente deve avere tracciamento su livello base/fibra.

### 4.8 Criterio di accettazione per strutture avanzate

Una struttura avanzata (`monoidal`, `enriched`, `fibration`, `topos`) è ordinativamente accettabile se:

1. definita e verificata classicamente;
2. testata su invarianti ordinativi minimi;
3. robusta su variazioni contestuali rilevanti;
4. dotata di mappa fallimenti specifica.

Questa regola unifica i quattro blocchi in una policy comune.

### 4.9 Mappa fallimenti specifica del capitolo

1. **F-Mon2**: tensor formalmente corretto con simmetria ordinativamente distruttiva.
2. **F-Enr1**: arricchimento informativo ma instabile su composizione.
3. **F-Fib1**: lift cartesiano con perdita verticale critica.
4. **F-Fib2**: coerenza di fibra alta, coerenza di base bassa.
5. **F-Top1**: inferenza interna valida, ma non trasferibile operativamente.
6. **F-Dyn1**: validità puntuale alta, deriva temporale verso classe C.

Questa tipologia è utile per collegare teoria avanzata e benchmark dedicati.

### 4.10 Controllo di complessità: quando fermarsi

Una lezione pratica del capitolo è che più struttura non significa sempre più scienza. Se `Cost_str` cresce senza migliorare decisione o robustezza, l’estensione va ridotta.

Regola pragmatica:

1. aggiungere complessità solo se migliora almeno uno tra:
   - precisione diagnostica;
   - robustezza;
   - trasferibilità.

Se nessun miglioramento è misurabile, la complessità è epistemicamente ingiustificata.

### 4.11 Compatibilità con recupero classico

Anche qui vale F10:

1. disattivando il layer ordinativo, restano monoidali/enriched/fibrations/topos classici;
2. attivando il layer, si ottiene filtro di realtà compositiva senza negazione del quadro classico.

### 4.12 Condizione di non-ridondanza del capitolo

Il capitolo è non ridondante se esiste almeno un caso in cui:

1. la struttura avanzata classica è valida;
2. la stessa struttura fallisce in senso ordinativo per motivi tracciabili.

Questa condizione è soddisfatta dai pattern F-Mon2/F-Fib1/F-Top1/D04/D05 e dai casi applicativi ad alta stratificazione.

### 4.13 Matrice stratificata di validazione avanzata

Per mantenere confrontabili analisi diverse, proponiamo una matrice di validazione a tre strati:

1. **Strato Formale (SF)**: verifica classica della struttura avanzata;
2. **Strato Ordinativo (SO)**: verifica su `Coh/Phi/Delta`, margine e robustezza;
3. **Strato Dinamico (SD)**: verifica della stabilità temporale su evoluzioni non banali.

Decisione proposta:

1. `accepted_strong` solo se SF, SO e SD sono positivi;
2. `accepted_limited` se SF e SO positivi ma SD incompleto (uso limitato e monitorato);
3. `revise` se SF positivo ma SO o SD negativi;
4. `reject` se SF negativo o fallimenti ordinativi non recuperabili.

Questa matrice evita un problema frequente: strutture avanzate formalmente corrette promosse troppo presto senza evidenza dinamica.

### 4.14 Coupling tra tensor e arricchimento

In molte applicazioni, monoidalità e arricchimento vengono usati insieme. Il coupling tra i due livelli può produrre effetti non lineari.

Proponiamo di monitorare:

`Kappa_enr_tensor := Sens_tensor(Enr) + Sens_enr(tensor)`.

Interpretazione:

1. `Kappa` basso: interazione controllata;
2. `Kappa` medio: interazione utile ma sensibile;
3. `Kappa` alto: rischio di instabilità con piccole variazioni di configurazione.

Azioni consigliate quando `Kappa` è alto:

1. ridurre dimensionalità dell’arricchimento;
2. restringere classe di oggetti su cui applicare `tensor`;
3. introdurre normalizzazione intermedia.

Questo blocco migliora la diagnosi preventiva: invece di reagire al collasso, si monitorano indicatori che lo anticipano.

### 4.15 Regola di trasporto base-fibra nei sistemi fibrati

Per le fibrations in contesti reali proponiamo una regola di trasporto in due fasi.

1. **Fase fibra**: validazione locale dei costrutti e delle inferenze;
2. **Fase base**: validazione dell’impatto aggregato sul livello superiore.

Solo il passaggio congiunto delle due fasi autorizza inferenze operative forti.  
Questo impedisce due errori classici:

1. assumere che “vero in fibra” implichi “robusto in base”;
2. imporre vincoli di base che annullano informazione utile delle fibre.

La regola rende esplicita la responsabilità di ogni livello nella tenuta complessiva.

### 4.16 Protocollo minimo avanzato (PMA-7)

Per standardizzare la verifica di strutture avanzate proponiamo un protocollo in sette passi:

1. definire struttura classica e dominio d’uso;
2. dichiarare `Omega`, soglie e invarianti critici;
3. verificare SF (assiomi classici della struttura);
4. verificare SO (metriche ordinative);
5. verificare SD (stabilità temporale);
6. classificare fallimenti secondo F-Mon/F-Enr/F-Fib/F-Top/F-Dyn;
7. assegnare stato finale con motivazione e limiti dichiarati.

Il PMA-7 non sostituisce prove matematiche complete, ma uniforma la fase di validazione comparativa e prepara direttamente i capitoli metodologici successivi.

---

## 5. Proposizioni e teoremi locali

### Proposizione 7.1 (Simmetria monoidale condizionata)

Enunciato:
La simmetria monoidale è ordinativamente ammissibile solo su domini che non perdono informazione funzionale sotto scambio.

Intuizione:
domini direzionali possono violare stabilità pur mantenendo validità classica.

Stato: `in_review`.

### Proposizione 7.2 (Necessità di coerenza multilivello nelle fibrations)

Enunciato:
La sola correttezza del lift cartesiano non garantisce affidabilità ordinativa della stratificazione.

Intuizione:
serve compatibilità simultanea base-fibra-passaggio.

Stato: `validated`.

### Teorema 7.3 (Vincolo di allineamento verticale)

Ipotesi:
1. sistema fibrato con inferenze interne operative;
2. tracciamento completo base/fibra;
3. assenza di perdita verticale critica.

Tesi:
Le inferenze stratificate sono ordinativamente affidabili nel dominio dichiarato.

Proof sketch:
1. il tracciamento elimina ambiguità di livello;
2. l’assenza di perdita critica preserva coerenza multilivello;
3. segue affidabilità operativa dell’inferenza.

Conseguenze:
criterio pratico per usare fibrations in pipeline reali.

Stato: `in_proof`.

### Teorema 7.4 (Deriva dinamica di strutture avanzate)

Ipotesi:
1. sequenza temporale `C_t` con transizioni `T_t`;
2. monitoraggio su invarianti globali;
3. presenza di accumulo negativo oltre soglia.

Tesi:
Una struttura avanzata può passare da ordinativamente valida a non valida pur restando formalmente lecita.

Proof sketch:
1. validità classica è puntuale e sintattica;
2. accumulo dinamico può degradare margine ordinativo;
3. la dinamica produce crossing verso classe B/C.

Conseguenze:
necessità di validazione temporale, non solo statica.

Stato: `in_proof`.

### Proposizione 7.5 (Topos non implica realtà ordinativa)

Enunciato:
La ricchezza logica interna di un topos non implica automaticamente robustezza ordinativa dei costrutti usati.

Intuizione:
verità interna e operatività esterna sono livelli distinti.

Stato: `validated`.

### Teorema 7.6 (Criterio minimo di accettazione per strutture avanzate)

Ipotesi:
1. validità classica della struttura;
2. test ordinativo su invarianti;
3. robustezza contestuale;
4. mappa fallimenti specifica disponibile.

Tesi:
La struttura può essere accettata per uso operativo ordinativo.

Proof sketch:
1. requisito classico garantisce correttezza formale;
2. requisiti ordinativi garantiscono realtà compositiva;
3. la mappa fallimenti garantisce falsificabilità.

Conseguenze:
fornisce standard unico per monoidali/enriched/fibrations/topos.

Stato: `in_proof`.

### Proposizione 7.7 (Utilità della matrice SF/SO/SD)

Enunciato:
La matrice stratificata SF/SO/SD riduce errori di attribuzione causale nei fallimenti di strutture avanzate.

Intuizione:
separando forma, validità ordinativa e dinamica, si evita di confondere errori assiomatici con instabilità applicative.

Stato: `in_review`.

### Teorema 7.8 (Necessità del controllo dinamico per accettazione forte)

Ipotesi:
1. struttura avanzata con SF e SO positivi;
2. dominio con evoluzione temporale rilevante;
3. assenza di verifica SD.

Tesi:
Non è possibile dichiarare `accepted_strong` senza controllo dinamico.

Proof sketch:
1. SF e SO descrivono correttezza e affidabilità locale;
2. in domini dinamici può emergere deriva non osservabile staticamente;
3. quindi SD è condizione necessaria per accettazione forte.

Conseguenze:
formalizza il passaggio da validazione statica a validazione evolutiva.

Stato: `in_proof`.

### Proposizione 7.9 (Monitoraggio del coupling come prevenzione)

Enunciato:
Il monitoraggio di `Kappa_enr_tensor` riduce il rischio di instabilità non lineari in strutture monoidali arricchite.

Intuizione:
la sensibilità incrociata alta è spesso un segnale precoce di collasso su catene compositive complesse.

Stato: `in_review`.

---

## 6. Implicazioni operative

### 6.1 Per progettazione di architetture complesse

Quando si introducono strutture avanzate, è utile decidere in anticipo:

1. quale guadagno diagnostico ci si aspetta;
2. quale costo strutturale è accettabile;
3. quale criterio farà scattare revisione o rollback.

### 6.2 Per benchmark dedicati

È consigliato preparare suite specifiche:

1. `MON_SUITE` per test tensor/simmetria;
2. `ENR_SUITE` per stabilità arricchita;
3. `FIB_SUITE` per coerenza multilivello;
4. `TOP_SUITE` per trasferibilità inferenze interne;
5. `DYN_SUITE` per deriva temporale.

### 6.3 Per reporting scientifico

Ogni risultato su strutture avanzate dovrebbe riportare:

1. definizione classica usata;
2. vincolo ordinativo applicato;
3. classe di fallimento osservata (se presente);
4. stato finale con motivazione.

### 6.4 Per continuità con `v1.4`

Il capitolo fornisce già i mattoni metodologici dei Capitoli 12-14:

1. metrica multilivello;
2. design benchmark orientato a fallimenti reali;
3. governance del costo di complessità.

### 6.5 Per uso interdisciplinare

In contesti non puramente matematici, questa parte aiuta a evitare due estremi:

1. riduzionismo formale (solo eleganza strutturale);
2. empirismo scollegato (solo risultato numerico senza struttura).

La combinazione di entrambi è il contributo operativo di OCT in strutture avanzate.

### 6.6 Per manutenzione del manoscritto

Ogni modifica a questo capitolo dovrebbe propagare controlli almeno su:

1. claim ledger dei Capitoli 6-7;
2. protocollo di validazione del Capitolo 12;
3. checklist benchmark del Capitolo 13.

Questo evita disallineamenti tra teoria avanzata e infrastruttura metodologica.

### 6.7 Per policy di rilascio progressivo

In progetti applicativi è utile adottare una policy a maturità progressiva:

1. fase esplorativa: strutture con stato `in_review` ammesse solo in sandbox;
2. fase pre-rilascio: richiesti SF+SO positivi con limiti espliciti;
3. fase critica: richiesti SF+SO+SD con margine ordinativo minimo garantito.

Questa policy riduce il rischio di rilasciare strutture eleganti ma non robuste.

### 6.8 Per documentazione e peer review

Per aumentare chiarezza è consigliabile allegare, per ogni struttura avanzata:

1. tabella SF/SO/SD;
2. classe di fallimento prevalente;
3. stato finale (`accepted_limited`, `accepted_strong`, `revise`, `reject`);
4. azione correttiva proposta.

Questo formato aiuta revisori con background diversi a convergere su valutazioni comparabili.
Inoltre rende più trasparente il rapporto tra eleganza formale e robustezza operativa.

---

## 7. Limiti e non-claim

Limiti espliciti:

1. il capitolo non contiene prove complete chiuse per tutte le varianti avanzate;
2. la metrica `Cost_str` è proposta in forma minima, da specializzare per dominio;
3. la trattazione dei topos ordinativi è intenzionalmente prudente e non esaustiva.

Failure mode riconosciuti:

1. introdurre arricchimento senza guadagno misurabile;
2. usare fibrations senza controllo base-fibra;
3. assumere simmetria monoidale in domini direzionali;
4. validare strutture statiche ignorando deriva temporale;
5. usare logica interna del topos senza test di trasferibilità operativa.

Box C - Non-claim

Questo capitolo non implica:
1. che ogni struttura avanzata classica debba avere un corrispettivo ordinativo utile;
2. che la complessità strutturale sia di per sé un valore scientifico;
3. che i criteri qui proposti sostituiscano validazione empirica indipendente.

---

## 8. Claim Ledger (S0-S3)

| ID | Claim | Tipo | Evidenza | Stato |
|---|---|---|---|---|
| C7.1 | Le strutture monoidali richiedono simmetria condizionata in domini asimmetrici | formale | S2 | in_review |
| C7.2 | Le fibrations richiedono coerenza multilivello esplicita | formale-operativo | S1 | validated |
| C7.3 | La validità logica interna di un topos non implica validità ordinativa esterna | metateorico | S1 | validated |
| C7.4 | Le strutture avanzate possono mostrare deriva temporale pur restando formalmente lecite | formale-operativo | S2 | in_proof |
| C7.5 | `Cost_str` è utile come indicatore di controllo della complessità strutturale | metodologico | S1 | in_review |
| C7.6 | Il criterio minimo di accettazione avanzata unifica monoidali/enriched/fibrations/topos | metodologico | S2 | in_proof |
| C7.7 | Il capitolo chiude l’espansione classica `v1.3` in forma coerente con i blocchi precedenti | programmatico | S1 | in_review |

---

## 9. Bridge al Capitolo 12

Con questo capitolo si chiude la milestone `v1.3`:

1. Capitolo 4: mattoni locali;
2. Capitolo 5: costrutti universali;
3. Capitolo 6: livello trasformazionale;
4. Capitolo 7: strutture avanzate e dinamiche categoriali.

Il prossimo passaggio (`v1.4`) non aggiunge solo nuova teoria, ma standardizza il metodo:

1. Capitolo 12 - protocollo scientifico OCT;
2. Capitolo 13 - benchmark e replicabilità;
3. Capitolo 14 - governance epistemica e quality gates.

In sintesi: i capitoli 4-7 hanno esteso il linguaggio; i capitoli 12-14 ne definiranno la pratica scientifica condivisibile.

---

## Riferimenti

Riferimenti di framework interno:

1. Ghioni, F. (2026). `TE_CORE_v5.1.md`.
2. Ghioni, F. (2026). `Ordinative_Set_Theory_OST_A_Concise_Guide_For_AI_v2_1.md`.
3. `OCT_FOUNDATIONAL_BOOK_CHAPTER_06_v1_0.md`.
4. `OCT_FOUNDATIONAL_BOOK_CHAPTER_08_v1_0.md`.
5. `OCT_FOUNDATIONAL_BOOK_CHAPTER_11_v1_0.md`.

Riferimenti primari:

1. Mac Lane, S. (1998). *Categories for the Working Mathematician*.
2. Riehl, E. (2016). *Category Theory in Context*.
3. Spivak, D. (2014). *Category Theory for the Sciences*.
4. Borceux, F. (1994). *Handbook of Categorical Algebra*.
