# Ontologie JSON — vue d'ensemble

L'objet racine est [`situation_analysis`](https://github.com/s-geffroy/SIPC/blob/main/schemas/situation_analysis.schema.json).
Il représente une situation sociale internationale et agrège tous les autres profils.

## Architecture des schémas

### Couche ontologique
- `actor_profile` — personnes collectives
- `relation_profile` — relations entre acteurs
- `field_profile` — champs
- `capital_profile` — capitaux et convertibilité
- `dependency_profile` — dépendances et weaponisation
- `norm_profile` — normes
- `institution_profile` — institutions

### Couche dynamique
- `mechanism_profile` — mécanismes causaux
- `trajectory_profile` — trajectoires conditionnelles

### Couche probatoire
- `evidence_profile` — hypothèses concurrentes ([ACH](../05_preuve/ach.md)), preuves,
  contre-hypothèses, Key Assumptions Check, premortem
- `source_profile` — sources d'information gradées ([fiabilité Admiralty](../05_preuve/sources_et_claims.md))
- `diagnostic_profile` — synthèse finale hiérarchisée

### Objet racine
- `situation_analysis`

## Champs obligatoires de l'objet racine

`schema_version`, `analysis_id`, `situation`, `actors`, `relations`, `activated_fields`,
`dominant_mechanism`, `trajectories` (≥ 1), `evidence`, `diagnostic`, `analytical_status`.

Les blocs `capital_structure`, `dependencies`, `norms`, `institutions`,
`secondary_mechanisms`, `sources` et `revision_history` sont **optionnels** : on ne remplit pas
mécaniquement un module si la situation ne l'active pas (mais le tier `VALIDATED` exige `sources`
et une [ACH](../05_preuve/ach.md) renseignées).

## Format de sortie recommandé

1. `analysis.md` — diagnostic humain ;
2. `situation_analysis.json` — objet exploitable ;
3. les profils `evidence`, `trajectories`, `diagnostic` qu'il contient.

## Principe V1

Cette ontologie **structure** l'analyse ; elle ne remplace pas l'enquête empirique. Les scores
restent prudents tant qu'il n'existe pas de calibration empirique robuste. Voir
[Règles de validation](regles_validation.md) et [Limites](../limites.md).
