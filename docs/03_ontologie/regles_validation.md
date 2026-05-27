# Règles de validation

La SIPC distingue deux niveaux de validation, **tous deux outillés et exécutés en CI**.

## Modèle de conformité gradué

Les règles doctrinales s'appliquent selon la maturité de l'analyse (`analytical_status`) :

| Tier | Exigences |
|---|---|
| `DRAFT` | validité structurelle (JSON Schema) ; règles doctrinales en simple avertissement |
| `REVIEW_REQUIRED` | règles de base **bloquantes** (mécanisme dominant, contre-hypothèse, signaux d'invalidation, intégrité référentielle, cohérence de [calibration](../05_preuve/calibration.md)) |
| `VALIDATED` | règles de base **+** règles strictes V2 : [ACH](../05_preuve/ach.md) renseignée et cohérente, [sources gradées](../05_preuve/sources_et_claims.md) et reliées, suivi des signaux d'invalidation, confiance/statut probatoire cohérents |

Ce modèle permet d'amorcer une analyse en `DRAFT` sans blocage, puis de la durcir
progressivement jusqu'au tier `VALIDATED` (exemple « gold standard » : le cas Taïwan).

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
