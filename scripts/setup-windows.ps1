#Requires -Version 5.1
<#
.SYNOPSIS
  Setup del sistema híbrido Dev Muscle en Windows
#>

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$Templates = Join-Path $Root "templates"

Write-Host "=== Hybrid Dev System Setup ===" -ForegroundColor Cyan

# 1. Ollama
Write-Host "`n[1/5] Verificando Ollama..." -ForegroundColor Yellow
$ollama = Get-Command ollama -ErrorAction SilentlyContinue
if (-not $ollama) {
    Write-Host "  FALTA: Instala Ollama desde https://ollama.com" -ForegroundColor Red
    exit 1
}

# Iniciar Ollama si no responde
try {
    Invoke-RestMethod -Uri "http://localhost:11434/api/tags" -TimeoutSec 3 | Out-Null
    Write-Host "  Ollama ya corre" -ForegroundColor Green
} catch {
    Write-Host "  Iniciando Ollama..." -ForegroundColor Yellow
    Start-Process "$env:LOCALAPPDATA\Programs\Ollama\ollama.exe" -ArgumentList "serve" -WindowStyle Hidden
    Start-Sleep -Seconds 5
}

# 2. Modelos
Write-Host "`n[2/5] Descargando modelos (puede tardar)..." -ForegroundColor Yellow
$models = @("qwen2.5-coder:14b", "qwen2.5-coder:1.5b", "nomic-embed-text")
foreach ($m in $models) {
    Write-Host "  Pull $m..."
    ollama pull $m
}

Write-Host "  Creando qwen-coder-32k..."
$modelfile = Join-Path $Templates "Modelfile"
if (Test-Path $modelfile) {
    ollama create qwen-coder-32k -f $modelfile 2>$null
    if ($LASTEXITCODE -ne 0) {
        ollama create qwen-coder-32k -f $modelfile
    }
}

# 3. Continue config
Write-Host "`n[3/5] Configurando Continue..." -ForegroundColor Yellow
$continueDir = Join-Path $env:USERPROFILE ".continue"
if (-not (Test-Path $continueDir)) { New-Item -ItemType Directory -Path $continueDir | Out-Null }
Copy-Item (Join-Path $Templates "continue-config.yaml") (Join-Path $continueDir "config.yaml") -Force
Write-Host "  config.yaml copiado a $continueDir" -ForegroundColor Green

# 4. Skills ya en ~/.cursor/skills/
Write-Host "`n[4/5] Skills Dev Muscle en ~/.cursor/skills/" -ForegroundColor Green
Get-ChildItem (Join-Path $env:USERPROFILE ".cursor\skills\dev-muscle-*") -ErrorAction SilentlyContinue | ForEach-Object {
    Write-Host "  - $($_.Name)"
}

# 5. Resumen
Write-Host "`n[5/5] Pendiente manual en Cursor:" -ForegroundColor Yellow
Write-Host "  - Instalar extension Continue"
Write-Host "  - Instalar extension Cline"
Write-Host "  - Cline: Provider Ollama, Model qwen-coder-32k, Compact Prompt ON"

Write-Host "`n=== Setup completado ===" -ForegroundColor Cyan
Write-Host "Docs: $Root\docs\CURSOR-WORKFLOW.md"
