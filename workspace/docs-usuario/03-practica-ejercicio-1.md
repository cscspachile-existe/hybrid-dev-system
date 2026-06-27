# Práctica — Ejercicio 1 (aprender haciendo)

Tiempo: ~20 minutos. **Objetivo:** completar una tarea real usando solo herramientas locales (0 créditos).

---

## Paso 1: Crear proyecto de práctica

```powershell
cd C:\Users\claud\dev-projects\hybrid-dev-system\workspace\proyectos
mkdir practica-01
cd practica-01
git init
Copy-Item ..\..\..\templates\AGENTS.md .
Copy-Item -Recurse ..\..\..\templates\.cursor .
```

Abre en Cursor: **File → Open Folder** → `practica-01`

---

## Paso 2: Continue — preguntar (2 min)

1. Abre panel **Continue** (barra lateral)
2. Escribe:

```
@AGENTS.md Resume en 3 bullets qué stack usaré en este proyecto de práctica
```

3. Observa: responde con Ollama local, sin créditos.

---

## Paso 3: Cline — crear código (10 min)

1. Abre panel **Cline**
2. Verifica: Provider **Ollama**, Model **qwen-coder-32k**
3. Modo **Plan**, escribe:

```
Crea una página HTML simple "Hola Dev Muscle" con:
- Título h1
- Párrafo de bienvenida en español
- Estilos CSS inline, fondo oscuro
- Guardar como index.html en la raíz del proyecto
```

4. Revisa el plan → **Act** → aprueba cambios
5. Abre `index.html` en el navegador (clic derecho → Open with Live Server o abrir archivo)

**Aprendiste:** Cline crea archivos de forma autónoma con aprobación.

---

## Paso 4: Continue — editar (3 min)

1. Selecciona el `<h1>` en `index.html`
2. En Continue, usa **Edit** (o Ctrl+L con selección):

```
Cambia el título a "Práctica 01 — Sistema Híbrido" y añade un botón "Empezar"
```

**Aprendiste:** Continue edita código existente.

---

## Paso 5: Dev Muscle — orquestar (3 min)

1. Cursor Chat (`Ctrl+L`):

```
@dev-muscle-orchestrator

Acabo de crear index.html con Cline.
¿Debo guardar algún patrón en Rules para futuras páginas HTML de práctica?
```

2. Si propone una Rule, créala en `.cursor/rules/html-practica.mdc`

**Aprendiste:** el orquestador guía memoria y convenciones.

---

## Paso 6: Git — respaldar (2 min)

```powershell
git add .
git commit -m "practica-01: primera pagina con Cline local"
```

---

## Checklist — ¿lo lograste?

- [ ] Continue respondió en chat
- [ ] Cline creó `index.html` en Plan → Act
- [ ] Continue editó el archivo
- [ ] Dev Muscle sugirió o creó una Rule
- [ ] Commit en git

## Siguiente ejercicio

Cuando domines esto, prueba [04-prompts-y-navegacion.md](04-prompts-y-navegacion.md) con una tarea más grande (componente React o endpoint API).
