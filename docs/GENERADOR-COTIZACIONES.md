# Generador de cotizaciones Mercado Público

Proyecto: `workspace/proyectos/generador-cotizaciones/`

## Problema
El formato de cotización oficial vive en un `.docx`. Cambiar cliente, ítems y precios a mano en Word es lento y propenso a errores (totales, IVA, ID de proceso).

## Solución elegida
**Excel maestro → script Python → DOCX** (misma estructura de la plantilla CSC: secciones 1–5).

Alternativa ya cableada: **SQLite → DOCX** (`python generar_cotizacion.py desde-db archivo.db ID-PROCESO`) usando `schema/cotizaciones.sql`.

## Por qué no solo Google Docs
Docs es bueno para el formato visual final, malo como fuente de datos (ítems variables, cálculos). El Excel/BD guarda datos; el generador arma el documento.

## Referencia de formato
Documento de ejemplo: cotización `5178-4975-COT26` (Universidad de Chile / Facultad de Medicina).
