"""Chaque exemple valide contre le schéma racine ``situation_analysis``."""
import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator

import validate_json_files as v

EXAMPLES = sorted((Path(__file__).resolve().parents[1] / "examples").rglob("situation_analysis.json"))


def test_examples_exist():
    assert len(EXAMPLES) == 3, "trois exemples attendus"


@pytest.mark.parametrize("path", EXAMPLES, ids=lambda p: p.parent.name)
def test_example_validates_against_schema(path):
    registry = v.load_registry()
    root = registry.get_or_retrieve(v.ROOT_SCHEMA_ID).value.contents
    validator = Draft202012Validator(root, registry=registry)
    data = json.loads(path.read_text(encoding="utf-8"))
    errors = sorted(validator.iter_errors(data), key=lambda e: e.path)
    assert not errors, "\n".join(f"{list(e.absolute_path)}: {e.message}" for e in errors)
