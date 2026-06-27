# Checklist de instalación

## Ya instalado en tu máquina

- [x] **Ollama** v0.30.9
- [x] **Git** 2.54.0
- [x] **GitHub CLI** (cuenta: cscspachile-existe)
- [x] **Cursor** (IDE)

## Debes instalar manualmente (extensiones en Cursor)

1. Abre Cursor
2. `Ctrl+Shift+X` → Extensions
3. Busca e instala:
   - [ ] **Continue** (Continue.dev)
   - [ ] **Cline** (saoudrizwan.claude-dev)

## Modelos Ollama (script automático)

Ejecuta desde PowerShell:

```powershell
cd C:\Users\claud\dev-projects\hybrid-dev-system\scripts
.\setup-windows.ps1
```

O manualmente:

```powershell
ollama pull qwen2.5-coder:14b
ollama pull qwen2.5-coder:1.5b
ollama pull nomic-embed-text
ollama create qwen-coder-32k -f C:\Users\claud\dev-projects\hybrid-dev-system\templates\Modelfile
```

## Configuración aplicada automáticamente

- [x] `~/.continue/config.yaml` — modelos Ollama locales
- [x] `~/.cursor/skills/dev-muscle-*` — agentes
- [x] Templates en `hybrid-dev-system/templates/`

## Opcional

- [ ] **Aider** — `pip install aider-chat` (terminal pair programming)
- [ ] **Python 3.10+** — para Aider
- [ ] GPU NVIDIA con CUDA — acelera Ollama

## Verificar que todo funciona

```powershell
ollama list
curl http://localhost:11434/api/tags
```

En Cursor: panel Continue → escribe "Hola" → debe responder con modelo local.
