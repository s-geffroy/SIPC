# Règles de validation

La SIPC distingue deux niveaux de validation, **tous deux outillés et exécutés en CI**.

## 1. Validation structurelle (JSON Schema)

Outil : [`tools/validate_json_files.py`](https://github.com/s-geffroy/SIPC/blob/main/tools/validate_json_files.py).

- Construit un **registre local** de tous les schémas (résolution hors-ligne des `$ref`,
  aucun accès réseau).
- Valide chaque analyse contre `situation_analysis.schema.json` (Draft 2020-12).
- Vérifie que les schémas sont eux-mêmes bien formés.

```bash
make validate          # docker compose run --rm sipc python tools/validate_json_files.py examples schemas
```

## 2. Validation doctrinale (règles non exprimables en JSON Schema)

Outil : [`tools/check_doctrine.py`](https://github.com/s-geffroy/SIPC/blob/main/tools/check_doctrine.py).

Le JSON Schema vérifie la forme ; il ne peut garantir la **discipline analytique**. Le linter
encode les règles SIPC :

### Erreurs (bloquantes)
- présence d'un **mécanisme dominant** ;
- au moins une **trajectoire** ;
- au moins une **contre-hypothèse** ;
- ≥ 1 **signal d'invalidation** pour le mécanisme dominant, chaque trajectoire, le profil de
  preuve et le diagnostic ;
- **intégrité référentielle** :
    - `diagnostic.dominant_mechanism_id` = `dominant_mechanism.mechanism_id` ;
    - `diagnostic.dominant_trajectory_id` ∈ trajectoires présentes ;
    - `trajectory.situation_id` = `situation.situation_id` ;
    - `secondary_mechanism_ids` ⊆ mécanismes secondaires présents ;
    - acteurs référencés dans les relations existants ;
- **« pas de score sans justification »** : un statut probatoire fort (`MODERATELY_SUPPORTED`,
  `STRONGLY_SUPPORTED`) est interdit si `evidence_items` est vide.

### Avertissements (non bloquants)
- plus de **4 mécanismes secondaires** (risque d'hypertrophie) ;
- **confiance élevée** malgré un statut probatoire faible.

```bash
make lint              # docker compose run --rm sipc python tools/check_doctrine.py examples
```

## 3. Tests automatisés

`make test` exécute pytest : validité des schémas, conformité des trois exemples, et un
**test négatif** (`tests/fixtures/broken_analysis.json`) qui doit être rejeté — preuve que la
conformité est réellement vérifiée et non en trompe-l'œil.

!!! quote
    Une absence de preuve ne doit pas être traitée comme une preuve d'absence.
