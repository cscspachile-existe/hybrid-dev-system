# Cuándo escalar a Cursor cloud

## Antes de gastar créditos

1. **Settings → Usage** — ¿cuánto queda del mes?
2. **¿Existe Rule?** — busca en `.cursor/rules/` y `AGENTS.md`
3. **¿Probaste local 2 veces?** — Cline o Continue

---

## Usa cloud SOLO si

| Situación | Ejemplo |
|-----------|---------|
| Cline falló 2× misma tarea | Bug que local no entiende |
| Arquitectura nueva | Diseñar sistema desde cero |
| Seguridad crítica | Auth, permisos, auditoría |
| Integración desconocida | API nunca usada en el proyecto |
| Tú lo pides explícitamente | "Necesito Opus para esto" |

---

## Config recomendada al escalar

```
Cursor Agent (Ctrl+I):
- Auto: OFF
- MAX Mode: OFF
- Modelo: Composer 2.5 Fast (normal) o Sonnet (difícil)
```

Incluye en el prompt:

```
@AGENTS.md
@.cursor/rules/hybrid-workflow.mdc

[Tu tarea]
```

---

## Después de resolver con cloud (obligatorio)

Para que **no vuelvas a pagar** la misma tarea:

1. Crea `.cursor/rules/nombre-patron.mdc` con lo aprendido
2. Actualiza `AGENTS.md` si hubo decisión de arquitectura
3. `git commit -m "docs: add pattern X"`

La próxima vez → **Cline/Continue local**.

---

## Ejemplo

```
❌ Mal: Cada CRUD → Cursor Agent (gasta créditos)

✅ Bien:
   1. Primer CRUD usuarios → Cursor cloud (difícil)
   2. Guardar patrón en rules/api-crud.mdc
   3. CRUD productos, pedidos… → Cline local (gratis)
```
