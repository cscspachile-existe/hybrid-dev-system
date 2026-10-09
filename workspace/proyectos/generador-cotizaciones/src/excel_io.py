"""Lectura y creación del Excel maestro de cotizaciones."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from openpyxl import Workbook, load_workbook

from .formato_clp import parsear_monto


@dataclass
class ItemCotizacion:
    descripcion: str
    cantidad: float
    precio_unitario_neto: float
    item: int | None = None

    @property
    def subtotal_neto(self) -> float:
        return float(self.cantidad) * float(self.precio_unitario_neto)


@dataclass
class CotizacionData:
    emisor: dict[str, str] = field(default_factory=dict)
    cotizacion: dict[str, str] = field(default_factory=dict)
    condiciones: dict[str, str] = field(default_factory=dict)
    items: list[ItemCotizacion] = field(default_factory=list)

    @property
    def iva_pct(self) -> float:
        raw = self.condiciones.get("iva_pct", "19")
        try:
            return float(str(raw).replace("%", "").strip() or 19)
        except ValueError:
            return 19.0

    @property
    def subtotal_neto(self) -> float:
        return sum(i.subtotal_neto for i in self.items)

    @property
    def iva(self) -> float:
        return round(self.subtotal_neto * (self.iva_pct / 100.0))

    @property
    def total_bruto(self) -> float:
        return self.subtotal_neto + self.iva


EMISOR_DEFAULTS = {
    "razon_social": "CSC PRODUCTOS Y SERVICIOS SPA",
    "nombre_fantasia": "CSC SPA",
    "rut": "78.043.456-2",
    "domicilio_legal": "Nueva Central 4142, Conchalí, Región Metropolitana",
    "condicion_proveedor": (
        "Empresa de Menor Tamaño (EMT) – Acreditada y Hábil en Mercado Público"
    ),
    "contacto_comercial": "Info@existe.cl | +56 997284781",
}

CONDICIONES_DEFAULTS = {
    "plazo_entrega": (
        "5 días hábiles contados desde la recepción de la Orden de Compra aceptada."
    ),
    "garantia_tecnica": (
        "12 meses (1 año) con soporte técnico local directo en Conchalí y "
        "reposición inmediata de componentes ante fallas de fabricación."
    ),
    "validez_oferta": "30 días corridos a partir de la fecha de emisión.",
    "forma_pago": (
        "De acuerdo con las políticas de Compras Públicas "
        "(30 días contra recepción conforme y recepción de factura electrónica)."
    ),
    "iva_pct": "19",
}

COTIZACION_KEYS = [
    "id_proceso",
    "titulo_oferta",
    "cliente",
    "unidad_solicitante",
    "responsable_proceso",
    "referencia_proceso",
    "justificacion_tecnica",
    "fecha_emision",
]


def _kv_from_sheet(ws) -> dict[str, str]:
    data: dict[str, str] = {}
    for row in ws.iter_rows(min_row=2, values_only=True):
        if not row or row[0] is None:
            continue
        clave = str(row[0]).strip()
        valor = "" if row[1] is None else str(row[1]).strip()
        data[clave] = valor
    return data


def _write_kv_sheet(ws, titulo_a: str, titulo_b: str, pairs: list[tuple[str, str]]):
    ws["A1"] = titulo_a
    ws["B1"] = titulo_b
    for i, (k, v) in enumerate(pairs, start=2):
        ws[f"A{i}"] = k
        ws[f"B{i}"] = v
    ws.column_dimensions["A"].width = 28
    ws.column_dimensions["B"].width = 90


def leer_excel(path: str | Path) -> CotizacionData:
    """Lee el Excel maestro (hojas Emisor, Cotizacion, Items, Condiciones)."""
    wb = load_workbook(path, data_only=True)
    for hoja in ("Emisor", "Cotizacion", "Items", "Condiciones"):
        if hoja not in wb.sheetnames:
            raise ValueError(f"Falta la hoja '{hoja}' en {path}")

    emisor = {**EMISOR_DEFAULTS, **_kv_from_sheet(wb["Emisor"])}
    cotizacion = _kv_from_sheet(wb["Cotizacion"])
    condiciones = {**CONDICIONES_DEFAULTS, **_kv_from_sheet(wb["Condiciones"])}

    items: list[ItemCotizacion] = []
    ws = wb["Items"]
    headers = [str(c.value).strip().lower() if c.value else "" for c in ws[1]]
    col = {h: i for i, h in enumerate(headers)}
    required = ("descripcion", "cantidad", "precio_unitario_neto")
    for req in required:
        if req not in col:
            raise ValueError(
                "La hoja Items debe tener columnas: item, descripcion, "
                "cantidad, precio_unitario_neto"
            )

    for row in ws.iter_rows(min_row=2, values_only=True):
        if not row or all(c is None or str(c).strip() == "" for c in row):
            continue
        desc = row[col["descripcion"]]
        if desc is None or str(desc).strip() == "":
            continue
        num = None
        if "item" in col and row[col["item"]] not in (None, ""):
            try:
                num = int(row[col["item"]])
            except (TypeError, ValueError):
                num = None
        items.append(
            ItemCotizacion(
                item=num,
                descripcion=str(desc).strip(),
                cantidad=parsear_monto(row[col["cantidad"]]) or 1,
                precio_unitario_neto=parsear_monto(row[col["precio_unitario_neto"]]),
            )
        )

    if not items:
        raise ValueError("La hoja Items no tiene filas de productos.")

    for i, it in enumerate(items, start=1):
        if it.item is None:
            it.item = i

    if not cotizacion.get("id_proceso"):
        raise ValueError("Cotizacion.id_proceso es obligatorio.")
    if not cotizacion.get("cliente"):
        raise ValueError("Cotizacion.cliente es obligatorio.")

    # Valores derivados útiles
    if not cotizacion.get("titulo_oferta"):
        cotizacion["titulo_oferta"] = (
            "Oferta Técnico-Económica para Mercado Público | "
            f"Licitación ID {cotizacion['id_proceso']}"
        )
    if not cotizacion.get("referencia_proceso"):
        cotizacion["referencia_proceso"] = (
            f"Solicitud de Cotización ID {cotizacion['id_proceso']}"
        )

    return CotizacionData(
        emisor=emisor,
        cotizacion=cotizacion,
        condiciones=condiciones,
        items=items,
    )


def crear_plantilla_excel(
    path: str | Path,
    ejemplo: bool = False,
) -> Path:
    """Crea Excel vacío o con el ejemplo Universidad de Chile."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    wb = Workbook()

    # Emisor
    ws = wb.active
    ws.title = "Emisor"
    _write_kv_sheet(
        ws,
        "campo",
        "valor",
        [(k, v) for k, v in EMISOR_DEFAULTS.items()],
    )

    # Cotizacion
    ws = wb.create_sheet("Cotizacion")
    if ejemplo:
        cotiz_vals: dict[str, Any] = {
            "id_proceso": "5178-4975-COT26",
            "titulo_oferta": (
                "Oferta Técnico-Económica para Mercado Público | "
                "Licitación ID 5178-4975-COT26"
            ),
            "cliente": "Universidad de Chile",
            "unidad_solicitante": "Facultad de Medicina.",
            "responsable_proceso": "",
            "referencia_proceso": "Solicitud de Cotización ID 5178-4975-COT26",
            "justificacion_tecnica": (
                "Se sugiere la propuesta técnica con equipos Asus "
                '(modelos Vivobook de 14" y 15.6") frente a opciones como el '
                "HP 240 G10 (Intel Core 7-150U). Aunque ambas alternativas poseen "
                "idéntica memoria (16GB RAM) y capacidad (512GB SSD), la "
                "arquitectura del procesador Intel Core 7 cotizado (Core 7-350) "
                "garantiza una capacidad de cómputo superior para cargas exigentes "
                "mediante sus núcleos de alto desempeño. Asimismo, la serie Asus "
                "Vivobook incluye pantallas con tecnología avanzada, diseño "
                "térmico eficiente y conectividad Wi-Fi 6, asegurando mayor "
                "durabilidad y máxima productividad operativa."
            ),
            "fecha_emision": "2026-10-05",
        }
    else:
        cotiz_vals = {k: "" for k in COTIZACION_KEYS}
        cotiz_vals["id_proceso"] = "XXXX-XXXX-COTXX"
        cotiz_vals["cliente"] = "Nombre del organismo"

    _write_kv_sheet(
        ws,
        "campo",
        "valor",
        [(k, cotiz_vals.get(k, "")) for k in COTIZACION_KEYS],
    )

    # Items
    ws = wb.create_sheet("Items")
    headers = ["item", "descripcion", "cantidad", "precio_unitario_neto"]
    for i, h in enumerate(headers, start=1):
        ws.cell(1, i, h)
    if ejemplo:
        filas = [
            (
                1,
                'Notebook Asus Vivobook 14 (Modelo X1404MA-EB315W) Intel Core 7-350, '
                '14" FHD 60Hz, 16GB RAM, 512GB SSD, Windows 11 Home.',
                1,
                671428,
            ),
            (
                2,
                'Notebook Asus 15.6" FHD Intel Core 7 150U, 16GB DDR5, 512GB SSD, '
                "Windows 11 Home, Color Azul (Quiet Blue)",
                1,
                587394,
            ),
        ]
        for r, fila in enumerate(filas, start=2):
            for c, val in enumerate(fila, start=1):
                ws.cell(r, c, val)
    else:
        ws.cell(2, 1, 1)
        ws.cell(2, 2, "Descripción del producto según bases / ficha técnica")
        ws.cell(2, 3, 1)
        ws.cell(2, 4, 0)
    ws.column_dimensions["A"].width = 8
    ws.column_dimensions["B"].width = 80
    ws.column_dimensions["C"].width = 12
    ws.column_dimensions["D"].width = 22

    # Condiciones
    ws = wb.create_sheet("Condiciones")
    _write_kv_sheet(
        ws,
        "campo",
        "valor",
        [(k, v) for k, v in CONDICIONES_DEFAULTS.items()],
    )

    # Instrucciones
    ws = wb.create_sheet("INSTRUCCIONES")
    ws["A1"] = "Cómo usar este Excel"
    instrucciones = [
        "1. Completa la hoja Cotizacion (id_proceso y cliente son obligatorios).",
        "2. Agrega o edita filas en Items (precio_unitario_neto = neto, sin IVA).",
        "3. Emisor y Condiciones ya vienen con datos CSC; cámbialos solo si aplica.",
        "4. Guarda el archivo y ejecuta: python3 generar_cotizacion.py datos/tu-archivo.xlsx",
        "5. El DOCX sale en carpeta salida/ listo para Mercado Público.",
        "6. No borres los nombres de las hojas ni los nombres de campo (columna A).",
        "7. Subtotales, IVA 19% y total se calculan solos al generar el documento.",
    ]
    for i, linea in enumerate(instrucciones, start=3):
        ws[f"A{i}"] = linea
    ws.column_dimensions["A"].width = 100

    wb.save(path)
    return path
