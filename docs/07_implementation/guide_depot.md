# Guide du dépôt et conventions

## Structure

```text
sipc-site/
├── docs/            # documentation MkDocs (ce site)
├── schemas/         # 13 schémas JSON (Draft 2020-12)
├── examples/        # 3 cas complets (JSON + analysis.md)
├── tools/           # validate_json_files.py, check_doctrine.py, render_summary.py
├── tests/           # pytest (schémas, exemples, test négatif)
├── references/      # bibliographie BibTeX
└── .github/workflows/docs.yml   # validation + lint + tests + déploiement Pages
```

## Outillage — tout en Docker

!!! warning "Aucune installation locale"
    Toute commande Python (validation, lint, tests, MkDocs) s'exécute dans le conteneur. Le
    `Makefile` encapsule `docker compose run --rm sipc …`.

```bash
make build      # construit l'image
make validate   # JSON Schema
make lint       # règles doctrinales
make test       # pytest
make check      # validate + lint + test
make docs       # mkdocs build --strict
make serve      # site local sur http://localhost:8000
```

## Convention de nommage et i18n

- **Prose** : français.
- **Enums et identifiants** (`object_id`) : anglais, MAJUSCULES, motif `^[A-Z0-9_:\-.]+$`
  (ex. `ACT_CHINA`, `MECH_RECOGNITION_SOVEREIGNTY_CONFLICT_001`).
- Préfixes recommandés : `ACT_` acteur, `REL_` relation, `DEP_` dépendance, `NORM_`,
  `INST_`, `CAP_`, `MECH_`, `TRAJ_`, `EVID_`, `HYP_`, `SIT_`, `ANALYSIS_`.

## Versionnage

- `schema_version` suit le motif `1.x[.y]`. Les changements de structure incrémentent la
  version mineure ; la documentation évolue via le `CHANGELOG.md`.
- Statuts de maturité d'une analyse : `analytical_status` (`DRAFT` → `REVIEW_REQUIRED` →
  `VALIDATED`).

## Pipeline de validation

À chaque `push` sur `main`, GitHub Actions exécute `validate` + `lint` + `pytest`, puis
construit et déploie le site sur GitHub Pages. Voir
[Règles de validation](../03_ontologie/regles_validation.md).
