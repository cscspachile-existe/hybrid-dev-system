# Generador de Cotizaciones (Mercado Público)

Arma cotizaciones oficiales CSC SPA en **DOCX** cambiando solo un **Excel**.  
Formato alineado a tu plantilla `5178-4975-COT26.docx` (Oferta Técnico-Económica).

## Recomendación (especialista licitaciones)

| Opción | Cuándo usarla | Pros | Contras |
|--------|---------------|------|---------|
| **A. Excel → DOCX (esta)** | Hoy, 1–20 cotizaciones/semana | Rápido, sin BD, mismo formato cada vez | Hay que abrir Excel |
| **B. Google Sheet → DOCX** | Editas en el celular/Drive | Colaborativo | Hay que bajar a `.xlsx` o conectar API |
| **C. Base de datos → DOCX** | Catálogo + muchas OC | Una sola fuente de verdad | Requiere carga de productos |

**Empieza por A.** Cuando el catálogo esté estable, migra a C con el SQL de `schema/`.

## Estructura del Excel

| Hoja | Qué editas |
|------|------------|
| `Cotizacion` | ID proceso, cliente, unidad, justificación técnica |
| `Items` | Descripción, cantidad, **precio unitario neto** |
| `Emisor` | Datos CSC (casi nunca cambia) |
| `Condiciones` | Plazo, garantía, validez, pago, IVA % |
| `INSTRUCCIONES` | Ayuda — no borres las otras hojas |

El script calcula solo: subtotal neto, IVA y total bruto.

## Uso rápido

```bash
cd workspace/proyectos/generador-cotizaciones
pip install -r requirements.txt   # o: pip3 install -r requirements.txt

# Usa python3 (Linux/Cloud Agent). En Windows: py o python.
# 1) Crear Excel de ejemplo (Universidad de Chile / COT26)
python3 generar_cotizacion.py plantilla --ejemplo -o datos/ejemplo-5178-4975-COT26.xlsx

# 2) Crear Excel vacío para una cotización nueva
python3 generar_cotizacion.py plantilla -o datos/nueva-cotizacion.xlsx

# 3) Generar el DOCX
python3 generar_cotizacion.py datos/ejemplo-5178-4975-COT26.xlsx

# 4) (Opcional) Desde SQLite
# sqlite3 datos/cotizaciones.db < schema/cotizaciones.sql
# python3 generar_cotizacion.py desde-db datos/cotizaciones.db 5178-4975-COT26
```

Salida: `salida/COTIZACION-<id_proceso>.docx`

## Flujo de trabajo en licitaciones

1. Abre la cotización en Mercado Público y anota el **ID** (ej. `5178-4975-COT26`).
2. Copia `plantilla-datos.xlsx` → `datos/<ID>.xlsx`.
3. Completa cliente, ítems y justificación técnica (matriz de cumplimiento).
4. Genera el DOCX y súbelo / adjúntalo al proceso.
5. No edites el DOCX a mano salvo detalle tipográfico: **la fuente de verdad es el Excel**.

## Alternativa desde base de datos

1. Crea tablas con `schema/cotizaciones.sql` (SQLite o Postgres).
2. Carga emisor + cotización + ítems.
3. Exporta a Excel con las mismas hojas **o** (próximo paso) agrega un lector SQL en `src/` que reutilice `generar_docx.py`.

El DOCX no cambia: solo cambia de dónde salen los datos.

## Google Sheet de apoyo (ítems)

Hoja de ejemplo de ítems (puedes copiar filas y pegarlas en el Excel local):  
https://docs.google.com/spreadsheets/d/1PnxNow-S8DGwmasO6OjnW-brSzRQ199YUGVa3y5WCk0/edit

Para generar el DOCX oficial sigue usando el **Excel completo** (`Emisor` + `Cotizacion` + `Items` + `Condiciones`) en esta carpeta.

## OCRV de esta herramienta

- **Objetivo:** generar cotización DOCX sin reescribir el formato.
- **Contexto:** CSC SPA / Mercado Público / plantilla secciones 1–5.
- **Restricción:** precios netos en Excel; IVA configurable (default 19%).
- **Validación:** abrir el DOCX y verificar ID, ítems, subtotal, IVA y total.
