# Plan maestro: Sistema híbrido de desarrollo

## Objetivo

Usar **Cursor como IDE principal**, con una capa local (Ollama + Continue + Cline) que hace el trabajo repetitivo **sin créditos**, y escalar a **Cursor Agent cloud** solo cuando lo local no alcanza.

La "memoria" no entrena modelos — persiste conocimiento en **Rules, Skills y AGENTS.md**.

---

## Arquitectura

```
┌─────────────────────────────────────────────────────────┐
│                    CURSOR (IDE)                         │
│  Tab autocomplete │ Agent cloud │ Rules │ Skills        │
├─────────────────────────────────────────────────────────┤
│  Continue.dev     │  Cline                              │
│  Chat + Tab local │  Agente Plan/Act                    │
├─────────────────────────────────────────────────────────┤
│                    OLLAMA (local)                       │
│  qwen2.5-coder:14b │ 1.5b autocomplete │ nomic-embed   │
├─────────────────────────────────────────────────────────┤
│  MEMORIA COMPARTIDA                                     │
│  AGENTS.md │ .cursor/rules/ │ ~/.cursor/skills/         │
└─────────────────────────────────────────────────────────┘
```

---

## Flujo de decisión

| Tarea | Herramienta | Costo |
|-------|-------------|-------|
| Autocomplete mientras escribes | Continue + Ollama 1.5B | Gratis |
| Explicar código, chat simple | Continue chat | Gratis |
| Crear componente, CRUD, refactor | Cline Plan → Act | Gratis |
| Buscar en codebase | Continue `@Codebase` | Gratis |
| Arquitectura compleja, bug difícil | Cursor Agent (Opus/Sonnet) | Créditos |
| Tab rápido nativo | Cursor Tab | Créditos plan |

### Regla de escalación

1. Intentar **local** (Cline o Continue) primero
2. Si falla **2 veces** o es claramente complejo → **Cursor cloud**
3. Al resolver con cloud → **crear/actualizar Rule o Skill** (memoria)
4. La próxima vez igual → **local** (ya está en memoria)

---

## Agentes (Skills)

| Skill | Rol |
|-------|-----|
| `dev-muscle-orchestrator` | Punto de entrada — decide local vs cloud |
| `dev-muscle-frontend` | React, Next.js, Tailwind, UI |
| `dev-muscle-backend` | API, DB, auth, servicios |
| `dev-muscle-wordpress` | WordPress, WooCommerce, plugins |

El orquestador delega al especialista según el tema. Todos comparten AGENTS.md y Rules.

---

## Ritual de memoria (2 min al terminar sesión)

1. ¿Resolviste algo nuevo con Cursor cloud? → Rule en `.cursor/rules/`
2. ¿Flujo que repites? → Skill en `~/.cursor/skills/`
3. ¿Decisión de arquitectura? → Actualizar `AGENTS.md`
4. ¿Cline hizo algo bien? → Git commit = memoria para `@Codebase`

---

## Hardware recomendado

| RAM/VRAM | Modelo chat | Autocomplete |
|----------|-------------|--------------|
| 8 GB | qwen2.5-coder:7b | qwen2.5-coder:1.5b |
| 16 GB | qwen2.5-coder:14b | qwen2.5-coder:1.5b |
| 24 GB+ | qwen2.5-coder:32b | qwen2.5-coder:1.5b |

---

## Productos del mercado

### Instalados / configurados

- Cursor (IDE)
- Ollama (modelos locales)
- Continue.dev (extensión)
- Cline (extensión)
- Git + GitHub CLI

### Opcionales

- Aider (terminal, pair programming)
- MCP servers (DB, APIs externas)
- Cursor Automations (tareas programadas)
