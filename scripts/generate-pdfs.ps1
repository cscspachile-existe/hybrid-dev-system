#Requires -Version 5.1
<#
.SYNOPSIS
  Genera PDFs del sistema híbrido Dev Muscle (Node/PDFKit, sin Chromium)
#>

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$PdfDir = Join-Path $Root "workspace\docs-usuario\pdf"
$UsuarioMd = Join-Path $PdfDir "Guia-Usuario-Sistema-Hibrido.md"
$SistemaMd = Join-Path $PdfDir "Sistema-Hibrido-Documentacion-Completa.md"
$PdfGenDir = Join-Path $PSScriptRoot "pdf-gen"

New-Item -ItemType Directory -Force -Path $PdfDir | Out-Null

function Merge-Markdown {
    param(
        [string]$Output,
        [string[]]$Files,
        [string]$Title,
        [string]$Subtitle
    )
    $sb = New-Object System.Text.StringBuilder
    [void]$sb.AppendLine("# $Title")
    [void]$sb.AppendLine("")
    [void]$sb.AppendLine("**$Subtitle**")
    [void]$sb.AppendLine("")
    [void]$sb.AppendLine("Generado: $(Get-Date -Format 'yyyy-MM-dd HH:mm')")
    [void]$sb.AppendLine("")
    [void]$sb.AppendLine("---")
    [void]$sb.AppendLine("")
    foreach ($f in $Files) {
        if (-not (Test-Path $f)) { Write-Warning "Skip missing: $f"; continue }
        [void]$sb.AppendLine((Get-Content $f -Raw -Encoding UTF8))
        [void]$sb.AppendLine("")
        [void]$sb.AppendLine("---")
        [void]$sb.AppendLine("")
    }
    $utf8NoBom = New-Object System.Text.UTF8Encoding $false
    [System.IO.File]::WriteAllText($Output, $sb.ToString(), $utf8NoBom)
}

$usuarioFiles = @(
    (Join-Path $Root "workspace\docs-usuario\01-empezar-aqui.md"),
    (Join-Path $Root "workspace\docs-usuario\02-como-funciona-el-sistema.md"),
    (Join-Path $Root "workspace\docs-usuario\03-practica-ejercicio-1.md"),
    (Join-Path $Root "workspace\docs-usuario\04-prompts-y-navegacion.md"),
    (Join-Path $Root "workspace\docs-usuario\05-escalar-a-cursor-cloud.md"),
    (Join-Path $Root "workspace\docs-usuario\06-memoria-y-organizacion.md")
)

Merge-Markdown -Output $UsuarioMd -Files $usuarioFiles `
    -Title "Guia de lectura - Sistema hibrido Dev Muscle" `
    -Subtitle "Para el usuario - Aprender haciendo - Cursor + Continue + Cline + Ollama"

$sistemaFiles = @(
    (Join-Path $Root "docs\ESQUEMA-HIBRIDO.md"),
    (Join-Path $Root "docs\HYBRID-DEV-PLAN.md"),
    (Join-Path $Root "docs\CURSOR-WORKFLOW.md"),
    (Join-Path $Root "docs\PROMPT-MAESTRO.md"),
    (Join-Path $Root "docs\SETUP-GUIDE.md"),
    (Join-Path $Root "docs\INSTALL-CHECKLIST.md"),
    (Join-Path $Root "workspace\README.md"),
    (Join-Path $Root "skills\dev-muscle-orchestrator\SKILL.md")
) + $usuarioFiles

Merge-Markdown -Output $SistemaMd -Files $sistemaFiles `
    -Title "Documentacion completa - Sistema hibrido Dev Muscle" `
    -Subtitle "Referencia tecnica + guia usuario + workspace"

Write-Host "Instalando PDFKit..." -ForegroundColor Cyan
Push-Location $PdfGenDir
try {
    if (-not (Test-Path "node_modules\pdfkit")) {
        npm install --no-fund --no-audit 2>&1 | Out-Null
    }
} finally {
    Pop-Location
}

$pdf1 = Join-Path $PdfDir "Guia-Usuario-Sistema-Hibrido.pdf"
$pdf2 = Join-Path $PdfDir "Sistema-Hibrido-Documentacion-Completa.pdf"

Write-Host "Generando PDFs..." -ForegroundColor Cyan
node (Join-Path $PdfGenDir "md-to-pdf.mjs") $UsuarioMd $pdf1
node (Join-Path $PdfGenDir "md-to-pdf.mjs") $SistemaMd $pdf2

if (-not (Test-Path $pdf1)) { throw "No se creo $pdf1" }
if (-not (Test-Path $pdf2)) { throw "No se creo $pdf2" }

$s1 = (Get-Item $pdf1).Length
$s2 = (Get-Item $pdf2).Length
if ($s1 -lt 10240) { Write-Warning "PDF usuario pequeno: $s1 bytes" }
if ($s2 -lt 10240) { Write-Warning "PDF sistema pequeno: $s2 bytes" }

Write-Host ""
Write-Host "OK PDFs generados:" -ForegroundColor Green
Write-Host "  $pdf1 ($s1 bytes)"
Write-Host "  $pdf2 ($s2 bytes)"
