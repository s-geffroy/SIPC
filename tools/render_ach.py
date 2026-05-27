#!/usr/bin/env python3
"""Rend la matrice ACH (Analyse des Hypothèses Concurrentes) d'une analyse SIPC.

Produit un tableau Markdown hypothèses × preuves, avec le décompte des preuves
inconsistantes par hypothèse (logique d'élimination de Heuer : retenir l'hypothèse la
moins infirmée, non la plus confirmée).

Usage:
    python tools/render_ach.py examples/taiwan_strait/situation_analysis.json
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

SYMBOLS = {"CONSISTENT": "+", "INCONSISTENT": "−", "NEUTRAL": "·"}


def render(data: dict) -> str:
    evidence = data.get("evidence", {}) or {}
    hypotheses = evidence.get("hypotheses", []) or []
    items = evidence.get("evidence_items", []) or []
    if not hypotheses:
        return "_Aucune hypothèse ACH renseignée dans cette analyse._"

    hyp_ids = [h.get("hypothesis_id") for h in hypotheses]
    labels = {h.get("hypothesis_id"): h.get("label", h.get("hypothesis_id")) for h in hypotheses}
    leads = {h.get("hypothesis_id") for h in hypotheses if h.get("is_lead")}

    lines: list[str] = ["# Matrice ACH", ""]
    lines.append("Légende : `+` consistant, `−` inconsistant, `·` neutre. "
                 "Diag. = diagnosticité de la preuve.")
    lines.append("")

    header = "| Preuve | Diag. | " + " | ".join(labels[h] for h in hyp_ids) + " |"
    sep = "|---|---|" + "---|" * len(hyp_ids)
    lines.append(header)
    lines.append(sep)

    inconsistent = {h: 0 for h in hyp_ids}
    for item in items:
        cmap = {c.get("hypothesis_id"): c.get("consistency") for c in item.get("consistency", []) or []}
        cells = []
        for h in hyp_ids:
            c = cmap.get(h, "NEUTRAL")
            if c == "INCONSISTENT":
                inconsistent[h] += 1
            cells.append(SYMBOLS.get(c, "·"))
        diag = item.get("diagnosticity", "—")
        lines.append(f"| {item.get('evidence_id')} | {diag} | " + " | ".join(cells) + " |")

    lines.append("")
    lines.append("## Décompte des preuves inconsistantes (plus c'est bas, mieux c'est)")
    lines.append("")
    for h in sorted(hyp_ids, key=lambda x: inconsistent[x]):
        mark = " ← hypothèse dominante" if h in leads else ""
        lines.append(f"- **{labels[h]}** : {inconsistent[h]} inconsistance(s){mark}")

    return "\n".join(lines) + "\n"


def main(argv: list[str]) -> int:
    if not argv:
        print("Usage: python tools/render_ach.py <situation_analysis.json>")
        return 2
    data = json.loads(Path(argv[0]).read_text(encoding="utf-8"))
    print(render(data))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
