# Hybrid Dev System

Sistema híbrido de desarrollo: **Cursor + Ollama + Continue + Cline**.

- **Local (gratis):** Continue + Cline + Ollama para el 80% del trabajo
- **Cloud (créditos):** Cursor Agent solo cuando lo local no alcanza
- **Memoria:** Rules, Skills, AGENTS.md — no repetir lo ya resuelto

## Estructura

```
dev-projects/
├── hybrid-dev-system/     ← Este repo (documentación, templates, scripts)
└── [tus-proyectos]/        ← Cada proyecto con AGENTS.md + .cursor/rules/
```

## Inicio rápido

1. Ejecuta `scripts/setup-windows.ps1`
2. Instala extensiones en Cursor: **Continue** y **Cline**
3. Abre Cursor → chat con **Dev Muscle** (Skill: `dev-muscle-orchestrator`)
4. Lee `docs/CURSOR-WORKFLOW.md` para el flujo diario

## Documentación

| Archivo | Contenido |
|---------|-----------|
| [docs/HYBRID-DEV-PLAN.md](docs/HYBRID-DEV-PLAN.md) | Arquitectura completa |
| [docs/INSTALL-CHECKLIST.md](docs/INSTALL-CHECKLIST.md) | Qué instalar |
| [docs/CURSOR-WORKFLOW.md](docs/CURSOR-WORKFLOW.md) | Cómo interactuar con Cursor |
| [docs/SETUP-GUIDE.md](docs/SETUP-GUIDE.md) | Setup paso a paso |

## GitHub

Repo: `cscspachile-existe/hybrid-dev-system`
