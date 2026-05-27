# Triangulation probatoire

La SIPC est vulnérable à un risque sérieux : **produire des interprétations très intelligentes
mais insuffisamment prouvées.** La triangulation est la parade.

## Une hypothèse robuste relie

```text
sources déclaratives
+ comportements observables
+ données matérielles
+ séquence temporelle
+ réactions d'audience
+ contre-hypothèses
+ contradictions
+ signaux d'invalidation
+ niveau de confiance explicite
```

## Statuts probatoires

| Statut | Sens |
|---|---|
| `SPECULATIVE` | hypothèse non étayée |
| `WEAKLY_SUPPORTED` | indices faibles |
| `MODERATELY_SUPPORTED` | faisceau convergent partiel |
| `STRONGLY_SUPPORTED` | preuves convergentes robustes |
| `CONTESTED` | preuves contradictoires |
| `DISCONFIRMED` | hypothèse infirmée |
| `INSUFFICIENT_EVIDENCE` | matière insuffisante |

## Types de preuve (`evidence_type`)

`OFFICIAL_DISCOURSE`, `DOCTRINAL_DOCUMENT`, `OBSERVABLE_PRACTICE`, `MATERIAL_DATA`,
`SEQUENCE_TIMING`, `AUDIENCE_REACTION`, `SOURCE_DOCUMENT`, `COUNTER_EVIDENCE`,
`EXPERT_ASSESSMENT`, `UNKNOWN`, `OTHER`.

Chaque `evidence_item` porte trois scores prudents : `strength`, `reliability`,
`interpretation_risk`.

## Contre-hypothèses et invalidation

Toute hypothèse importante exige **au moins une contre-hypothèse** (avec plausibilité et
statut) et **au moins un signal d'invalidation** — un fait observable qui, s'il survenait,
ferait changer le diagnostic. Ces deux exigences sont **vérifiées par
[`check_doctrine.py`](../03_ontologie/regles_validation.md)**.

## Niveaux de confiance

Le niveau de confiance (`confidence` 0–1 et `confidence_label`) reste **prudent** tant qu'il
n'existe pas de calibration empirique. Un score n'a jamais de valeur sans justification textuelle.

!!! quote "Phrase centrale"
    Un diagnostic incertain n'est pas un échec. Un diagnostic faussement certain est une faute.
