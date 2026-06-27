# Guía de setup — Windows

## 1. Carpeta de proyectos

Todos tus proyectos viven bajo:

```
C:\Users\claud\dev-projects\
├── hybrid-dev-system\    ← documentación y templates (este repo)
└── mi-app\               ← tus proyectos
    ├── AGENTS.md
    └── .cursor\rules\
```

## 2. Ollama

```powershell
# Verificar servicio
ollama list

# Si no corre, iniciar
Start-Process "$env:LOCALAPPDATA\Programs\Ollama\ollama.exe" -ArgumentList "serve"

# Descargar modelos
ollama pull qwen2.5-coder:14b
ollama pull qwen2.5-coder:1.5b
ollama pull nomic-embed-text

# Modelo con contexto ampliado
ollama create qwen-coder-32k -f C:\Users\claud\dev-projects\hybrid-dev-system\templates\Modelfile
```

## 3. Continue en Cursor

Config en: `C:\Users\claud\.continue\config.yaml`

Copia desde template si no existe:

```powershell
Copy-Item C:\Users\claud\dev-projects\hybrid-dev-system\templates\continue-config.yaml `
  C:\Users\claud\.continue\config.yaml
```

Reinicia Cursor.

## 4. Cline en Cursor

1. Instala extensión Cline
2. Panel Cline → ⚙️ Settings:
   - API Provider: **Ollama**
   - Base URL: `http://localhost:11434`
   - Model: **qwen-coder-32k**
3. Features → **Use Compact Prompt: ON**

## 5. Nuevo proyecto

```powershell
cd C:\Users\claud\dev-projects
mkdir mi-nuevo-proyecto
cd mi-nuevo-proyecto
git init

# Copiar templates
Copy-Item ..\hybrid-dev-system\templates\AGENTS.md .
Copy-Item -Recurse ..\hybrid-dev-system\templates\.cursor .
```

Edita `AGENTS.md` con tu stack.

## 6. Skills (agentes)

Ya instalados en `C:\Users\claud\.cursor\skills\`:

- dev-muscle-orchestrator
- dev-muscle-frontend
- dev-muscle-backend
- dev-muscle-wordpress

Invocar en Cursor Chat: `@dev-muscle-orchestrator`

## 7. Script automático

```powershell
cd C:\Users\claud\dev-projects\hybrid-dev-system\scripts
.\setup-windows.ps1
```
