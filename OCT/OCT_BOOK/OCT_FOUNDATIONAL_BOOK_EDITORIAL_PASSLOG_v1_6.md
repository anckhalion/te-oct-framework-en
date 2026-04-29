# OCT Foundational Book - Editorial Passlog v1.6

Metadati:
- Versione: v1.6
- Data: 2026-04-22
- Stato: completed
- Scope: line editing globale, coerenza linguistica e controllo struttura capitoli 1-17

---

## 1) Obiettivo del pass

Completare la milestone `v1.6` con:

1. armonizzazione linguistica italiana (accenti e forme lessicali ricorrenti);
2. verifica coerenza strutturale dei capitoli (sezioni 1..9 + Claim Ledger + Riferimenti);
3. preparazione freeze candidate del manoscritto completo.

## 2) Interventi eseguiti

### 2.1 Armonizzazione linguistica

Applicato pass automatico controllato su capitoli 1-17 per normalizzare forme italiane non accentate ricorrenti, tra cui:

- `perche -> perché`, `piu -> più`, `puo -> può`, `cio -> ciò`;
- serie terminologica in `-ità`: `qualità`, `validità`, `capacità`, `replicabilità`, `responsabilità`, `tracciabilità`, ecc.

Nota: l'intervento è stato limitato ai file capitolo/bibliografia del libro per evitare effetti collaterali su altri artifact del progetto.

### 2.2 Correzioni puntuali post-pass

- Correzione lessicale residua in Capitolo 13: `instabilità`.

### 2.3 Verifica struttura capitoli

Controllo automatico superato su tutti i capitoli `01..17`:

1. presenza sezione `## 1.`;
2. presenza sezione `## 8. Claim Ledger`;
3. presenza sezione `## 9.`;
4. presenza sezione `## Riferimenti`.

Esito: `PASS` su 17/17 capitoli.

## 3) Artefatti impattati

Capitoli aggiornati linguisticamente:

1. `OCT_FOUNDATIONAL_BOOK_CHAPTER_01_v1_0.md`
2. `OCT_FOUNDATIONAL_BOOK_CHAPTER_03_v1_0.md`
3. `OCT_FOUNDATIONAL_BOOK_CHAPTER_05_v1_0.md`
4. `OCT_FOUNDATIONAL_BOOK_CHAPTER_09_v1_0.md`
5. `OCT_FOUNDATIONAL_BOOK_CHAPTER_10_v1_0.md`
6. `OCT_FOUNDATIONAL_BOOK_CHAPTER_12_v1_0.md`
7. `OCT_FOUNDATIONAL_BOOK_CHAPTER_13_v1_0.md`
8. `OCT_FOUNDATIONAL_BOOK_CHAPTER_14_v1_0.md`
9. `OCT_FOUNDATIONAL_BOOK_CHAPTER_15_v1_0.md`
10. `OCT_FOUNDATIONAL_BOOK_CHAPTER_16_v1_0.md`
11. `OCT_FOUNDATIONAL_BOOK_CHAPTER_17_v1_0.md`

## 4) Esito milestone

Milestone `v1.6`: `completed`.

Condizioni soddisfatte:

1. line editing globale eseguito;
2. coerenza notazionale/strutturale verificata;
3. freeze candidate emesso (vedi file dedicato).

## 5) Residui aperti (post-v1.6)

1. rifinitura citazionale formale (DOI/issue/page style unificato) per release editoriale finale;
2. eventuale pass di micro-copyediting umano focalizzato su ritmo/stile in lettura continua;
3. impacchettamento pubblicazione (GitHub/Zenodo/OSF/HF) della release freeze.
