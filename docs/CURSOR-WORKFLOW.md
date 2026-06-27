# Cómo interactuar con Cursor — flujo híbrido

Guía paso a paso para usar el sistema sin gastar créditos en lo repetitivo.

---

## Antes de empezar (una vez)

1. Ollama corriendo: `ollama serve` (o inicia desde bandeja de Windows)
2. Extensiones instaladas: **Continue** y **Cline**
3. Abre tu proyecto en Cursor

---

## Flujo diario — paso a paso

### Paso 1: Abre Cursor en tu proyecto

```
File → Open Folder → C:\Users\claud\dev-projects\tu-proyecto
```

Asegúrate de que exista `AGENTS.md` y `.cursor/rules/` (copia desde `templates/` si es proyecto nuevo).

---

### Paso 2: Consulta créditos (antes de usar cloud)

1. Clic en tu avatar (esquina inferior izquierda) o **Settings**
2. **Cursor Settings → Usage** o **Account → Usage**
3. Revisa cuánto del plan mensual queda

**Regla:** Si el crédito está bajo, usa **solo local** (Continue/Cline) ese día.

---

### Paso 3: Tarea nueva — empieza LOCAL

#### Opción A — Chat / explicaciones / edición simple

1. Panel **Continue** (icono lateral)
2. Selecciona modelo: **Qwen Coder 14B** (Ollama)
3. Escribe tu pregunta. Usa `@` para contexto:
   ```
   @src/auth.ts Explica cómo funciona la autenticación
   @Codebase ¿dónde se valida el email?
   ```

**Costo: 0 créditos**

#### Opción B — Crear código, refactor, multi-archivo

1. Panel **Cline** (icono lateral)
2. Verifica: Provider **Ollama**, Model **qwen-coder-32k**
3. Escribe la tarea
4. Modo **Plan** primero → revisa → **Act** para ejecutar

Ejemplo:
```
Crea un componente Button reutilizable con variantes primary/secondary.
Usa Tailwind. Sigue las convenciones de AGENTS.md.
```

**Costo: 0 créditos**

#### Opción C — Agente Cursor con memoria (Dev Muscle)

1. Abre **Cursor Chat** (`Ctrl+L`) o **Agent** (`Ctrl+I`)
2. Escribe al inicio del mensaje:
   ```
   @dev-muscle-orchestrator
   ```
3. Describe la tarea. El orquestador:
   - Lee Rules y AGENTS.md
   - Decide si es local o cloud
   - Te indica qué herramienta usar

**Costo:** Depende — si delega a local, 0. Si usa Agent nativo, créditos.

---

### Paso 4: ¿Cuándo escalar a Cursor cloud?

Usa **Cursor Agent** (modelo Opus/Sonnet, Auto OFF, MAX OFF) solo si:

- Cline falló 2 veces en la misma tarea
- Arquitectura nueva / diseño de sistema
- Bug muy difícil (race conditions, memory leaks)
- Code review de seguridad
- Integración compleja nunca hecha en el proyecto

**Cómo escalar:**

1. `Ctrl+I` → Agent
2. **Auto: OFF** → elige **Composer 2.5 Fast** o **Sonnet** según complejidad
3. **MAX Mode: OFF**
4. Incluye contexto: `@AGENTS.md` y rules relevantes

**Costo: créditos**

---

### Paso 5: Guardar en memoria (evitar repetir créditos)

Después de resolver algo (especialmente con cloud):

1. **Si fue un patrón nuevo** → crea Rule:
   ```
   .cursor/rules/mi-patron.mdc
   ```
2. **Si fue un flujo repetible** → actualiza Skill o crea uno
3. **Si fue decisión de arquitectura** → edita `AGENTS.md`
4. **Commit en git:**
   ```powershell
   git add .
   git commit -m "docs: add auth pattern to rules"
   ```

La próxima vez que pidas lo mismo, **Cline/Continue lo harán solos** leyendo Rules + `@Codebase`.

---

### Paso 6: Autocomplete mientras escribes

| Fuente | Cuándo | Créditos |
|--------|--------|----------|
| **Continue** (Ollama 1.5B) | Preferido — local | 0 |
| **Cursor Tab** | Si Continue no sugiere | Plan |

Para forzar local: desactiva Tab en Cursor Settings si quieres ahorrar al máximo.

---

## Tabla rápida: qué usar

| Quiero... | Uso... | Panel |
|-----------|--------|-------|
| Preguntar sobre código | Continue | Continue |
| Completar mientras escribo | Continue | Editor |
| Crear archivos / refactor | Cline Plan→Act | Cline |
| Buscar en todo el repo | Continue `@Codebase` | Continue |
| Hablar con mi agente | `@dev-muscle-orchestrator` | Cursor Chat |
| Algo muy difícil | Cursor Agent cloud | Agent (Ctrl+I) |
| Ver créditos restantes | Settings → Usage | — |

---

## Ejemplo de sesión completa

```
1. Abro proyecto en Cursor
2. Settings → Usage → veo 40% créditos restantes → priorizo local
3. Continue: "@Codebase ¿cómo está hecho el login?"
4. Cline Plan: "Añade campo teléfono al formulario de registro"
5. Cline Act → apruebo cambios → 0 créditos
6. Bug raro en producción → Cline falla 2 veces
7. Escalo: Cursor Agent (Sonnet) → resuelve
8. Creo .cursor/rules/phone-validation.mdc con el patrón
9. git commit
10. Próxima vez "añade teléfono a otro form" → Cline solo, 0 créditos
```

---

## Prompt maestro (copiar al iniciar chat con Dev Muscle)

```
Eres Dev Muscle, mi orquestador de desarrollo híbrido.

Reglas:
1. Siempre lee AGENTS.md y .cursor/rules/ antes de actuar
2. Tareas repetitivas o con Rule existente → indícame usar Continue o Cline (local, 0 créditos)
3. Solo escala a Cursor cloud si: (a) no hay Rule, (b) Cline falló 2 veces, (c) arquitectura/seguridad compleja
4. Al terminar algo nuevo con cloud → propón crear Rule o actualizar AGENTS.md
5. Responde en español
6. Antes de usar cloud, recuérdame revisar Usage en Cursor Settings

Stack del proyecto: [ver AGENTS.md]
```
