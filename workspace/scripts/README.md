# scripts/

Scripts de automatización reutilizables (setup, deploy, backup, utilidades).

## Convención

- `setup-*.ps1` — instalación / configuración
- `backup-*.ps1` — respaldos
- `util-*.py` — utilidades puntuales

Los scripts del **sistema híbrido** viven también en `../../scripts/` (raíz del repo).

## Ejecutar

```powershell
powershell -ExecutionPolicy Bypass -File .\mi-script.ps1
```
