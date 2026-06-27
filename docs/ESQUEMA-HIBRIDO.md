# Esquema híbrido — revisión y aclaración

## ¿Tenemos el esquema híbrido?

**Sí.** Está implementado y operativo en tu máquina.

---

## Esquema real (lo que tienes)

```
┌─────────────────────────────────────────────────────────┐
│  CURSOR (IDE — reemplaza VS Code en este setup)         │
│  ├── Tab / Agent cloud (créditos, escalación)           │
│  ├── Rules + Skills (memoria)                           │
│  ├── Continue.dev (extensión)                           │
│  └── Cline (extensión)                                  │
├─────────────────────────────────────────────────────────┤
│  OLLAMA (motor local, sin créditos)                     │
│  qwen-coder-32k │ 1.5b autocomplete │ nomic-embed       │
├─────────────────────────────────────────────────────────┤
│  MEMORIA + ORGANIZACIÓN                                 │
│  workspace/ │ AGENTS.md │ .cursor/rules/ │ GitHub       │
└─────────────────────────────────────────────────────────┘
```

---

## VS Code + Continue + Cline + Ollama vs tu setup

| Documentación genérica | Tu setup real |
|------------------------|---------------|
| VS Code como editor | **Cursor** como editor |
| Continue en VS Code | **Continue en Cursor** ✓ |
| Cline en VS Code | **Cline en Cursor** ✓ |
| Ollama local | **Ollama local** ✓ |
| Cursor aparte | **Cursor integra todo** ✓ |

**Conclusión:** El esquema es el mismo. Solo cambia el nombre del IDE: usas **Cursor** en lugar de VS Code. No necesitas ambos.

---

## Estado de componentes (tu PC)

| Componente | Estado |
|------------|--------|
| Cursor IDE | ✓ Instalado |
| Ollama + modelos | ✓ Configurado |
| Continue | ✓ Extensión + config.yaml |
| Cline | ✓ Extensión + Ollama configurado |
| Dev Muscle Skills | ✓ ~/.cursor/skills/ |
| Workspace ordenado | ✓ workspace/ |
| GitHub | ✓ hybrid-dev-system |

---

## Flujo de costos

```
80% tareas → Continue / Cline + Ollama → $0
15% tareas → Cursor Tab → créditos plan
5% tareas  → Cursor Agent cloud → créditos (escalación)
```

Memoria (Rules) reduce el 5% con el tiempo.

---

## Carpeta local + GitHub

```
C:\Users\claud\dev-projects\
└── hybrid-dev-system/          ← repo GitHub
    ├── workspace/              ← proyectos, docs, assets ordenados
    ├── docs/                   ← documentación técnica
    ├── skills/                 ← backup agentes
    ├── templates/              ← plantillas nuevos proyectos
    └── scripts/                ← setup, configure-cline, etc.
```

URL: https://github.com/cscspachile-existe/hybrid-dev-system

---

## Documentación usuario (empezar)

👉 [workspace/docs-usuario/01-empezar-aqui.md](../workspace/docs-usuario/01-empezar-aqui.md)
