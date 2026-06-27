# Prompts y navegación entre herramientas

## Regla de oro

> **Empieza siempre local.** Escala a Cursor cloud solo si local falla 2 veces o la tarea es claramente difícil.

---

## Tabla: qué herramienta usar

| Quiero… | Herramienta | Panel / atajo |
|---------|-------------|---------------|
| Preguntar sobre código | Continue | Continue |
| Completar mientras escribo | Continue | Editor |
| Buscar en todo el repo | Continue | `@Codebase` en chat |
| Crear archivos / refactor | Cline | Cline → Plan → Act |
| No sé por dónde empezar | Dev Muscle | Cursor Chat `@dev-muscle-orchestrator` |
| Bug muy difícil | Cursor Agent | `Ctrl+I` |
| Ver créditos | Cursor | Settings → Usage |

---

## Prompts listos para copiar

### Continue — explicar

```
@src/archivo.ts Explica qué hace este archivo en español, en 5 bullets
```

### Continue — buscar

```
@Codebase ¿dónde se valida el email del usuario?
```

### Cline — crear feature

```
Crea [descripción].
Sigue AGENTS.md y .cursor/rules/.
Stack: [tu stack].
Responde/ejecuta en español en comentarios de commit.
```

### Dev Muscle — orquestador

```
@dev-muscle-orchestrator

Tarea: [describe aquí]
Prioridad: local si es posible
Stack: ver AGENTS.md
```

### Dev Muscle + especialista frontend

```
@dev-muscle-orchestrator @dev-muscle-frontend

Crea componente Button con variantes primary/secondary en Tailwind.
Local primero.
```

### Escalar a cloud (solo cuando haga falta)

```
@dev-muscle-orchestrator

Escalar a Cursor cloud. Créditos OK.
Tarea: [descripción compleja]
Incluye @AGENTS.md
```

---

## Cómo moverte entre paneles en Cursor

```
Barra lateral izquierda:
├── 📁 Explorer        → archivos
├── 🔍 Search          → buscar texto
├── Continue           → chat local + autocomplete
├── Cline              → agente Plan/Act
└── (otros)

Atajos útiles:
Ctrl+L     → Cursor Chat (Agent / Dev Muscle)
Ctrl+I     → Cursor Agent (cloud)
Ctrl+`     → Terminal
Ctrl+Shift+P → Command Palette
```

---

## Flujo típico de una sesión

```
1. Abrir proyecto en Cursor
2. Settings → Usage (créditos)
3. Tarea nueva:
   a. ¿Solo pregunta? → Continue
   b. ¿Crear código? → Cline Plan → Act
   c. ¿Duda de herramienta? → @dev-muscle-orchestrator
4. Al terminar algo nuevo → Rule o AGENTS.md
5. git commit
```

---

## Errores comunes

| Error | Solución |
|-------|----------|
| Continue no responde | `ollama serve` o reiniciar Ollama |
| Cline "connection refused" | Ollama no corre |
| Cline muy lento | Compact prompt ON (ya configurado) |
| Gasto créditos sin querer | Auto OFF, usar Continue/Cline primero |
| IA repite lo mismo | Crear Rule en `.cursor/rules/` |

---

## Práctica sugerida

Repite [03-practica-ejercicio-1.md](03-practica-ejercicio-1.md) cambiando la tarea:

- Ejercicio 2: Cline crea `styles.css` separado
- Ejercicio 3: Continue `@Codebase` en un proyecto más grande
- Ejercicio 4: Dev Muscle te pide escalar a cloud en un bug inventado
