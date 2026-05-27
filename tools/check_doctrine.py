#!/usr/bin/env python3
"""Linter doctrinal SIPC — modèle de conformité gradué.

Le JSON Schema vérifie la structure ; ce linter encode la *discipline analytique* que
les schémas ne peuvent exprimer. Les règles sont graduées selon ``analytical_status`` :

- ``DRAFT`` : les règles de base sont émises en AVERTISSEMENT (non bloquant).
- ``REVIEW_REQUIRED`` : règles de base en ERREUR (mécanisme dominant, contre-hypothèse,
  signaux d'invalidation, intégrité référentielle, cohérence de calibration).
- ``VALIDATED`` : règles de base + règles strictes V2 (ACH renseignée et cohérente, sources
  gradées et reliées, suivi des signaux d'invalidation).

Usage:
    python tools/check_doctrine.py examples
    python tools/check_doctrine.py examples/taiwan_strait/situation_analysis.json
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from sipc_rules import BAND_RANGES, band_contains, is_analysis

ROOT = Path(__file__).resolve().parents[1]

MAX_SECONDARY_MECHANISMS = 4
STRONG_STATUSES = {"MODERATELY_SUPPORTED", "STRONGLY_SUPPORTED"}
WEAK_STATUSES = {"SPECULATIVE", "WEAKLY_SUPPORTED", "INSUFFICIENT_EVIDENCE"}
HIGH_CONFIDENCE = 0.75
HIGH_STRENGTH = 0.7
LOW_RELIABILITY_GRADES = {"E", "F"}


class Report:
    def __init__(self, source: str) -> None:
        self.source = source
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, msg: str) -> None:
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)

    def emit(self, msg: str, *, blocking: bool) -> None:
        """Émet en ERREUR si bloquant, sinon en AVERTISSEMENT (utilisé pour le tier DRAFT)."""
        (self.error if blocking else self.warn)(msg)


def _has_signal(obj: dict, key: str = "invalidation_signals") -> bool:
    return isinstance(obj.get(key), list) and len(obj[key]) > 0


def _all_signals(data: dict) -> list[dict]:
    """Tous les signaux d'invalidation portés par l'analyse."""
    signals: list[dict] = []
    dom = data.get("dominant_mechanism") or {}
    signals += dom.get("invalidation_signals", []) or []
    for traj in data.get("trajectories", []) or []:
        signals += traj.get("invalidation_signals", []) or []
    signals += (data.get("evidence") or {}).get("invalidation_signals", []) or []
    signals += (data.get("diagnostic") or {}).get("invalidation_signals", []) or []
    return signals


# --------------------------------------------------------------------------- base

def check_base(data: dict, report: Report, *, blocking: bool) -> None:
    """Règles doctrinales de base (tiers REVIEW_REQUIRED et VALIDATED en bloquant)."""
    situation = data.get("situation", {})
    situation_id = situation.get("situation_id")
    actor_ids = {a.get("actor_id") for a in (data.get("actors", []) or [])}

    dominant = data.get("dominant_mechanism")
    if not dominant:
        report.emit("Mécanisme dominant absent (pas de diagnostic sans mécanisme dominant).", blocking=blocking)
    elif not _has_signal(dominant):
        report.emit("Le mécanisme dominant n'a aucun signal d'invalidation.", blocking=blocking)

    secondary = data.get("secondary_mechanisms", []) or []
    if len(secondary) > MAX_SECONDARY_MECHANISMS:
        report.warn(
            f"{len(secondary)} mécanismes secondaires (> {MAX_SECONDARY_MECHANISMS}) : "
            "risque d'hypertrophie, hiérarchiser."
        )

    trajectories = data.get("trajectories", []) or []
    if not trajectories:
        report.emit("Aucune trajectoire (>= 1 trajectoire conditionnelle requise).", blocking=blocking)
    traj_ids = set()
    for traj in trajectories:
        traj_ids.add(traj.get("trajectory_id"))
        if not _has_signal(traj):
            report.emit(f"Trajectoire '{traj.get('trajectory_id')}' sans signal d'invalidation.", blocking=blocking)
        if traj.get("situation_id") != situation_id:
            report.emit(
                f"Trajectoire '{traj.get('trajectory_id')}' rattachée à situation "
                f"'{traj.get('situation_id')}' != '{situation_id}'.",
                blocking=blocking,
            )
        # Calibration : un estimé numérique doit respecter sa bande probabiliste.
        est = traj.get("numeric_estimate")
        band = traj.get("probability_band")
        if isinstance(est, (int, float)) and not band_contains(band, est):
            low, high = BAND_RANGES.get(band, (None, None))
            report.emit(
                f"Trajectoire '{traj.get('trajectory_id')}' : numeric_estimate {est} hors de la "
                f"bande '{band}' ([{low}, {high}]).",
                blocking=blocking,
            )

    evidence = data.get("evidence", {}) or {}
    if not (evidence.get("counter_hypotheses") or []):
        report.emit("Profil de preuve sans contre-hypothèse (>= 1 requise).", blocking=blocking)
    if not _has_signal(evidence):
        report.emit("Profil de preuve sans signal d'invalidation.", blocking=blocking)
    if evidence.get("evidence_status") in STRONG_STATUSES and not (evidence.get("evidence_items") or []):
        report.emit(
            f"Statut probatoire '{evidence.get('evidence_status')}' revendiqué sans evidence_item "
            "(pas de score sans justification).",
            blocking=blocking,
        )

    diagnostic = data.get("diagnostic", {}) or {}
    if not _has_signal(diagnostic):
        report.emit("Diagnostic sans signal d'invalidation.", blocking=blocking)

    if dominant:
        dom_id = dominant.get("mechanism_id")
        if diagnostic.get("dominant_mechanism_id") != dom_id:
            report.emit(
                f"diagnostic.dominant_mechanism_id ('{diagnostic.get('dominant_mechanism_id')}') "
                f"!= dominant_mechanism.mechanism_id ('{dom_id}').",
                blocking=blocking,
            )

    dom_traj = diagnostic.get("dominant_trajectory_id")
    if dom_traj and dom_traj not in traj_ids:
        report.emit(f"diagnostic.dominant_trajectory_id '{dom_traj}' absent des trajectoires.", blocking=blocking)

    sec_ids_present = {m.get("mechanism_id") for m in secondary}
    for ref_id in diagnostic.get("secondary_mechanism_ids", []) or []:
        if ref_id not in sec_ids_present:
            report.emit(
                f"diagnostic.secondary_mechanism_ids référence '{ref_id}' absent des mécanismes secondaires.",
                blocking=blocking,
            )

    for rel in data.get("relations", []) or []:
        for endpoint in ("source_actor_id", "target_actor_id"):
            ref = rel.get(endpoint)
            if ref and ref not in actor_ids:
                report.emit(f"Relation '{rel.get('relation_id')}' référence un acteur inconnu : '{ref}'.", blocking=blocking)

    # Cohérence calibration : confiance du diagnostic vs son label.
    diag_conf = diagnostic.get("confidence")
    diag_label = diagnostic.get("confidence_label")
    if isinstance(diag_conf, (int, float)) and diag_label and not band_contains(diag_label, diag_conf):
        low, high = BAND_RANGES.get(diag_label, (None, None))
        report.emit(
            f"diagnostic.confidence {diag_conf} incohérent avec confidence_label '{diag_label}' "
            f"([{low}, {high}]).",
            blocking=blocking,
        )


# ---------------------------------------------------------------------- validated

def check_validated(data: dict, report: Report) -> None:
    """Règles strictes V2, exigées uniquement au tier VALIDATED."""
    evidence = data.get("evidence", {}) or {}
    diagnostic = data.get("diagnostic", {}) or {}

    # --- Axe 1 : confiance élevée + statut faible devient bloquant.
    if isinstance(diagnostic.get("confidence"), (int, float)) and diagnostic["confidence"] >= HIGH_CONFIDENCE:
        if diagnostic.get("evidence_status") in WEAK_STATUSES:
            report.error(
                f"Confiance élevée ({diagnostic['confidence']}) incompatible avec un statut "
                f"probatoire faible ('{diagnostic.get('evidence_status')}')."
            )

    # --- Axe 2 : ACH renseignée et cohérente.
    hypotheses = evidence.get("hypotheses", []) or []
    items = evidence.get("evidence_items", []) or []
    if len(hypotheses) < 2:
        report.error("ACH absente : au moins deux hypothèses concurrentes sont requises (evidence.hypotheses).")
    if not any(i.get("diagnosticity") == "HIGH" for i in items):
        report.error("ACH faible : aucune preuve à diagnosticité HIGH (preuve discriminante manquante).")
    if not (evidence.get("key_assumptions") or []):
        report.error("Key Assumptions Check absent (evidence.key_assumptions vide).")

    if hypotheses:
        # Logique d'élimination de Heuer : l'hypothèse dominante doit être la MOINS infirmée.
        inconsistent = {h.get("hypothesis_id"): 0 for h in hypotheses}
        for item in items:
            for c in item.get("consistency", []) or []:
                hid = c.get("hypothesis_id")
                if hid in inconsistent and c.get("consistency") == "INCONSISTENT":
                    inconsistent[hid] += 1
        leads = [h.get("hypothesis_id") for h in hypotheses if h.get("is_lead")]
        if leads:
            min_inconsistent = min(inconsistent.values())
            for lead in leads:
                if inconsistent.get(lead, 0) > min_inconsistent:
                    report.error(
                        f"Incohérence ACH : l'hypothèse dominante '{lead}' n'est pas la moins infirmée "
                        f"({inconsistent.get(lead)} preuves inconsistantes contre un minimum de {min_inconsistent})."
                    )

    # --- Axe 3 : sources gradées et reliées (source != preuve).
    source_ids = {s.get("source_id") for s in (data.get("sources", []) or [])}
    reliability_by_id = {s.get("source_id"): s.get("reliability") for s in (data.get("sources", []) or [])}
    for item in items:
        refs = item.get("source_ids", []) or []
        if not refs:
            report.error(f"Preuve '{item.get('evidence_id')}' sans source (source != preuve).")
        for ref in refs:
            if ref not in source_ids:
                report.error(f"Preuve '{item.get('evidence_id')}' référence une source inconnue : '{ref}'.")
            elif reliability_by_id.get(ref) in LOW_RELIABILITY_GRADES and (item.get("strength") or 0) >= HIGH_STRENGTH:
                report.warn(
                    f"Preuve '{item.get('evidence_id')}' de forte intensité repose sur une source peu "
                    f"fiable (reliability '{reliability_by_id.get(ref)}')."
                )

    # --- Axe 4 : suivi des signaux d'invalidation.
    for sig in _all_signals(data):
        if not (sig.get("monitoring_indicators") or []):
            report.error(
                f"Signal d'invalidation sans indicateur de suivi : '{sig.get('signal')}' "
                "(monitoring_indicators requis au tier VALIDATED)."
            )

    # Cohérence chronologique de l'historique de révision.
    dates = [r.get("date") for r in (data.get("revision_history", []) or []) if r.get("date")]
    if dates != sorted(dates):
        report.warn("revision_history : les dates ne sont pas ordonnées chronologiquement.")


def check_analysis(data: dict, report: Report) -> None:
    """Applique les règles selon le tier déduit de ``analytical_status``."""
    tier = data.get("analytical_status", "DRAFT")
    blocking = tier in {"REVIEW_REQUIRED", "VALIDATED", "CONTESTED"}
    check_base(data, report, blocking=blocking)
    if tier == "VALIDATED":
        check_validated(data, report)


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
        if not is_analysis(data):
            continue

        report = Report(str(path))
        check_analysis(data, report)
        total_errors += len(report.errors)
        total_warnings += len(report.warnings)

        tier = data.get("analytical_status", "DRAFT")
        if report.errors or report.warnings:
            print(f"\n{report.source}  [tier {tier}]")
            for msg in report.errors:
                print(f"  ERROR : {msg}")
            for msg in report.warnings:
                print(f"  WARN  : {msg}")
        else:
            print(f"\n{report.source}  [tier {tier}]\n  OK : conforme à la doctrine SIPC.")

    print(f"\nTotal : {total_errors} erreur(s), {total_warnings} avertissement(s).")
    return 1 if total_errors else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
