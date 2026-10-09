"""Lectura de cotización desde SQLite (misma forma que el Excel)."""

from __future__ import annotations

import sqlite3
from pathlib import Path

from .excel_io import (
    CONDICIONES_DEFAULTS,
    EMISOR_DEFAULTS,
    CotizacionData,
    ItemCotizacion,
)


def leer_sqlite(db_path: str | Path, id_proceso: str) -> CotizacionData:
    """Carga una cotización por id_proceso desde schema/cotizaciones.sql."""
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    try:
        cot = conn.execute(
            "SELECT * FROM cotizacion WHERE id_proceso = ?",
            (id_proceso,),
        ).fetchone()
        if cot is None:
            raise ValueError(f"No existe cotización con id_proceso={id_proceso}")

        emisor = dict(EMISOR_DEFAULTS)
        if cot["emisor_id"] is not None:
            row = conn.execute(
                "SELECT * FROM emisor WHERE id = ?",
                (cot["emisor_id"],),
            ).fetchone()
            if row:
                emisor.update(
                    {
                        "razon_social": row["razon_social"],
                        "nombre_fantasia": row["nombre_fantasia"] or "",
                        "rut": row["rut"],
                        "domicilio_legal": row["domicilio_legal"] or "",
                        "condicion_proveedor": row["condicion_proveedor"] or "",
                        "contacto_comercial": row["contacto_comercial"] or "",
                    }
                )

        items_rows = conn.execute(
            "SELECT * FROM cotizacion_item WHERE cotizacion_id = ? ORDER BY item",
            (cot["id"],),
        ).fetchall()
        items = [
            ItemCotizacion(
                item=r["item"],
                descripcion=r["descripcion"],
                cantidad=float(r["cantidad"]),
                precio_unitario_neto=float(r["precio_unitario_neto"]),
            )
            for r in items_rows
        ]
        if not items:
            raise ValueError(f"Cotización {id_proceso} sin ítems.")

        condiciones = dict(CONDICIONES_DEFAULTS)
        for k_db, k_out in (
            ("plazo_entrega", "plazo_entrega"),
            ("garantia_tecnica", "garantia_tecnica"),
            ("validez_oferta", "validez_oferta"),
            ("forma_pago", "forma_pago"),
        ):
            if cot[k_db]:
                condiciones[k_out] = cot[k_db]
        if cot["iva_pct"] is not None:
            condiciones["iva_pct"] = str(cot["iva_pct"])

        cotizacion = {
            "id_proceso": cot["id_proceso"],
            "titulo_oferta": cot["titulo_oferta"] or "",
            "cliente": cot["cliente"],
            "unidad_solicitante": cot["unidad_solicitante"] or "",
            "responsable_proceso": cot["responsable_proceso"] or "",
            "referencia_proceso": cot["referencia_proceso"] or "",
            "justificacion_tecnica": cot["justificacion_tecnica"] or "",
            "fecha_emision": str(cot["fecha_emision"] or ""),
        }
        return CotizacionData(
            emisor=emisor,
            cotizacion=cotizacion,
            condiciones=condiciones,
            items=items,
        )
    finally:
        conn.close()
