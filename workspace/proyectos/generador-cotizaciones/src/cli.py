"""CLI: generar cotización desde Excel (o crear plantilla)."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .excel_io import crear_plantilla_excel, leer_excel
from .generar_docx import generar_docx

ROOT = Path(__file__).resolve().parents[1]
SALIDA_DIR = ROOT / "salida"
DATOS_DIR = ROOT / "datos"


def _guardar(data, salida_arg: str | None) -> Path:
    id_proceso = data.cotizacion["id_proceso"].replace("/", "-")
    salida = Path(salida_arg) if salida_arg else SALIDA_DIR / f"COTIZACION-{id_proceso}.docx"
    out = generar_docx(data, salida)
    print(f"Cotización generada: {out}")
    print(
        f"Resumen: {len(data.items)} ítem(s) | "
        f"Neto {data.subtotal_neto:,.0f} | "
        f"IVA {data.iva:,.0f} | "
        f"Bruto {data.total_bruto:,.0f}".replace(",", ".")
    )
    return out


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description=(
            "Genera una Cotización Oficial (DOCX) para Mercado Público "
            "desde un Excel maestro o SQLite."
        )
    )
    sub = p.add_subparsers(dest="comando")

    gen = sub.add_parser("generar", help="Generar DOCX desde Excel")
    gen.add_argument(
        "excel",
        nargs="?",
        default=str(DATOS_DIR / "ejemplo-5178-4975-COT26.xlsx"),
        help="Ruta al Excel de datos",
    )
    gen.add_argument(
        "-o",
        "--salida",
        default=None,
        help="Ruta del DOCX de salida (por defecto salida/COTIZACION-<id>.docx)",
    )

    plant = sub.add_parser("plantilla", help="Crear Excel vacío o de ejemplo")
    plant.add_argument(
        "-o",
        "--salida",
        default=str(DATOS_DIR / "plantilla-datos.xlsx"),
        help="Ruta del Excel a crear",
    )
    plant.add_argument(
        "--ejemplo",
        action="store_true",
        help="Incluir datos de ejemplo (Universidad de Chile / COT26)",
    )

    db = sub.add_parser("desde-db", help="Generar DOCX desde SQLite")
    db.add_argument("sqlite", help="Ruta al archivo .sqlite / .db")
    db.add_argument("id_proceso", help="ID del proceso (ej. 5178-4975-COT26)")
    db.add_argument("-o", "--salida", default=None, help="Ruta DOCX de salida")
    return p


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    # Atajo: si el primer arg es un .xlsx, asumir "generar"
    if argv and argv[0].lower().endswith((".xlsx", ".xlsm")):
        argv = ["generar", *argv]

    parser = build_parser()
    if not argv:
        argv = ["generar"]

    args = parser.parse_args(argv)

    if args.comando == "plantilla":
        path = crear_plantilla_excel(args.salida, ejemplo=args.ejemplo)
        print(f"Plantilla creada: {path}")
        return 0

    if args.comando == "generar":
        excel = Path(args.excel)
        if not excel.exists():
            print(f"No existe el Excel: {excel}", file=sys.stderr)
            print(
                "Crea uno con: python generar_cotizacion.py plantilla --ejemplo",
                file=sys.stderr,
            )
            return 1
        _guardar(leer_excel(excel), args.salida)
        return 0

    if args.comando == "desde-db":
        from .db_io import leer_sqlite

        db_path = Path(args.sqlite)
        if not db_path.exists():
            print(f"No existe la base: {db_path}", file=sys.stderr)
            return 1
        _guardar(leer_sqlite(db_path, args.id_proceso), args.salida)
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
