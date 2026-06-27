#Requires -Version 5.1
<#
.SYNOPSIS
  Configura Cline para Ollama (sistema híbrido Dev Muscle)
#>

$ErrorActionPreference = "Stop"
$now = (Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ss.fffZ")
$clineData = Join-Path $env:USERPROFILE ".cline\data"
$settingsDir = Join-Path $clineData "settings"

New-Item -ItemType Directory -Force -Path $settingsDir | Out-Null

$providers = @{
  version = 1
  lastUsedProvider = "ollama"
  providers = @{
    ollama = @{
      settings = @{
        provider = "ollama"
        baseUrl = "http://localhost:11434"
        model = "qwen-coder-32k"
        contextWindow = 32768
      }
      updatedAt = $now
      tokenSource = "manual"
    }
  }
}

$providersPath = Join-Path $settingsDir "providers.json"
$providers | ConvertTo-Json -Depth 10 | Set-Content -Path $providersPath -Encoding UTF8

$globalStatePath = Join-Path $clineData "globalState.json"
$globalState = @{}
if (Test-Path $globalStatePath) {
  $globalState = Get-Content $globalStatePath -Raw | ConvertFrom-Json -AsHashtable
}

$updates = @{
  welcomeViewCompleted = $true
  planModeApiProvider = "ollama"
  actModeApiProvider = "ollama"
  planModeOllamaModelId = "qwen-coder-32k"
  actModeOllamaModelId = "qwen-coder-32k"
  ollamaBaseUrl = "http://localhost:11434"
  ollamaApiOptionsCtxNum = "32768"
  customPrompt = "compact"
  preferredLanguage = "Spanish"
  mode = "act"
}

foreach ($key in $updates.Keys) {
  $globalState[$key] = $updates[$key]
}

$globalState | ConvertTo-Json -Depth 10 | Set-Content -Path $globalStatePath -Encoding UTF8

Write-Host "Cline configurado:" -ForegroundColor Green
Write-Host "  Provider: Ollama"
Write-Host "  Model: qwen-coder-32k"
Write-Host "  Base URL: http://localhost:11434"
Write-Host "  Compact prompt: ON"
Write-Host ""
Write-Host "Recarga Cursor (Ctrl+Shift+P -> Developer: Reload Window)" -ForegroundColor Yellow
