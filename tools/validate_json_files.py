#!/usr/bin/env python3
"""Validation JSON Schema des analyses SIPC.

Contrairement à la V1 source (qui ne vérifiait que la syntaxe JSON et ignorait
ses arguments), ce script :

1. accepte des chemins en argument (fichiers ou dossiers) ;
2. construit un registre local de TOUS les schémas (résolution hors-ligne des
   ``$ref`` inter-fichiers, aucun accès réseau) ;
3. valide chaque ``*.json`` qui ressemble à une analyse (clé ``analysis_id``)
   contre ``situation_analysis.schema.json`` ;
4. vérifie aussi que chaque schéma est lui-même un JSON Schema bien formé.

Usage:
    python tools/validate_json_files.py examples schemas
    python tools/validate_json_files.py examples/taiwan_strait/situation_analysis.json
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "schemas"
ROOT_SCHEMA_ID = "https://example.org/sipc/schemas/situation_analysis.schema.json"


def load_registry() -> Registry:
    """Charge tous les schémas locaux dans un registre, indexés par leur ``$id``."""
    resources = []
    for schema_path in sorted(SCHEMA_DIR.glob("*.schema.json")):
        contents = json.loads(schema_path.read_text(encoding="utf-8"))
        resource = Resource.from_contents(contents)
        resources.append((contents["$id"], resource))
    return Registry().with_resources(resources)


def iter_json_files(targets: list[str]) -> list[Path]:
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
    targets = argv or ["examples", "schemas"]
    registry = load_registry()
    root_schema = registry.get_or_retrieve(ROOT_SCHEMA_ID).value.contents
    validator = Draft202012Validator(root_schema, registry=registry)

    errors: list[str] = []
    checked_analyses = 0

    for path in iter_json_files(targets):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{path}: JSON invalide — {exc}")
            continue

        # On ne valide contre le schéma racine que les objets d'analyse.
        if isinstance(data, dict) and "analysis_id" in data and "situation" in data:
            checked_analyses += 1
            schema_errors = sorted(validator.iter_errors(data), key=lambda e: e.path)
            for err in schema_errors:
                location = "/".join(str(p) for p in err.absolute_path) or "<racine>"
                errors.append(f"{path} [{location}]: {err.message}")

    # Validation méta : les schémas eux-mêmes sont-ils de bons JSON Schema ?
    for schema_path in sorted(SCHEMA_DIR.glob("*.schema.json")):
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        try:
            Draft202012Validator.check_schema(schema)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{schema_path}: schéma invalide — {exc}")

    if errors:
        print("ÉCHEC de la validation :")
        for line in errors:
            print(f"  - {line}")
        return 1

    print(f"OK : {checked_analyses} analyse(s) valide(s), schémas conformes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
