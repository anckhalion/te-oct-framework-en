# OCT Scientific Style Template v1.0

Template uniforme per la stesura del testo fondativo OCT.
Uso: obbligatorio per tutti i capitoli del libro.

---

## 1. Metadati di capitolo (header standard)

```text
Titolo capitolo:
Versione:
Data:
Stato: draft | in_review | candidate | frozen
Autore:
Allineato a: TE_CORE v5.1 / OST v2.1 / OCT baseline
```

---

## 2. Struttura fissa del capitolo

Ogni capitolo deve seguire questo ordine:

1. **Problema**
2. **Tesi del capitolo**
3. **Definizioni canoniche**
4. **Sviluppo formale**
5. **Proposizioni/teoremi locali**
6. **Implicazioni operative**
7. **Limiti e non-claim**
8. **Claim Ledger (`S0-S3`)**
9. **Bridge al capitolo successivo**

---

## 3. Registro linguistico (uniforme)

Stile richiesto:
- assertivo ma non enfatico;
- lessico tecnico coerente;
- frasi brevi e disambiguate;
- evitare linguaggio promozionale.
- ortografia italiana completa in UTF-8 (accenti obbligatori: `è`, `à`, `ì`, `ò`, `ù` quando dovuti).

Regole:
1. usare "proponiamo", "definiamo", "mostriamo", "limitiamo";
2. evitare "proviamo definitivamente" salvo prova completa;
3. separare sempre fatti, inferenze, ipotesi;
4. ogni claim deve essere tracciabile.

---

## 4. Notazione canonica

Notazione minima obbligatoria:

- `Omega`: contesto osservativo;
- `Coh_Omega(D)`: coerenza del diagramma `D` in `Omega`;
- `Phi_Omega(D)`: funzione emergente in `Omega`;
- `Delta_Omega(D) = 1 - Coh_Omega(D)`;
- `tau`: soglia minima di coerenza;
- `D` OCT-reale iff `Coh_Omega(D) >= tau` e `Phi_Omega(D) != 0`.

Regole:
1. non introdurre varianti simboliche senza dizionario locale;
2. dichiarare dominio/codominio di ogni funzione;
3. tipizzare sempre i nuovi operatori.

---

## 5. Template per definizioni, proposizioni e teoremi

Definizione:

```text
Definizione X (Nome).
Enunciato formale.
Commento operativo (2-4 righe).
```

Proposizione:

```text
Proposizione X (Nome).
Enunciato.
Intuizione.
```

Teorema:

```text
Teorema X (Nome).
Ipotesi:
Tesi:
Proof sketch:
Conseguenze:
Stato: in_proof | revise | validated
```

---

## 6. Politica evidenza (Claim Ledger)

Schema obbligatorio a fine capitolo:

| ID | Claim | Tipo | Evidenza | Stato |
|---|---|---|---|---|
| Cx.y | ... | formale/empirico/interpretativo | S0/S1/S2/S3 | validated/revise/reject |

Definizione sintetica:
- `S0`: dato verificato esterno/replicato;
- `S1`: inferenza forte triangolabile;
- `S2`: inferenza teorica plausibile ma non chiusa;
- `S3`: ipotesi di lavoro.

---

## 7. Citazioni e riferimenti

Regole:
1. citare sempre fonte primaria quando disponibile (paper, docs ufficiali, dataset DOI);
2. riportare DOI/URL persistente dove possibile;
3. separare "Riferimenti primari" e "Riferimenti di framework interno";
4. evitare riferimenti non verificabili per claim `S0/S1`.

Formato bibliografico:
- autore, anno, titolo, venue/editore, DOI/URL.

---

## 8. Sezione limiti (obbligatoria)

Checklist minima:
1. cosa il capitolo non dimostra;
2. ipotesi non testate;
3. dipendenze da lavori futuri;
4. possibili failure mode.

Regola:
- una teoria presentata senza limiti espliciti e editorialmente incompleta.

---

## 9. Box standard riusabili

Box A - Distinzione classico/OCT:

```text
Classico: [definizione]
Limite classico: [limite]
OCT: [estensione]
```

Box B - Validazione:

```text
Protocollo:
Metrica:
Criterio di accettazione:
Esito atteso:
```

Box C - Non-claim:

```text
Questo capitolo non implica:
1.
2.
3.
```

---

## 10. Template minimo di capitolo (copia/incolla)

```text
# Capitolo X - [Titolo]

## 1. Problema

## 2. Tesi del capitolo

## 3. Definizioni canoniche

## 4. Sviluppo formale

## 5. Proposizioni e teoremi locali

## 6. Implicazioni operative

## 7. Limiti e non-claim

## 8. Claim Ledger (S0-S3)

## 9. Bridge al Capitolo X+1

## Riferimenti
```

---

## 11. Quality Gate prima del freeze

Un capitolo può passare a `candidate` solo se:
1. notazione coerente al 100% con schema canonico;
2. nessun claim senza etichetta evidenza;
3. almeno un controesempio o failure mode discusso;
4. bibliografia verificata;
5. lunghezza entro +/-10% del target parole assegnato.






