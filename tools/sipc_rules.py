"""Constantes et helpers partagés par l'outillage SIPC.

Centralise la calibration probabiliste (échelle estimative ancrée) et les helpers
réutilisés par le validateur, le linter doctrinal, le rendu ACH et le backtesting.
"""
from __future__ import annotations

# Échelle estimative ancrée : mot -> plage numérique [min, max] inclusive.
# Inspirée des « Words of Estimative Probability » des standards d'analyse.
BAND_RANGES: dict[str, tuple[float, float]] = {
    "LOW": (0.05, 0.20),
    "MEDIUM_LOW": (0.20, 0.40),
    "MEDIUM": (0.40, 0.60),
    "MEDIUM_HIGH": (0.60, 0.80),
    "HIGH": (0.80, 0.95),
}

# Tolérance sur les bornes (les plages se touchent ; on accepte la valeur frontière).
BAND_TOLERANCE = 1e-9


def band_contains(band: str, value: float) -> bool:
    """Vrai si `value` tombe dans la plage du `band` (UNKNOWN accepte tout)."""
    if band == "UNKNOWN" or band not in BAND_RANGES:
        return True
    low, high = BAND_RANGES[band]
    return (low - BAND_TOLERANCE) <= value <= (high + BAND_TOLERANCE)


def band_midpoint(band: str) -> float | None:
    """Point médian d'une bande probabiliste, pour le backtesting (None si inconnu)."""
    if band not in BAND_RANGES:
        return None
    low, high = BAND_RANGES[band]
    return (low + high) / 2.0


def is_analysis(data: object) -> bool:
    """Vrai si l'objet ressemble à un `situation_analysis`."""
    return isinstance(data, dict) and "analysis_id" in data and "situation" in data
