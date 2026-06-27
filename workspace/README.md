# Workspace de desarrollo

Carpetas ordenadas para todo lo que usas al desarrollar. Respaldadas en GitHub dentro de [hybrid-dev-system](https://github.com/cscspachile-existe/hybrid-dev-system).

## Mapa rápido

| Carpeta | Qué guardar |
|---------|-------------|
| [proyectos/](proyectos/) | Código fuente (apps, plugins, sitios) |
| [scripts/](scripts/) | Automatización (.ps1, .sh, .py) |
| [ejecutables/](ejecutables/) | Binarios locales (ver README — no subir todo) |
| [base-datos/](base-datos/) | Schemas, migraciones, seeds (no .db grandes) |
| [imagenes/](imagenes/) | Screenshots, diagramas, assets de doc |
| [docs-usuario/](docs-usuario/) | Manuales para ti (cómo usar el sistema) |
| [docs-agentes/](docs-agentes/) | AGENTS.md, rules, contexto para IA |
| [referencia/](referencia/) | APIs, cheatsheets, links, notas técnicas |

## Regla de oro

- **Código** → `proyectos/nombre-del-proyecto/`
- **“La IA debe saber esto”** → `docs-agentes/` o `.cursor/rules/` dentro del proyecto
- **“Yo debo leer esto”** → `docs-usuario/`

## Empezar un proyecto nuevo

```powershell
cd C:\Users\claud\dev-projects\hybrid-dev-system\workspace\proyectos
mkdir mi-app
cd mi-app
git init
Copy-Item ..\..\..\templates\AGENTS.md .
Copy-Item -Recurse ..\..\..\templates\.cursor .
```

Ver [docs-usuario/01-empezar-aqui.md](docs-usuario/01-empezar-aqui.md)
