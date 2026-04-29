$ErrorActionPreference = 'Stop'

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = Resolve-Path (Join-Path $scriptDir '..')

Push-Location $projectRoot
try {
  $scratch = @('main.aux','main.out','main.toc','main.fls','main.fdb_latexmk','main.lof','main.lot')
  foreach($f in $scratch){
    if(Test-Path $f){ Remove-Item -Force $f }
  }

  Write-Host 'Step 1/2: Converting Markdown to LaTeX...'
  & (Join-Path $scriptDir 'convert_markdown_to_latex.ps1')

  Write-Host 'Step 2/2: Building PDF with XeLaTeX...'
  & xelatex -interaction=nonstopmode -halt-on-error main.tex | Out-Host
  if($LASTEXITCODE -ne 0){ throw 'XeLaTeX first pass failed.' }

  & xelatex -interaction=nonstopmode -halt-on-error main.tex | Out-Host
  if($LASTEXITCODE -ne 0){ throw 'XeLaTeX second pass failed.' }

  Write-Host 'Build completed: main.pdf'
}
finally {
  Pop-Location
}
