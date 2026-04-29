# Overleaf Setup

1. Upload this folder as a new Overleaf project.
2. Set compiler to XeLaTeX.
3. Main file: `main.tex`.
4. Re-run compile twice to resolve TOC references.

If source Markdown changes, regenerate LaTeX locally with:

```powershell
pwsh ./scripts/convert_markdown_to_latex.ps1
```
