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
