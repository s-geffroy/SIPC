# SIPC — Sociologie Internationale des Personnes Collectives

Cadre théorique et opérationnel pour analyser les relations internationales comme une société
mondiale stratifiée de **personnes collectives inégales**. Ce dépôt regroupe la doctrine, la
méthode, l'**ontologie JSON** outillée et trois exemples appliqués et validés.

📖 **Site** : https://s-geffroy.github.io/SIPC/

## Contenu

| Dossier | Rôle |
|---|---|
| `docs/` | documentation MkDocs (théorie, méthode, ontologie, mécanismes, preuve, exemples) |
| `schemas/` | 13 schémas JSON (Draft 2020-12), objet racine `situation_analysis` |
| `examples/` | 3 cas complets : détroit de Taïwan, guerre en Ukraine, rivalité tech US-Chine |
| `tools/` | validateur JSON Schema, **linter doctrinal**, générateur de résumé |
| `tests/` | suite pytest, incluant un test négatif |
| `paper/` | papier académique **LaTeX** (`sipc_paper.tex`) — source de vérité, compilé en PDF par la CI |
| `references/` | bibliographie BibTeX, liste de lecture |

## Démarrage rapide (Docker)

Aucune installation locale : tout passe par le conteneur.

```bash
make build      # construit l'image outillée
make check      # validation JSON Schema + linter doctrinal + tests
make paper      # compile le papier LaTeX en PDF (docs/assets/sipc_paper.pdf)
make docs       # compile le papier puis le site (mkdocs build --strict)
make serve      # site local sur http://localhost:8000
```

Commandes individuelles : `make validate`, `make lint`, `make test`.

## Discipline de conformité

Au-delà de la structure (JSON Schema), `tools/check_doctrine.py` impose les règles de la SIPC :
un **mécanisme dominant**, au moins une **contre-hypothèse**, des **signaux d'invalidation**,
l'**intégrité référentielle** entre objets, et « pas de score sans justification ». Ces règles
sont exécutées en intégration continue à chaque `push`.

## Licence

Documentation et schémas sous licence **CC BY 4.0** (voir `LICENSE`).
