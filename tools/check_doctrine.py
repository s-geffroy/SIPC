#!/usr/bin/env python3
"""Linter doctrinal SIPC.

Le JSON Schema vérifie la structure ; il ne peut pas garantir la *discipline
analytique* de la SIPC. Ce linter encode les règles doctrinales (synthèse A§10/§14,
ontologie D, plan B§5) que les schémas ne peuvent exprimer :

ERREURS (bloquantes) :
  - un mécanisme dominant doit être présent ;
  - au moins une trajectoire ;
  - au moins une contre-hypothèse dans le profil de preuve ;
  - chaque mécanisme dominant, trajectoire et diagnostic porte >= 1 signal d'invalidation ;
  - intégrité référentielle (ids cohérents entre objets) ;
  - « pas de score sans justification » : un statut probatoire fort exige des preuves.

AVERTISSEMENTS (non bloquants) :
  - plus de 4 mécanismes secondaires (risque d'hypertrophie, A§14) ;
  - confiance élevée alors que le statut probatoire est faible/spéculatif.

Usage:
    python tools/check_doctrine.py examples
    python tools/check_doctrine.py examples/taiwan_strait/situation_analysis.json
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

MAX_SECONDARY_MECHANISMS = 4
STRONG_STATUSES = {"MODERATELY_SUPPORTED", "STRONGLY_SUPPORTED"}
WEAK_STATUSES = {"SPECULATIVE", "WEAKLY_SUPPORTED", "INSUFFICIENT_EVIDENCE"}
HIGH_CONFIDENCE = 0.75


class Report:
    def __init__(self, source: str) -> None:
        self.source = source
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, msg: str) -> None:
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)


def _has_signal(obj: dict, key: str = "invalidation_signals") -> bool:
    return isinstance(obj.get(key), list) and len(obj[key]) > 0


def check_analysis(data: dict, report: Report) -> None:
    situation = data.get("situation", {})
    situation_id = situation.get("situation_id")
    actors = data.get("actors", []) or []
    actor_ids = {a.get("actor_id") for a in actors}

    # --- Mécanisme dominant ---
    dominant = data.get("dominant_mechanism")
    if not dominant:
        report.error("Mécanisme dominant absent (règle SIPC : pas de diagnostic sans mécanisme dominant).")
    elif not _has_signal(dominant):
        report.error("Le mécanisme dominant n'a aucun signal d'invalidation.")

    # --- Mécanismes secondaires : discipline anti-hypertrophie ---
    secondary = data.get("secondary_mechanisms", []) or []
    if len(secondary) > MAX_SECONDARY_MECHANISMS:
        report.warn(
            f"{len(secondary)} mécanismes secondaires (> {MAX_SECONDARY_MECHANISMS}) : "
            "risque d'hypertrophie, hiérarchiser."
        )

    # --- Trajectoires ---
    trajectories = data.get("trajectories", []) or []
    if not trajectories:
        report.error("Aucune trajectoire (>= 1 trajectoire conditionnelle requise).")
    traj_ids = set()
    for traj in trajectories:
        traj_ids.add(traj.get("trajectory_id"))
        if not _has_signal(traj):
            report.error(f"Trajectoire '{traj.get('trajectory_id')}' sans signal d'invalidation.")
        if traj.get("situation_id") != situation_id:
            report.error(
                f"Trajectoire '{traj.get('trajectory_id')}' rattachée à situation "
                f"'{traj.get('situation_id')}' != '{situation_id}'."
            )

    # --- Preuve : contre-hypothèses obligatoires ---
    evidence = data.get("evidence", {}) or {}
    counter = evidence.get("counter_hypotheses", []) or []
    if not counter:
        report.error("Profil de preuve sans contre-hypothèse (>= 1 requise).")
    if not _has_signal(evidence):
        report.error("Profil de preuve sans signal d'invalidation.")

    # --- Pas de score sans justification ---
    if evidence.get("evidence_status") in STRONG_STATUSES and not (evidence.get("evidence_items") or []):
        report.error(
            f"Statut probatoire '{evidence.get('evidence_status')}' revendiqué sans aucun "
            "evidence_item (pas de score sans justification)."
        )

    # --- Diagnostic et intégrité référentielle ---
    diagnostic = data.get("diagnostic", {}) or {}
    if not _has_signal(diagnostic):
        report.error("Diagnostic sans signal d'invalidation.")

    if dominant:
        dom_id = dominant.get("mechanism_id")
        if diagnostic.get("dominant_mechanism_id") != dom_id:
            report.error(
                f"diagnostic.dominant_mechanism_id ('{diagnostic.get('dominant_mechanism_id')}') "
                f"!= dominant_mechanism.mechanism_id ('{dom_id}')."
            )

    dom_traj = diagnostic.get("dominant_trajectory_id")
    if dom_traj and dom_traj not in traj_ids:
        report.error(f"diagnostic.dominant_trajectory_id '{dom_traj}' absent des trajectoires.")

    sec_ids_present = {m.get("mechanism_id") for m in secondary}
    for ref_id in diagnostic.get("secondary_mechanism_ids", []) or []:
        if ref_id not in sec_ids_present:
            report.error(f"diagnostic.secondary_mechanism_ids référence '{ref_id}' absent des mécanismes secondaires.")

    # --- Relations : acteurs référencés existants ---
    for rel in data.get("relations", []) or []:
        for endpoint in ("source_actor_id", "target_actor_id"):
            ref = rel.get(endpoint)
            if ref and ref not in actor_ids:
                report.error(f"Relation '{rel.get('relation_id')}' référence un acteur inconnu : '{ref}'.")

    # --- Confiance vs statut probatoire (avertissement) ---
    diag_conf = diagnostic.get("confidence")
    if isinstance(diag_conf, (int, float)) and diag_conf >= HIGH_CONFIDENCE:
        if diagnostic.get("evidence_status") in WEAK_STATUSES:
            report.warn(
                f"Confiance élevée ({diag_conf}) malgré un statut probatoire faible "
                f"('{diagnostic.get('evidence_status')}')."
            )


def iter_analyses(targets: list[str]) -> list[Path]:
    files: list[Path] = []
    for target in targets:
        path = (ROOT / target) if not Path(target).is_absolute() else Path(target)
        if path.is_dir():
            files.extend(sorted(path.rglob("*.json")))
        elif path.is_file():
            files.append(path)
        else:
            print(f"AVERTISSEMENT: chemin introuvable, ignoré : {target}")
    return files


def main(argv: list[str]) -> int:
    targets = argv or ["examples"]
    total_errors = 0
    total_warnings = 0

    for path in iter_analyses(targets):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        if not (isinstance(data, dict) and "analysis_id" in data and "situation" in data):
            continue

        report = Report(str(path))
        check_analysis(data, report)
        total_errors += len(report.errors)
        total_warnings += len(report.warnings)

        if report.errors or report.warnings:
            print(f"\n{report.source}")
            for msg in report.errors:
                print(f"  ERROR : {msg}")
            for msg in report.warnings:
                print(f"  WARN  : {msg}")
        else:
            print(f"\n{report.source}\n  OK : conforme à la doctrine SIPC.")

    print(f"\nTotal : {total_errors} erreur(s), {total_warnings} avertissement(s).")
    return 1 if total_errors else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
