param(
  [string]$SourceDir = "../OCT_BOOK",
  [string]$OutDir = ".."
)

$ErrorActionPreference = 'Stop'

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = Resolve-Path (Join-Path $scriptDir $OutDir)
$sourceRoot = Resolve-Path (Join-Path $projectRoot $SourceDir)
$tmpDir = Join-Path $projectRoot 'tmp'
$chaptersDir = Join-Path $projectRoot 'chapters'
$backmatterDir = Join-Path $projectRoot 'backmatter'
$filtersDir = Join-Path $scriptDir 'filters'

New-Item -ItemType Directory -Force -Path $tmpDir,$chaptersDir,$backmatterDir | Out-Null

function Remove-MetadataBlock {
  param([string]$Text)

  $lines = $Text -split "`r?`n"
  $metaStart = -1
  for($i=0; $i -lt $lines.Count; $i++){
    if($lines[$i].Trim() -eq 'Metadati:') { $metaStart = $i; break }
  }

  if($metaStart -lt 0){ return $Text }

  $hr = -1
  for($j=$metaStart; $j -lt $lines.Count; $j++){
    if($lines[$j].Trim() -eq '---'){ $hr = $j; break }
  }

  if($hr -lt 0){ return $Text }

  $head = if($metaStart -gt 0){ $lines[0..($metaStart-1)] } else { @() }
  $tail = if($hr + 1 -lt $lines.Count){ $lines[($hr+1)..($lines.Count-1)] } else { @() }

  return (($head + '' + $tail) -join "`n")
}

function Normalize-UnicodeSymbols {
  param([string]$Text)

  $norm = $Text
  $norm = $norm.Replace('∧',' AND ')
  $norm = $norm.Replace('∨',' OR ')
  $norm = $norm.Replace('∘',' o ')
  $norm = $norm.Replace('≠',' != ')
  $norm = $norm.Replace('≃',' ~= ')
  $norm = $norm.Replace('≅',' ~= ')
  $norm = $norm.Replace('∩',' inter ')
  $norm = $norm.Replace('⟨','<')
  $norm = $norm.Replace('⟩','>')
  return $norm
}

$chapterFiles = Get-ChildItem -Path $sourceRoot -File |
  Where-Object { $_.Name -match '^OCT_FOUNDATIONAL_BOOK_CHAPTER_(\d{2})_v1_0\.md$' } |
  Sort-Object Name

if(-not $chapterFiles){ throw "Nessun capitolo trovato in $sourceRoot" }

foreach($file in $chapterFiles){
  $num = [regex]::Match($file.Name, '(\d{2})').Groups[1].Value
  $cleanPath = Join-Path $tmpDir ("ch{0}.md" -f $num)
  $outPath = Join-Path $chaptersDir ("ch{0}.tex" -f $num)

  $raw = Get-Content -Raw -Path $file.FullName
  $clean = Remove-MetadataBlock -Text $raw
  $clean = Normalize-UnicodeSymbols -Text $clean
  Set-Content -Path $cleanPath -Value $clean -Encoding UTF8

  $args = @(
    $cleanPath,
    '--from=gfm+smart',
    '--to=latex',
    '--top-level-division=chapter',
    '--lua-filter', (Join-Path $filtersDir 'strip_header_ids.lua'),
    '--wrap=preserve',
    '--output', $outPath
  )

  & pandoc @args
  if($LASTEXITCODE -ne 0){ throw "Pandoc conversion failed for $($file.Name)" }
  Write-Host "Generated $outPath"
}

$biblioMd = Join-Path $sourceRoot 'OCT_FOUNDATIONAL_BOOK_BIBLIOGRAPHY_CONSOLIDATED_v1_0.md'
if(Test-Path $biblioMd){
  $biblioRaw = Get-Content -Raw -Path $biblioMd
  $biblioClean = Remove-MetadataBlock -Text $biblioRaw
  $biblioClean = Normalize-UnicodeSymbols -Text $biblioClean
  $biblioTmp = Join-Path $tmpDir 'bibliography_consolidated.md'
  $biblioTex = Join-Path $backmatterDir 'bibliography_consolidated.tex'
  Set-Content -Path $biblioTmp -Value $biblioClean -Encoding UTF8

  & pandoc $biblioTmp '--from=gfm+smart' '--to=latex' '--top-level-division=chapter' '--lua-filter' (Join-Path $filtersDir 'strip_header_ids.lua') '--wrap=preserve' '--output' $biblioTex
  if($LASTEXITCODE -ne 0){ throw "Pandoc conversion failed for consolidated bibliography" }
  Write-Host "Generated $biblioTex"
}

Write-Host 'Conversion completed.'
