#!/usr/bin/env python3
"""Génère un résumé Markdown exécutif à partir d'un ``situation_analysis.json``.

Sert à produire/rafraîchir les pages ``examples/<cas>/analysis.md`` à partir de
l'objet JSON, en garantissant que la prose reste cohérente avec les données.

Usage:
    python tools/render_summary.py examples/taiwan_strait/situation_analysis.json
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import render_ach


def render(data: dict) -> str:
    situation = data.get("situation", {})
    diagnostic = data.get("diagnostic", {})
    dominant = data.get("dominant_mechanism", {})
    lines: list[str] = []

    lines.append(f"# {situation.get('name', data.get('analysis_id', 'Analyse SIPC'))}")
    lines.append("")
    lines.append(f"- **Portée géographique** : {situation.get('scope', {}).get('geographic', '—')}")
    lines.append(f"- **Type de situation** : {', '.join(situation.get('situation_type', []))}")
    lines.append(f"- **Phase actuelle** : {situation.get('current_phase', '—')}")
    lines.append("")

    lines.append("## Diagnostic exécutif")
    lines.append("")
    lines.append(diagnostic.get("executive_summary", "—"))
    lines.append("")

    lines.append("## Mécanisme dominant")
    lines.append("")
    lines.append(f"**{dominant.get('name', '—')}** (`{dominant.get('mechanism_type', '—')}`) — "
                 f"{dominant.get('minimal_definition', '')}")
    lines.append("")

    lines.append("## Trajectoires")
    lines.append("")
    for traj in data.get("trajectories", []):
        lines.append(f"- **{traj.get('name', '—')}** (`{traj.get('trajectory_type', '—')}`, "
                     f"probabilité {traj.get('probability_band', '—')}) — {traj.get('mechanism_path', '')}")
    lines.append("")

    lines.append("## Risque principal et signaux à surveiller")
    lines.append("")
    lines.append(f"**Risque** : {diagnostic.get('main_risk', '—')}")
    lines.append("")
    for sig in diagnostic.get("main_watch_signals", []):
        lines.append(f"- {sig}")
    lines.append("")

    lines.append(f"> **Confiance** : {diagnostic.get('confidence_label', '—')} "
                 f"({diagnostic.get('confidence', '—')}) · "
                 f"**Statut probatoire** : `{diagnostic.get('evidence_status', '—')}`")
    lines.append("")

    evidence = data.get("evidence", {}) or {}
    if evidence.get("hypotheses"):
        ach = render_ach.render(data).replace("# Matrice ACH", "## Matrice ACH", 1)
        lines.append(ach)
        if evidence.get("key_assumptions"):
            lines.append("## Hypothèses clés (Key Assumptions Check)")
            lines.append("")
            for ka in evidence["key_assumptions"]:
                lines.append(f"- **{ka.get('assumption')}** — `{ka.get('status')}` : {ka.get('impact_if_wrong')}")
            lines.append("")

    return "\n".join(lines)


def main(argv: list[str]) -> int:
    if not argv:
        print("Usage: python tools/render_summary.py <situation_analysis.json>")
        return 2
    data = json.loads(Path(argv[0]).read_text(encoding="utf-8"))
    print(render(data))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
