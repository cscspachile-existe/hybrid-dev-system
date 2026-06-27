# Memoria y organización

## Dos tipos de documentación

| Para | Carpeta | Ejemplo |
|------|---------|---------|
| **Ti** (leer, aprender) | `workspace/docs-usuario/` | Este manual |
| **Agentes** (reglas, contexto) | `workspace/docs-agentes/` + `.cursor/rules/` | Patrones API |

---

## Memoria del sistema híbrido

La IA **no aprende sola**. Tú (o el agente) escribes archivos:

| Artefacto | Ubicación | Quién lo lee |
|-----------|-----------|--------------|
| AGENTS.md | Raíz del proyecto | Todos |
| Rules | `.cursor/rules/*.mdc` | Cursor, Cline |
| Skills | `~/.cursor/skills/` | Cursor Agent |
| Cline rules | `.clinerules/` | Cline |
| Git history | Commits | @Codebase |

---

## Ritual al terminar sesión (2 min)

```
□ ¿Resolví algo nuevo con cloud?
  → Crear/actualizar Rule

□ ¿Decisión de arquitectura?
  → Actualizar AGENTS.md

□ ¿Screenshot útil?
  → workspace/imagenes/capturas/

□ ¿Script reutilizable?
  → workspace/scripts/

□ git add + commit + push
```

---

## Respaldar en GitHub

Repo: https://github.com/cscspachile-existe/hybrid-dev-system

```powershell
cd C:\Users\claud\dev-projects\hybrid-dev-system
git add .
git commit -m "docs: actualizar workspace y practica"
git push
```

**No subas:** `.db` grandes, `.env`, passwords, ejecutables pesados.

---

## Estructura workspace (resumen)

```
workspace/
├── proyectos/       ← tu código
├── scripts/         ← automatización
├── base-datos/      ← schemas (no dumps sensibles)
├── imagenes/        ← capturas, diagramas
├── docs-usuario/    ← manuales (tú)
├── docs-agentes/    ← contexto IA
├── referencia/      ← cheatsheets, links
└── ejecutables/     ← solo notas (INSTALADOS.md)
```

---

## Aprender haciendo — ruta sugerida

| Semana | Actividad |
|--------|-----------|
| 1 | Ejercicio 1 + Continue chat |
| 2 | Cline Plan/Act en proyecto real |
| 3 | Crear 3 Rules de patrones tuyos |
| 4 | Escalar 1 vez a cloud + documentar patrón |
| 5 | Proyecto completo solo local |
