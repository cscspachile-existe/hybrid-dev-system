# Empezar aquí

## ¿Qué tienes montado?

Un **sistema híbrido de desarrollo** en tu PC:

```
Cursor (tu IDE — no necesitas VS Code aparte)
├── Continue    → chat y autocomplete local
├── Cline       → agente que crea/edita archivos
├── Dev Muscle  → agente orquestador (@dev-muscle-orchestrator)
└── Ollama      → modelos de IA en tu máquina (gratis)
```

**Importante:** Cursor ya es un fork de VS Code. Las extensiones Continue y Cline viven **dentro de Cursor**. No hace falta abrir VS Code por separado.

## Dónde está todo en tu disco

| Qué | Ruta |
|-----|------|
| Proyectos y workspace | `C:\Users\claud\dev-projects\hybrid-dev-system\workspace\` |
| Documentación sistema | `...\hybrid-dev-system\docs\` |
| Skills (agentes) | `C:\Users\claud\.cursor\skills\dev-muscle-*` |
| Config Continue | `C:\Users\claud\.continue\config.yaml` |
| Config Cline | `C:\Users\claud\.cline\data\` |
| GitHub | https://github.com/cscspachile-existe/hybrid-dev-system |

## Antes de cada sesión (30 segundos)

1. Ollama corriendo (icono en bandeja Windows)
2. Abrir **Cursor**
3. Abrir carpeta: `workspace\proyectos\tu-proyecto` (o crear uno)
4. Opcional: Settings → Usage → ver créditos restantes

## Siguiente paso

Lee [02-como-funciona-el-sistema.md](02-como-funciona-el-sistema.md) y luego haz [03-practica-ejercicio-1.md](03-practica-ejercicio-1.md).
