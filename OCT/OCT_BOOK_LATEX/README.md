# OCT Book LaTeX (Overleaf-ready)

Questa cartella contiene la pipeline di conversione del manoscritto OCT da Markdown a LaTeX.

## Struttura

- `main.tex`: file principale del libro.
- `preamble.tex`: pacchetti e impostazioni tipografiche.
- `chapters/`: capitoli convertiti da Markdown.
- `backmatter/`: materiale di chiusura (bibliografia consolidata).
- `scripts/convert_markdown_to_latex.ps1`: conversione automatica con Pandoc.
- `scripts/build_pdf.ps1`: conversione + build XeLaTeX locale.

## Uso locale (Windows PowerShell)

```powershell
pwsh ./scripts/build_pdf.ps1
```

## Uso Overleaf

1. Esegui localmente `scripts/build_pdf.ps1` almeno una volta per generare `chapters/*.tex`.
2. Comprimi la cartella `OCT_BOOK_LATEX` in zip.
3. Importa lo zip in Overleaf.
4. Seleziona compilatore **XeLaTeX**.
5. File principale: `main.tex`.

## Note

- I capitoli vengono ripuliti dal blocco iniziale `Metadati:` durante la conversione.
- La bibliografia è mantenuta come capitolo consolidato in backmatter.
- Per la release finale stampa, aggiorna il colophon e i metadati editoriali (ISBN, copyright, anno).
