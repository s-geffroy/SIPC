"""Tests des outils SIPC : rendu ACH et backtesting (score de Brier)."""
import json
from pathlib import Path

import render_ach
import score_backtest
from sipc_rules import band_contains, band_midpoint

ROOT = Path(__file__).resolve().parents[1]
GOLD = ROOT / "examples" / "taiwan_strait" / "situation_analysis.json"


def test_render_ach_matrix():
    data = json.loads(GOLD.read_text(encoding="utf-8"))
    out = render_ach.render(data)
    assert "Matrice ACH" in out
    # L'hypothèse dominante (reconnaissance) doit être marquée comme telle.
    assert "← hypothèse dominante" in out
    assert "Conflit de reconnaissance dominant" in out


def test_brier_known_value():
    rows = [("t1", 0.8, 1.0), ("t2", 0.3, 0.0)]
    # ((0.8-1)^2 + (0.3-0)^2) / 2 = (0.04 + 0.09) / 2 = 0.065
    assert abs(score_backtest.brier(rows) - 0.065) < 1e-9


def test_brier_empty_is_none():
    assert score_backtest.brier([]) is None


def test_band_helpers():
    assert band_contains("MEDIUM", 0.5)
    assert not band_contains("LOW", 0.9)
    assert band_contains("UNKNOWN", 0.99)  # UNKNOWN accepte tout
    assert band_midpoint("HIGH") == 0.875
    assert band_midpoint("UNKNOWN") is None
