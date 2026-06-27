# Cómo funciona el sistema (para humanos)

## La idea en una frase

**Local primero (gratis), Cursor cloud solo si hace falta, memoria en archivos para no repetir.**

---

## Las piezas y qué hace cada una

### 1. Cursor — tu mesa de trabajo

| Rol | Qué es |
|-----|--------|
| IDE | Editor de código, archivos, terminal integrada |
| Tab | Autocompletado rápido (usa créditos del plan) |
| Agent cloud | Agente potente Opus/Sonnet (usa créditos) |
| Rules / Skills | Memoria persistente del proyecto |

**Cuándo usarlo:** siempre abierto. Agent cloud solo para tareas difíciles.

---

### 2. Ollama — el motor local

| Rol | Qué es |
|-----|--------|
| Servidor local | Corre modelos en tu PC |
| Sin internet | Inferencia sin API |
| Sin créditos | No gasta plan de Cursor |

**Modelos que tienes:** `qwen-coder-32k`, `qwen2.5-coder:14b`, `1.5b`, `nomic-embed-text`

**Cuándo usarlo:** siempre detrás de Continue y Cline (automático).

---

### 3. Continue — asistente al lado

| Rol | Panel en Cursor |
|-----|-----------------|
| Chat | Preguntas, explicaciones |
| Autocomplete | Sugerencias mientras escribes (local) |
| @Codebase | Buscar en todo el proyecto |
| Edit | Modificar código seleccionado |

**Cuándo usarlo:**
- "¿Qué hace este archivo?"
- "Explícame este error"
- Autocomplete sin gastar Tab de Cursor
- `@Codebase ¿dónde está la validación?`

**Costo:** 0 créditos

---

### 4. Cline — el ejecutor

| Rol | Panel en Cursor |
|-----|-----------------|
| Plan | Propone plan sin tocar archivos |
| Act | Crea/edita archivos, corre comandos |
| Aprobación | Tú apruebas cada paso |

**Cuándo usarlo:**
- Crear archivos nuevos
- Refactor en varios archivos
- Instalar dependencias
- CRUD, componentes, scripts

**Costo:** 0 créditos (con Ollama)

---

### 5. Dev Muscle — tu orquestador

| Rol | Cursor Chat con `@dev-muscle-orchestrator` |
|-----|---------------------------------------------|
| Decide | Local vs cloud |
| Delega | Frontend, backend, WordPress |
| Recuerda | Lee AGENTS.md y Rules |

**Cuándo usarlo:** cuando no sabes qué herramienta elegir.

---

## Diagrama del flujo

```
                    ┌──────────────┐
                    │  Tu tarea    │
                    └──────┬───────┘
                           │
              ┌────────────▼────────────┐
              │  ¿Patrón ya en Rules?   │
              └────────────┬────────────┘
                    sí     │     no
              ┌───────────┴───────────┐
              ▼                       ▼
     Continue / Cline            Intentar local
     (Ollama, 0 €)              primero
              │                       │
              │              ¿Falló 2 veces?
              │                       │
              │                       ▼
              │              Cursor Agent cloud
              │                       │
              └───────────┬───────────┘
                          ▼
                 Guardar en Rules / AGENTS.md
                 (próxima vez = local)
```

---

## VS Code vs Cursor — aclaración

| Pregunta | Respuesta |
|----------|-----------|
| ¿Necesito VS Code? | **No** |
| ¿Continue/Cline funcionan? | **Sí, dentro de Cursor** |
| ¿Es el mismo esquema que "VS Code + Continue + Cline + Ollama"? | **Sí**, pero el editor es **Cursor**, no VS Code aparte |

---

## Siguiente

Practica con [03-practica-ejercicio-1.md](03-practica-ejercicio-1.md)
