# AGENTS.md — generador-cotizaciones

## Qué es
Genera cotizaciones oficiales Mercado Público (DOCX) desde un Excel maestro.
Formato basado en la oferta CSC SPA (secciones 1–5 + tablas emisor/ítems).

## Datos de entrada
- Excel con hojas fijas: `Emisor`, `Cotizacion`, `Items`, `Condiciones`.
- Precios siempre **netos** (sin IVA). IVA 19% se calcula al generar.
- Esquema BD equivalente: `schema/cotizaciones.sql`.

## Comandos
```bash
pip install -r requirements.txt
python3 generar_cotizacion.py plantilla --ejemplo
python3 generar_cotizacion.py datos/ejemplo-5178-4975-COT26.xlsx
```

## No hacer
- No hardcodear precios de una licitación en el código.
- No subir a git DOCX de salida ni el `.docx` original con fuentes embebidas.
- No cambiar nombres de hojas ni claves de columna A sin actualizar `excel_io.py`.
