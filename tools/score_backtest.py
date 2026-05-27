#!/usr/bin/env python3
"""Backtesting des trajectoires SIPC : score de Brier.

Pour chaque trajectoire dont l'``outcome.status`` est REALIZED ou NOT_REALIZED, on
compare la probabilité prévue (``numeric_estimate`` ou point médian de ``probability_band``)
au résultat observé (1 si REALIZED, 0 sinon). Le score de Brier moyen mesure la
calibration : 0 = parfait, 0.25 = équivalent au hasard sur une prévision à 50 %.

Usage:
    python tools/score_backtest.py examples
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from sipc_rules import band_midpoint, is_analysis

ROOT = Path(__file__).resolve().parents[1]
SCORED_STATUSES = {"REALIZED": 1.0, "NOT_REALIZED": 0.0}


def predicted_probability(traj: dict) -> float | None:
    est = traj.get("numeric_estimate")
    if isinstance(est, (int, float)):
        return float(est)
    return band_midpoint(traj.get("probability_band"))


def collect(targets: list[str]) -> list[tuple[str, float, float]]:
    """Retourne (trajectory_id, probabilité prévue, résultat observé) scorables."""
    rows: list[tuple[str, float, float]] = []
    for target in targets:
        path = (ROOT / target) if not Path(target).is_absolute() else Path(target)
        files = sorted(path.rglob("*.json")) if path.is_dir() else [path]
        for f in files:
            try:
                data = json.loads(f.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                continue
            if not is_analysis(data):
                continue
            for traj in data.get("trajectories", []) or []:
                outcome = traj.get("outcome") or {}
                if outcome.get("status") in SCORED_STATUSES:
                    p = predicted_probability(traj)
                    if p is not None:
                        rows.append((traj.get("trajectory_id"), p, SCORED_STATUSES[outcome["status"]]))
    return rows


def brier(rows: list[tuple[str, float, float]]) -> float | None:
    if not rows:
        return None
    return sum((p - o) ** 2 for _, p, o in rows) / len(rows)


def main(argv: list[str]) -> int:
    targets = argv or ["examples"]
    rows = collect(targets)
    if not rows:
        print("Aucune trajectoire avec résultat observé (outcome REALIZED/NOT_REALIZED) à scorer.")
        return 0
    for tid, p, o in rows:
        print(f"  {tid}: prévu={p:.2f}  observé={o:.0f}  (Brier={ (p-o)**2 :.3f})")
    print(f"\nScore de Brier moyen sur {len(rows)} trajectoire(s) : {brier(rows):.4f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
