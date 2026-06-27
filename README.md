# Hybrid Dev System

Sistema híbrido de desarrollo: **Cursor + Ollama + Continue + Cline**.

- **Local (gratis):** Continue + Cline + Ollama para el 80% del trabajo
- **Cloud (créditos):** Cursor Agent solo cuando lo local no alcanza
- **Memoria:** Rules, Skills, AGENTS.md — no repetir lo ya resuelto

## Estructura

```
hybrid-dev-system/
├── workspace/              ← Carpetas ordenadas (proyectos, docs, scripts…)
│   ├── proyectos/          ← Código fuente
│   ├── docs-usuario/       ← Manuales (aprender haciendo)
│   ├── docs-agentes/       ← Contexto para IA
│   ├── scripts/            ← Automatización
│   ├── base-datos/         ← Schemas, migraciones
│   ├── imagenes/           ← Capturas, diagramas
│   ├── referencia/         ← Cheatsheets, links
│   └── ejecutables/        ← Notas de tools instalados
├── docs/                   ← Documentación técnica
├── skills/                 ← Agentes Dev Muscle
├── templates/              ← Plantillas nuevos proyectos
└── scripts/                ← Setup Ollama, Cline, etc.
```

## Inicio rápido (aprender haciendo)

1. Lee [workspace/docs-usuario/01-empezar-aqui.md](workspace/docs-usuario/01-empezar-aqui.md)
2. Haz [workspace/docs-usuario/03-practica-ejercicio-1.md](workspace/docs-usuario/03-practica-ejercicio-1.md)
3. Consulta [docs/ESQUEMA-HIBRIDO.md](docs/ESQUEMA-HIBRIDO.md) para la arquitectura

## Documentación

| Archivo | Contenido |
|---------|-----------|
| [docs/HYBRID-DEV-PLAN.md](docs/HYBRID-DEV-PLAN.md) | Arquitectura completa |
| [docs/INSTALL-CHECKLIST.md](docs/INSTALL-CHECKLIST.md) | Qué instalar |
| [docs/CURSOR-WORKFLOW.md](docs/CURSOR-WORKFLOW.md) | Cómo interactuar con Cursor |
| [docs/SETUP-GUIDE.md](docs/SETUP-GUIDE.md) | Setup paso a paso |

## GitHub

Repo: `cscspachile-existe/hybrid-dev-system`
