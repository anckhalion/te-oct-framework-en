# Capitolo 5 - Isomorfismi, equivalenze, limiti e colimiti con vincolo ordinativo

Metadati:
- Versione: v1.0
- Data: 2026-04-22
- Stato: draft completo
- Autore: Fabio Ghioni
- Allineato a: TE_CORE v5.1 / OST v2.1 / OCT baseline v1.0 candidate
- Target parole capitolo: 3.500

---

## 1. Problema

Il Capitolo 4 ha definito l’estensione ordinativa delle unità di base: oggetti, morfismi, composizione e identità. Questo è sufficiente per controllare la dinamica locale di una categoria ordinativa, ma non basta per affrontare i costrutti classici che, nella pratica matematica, determinano la potenza reale del formalismo:

1. isomorfismi;
2. equivalenze;
3. limiti;
4. colimiti.

Nel quadro classico questi costrutti sono centrali perché esprimono nozioni di “stessa struttura”, “stessa teoria fino a traduzione”, “migliore oggetto universale di compatibilità” e “migliore oggetto universale di aggregazione”. In OCT non vengono rimossi; vengono sottoposti a un vincolo aggiuntivo: validità ordinativa nel contesto `Omega`.

Il problema del capitolo è quindi:

**come preservare l’apparato universale classico senza trattare come equivalenti o universalmente validi costrutti che risultano sterili o degenerativi in termini ordinativi?**

La difficoltà non è banale:

1. se il filtro ordinativo è troppo rigido, può distruggere la trasferibilità dei risultati;
2. se è troppo permissivo, non evita gli errori che OCT vuole correggere.

Per questo il capitolo adotta una strategia di “selettività controllata”:

1. la struttura classica resta necessaria;
2. la validità ordinativa decide l’operatività reale del costrutto nel dominio osservato.

### 1.1 Nodo critico: “stesso” non significa sempre “equivalente operativamente”

Nel classico:

1. isomorfismo implica sostituibilità strutturale;
2. equivalenza categoriale implica stessa teoria “a meno di traduzione”.

In OCT:

1. queste nozioni restano valide sul piano sintattico;
2. non implicano automaticamente equivalenza ordinativa su funzione, persistenza e robustezza.

La differenza è la stessa già incontrata nei capitoli precedenti, ma qui viene formalizzata sui costrutti più forti del linguaggio categoriale.

### 1.2 Perché limiti e colimiti sono il test più severo

Limiti e colimiti sono il cuore della “universalità” in category theory. Se OCT non riesce a trattarli in modo coerente, l’estensione resta locale. Se li tratta in modo formalmente stabile, l’estensione diventa sistemica.

Questo capitolo lavora esattamente su quel confine:

1. mostra quando una costruzione universale classica resta universalmente valida in senso ordinativo;
2. mostra quando la costruzione resta formalmente lecita ma è ordinativamente vuota.

---

## 2. Tesi del capitolo

La tesi è articolata in nove enunciati.

1. L’isomorfismo classico resta invariato come nozione strutturale, ma non implica automaticamente isomorfismo ordinativo.
2. L’equivalenza classica di categorie non implica equivalenza ordinativa piena.
3. Limiti classici e limiti ordinativi coincidono solo sotto vincoli di coerenza ed emergenza.
4. Colimiti classici e colimiti ordinativi coincidono solo se l’aggregazione non annulla la funzione emergente.
5. È possibile definire nozioni di isomorfismo/equivalenza/limite/colimite ordinativi senza contraddire il quadro classico.
6. La non-ridondanza di OCT emerge in modo naturale proprio sui costrutti universali.
7. La selettività ordinativa è compatibile con il funtore di oblio verso la teoria classica.
8. La distinzione tra “universale formale” e “universale reale” è metodologicamente necessaria.
9. Questo capitolo prepara direttamente funtori, naturali e aggiunzioni del Capitolo 6.

---

## 3. Definizioni canoniche

### Definizione 5.1 (Isomorfismo ordinativo)

Siano `A_Omega`, `B_Omega` oggetti ordinativi. Un isomorfismo ordinativo è una coppia `f: A_Omega->B_Omega`, `g: B_Omega->A_Omega` tale che:

1. `g∘f = id_A` e `f∘g = id_B` in senso classico;
2. `Adm_Omega(f)`, `Adm_Omega(g)`;
3. le identità risultanti sono ordinativamente neutre.

### Definizione 5.2 (Equivalenza ordinativa di categorie)

Due categorie ordinative `C_Omega`, `D_Omega` sono ordinativamente equivalenti se esistono funtori `F`, `G` che realizzano equivalenza classica e preservano invarianti ordinativi dichiarati entro tolleranza.

### Definizione 5.3 (Limite ordinativo)

Dato un diagramma `D`, un limite ordinativo è un limite classico `Lim(D)` che soddisfa:

1. `Coh_Omega(Lim(D)) >= tau_lim`;
2. `Phi_Omega(Lim(D)) != 0`;
3. stabilità locale su vicinato contestuale dichiarato.

### Definizione 5.4 (Colimite ordinativo)

Dato `D`, un colimite ordinativo è un colimite classico `Colim(D)` che soddisfa:

1. `Coh_Omega(Colim(D)) >= tau_colim`;
2. `Phi_Omega(Colim(D)) != 0`;
3. assenza di perdita emergenziale critica in aggregazione.

### Definizione 5.5 (Universalità selettiva)

Una costruzione universale è selettivamente valida in OCT se:

1. è universale nel senso classico;
2. supera il gate ordinativo nel contesto osservativo.

### Definizione 5.6 (Falso universale ordinativo)

Costrutto formalmente universale ma ordinativamente invalido (sterile o degenerativo) nel dominio dichiarato.

### Definizione 5.7 (Scarto di equivalenza)

Scarto tra equivalenza classica e ordinativa:

`Gap_eq(Omega) := Eq_class - Eq_ord,Omega`

inteso come divergenza di classificazione su un insieme di test strutturali.

---

## 4. Sviluppo formale

### 4.1 Isomorfismo: conservazione e vincolo

La nozione classica di isomorfismo resta intatta:

1. esistenza di inversi;
2. composizione con identità.

In OCT aggiungiamo:

1. ammissibilità ordinativa dei morfismi coinvolti;
2. neutralità ordinativa delle identità risultanti.

Ne segue una distinzione netta:

1. isomorfismo classico puro;
2. isomorfismo classico + ordinativo.

Errore evitato:

1. inferire uguaglianza operativa totale da sola invertibilità strutturale.

### 4.2 Equivalenza di categorie: dove nasce lo scarto

Nel classico, equivalenza categoriale significa “stessa teoria fino a equivalenza”. In OCT questa affermazione resta vera sul piano strutturale, ma non è automaticamente vera sul piano ordinativo.

Perché può emergere scarto:

1. `F` e `G` possono preservare forme ma non robustezza contestuale;
2. la stessa struttura può produrre dinamiche emergenti diverse in contesti differenti;
3. alcune trasformazioni possono introdurre perdita ontologica (D03).

Quindi:

1. `C ≃ D` classico non implica `C ≃ord D`;
2. serve controllo invarianti ordinativi sulle immagini funtoriali rilevanti.

### 4.3 Limiti: universalità non basta

Nel classico, `Lim(D)` è definito dalla proprietà universale del cono terminale. In OCT questa proprietà resta necessaria ma non sufficiente.

Condizione aggiuntiva:

1. il limite deve essere ordinativamente non sterile e non degenerativo.

Caso tipico di falso universale:

1. il limite classico esiste;
2. struttura formalmente corretta;
3. emergenza funzionale nulla (`Phi=0`) o margine coerentivo insufficiente.

Conclusione:

1. limite classico non implica limite ordinativo reale.

### 4.4 Colimiti: aggregare non significa integrare

Il colimite classico privilegia la compatibilità di coconi e l’universalità di aggregazione. In OCT serve anche:

1. conservazione di coerenza oltre soglia;
2. funzione emergente non nulla dell’aggregato.

Differenza pratica:

1. un colimite può “unire” formalmente componenti senza produrre integrazione ordinativa;
2. l’aggregazione può perfino aumentare rumore o annullare funzione.

Questa è la ragione per cui parliamo di universalità selettiva:

1. non ogni “migliore aggregatore formale” è “migliore aggregatore reale”.

### 4.5 Relazione tra isomorfismi/equivalenze e limiti/colimiti

Le quattro nozioni sono spesso studiate separatamente, ma in OCT sono interdipendenti.

1. un forte `Gap_eq` influenza trasferibilità di limiti/colimiti tra categorie equivalenti classiche;
2. limiti/colimiti ordinativamente instabili possono produrre falsi segnali di equivalenza operativa;
3. isomorfismi locali non garantiscono universalità ordinativa globale.

Da qui segue un principio metodologico:

1. equivalenze e universalità devono essere valutate in coppia quando il dominio è dinamico o ad alta sensibilità relazionale.

### 4.6 Criterio di accettazione per costrutti universali

Per uso operativo, proponiamo una regola minima:

un limite/colimite può essere dichiarato ordinativamente valido solo se:

1. proprietà universale classica verificata;
2. gate `Coh/Phi` superato;
3. robustezza minima su perturbazioni dichiarate;
4. classificazione non ricade in sterilità.

Questa regola riduce sia overclaiming teorico sia regressioni applicative.

### 4.7 Stabilità di equivalenza sotto variazione contestuale

Per equivalenze classiche candidate a equivalenza ordinativa, va testata la stabilità su `N_epsilon(Omega)`.

Richiesta minima:

1. immagini funtoriali critiche non devono attraversare sistematicamente il confine A/B/C;
2. la divergenza residua deve restare entro banda dichiarata.

In assenza di questo controllo:

1. l’equivalenza ordinativa rischia di essere artefatto locale.

### 4.8 Matrice di fallimento specifica del capitolo

Tipi di fallimento frequenti:

1. **F-Iso1**: isomorfismo classico con perdita ordinativa su inverso;
2. **F-Eq1**: equivalenza classica con divergenza stabile di invarianti;
3. **F-Lim1**: limite classico sterile (`Phi=0`);
4. **F-Lim2**: limite classico fragile (`Coh` al bordo);
5. **F-Col1**: colimite aggregativo con perdita emergenziale;
6. **F-Col2**: colimite formalmente corretto ma non robusto su perturbazioni.

Questa matrice serve a collegare teoria e debugging nei capitoli successivi.

### 4.9 Compatibilità con il recupero classico

Il capitolo è coerente con F10:

1. disattivando il filtro ordinativo, si recuperano isomorfismi/equivalenze/limiti/colimiti classici;
2. attivando il filtro, si ottiene selettività senza contraddire la struttura classica.

Questo punto è essenziale per mantenere continuità didattica e matematica.

### 4.10 Implicazione strategica per il libro

La selettività introdotta qui modifica il modo di leggere l’intero corpus classico:

1. non basta chiedere “esiste?”;
2. bisogna chiedere “esiste ed è ordinativamente reale nel contesto dichiarato?”.

Questa doppia domanda diventa standard anche per il Capitolo 6 (funtori, naturali, aggiunzioni, monadi/comonadi).

### 4.11 Condizione di non-ridondanza del capitolo

Il capitolo è non ridondante se esiste almeno un caso per ciascuna coppia:

1. isomorfismo classico valido / isomorfismo ordinativo invalido;
2. equivalenza classica valida / equivalenza ordinativa invalida;
3. limite classico esistente / limite ordinativo non reale;
4. colimite classico esistente / colimite ordinativo non reale.

Questa condizione è soddisfatta dal programma teorematico F01, F05, F06, F07 già fissato nei capitoli precedenti.

### 4.12 Trasporto di equivalenza e perdita ordinativa

Quando una equivalenza classica `F: C->D` viene usata come trasporto di risultati, in OCT bisogna valutare il costo ordinativo del trasporto.

Definiamo una misura sintetica:

`Loss_tr_Omega(F) := w1*DeltaCoh + w2*DeltaPhi + w3*Instab`,

dove:

1. `DeltaCoh` misura la variazione media di coerenza su oggetti/morfismi test;
2. `DeltaPhi` misura variazione emergenziale;
3. `Instab` misura frequenza di attraversamenti A/B/C dopo trasporto.

Interpretazione:

1. `Loss_tr` basso: trasporto ordinativamente affidabile;
2. `Loss_tr` alto: equivalenza classica utile formalmente ma fragile operativamente.

Questo blocco non sostituisce la teoria dell’equivalenza, ma aiuta a decidere quando usare o meno un trasporto come argomento forte in un dominio applicativo.

### 4.13 Universalità sotto rumore strutturale

Un limite o colimite può essere accettabile in condizioni ideali ma non in condizioni realistiche. Per questo proponiamo una verifica di universalità sotto rumore controllato.

Schema:

1. calcolare il costrutto universale classico;
2. applicare perturbazioni compatibili con `N_epsilon(Omega)`;
3. verificare persistenza del gate ordinativo.

Criterio:

`UnivRob_Omega(U) = true` se per ogni perturbazione ammessa il costrutto resta nel dominio ordinativamente valido.

Conseguenze:

1. distingue universalità teorica da universalità robusta;
2. riduce rischio di sovrastima su casi “puliti” ma non replicabili.

### 4.14 Distinzione tra limite informativo e limite operativo

Nel trattamento di limiti e colimiti conviene separare:

1. **limite informativo**: minimizza ambiguità descrittiva nel diagramma;
2. **limite operativo**: massimizza tenuta ordinativa nelle condizioni d’uso.

In alcuni domini i due concetti coincidono, in altri divergono. La divergenza spiega perché un costrutto formalmente ottimale possa risultare pragmaticamente debole.

Questo punto è importante per evitare un errore frequente:

1. usare criteri informativi puri per giustificare decisioni operative ad alta criticità.

### 4.15 Pattern tipici di falsa equivalenza

Osserviamo quattro pattern ricorrenti.

1. **Pattern E1 - Equivalenza di forma, divergenza di traiettoria**  
   stesse relazioni iniziali, dinamiche emergenti divergenti.

2. **Pattern E2 - Equivalenza locale, collasso globale**  
   traduzioni corrette modulo per modulo, ma incompatibilità cumulativa.

3. **Pattern E3 - Universalità sterile**  
   soluzione universale formale senza funzione emergente apprezzabile.

4. **Pattern E4 - Aggregazione degenerativa**  
   colimite che unifica ma riduce capacità operativa del sistema aggregato.

Riconoscere questi pattern accelera sia proof design sia debugging sperimentale.

### 4.16 Protocollo minimo di verifica per limiti e colimiti

Per rendere replicabile la valutazione ordinativa proponiamo una pipeline minima in sei passi.

1. costruzione del costrutto classico (`Lim` o `Colim`) con prova formale standard;
2. specifica del contesto `Omega` e delle soglie `tau` pertinenti;
3. misura puntuale di `Coh_Omega` e `Phi_Omega`;
4. test su vicinato `N_epsilon(Omega)` con perturbazioni dichiarate;
5. classificazione finale (`accepted`, `revise`, `reject`);
6. registrazione nel claim ledger con evidenza `S0-S3`.

Questa pipeline crea continuità tra matematica e metodo:

1. la parte 1 garantisce rigore classico;
2. le parti 2-4 garantiscono rigore ordinativo;
3. le parti 5-6 garantiscono rigore epistemico.

In assenza di uno di questi passaggi, la decisione resta incompleta: o formalmente robusta ma operativamente cieca, o operativamente intuitiva ma teoricamente debole.

---

## 5. Proposizioni e teoremi locali

### Proposizione 5.1 (Necessità del vincolo ordinativo sugli isomorfismi)

Enunciato:
L’invertibilità classica non è condizione sufficiente per isomorfismo ordinativo.

Intuizione:
gli inversi possono essere tipologicamente corretti ma emergenzialmente sterili o non robusti.

Stato: `validated`.

### Proposizione 5.2 (Universalità selettiva dei limiti)

Enunciato:
Esistono limiti classici non accettabili come limiti ordinativi nel medesimo `Omega`.

Intuizione:
proprietà universale formale e validità ordinativa sono livelli distinti.

Stato: `in_proof`.

### Proposizione 5.3 (Universalità selettiva dei colimiti)

Enunciato:
Esistono colimiti classici con perdita emergenziale critica, quindi non ordinativamente validi.

Intuizione:
aggregazione strutturale non implica integrazione funzionale.

Stato: `in_proof`.

### Teorema 5.4 (Scarto di equivalenza non nullo in domini dinamici)

Ipotesi:
1. coppia di categorie classiche equivalenti;
2. mapping ordinativo su oggetti/morfismi critici;
3. divergenza stabile su almeno un invariante ordinativo.

Tesi:
`Gap_eq(Omega) > 0`.

Proof sketch:
1. l’equivalenza classica garantisce traduzione strutturale;
2. gli invarianti ordinativi rilevano differenze funzionali/robuste non assorbite dalla traduzione;
3. la divergenza stabile implica scarto positivo.

Conseguenze:
dimostra formalmente il valore aggiunto di OCT a livello categoriale globale.

Stato: `in_proof`.

### Teorema 5.5 (Criterio minimo per universalità ordinativa)

Ipotesi:
1. costrutto universale classico `U(D)` (limite o colimite);
2. gate ordinativo soddisfatto su `U(D)`;
3. robustezza locale su `N_epsilon(Omega)`.

Tesi:
`U(D)` è universalmente accettabile in senso ordinativo nel dominio dichiarato.

Proof sketch:
1. la proprietà universale classica stabilisce correttezza strutturale;
2. gate e robustezza stabiliscono realtà compositiva;
3. l’unione dei due livelli produce universalità ordinativa.

Conseguenze:
fornisce una regola unificata per trattare limiti e colimiti in OCT.

Stato: `in_proof`.

### Proposizione 5.6 (Non-invarianza automatica del trasporto funtoriale)

Enunciato:
Un funtore che realizza equivalenza classica non preserva automaticamente il livello di robustezza ordinativa.

Intuizione:
la preservazione strutturale non implica preservazione del margine `m_Omega`.

Stato: `in_review`.

### Teorema 5.7 (Vincolo di robustezza universale)

Ipotesi:
1. esistenza classica di `U(D)` (limite o colimite);
2. validità ordinativa puntuale di `U(D)` in `Omega`;
3. `UnivRob_Omega(U)=true`.

Tesi:
`U(D)` è universalmente utilizzabile in modo ordinativamente affidabile nel dominio dichiarato.

Proof sketch:
1. la validità puntuale garantisce ammissibilità iniziale;
2. la robustezza su vicinato evita falsi positivi da fitting locale;
3. quindi il costrutto è idoneo a uso operativo ripetibile.

Conseguenze:
fornisce criterio più forte del solo gate puntuale per capitoli applicativi futuri.

Stato: `in_proof`.

---

## 6. Implicazioni operative

### 6.1 Per progettazione matematica

Ogni volta che si usa “isomorfo”, “equivalente”, “limite”, “colimite” nel manoscritto OCT, è raccomandato specificare:

1. livello classico;
2. livello ordinativo;
3. eventuale gap tra i due livelli.

### 6.2 Per benchmarking

I benchmark dovrebbero includere set specifici:

1. casi con equivalenza classica ma divergenza ordinativa;
2. casi con universalità classica ma sterilità emergenziale;
3. casi robusti in cui classico e ordinativo coincidono.

Questo evita valutazioni sbilanciate su soli casi favorevoli.

### 6.3 Per interpretazione dei risultati

Quando un costrutto fallisce ordinativamente, non significa che la teoria classica sia “sbagliata”. Significa che, nel dominio osservato, il livello classico non basta per decisioni operative.

### 6.4 Per pipeline modulari

Nei sistemi composti da più moduli:

1. limiti e colimiti vanno valutati non solo per correttezza formale;
2. vanno valutati anche per effetti su coerenza globale e funzione emergente.

### 6.5 Per il Capitolo 6

Funtori e naturali del Capitolo 6 erediteranno direttamente questi vincoli:

1. preservazione classica;
2. preservazione ordinativa;
3. tracciamento esplicito degli scarti.

### 6.6 Per audit di equivalenze e universalità

Nelle revisioni tecniche è utile allegare una tabella per ogni costrutto candidato:

1. tipo (`iso`, `eq`, `lim`, `colim`);
2. validità classica (`si/no`);
3. validità ordinativa puntuale (`si/no`);
4. robustezza su `N_epsilon(Omega)` (`si/no`);
5. stato finale (`accepted`, `revise`, `reject`).

Questa tabella rende comparabili team diversi e riduce ambiguità nei passaggi tra release.

### 6.7 Per continuità editoriale del manoscritto

Nel testo finale dell’opera è consigliato mantenere per ciascun costrutto universale un box standard:

1. definizione classica sintetica;
2. estensione ordinativa;
3. controesempio tipico;
4. criterio di accettazione.

In questo modo il lettore non specialista mantiene orientamento, mentre il lettore tecnico trova rapidamente i punti di controllo formale.

### 6.8 Priorità operative per i prossimi capitoli

Per massimizzare continuità con il Capitolo 6 è utile fissare tre priorità immediate:

1. costruire esempi in cui un funtore preserva struttura ma non preserva classe A/B/C;
2. esplicitare almeno una aggiunzione classica che richiede vincolo ordinativo aggiuntivo;
3. preparare un caso monadico in cui la composizione iterata mostra differenza tra validità locale e validità globale.

Queste priorità evitano discontinuità tra capitoli e permettono di riusare direttamente la grammatica del Capitolo 5 nel trattamento di naturali, aggiunzioni e monadi/comonadi.

### 6.9 Regola pratica di comunicazione scientifica

Quando si presenta un risultato su limiti o colimiti in contesto OCT, è utile dichiarare sempre in apertura:

1. cosa è dimostrato in senso classico;
2. cosa è accettato in senso ordinativo;
3. quale parte resta in stato `in_proof` o `revise`.

Questa regola riduce incomprensioni tra lettori con background diversi e migliora la qualità delle revisioni tra pari, perché separa subito livello matematico, livello operativo e livello di evidenza disponibile.
Inoltre facilità la produzione di abstract tecnici sintetici coerenti con il claim ledger, utili per repository, preprint e comunicazioni istituzionali.

---

## 7. Limiti e non-claim

Limiti espliciti:

1. il capitolo non chiude tutte le prove complete di F05/F06/F07;
2. la robustezza di limiti/colimiti resta dipendente da modelli perturbativi dichiarati;
3. la misura di `Gap_eq` è presentata in forma concettuale minima, da raffinare.

Failure mode riconosciuti:

1. considerare `Gap_eq` nullo perché non misurato correttamente;
2. trattare casi sterilità come eccezioni trascurabili senza analisi;
3. usare solo esempi in cui classico e ordinativo coincidono;
4. applicare equivalenze categoriali senza verifica su invarianti ordinativi critici.

Box C - Non-claim

Questo capitolo non implica:
1. che i costrutti classici perdano validità matematica intrinseca;
2. che ogni limite o colimite classico sia ordinativamente invalido;
3. che OCT elimini il bisogno di dimostrazione classica dei costrutti universali.

---

## 8. Claim Ledger (S0-S3)

| ID | Claim | Tipo | Evidenza | Stato |
|---|---|---|---|---|
| C5.1 | Isomorfismo classico e isomorfismo ordinativo non coincidono in generale | formale | S2 | in_proof |
| C5.2 | Equivalenza classica non implica equivalenza ordinativa piena | formale | S2 | in_proof |
| C5.3 | Limiti classici richiedono filtro ordinativo per essere “reali” in `Omega` | formale | S2 | in_proof |
| C5.4 | Colimiti classici possono essere aggregativi ma non integrativi | formale-operativo | S2 | in_proof |
| C5.5 | La nozione di universalità selettiva è compatibile con il recupero classico | metateorico | S1 | validated |
| C5.6 | La matrice F-Iso/F-Eq/F-Lim/F-Col migliora la diagnosi operativa | metodologico | S1 | in_review |

---

## 9. Bridge al Capitolo 6

Il Capitolo 5 ha esteso in senso ordinativo i costrutti universali principali del quadro classico:

1. isomorfismi;
2. equivalenze;
3. limiti;
4. colimiti.

Il Capitolo 6 affronterà ora il livello trasformazionale superiore:

1. funtori e trasformazioni naturali;
2. aggiunzioni;
3. monadi e comonadi.

In particolare, il nodo centrale sarà capire quando una trasformazione tra categorie preserva non solo la forma, ma anche la validità ordinativa delle strutture trasportate.

---

## Riferimenti

Riferimenti di framework interno:

1. Ghioni, F. (2026). `TE_CORE_v5.1.md`.
2. Ghioni, F. (2026). `Ordinative_Set_Theory_OST_A_Concise_Guide_For_AI_v2_1.md`.
3. `OCT_FOUNDATIONAL_BOOK_CHAPTER_04_v1_0.md`.
4. `OCT_FOUNDATIONAL_BOOK_CHAPTER_08_v1_0.md`.
5. `OCT_FOUNDATIONAL_BOOK_CHAPTER_09_v1_0.md`.
6. `OCT_FOUNDATIONAL_BOOK_CHAPTER_10_v1_0.md`.

Riferimenti primari:

1. Mac Lane, S. (1998). *Categories for the Working Mathematician*.
2. Riehl, E. (2016). *Category Theory in Context*.
3. Spivak, D. (2014). *Category Theory for the Sciences*.

