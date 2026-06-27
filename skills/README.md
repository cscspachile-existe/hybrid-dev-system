# Instalar skills en Cursor

Copia la carpeta `skills/` a tu perfil de Cursor:

```powershell
Copy-Item -Recurse C:\Users\claud\dev-projects\hybrid-dev-system\skills\* `
  C:\Users\claud\.cursor\skills\ -Force
```

O instala solo el orquestador:

```powershell
Copy-Item -Recurse C:\Users\claud\dev-projects\hybrid-dev-system\skills\dev-muscle-orchestrator `
  C:\Users\claud\.cursor\skills\ -Force
```

Invocar en Cursor Chat: `@dev-muscle-orchestrator`
