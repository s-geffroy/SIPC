"""Les schémas SIPC sont des JSON Schema bien formés et chargeables en registre."""
import json
from pathlib import Path

from jsonschema import Draft202012Validator

import validate_json_files as v

SCHEMA_DIR = Path(__file__).resolve().parents[1] / "schemas"


def test_all_schemas_are_valid_json_schema():
    schemas = sorted(SCHEMA_DIR.glob("*.schema.json"))
    assert schemas, "aucun schéma trouvé"
    for path in schemas:
        schema = json.loads(path.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)


def test_registry_resolves_all_refs():
    registry = v.load_registry()
    root = registry.get_or_retrieve(v.ROOT_SCHEMA_ID).value.contents
    validator = Draft202012Validator(root, registry=registry)
    # Itérer sur un objet vide force la résolution des $ref ; aucune exception réseau attendue.
    list(validator.iter_errors({}))
