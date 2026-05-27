"""Le linter doctrinal accepte les exemples conformes et rejette les fautifs."""
import json
from pathlib import Path

import pytest

import check_doctrine as cd

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = sorted((ROOT / "examples").rglob("situation_analysis.json"))


def _errors_for(path: Path) -> list[str]:
    data = json.loads(path.read_text(encoding="utf-8"))
    report = cd.Report(str(path))
    cd.check_analysis(data, report)
    return report.errors


@pytest.mark.parametrize("path", EXAMPLES, ids=lambda p: p.parent.name)
def test_examples_pass_doctrine(path):
    assert _errors_for(path) == []


def test_broken_fixture_is_rejected():
    """Test négatif : une analyse au mécanisme dominant incohérent doit être rejetée."""
    fixture = ROOT / "tests" / "fixtures" / "broken_analysis.json"
    errors = _errors_for(fixture)
    assert errors, "le linter aurait dû signaler des erreurs sur la fixture fautive"
    joined = " | ".join(errors)
    assert "dominant_mechanism_id" in joined or "contre-hypothèse" in joined


# --- Règles V2 testées par mutation de l'exemple gold standard (Taïwan, VALIDATED) ---

import copy

import pytest

GOLD = ROOT / "examples" / "taiwan_strait" / "situation_analysis.json"


def _errors_for_data(data: dict) -> list[str]:
    report = cd.Report("mutated")
    cd.check_analysis(data, report)
    return report.errors


def _gold() -> dict:
    return copy.deepcopy(json.loads(GOLD.read_text(encoding="utf-8")))


def test_calibration_out_of_band_rejected():
    data = _gold()
    data["trajectories"][0]["numeric_estimate"] = 0.05  # incohérent avec MEDIUM_HIGH
    assert any("numeric_estimate" in e for e in _errors_for_data(data))


def test_validated_without_sources_rejected():
    data = _gold()
    data["sources"] = []
    assert any("source" in e.lower() for e in _errors_for_data(data))


def test_ach_incoherent_lead_rejected():
    data = _gold()
    # Désigner comme dominante l'hypothèse la plus infirmée.
    for h in data["evidence"]["hypotheses"]:
        h["is_lead"] = (h["hypothesis_id"] == "HYP_TECH_DEPENDENCY")
    assert any("ACH" in e for e in _errors_for_data(data))


def test_validated_missing_monitoring_indicators_rejected():
    data = _gold()
    data["dominant_mechanism"]["invalidation_signals"][0]["monitoring_indicators"] = []
    assert any("suivi" in e.lower() or "monitoring" in e.lower() for e in _errors_for_data(data))
