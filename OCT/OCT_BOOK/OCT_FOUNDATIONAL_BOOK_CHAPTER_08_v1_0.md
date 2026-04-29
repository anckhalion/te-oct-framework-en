# Capitolo 8 - Invarianti ordinativi e spazio di validità (`Coh`, `Phi`, `Delta`)

Metadati:
- Versione: v1.0
- Data: 2026-04-21
- Stato: draft completo
- Autore: Fabio Ghioni
- Allineato a: TE_CORE v5.1 / OST v2.1 / baseline OCT v1.0 candidate
- Target parole capitolo: 3.000

---

## 1. Problema

Con i Capitoli 1-3 abbiamo costruito il nucleo ontologico e assiomatico di OCT. Abbiamo stabilito che:

1. la validità sintattica classica è necessaria ma non sufficiente;
2. l’unità primaria operativa è la singolarità contestualizzata in `Omega`;
3. l’ammissibilità ordinativa richiede gate su coerenza, emergenza e non-degenerazione.

Manca però ancora un passaggio decisivo per rendere OCT una teoria scientificamente utilizzabile su larga scala: definire uno **spazio di validità** comune, in cui i risultati possano essere confrontati, auditati e falsificati in modo uniforme.

Senza questo spazio, il linguaggio `Coh_Omega`, `Phi_Omega`, `Delta_Omega` rischia di restare una notazione locale non interoperabile tra capitoli, domini e gruppi di ricerca. Con questo spazio, invece, gli enunciati diventano traducibili in condizioni verificabili.

Il problema del capitolo può essere formulato così:

**come definire invarianti ordinativi minimi che mantengano la generalità del quadro teorico e, allo stesso tempo, consentano decisioni operative robuste su ammissibilità, sterilità e degenerazione?**

La difficoltà è doppia:

1. se gli invarianti sono troppo deboli, non discriminano stati strutturalmente diversi;
2. se sono troppo rigidi, trasformano OCT in uno schema dominio-specifico e perdono trasferibilità.

Per questo il capitolo propone un impianto a due strati:

1. uno spazio di validità minimale, comune a tutti i domini;
2. invarianti ordinativi contestuali, espliciti ma parametrici.

### 1.1 Perché servono invarianti e non solo metriche

Una metrica fornisce un valore. Un invariante fornisce una regola di persistenza sotto trasformazioni ammesse. In OCT non basta misurare: bisogna sapere quali proprietà devono restare stabili affinché una composizione resti scientificamente accettabile.

In termini pratici:

1. `Coh` da sola non distingue automaticamente stabilità utile da stabilità sterile;
2. `Phi` da sola non distingue automaticamente emergenza robusta da picco transitorio;
3. `Delta` da sola non distingue automaticamente rumore locale da degenerazione strutturale.

Gli invarianti servono proprio a integrare queste misure in un criterio unico di giudizio.

### 1.2 Posizionamento rispetto al programma teorematico

Questo capitolo non chiude ancora i teoremi fondativi globali (Capitolo 9), ma prepara la loro base. In particolare:

1. definisce le coordinate minime del dominio di validità;
2. fissa condizioni necessarie per ammissibilità ordinativa;
3. introduce margini decisionali utili per prove, controesempi e benchmark.

In questo senso, il Capitolo 8 è il ponte tra l’assiomatica (Capitolo 3) e la teorematica completa (Capitoli 9-10) con critica dei limiti (Capitolo 11).

---

## 2. Tesi del capitolo

La tesi del capitolo è articolata in otto enunciati.

1. Esiste uno spazio di validità ordinativo minimale `V_Omega` coordinato da `Coh`, `Phi`, `Delta`.
2. Lo spazio di validità può essere partizionato in regioni operative con semantica scientifica esplicita.
3. L’ammissibilità ordinativa minima richiede congiuntamente soglia di coerenza e non-sterilità emergente.
4. La degenerazione ordinativa è un regime classificabile e non un semplice errore numerico.
5. Gli invarianti ordinativi devono essere definiti come proprietà di persistenza, non come valori puntuali.
6. Le decisioni robuste richiedono margini di sicurezza e gestione dell’incertezza.
7. Nessuna singola metrica scalare può sostituire integralmente la triade (`Coh`, `Phi`, `Delta`) senza perdita informativa critica.
8. Il quadro proposto è sufficiente per sostenere il ciclo di prove/controesempi dei capitoli successivi.

---

## 3. Definizioni canoniche

### Definizione 8.1 (Stato di validità ordinativo)

Dato un diagramma o processo `D` in contesto `Omega`, definiamo lo stato di validità:

`V_Omega(D) := <Coh_Omega(D), Phi_Omega(D), Delta_Omega(D)>`

con:

`Delta_Omega(D) = 1 - Coh_Omega(D)`.

### Definizione 8.2 (Normalizzazione emergenziale)

Per comparare domini eterogenei introduciamo una normalizzazione contestuale:

`PhiHat_Omega(D) in [0,1]`

ottenuta tramite regola dichiarata ex ante (es. min-max robusto, quantile clipping, trasformazione logaritmica normalizzata).

Commento operativo:
- la scelta della normalizzazione è dominio-dipendente;
- deve essere esplicitata nel protocollo (O7).

### Definizione 8.3 (Spazio di validità minimale)

Lo spazio minimale è:

`S_Omega := [0,1] x [0,1]`

con coordinate `(Coh_Omega, PhiHat_Omega)`, mentre `Delta_Omega` resta variabile derivata.

Interpretazione:

1. asse `x`: tenuta coerentiva;
2. asse `y`: potenza emergenziale normalizzata.

### Definizione 8.4 (Regione di ammissibilità minima)

Fissata soglia `tau in (0,1]`, definiamo:

`R_A(Omega,tau) := {D | Coh_Omega(D) >= tau and PhiHat_Omega(D) > 0}`.

Questa è la regione OCT-minima di realtà compositiva.

### Definizione 8.5 (Regione di sterilità)

`R_S(Omega,tau) := {D | Coh_Omega(D) >= tau and PhiHat_Omega(D) = 0}`.

Interpretazione:
- struttura stabile ma emergenzialmente piatta;
- utile come controesempio di sufficienza della sola coerenza.

### Definizione 8.6 (Regione di degenerazione)

`R_D(Omega,tau) := {D | Coh_Omega(D) < tau}`.

Interpretazione:
- perdita di coerenza sotto soglia;
- può coesistere con valori `Phi` non nulli ma non affidabili come validità robusta.

### Definizione 8.7 (Margine di validità)

Definiamo il margine:

`m_Omega(D) := Coh_Omega(D) - tau`.

Se `m_Omega(D) > 0`, la distanza dal bordo di degenerazione è positiva.

### Definizione 8.8 (Invariante di persistenza ordinativa)

Sia `Gamma = {D_t}` una traiettoria in intervallo `I`. Una proprietà `I_k` è invariante ordinativa su `Gamma` se:

1. è verificata in `t0`;
2. resta verificata per ogni `t in I` sotto perturbazioni ammesse.

In forma sintetica:

`Inv_k(Gamma,Omega) := forall t in I, P_k(D_t,Omega)`.

### Definizione 8.9 (Vicinato contestuale ammissibile)

`N_epsilon(Omega)` è la famiglia di contesti perturbati compatibili con le ipotesi sperimentali.

Serve per valutare robustezza locale:

`Rob_Omega(D) := forall omega' in N_epsilon(Omega), D in R_A(omega',tau')`.

### Definizione 8.10 (Indice composito ausiliario)

Per scopi diagnostici (non sostitutivi), si può introdurre:

`Q_Omega(D) := alpha*Coh_Omega(D) + beta*PhiHat_Omega(D) - gamma*Delta_Omega(D)`

con `alpha,beta,gamma >= 0`.

Nota:
- `Q` è strumento ausiliario per ranking;
- non sostituisce la decisione logica basata sulle regioni.

### Definizione 8.11 (Istanziazione costruttiva minima su benchmark fisico)

Per evitare che la triade resti puramente lessicale, definiamo una istanziazione minima calcolabile sul benchmark fisico standing-wave.

Indicatori grezzi normalizzati in `[0,1]`:
1. `g_geom`: deviazione geometrica media rispetto alla configurazione di riferimento;
2. `p_phase`: persistenza della controfase osservata;
3. `n_global`: globalita del pattern nodale.

Mappatura operativa proposta:

`Coh_Omega(D) := 1 - g_geom(D)`

`PhiHat_Omega(D) := clip( w_p * p_phase(D) + w_n * n_global(D), 0, 1 )`

con pesi `w_p,w_n >= 0` e `w_p + w_n = 1`.

`Delta_Omega(D) := 1 - Coh_Omega(D)`

Note:
1. questa istanziazione e dominio-specifica e non pretende universalita;
2. il valore scientifico sta nella tracciabilita completa del mapping;
3. ogni benchmark successivo deve dichiarare un mapping analogo.

### Definizione 8.12 (Regola anti-circolarita operativa)

In OCT, un operatore e considerato "operativo" in un dominio solo se esiste:
1. definizione semantica;
2. mapping costruttivo da variabili osservabili;
3. procedura di calcolo replicabile;
4. soglia decisionale preregistrata.

Senza questi quattro elementi, lo stato corretto del claim resta `in_review` o `revise`.

---

## 4. Sviluppo formale

### 4.1 Geometria operativa dello spazio `S_Omega`

Lo spazio `S_Omega` consente una lettura geometrica semplice ma potente.

1. bordo verticale `Coh=tau`: frontiera di degenerazione;
2. bordo orizzontale `PhiHat=0`: frontiera di sterilità;
3. quadrante superiore destro oltre `tau`: area ordinativamente ammissibile.

Questa geometria evita ambiguità ricorrenti nella pratica:

1. alta coerenza non implica automaticamente emergenza;
2. emergenza apparente non compensa coerenza sotto soglia;
3. la valutazione richiede congiunzione logica, non media intuitiva.

### 4.2 Partizione minima e semantica scientifica

La partizione `R_A`, `R_S`, `R_D` introduce tre semantiche:

1. **Ammissibile (`R_A`)**: candidata a sviluppo teorico e applicativo;
2. **Sterile (`R_S`)**: candidata a controesempio o riprogettazione;
3. **Degenerativa (`R_D`)**: candidata a esclusione o revisione strutturale.

Questa partizione è già sufficiente per un primo ciclo di audit.

### 4.3 Invarianti ordinativi proposti (I1-I5)

Definiamo cinque invarianti minimi.

1. **I1 - Invariante di soglia coerentiva**  
   Se `D` è ammesso, allora `Coh>=tau` resta vero lungo traiettoria valida.

2. **I2 - Invariante di non-sterilità**  
   Se `D` è ammesso, allora `PhiHat>0` non collassa a zero in regime operativo ordinario.

3. **I3 - Invariante di margine**  
   Il margine `m_Omega(D)` non deve oscillare sotto zero oltre frequenza tollerata dichiarata.

4. **I4 - Invariante di robustezza locale**  
   L’appartenenza a `R_A` resta stabile su `N_epsilon(Omega)` entro bande dichiarate.

5. **I5 - Invariante di tracciabilità**  
   Ogni transizione di regione deve essere registrabile con log causale e metadati.

I1-I5 non sono ridondanti:

1. I1-I2 governano il gate logico;
2. I3-I4 governano la stabilità dinamica;
3. I5 governa la validità epistemica e auditabile.

### 4.4 Regola di ammissibilità forte

Oltre alla regola minima, introduciamo una variante forte:

`AdmStrong_Omega(D) := (D in R_A) and (m_Omega(D) >= eta) and Rob_Omega(D)`

con `eta>0` margine di sicurezza dominio-specifico.

Interpretazione:

1. non basta stare “appena” sopra soglia;
2. serve distanza dal bordo e tenuta sotto perturbazione.

Questa regola è cruciale per ridurre falsi positivi in sistemi rumorosi.

### 4.5 Dinamica delle traiettorie ordinative

Per sequenze temporali `D_t` distinguiamo tre profili tipici:

1. **Traiettoria stabile**: resta in `R_A` con margine positivo;
2. **Traiettoria fragile**: alterna `R_A` e bordo di soglia;
3. **Traiettoria collassante**: attraversa verso `R_D` in modo persistente.

L’analisi traiettoriale evita errori da fotografia istantanea:

1. uno stato puntuale ammissibile può essere transitorio;
2. una breve escursione non implica necessariamente collasso strutturale.

### 4.6 Gestione dell’incertezza

In pratica, `Coh` e `Phi` non sono valori perfetti. Introduciamo stime intervallari:

1. `Coh in [Coh^- , Coh^+]`;
2. `PhiHat in [Phi^- , Phi^+]`.

Criterio conservativo minimo:

`D` è ammesso solo se `Coh^- >= tau` e `Phi^- > 0`.

Questa scelta privilegia robustezza su ottimismo, coerentemente con l’uso scientifico.

### 4.7 Perché la triade non è comprimibile in un unico scalare

È naturale cercare un solo punteggio `Q`. Tuttavia, la compressione completa produce perdita informativa in almeno due casi:

1. due stati con uguale `Q` ma uno sterile e uno non sterile;
2. due stati con uguale `Q` ma uno vicino al bordo degenerativo e l’altro robusto.

Quindi:

1. `Q` può ordinare;
2. solo la triade con regioni logiche può decidere in modo affidabile.

### 4.8 Matrice decisionale A/B/C/D

Introduciamo una matrice operativa standard:

1. **A**: `Syn=vero`, `Coh>=tau`, `Phi>0`;
2. **B**: `Syn=vero`, `Coh>=tau`, `Phi=0`;
3. **C**: `Syn=vero`, `Coh<tau`;
4. **D**: `Syn=falso`.

Uso:

1. stato A -> pipeline principale;
2. stati B-C -> analisi controesempi/riprogettazione;
3. stato D -> errore formale preliminare.

### 4.9 Relazione con gli assiomi O1-O7

Lo spazio di validità è pienamente coerente con il kernel assiomatico:

1. O1 corrisponde al filtro tra D e A/B/C;
2. O2 corrisponde alla frontiera `Coh>=tau`;
3. O3 corrisponde alla frontiera `Phi>0`;
4. O4 richiede verifica di regione sulla composta;
5. O5 usa persistenza locale dell’identità nel dominio A;
6. O6 è catturato da `Rob_Omega`;
7. O7 è implementato da I5 e dalla matrice tracciabile.

Questa corrispondenza rende il passaggio da teoria ad applicazione lineare e verificabile.

### 4.10 Esempio astratto di separazione

Consideriamo tre trasformazioni sintatticamente valide:

1. `h1`: `Coh=0.83`, `PhiHat=0.41`, `tau=0.70` -> regione A;
2. `h2`: `Coh=0.86`, `PhiHat=0.00`, `tau=0.70` -> regione B;
3. `h3`: `Coh=0.62`, `PhiHat=0.37`, `tau=0.70` -> regione C.

Osservazione:

1. `h2` e `h3` falliscono per motivi diversi;
2. la distinzione è indispensabile perché guida interventi differenti:
   - B: problema di funzione emergente;
   - C: problema di coerenza strutturale.

### 4.10-bis Esempio numerico completo (dal dato grezzo alla decisione)

Fissiamo:
1. `tau = 0.70`;
2. pesi `w_p = 0.6`, `w_n = 0.4`.

Tre istanze osservate:

1. `u1`: `g_geom=0.12`, `p_phase=0.84`, `n_global=0.78`;
2. `u2`: `g_geom=0.10`, `p_phase=0.02`, `n_global=0.03`;
3. `u3`: `g_geom=0.42`, `p_phase=0.66`, `n_global=0.59`.

Calcolo:

1. `u1`
   - `Coh = 1 - 0.12 = 0.88`
   - `PhiHat = 0.6*0.84 + 0.4*0.78 = 0.816`
   - `Delta = 0.12`
   - Regione: `A` (`Coh>=tau` e `PhiHat>0`)

2. `u2`
   - `Coh = 1 - 0.10 = 0.90`
   - `PhiHat = 0.6*0.02 + 0.4*0.03 = 0.024`
   - `Delta = 0.10`
   - Regione: `A` minima ma con emergenza quasi nulla
   - Policy forte: caso da `rework` se si impone soglia emergenziale addizionale `PhiHat>=0.05`

3. `u3`
   - `Coh = 1 - 0.42 = 0.58`
   - `PhiHat = 0.6*0.66 + 0.4*0.59 = 0.632`
   - `Delta = 0.42`
   - Regione: `C` (`Coh<tau`)

Risultato metodologico:
1. la pipeline distingue in modo non ambiguo coerenza bassa da emergenza bassa;
2. la policy forte (`AdmStrong`) evita falsi positivi su casi quasi sterili;
3. l'intero processo e replicabile da un team esterno usando gli stessi indicatori.

### 4.11 Condizione di trasferibilità tra contesti

Per evitare frammentazione, introduciamo un criterio di trasporto:

una classificazione è trasferibile da `Omega_1` a `Omega_2` se:

1. mapping delle variabili rilevanti è esplicito;
2. normalizzazione di `Phi` è dichiarata in entrambi i contesti;
3. le regioni A/B/C/D restano consistenti entro tolleranze definite.

Questo criterio non impone universalità assoluta, ma rende comparabili risultati tra domini.

---

## 5. Proposizioni e teoremi locali

### Proposizione 8.1 (Partizione minima dello spazio di validità)

Enunciato:
Per ogni `D` sintatticamente valido, lo stato appartiene esattamente a una tra `R_A`, `R_S`, `R_D`.

Intuizione:
Le condizioni su `Coh` e `Phi` definiscono insiemi disgiunti e coprenti nel dominio sintatticamente valido.

Stato: `validated`.

### Proposizione 8.2 (Necessità della doppia condizione)

Enunciato:
La sola condizione `Coh>=tau` non è sufficiente per ammissibilità ordinativa.

Intuizione:
Gli elementi di `R_S` mostrano controesempi espliciti: coerenza alta, emergenza nulla.

Stato: `validated`.

### Teorema 8.3 (Criterio minimo di ammissibilità)

Ipotesi:
1. `Syn(D)=vero`;
2. `Coh_Omega(D)>=tau`;
3. `PhiHat_Omega(D)>0`.

Tesi:
`D in R_A(Omega,tau)`.

Proof sketch:
La tesi segue direttamente dalla definizione di `R_A` come congiunzione delle tre condizioni.

Conseguenze:
fornisce un test decisionale minimo, ripetibile e dominio-agnostico.

Stato: `validated`.

### Teorema 8.4 (Stabilità robusta con margine positivo)

Ipotesi:
1. `D in R_A`;
2. `m_Omega(D)>=eta>0`;
3. le perturbazioni in `N_epsilon(Omega)` alterano `Coh` al massimo di `eps_c<eta` e non annullano `Phi`.

Tesi:
`D` resta in `R_A` nel vicinato perturbato.

Proof sketch:
1. da `m>=eta` e `eps_c<eta`, segue `Coh` ancora sopra soglia;
2. da non-annullamento di `Phi`, resta `Phi>0`;
3. quindi la classificazione resta invariata.

Conseguenze:
fornisce la base formale per `AdmStrong_Omega`.

Stato: `in_proof` (dipende da specifica completa dei modelli di perturbazione).

### Proposizione 8.5 (Non comprimibilità decisionale della triade)

Enunciato:
Non esiste in generale un singolo scalare `Q` che preservi tutte le decisioni logiche A/B/C/D senza perdita.

Intuizione:
Esistono stati con stesso `Q` e diversa appartenenza regionale.

Stato: `revise` (chiusura completa nel Capitolo 9).

---

## 6. Implicazioni operative

### 6.1 Per il programma teorematico (Capitoli 9-10)

Il capitolo fornisce la grammatica necessaria per enunciare e testare i teoremi F01-F10 e D01-D05:

1. dominio di definizione comune;
2. condizioni di ammissibilità esplicite;
3. margini e robustezza formalizzati.

### 6.2 Per la progettazione dei benchmark

Ogni benchmark OCT dovrebbe includere almeno:

1. stima di `Coh`, `Phi`, `Delta`;
2. classificazione A/B/C/D per ogni istanza;
3. analisi di sensibilità sulle soglie;
4. tracciamento delle transizioni di regione nel tempo.

Senza questi blocchi, il benchmark misura prestazione locale ma non validità ordinativa.

### 6.3 Per audit trail e governance

L’uso operativo di I5 implica:

1. log della soglia usata;
2. versione della normalizzazione `Phi`;
3. motivazione delle variazioni contestuali;
4. storico delle decisioni di ammissione/rigetto.

Questo rende i risultati verificabili anche da team indipendenti.

### 6.4 Per sistemi AI ordinativi

In pipeline agentiche, la triade consente:

1. filtro pre-decisione (evitare output strutturalmente degenerativi);
2. monitoraggio online di drift verso regioni B o C;
3. trigger automatici di revisione quando il margine `m` scende sotto allerta.

### 6.5 Per comunicazione scientifica pubblicabile

La chiarezza di `S_Omega`, regioni e invarianti riduce l’ambiguità interpretativa nei review process:

1. ciò che è dimostrato;
2. ciò che è solo plausibile;
3. ciò che è falsificabile con protocollo esplicito.

### 6.6 Per interoperabilità tra repository e release

Poiché il progetto è distribuito su più canali (manoscritto, repository tecnici, dataset), questo capitolo suggerisce una regola pratica: ogni release dovrebbe includere una tabella sintetica con `tau`, normalizzazione `Phi`, percentuale di casi A/B/C/D e policy di incertezza usata.  
Questa tabella rende comparabili versioni successive, evita regressioni silenziose e consente a revisori esterni di verificare se il miglioramento dichiarato è strutturale o solo parametrico.

---

## 7. Limiti e non-claim

Limiti espliciti:

1. il capitolo non fornisce una metrica universale unica per `Phi`;
2. non dimostra ancora la forma più generale degli invarianti su categorie avanzate;
3. non chiude la prova completa di non comprimibilità per tutti i possibili `Q`;
4. la robustezza dipende dalla qualità del modello perturbativo in `N_epsilon(Omega)`;
5. l’uso delle soglie resta sensibile alla qualità del protocollo empirico.
6. l'istanziazione costruttiva mostrata e esemplificativa e non sostituisce una calibrazione laboratorio-specifica.

Failure mode riconosciuti:

1. normalizzazione `Phi` mal definita -> falsi passaggi in A;
2. soglia `tau` troppo bassa -> ammissione di casi borderline instabili;
3. soglia `tau` troppo alta -> rigetto eccessivo di casi funzionali;
4. stime troppo rumorose -> oscillazione artificiale tra regioni;
5. audit incompleto -> impossibilità di replicare classificazioni.

Box C - Non-claim

Questo capitolo non implica:
1. che `Coh`, `Phi`, `Delta` siano già misure definitive in ogni dominio;
2. che l’appartenenza a regione A garantisca automaticamente successo applicativo;
3. che la parte empirica dei benchmark sia sostituibile da sola formalizzazione.

---

## 8. Claim Ledger (S0-S3)

| ID | Claim | Tipo | Evidenza | Stato |
|---|---|---|---|---|
| C8.1 | Esiste uno spazio minimo di validità ordinativa `S_Omega` coordinato da `Coh` e `PhiHat` con `Delta` derivata | formale | S2 | in_review |
| C8.2 | La partizione A/B/C permette una semantica decisionale non ambigua su ammissibilità, sterilità, degenerazione | formale-operativo | S1 | validated |
| C8.3 | La sola coerenza non è sufficiente per validità ordinativa | formale | S1 | validated |
| C8.4 | Il margine `m_Omega` è necessario per decisioni robuste vicino alla soglia | metodologico | S1 | in_review |
| C8.5 | `AdmStrong_Omega` riduce falsi positivi in contesti rumorosi rispetto al solo gate minimo | metodologico | S2 | revise |
| C8.6 | La triade (`Coh`,`Phi`,`Delta`) non è pienamente comprimibile in un singolo scalare senza perdita decisionale | metateorico | S2 | in_proof |
| C8.7 | La gestione conservativa dell’incertezza migliora l’affidabilità delle classificazioni | metodologico | S1 | validated |
| C8.8 | Gli invarianti I1-I5 costituiscono un nucleo sufficiente per avviare il programma teorematico F01-F10 | programmatico | S2 | in_review |
| C8.9 | Una istanziazione costruttiva benchmark-specifica della triade e possibile con pipeline trasparente e replicabile | metodologico | S1 | candidate |
| C8.10 | La policy forte con soglia emergenziale addizionale riduce falsi positivi vicino alla sterilita pratica | metodologico | S2 | in_review |

---

## 9. Bridge al Capitolo 9

Con questo capitolo abbiamo definito:

1. coordinate minime dello spazio di validità;
2. regioni logiche A/B/C;
3. invarianti I1-I5;
4. criteri di robustezza e margine.

Il Capitolo 9 userà questa base per formalizzare i teoremi fondativi F01-F10, con:

1. enunciati in forma tipizzata;
2. proof sketch coerenti con O1-O7 e con lo spazio `S_Omega`;
3. conseguenze teoriche e operative con classificazione `S0-S3`.

In sintesi: il Capitolo 8 costruisce il “piano cartesiano” di OCT; il Capitolo 9 ne dimostra le leggi strutturali.

---

## Riferimenti

Riferimenti di framework interno:

1. Ghioni, F. (2026). `TE_CORE_v5.1.md`.
2. Ghioni, F. (2026). `Ordinative_Set_Theory_OST_A_Concise_Guide_For_AI_v2_1.md`.
3. `OCT_THEOREM_PROGRAM_v0_1.md`.
4. `OCT_TYPED_FORMAL_SPEC_v0_1.md`.
5. `OCT_CLASSICAL_TO_ORDINATIVE_MAP_v0_1.md`.

Riferimenti primari:

1. Mac Lane, S. (1998). *Categories for the Working Mathematician*.
2. Riehl, E. (2016). *Category Theory in Context*.
3. Spivak, D. (2014). *Category Theory for the Sciences*.
4. Shannon, C. E. (1948). *A Mathematical Theory of Communication* (per il quadro metodologico su informazione e misura).
