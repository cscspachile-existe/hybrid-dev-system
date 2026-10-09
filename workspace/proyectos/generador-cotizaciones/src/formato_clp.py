"""Formato de montos en pesos chilenos (CLP)."""

from __future__ import annotations


def formatear_clp(monto: float | int, con_sufijo: bool = True) -> str:
    """Formatea 1258822 -> '$1.258.822 CLP' (punto como miles)."""
    valor = int(round(float(monto)))
    negativo = valor < 0
    valor = abs(valor)
    texto = f"{valor:,}".replace(",", ".")
    if negativo:
        texto = f"-{texto}"
    if con_sufijo:
        return f"${texto} CLP"
    return f"${texto}"


def parsear_monto(valor) -> float:
    """Acepta número o texto tipo '$671.428 CLP' / '671428'."""
    if valor is None or valor == "":
        return 0.0
    if isinstance(valor, (int, float)):
        return float(valor)
    texto = str(valor).strip().upper()
    for token in ("CLP", "$", " "):
        texto = texto.replace(token, "")
    texto = texto.replace(".", "").replace(",", ".")
    if not texto:
        return 0.0
    return float(texto)
