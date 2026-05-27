# Calibration probabiliste

Le risque classique d'une analyse qualitative est la **fausse précision** : annoncer
« probabilité 0,62 » sans fondement calibré. La SIPC y répond par une **échelle estimative
ancrée** qui relie des mots à des plages numériques explicites.

## Échelle estimative ancrée

| Bande (`probability_band` / `confidence_label`) | Plage numérique |
|---|---|
| `LOW` | 0,05 – 0,20 |
| `MEDIUM_LOW` | 0,20 – 0,40 |
| `MEDIUM` | 0,40 – 0,60 |
| `MEDIUM_HIGH` | 0,60 – 0,80 |
| `HIGH` | 0,80 – 0,95 |
| `UNKNOWN` | non quantifiable |

Inspirée des *Words of Estimative Probability*, cette table garantit que deux analystes
emploient les mêmes mots pour les mêmes ordres de grandeur, et rend les estimations comparables.

## Règles outillées

`tools/check_doctrine.py` vérifie la cohérence de calibration (bloquant dès le tier
`REVIEW_REQUIRED`) :

- si une trajectoire porte un `numeric_estimate`, il **doit tomber dans la plage** de sa
  `probability_band` ;
- la `confidence` du diagnostic doit être **cohérente avec son `confidence_label`**.

Au tier `VALIDATED`, une **confiance élevée associée à un statut probatoire faible** devient une
erreur bloquante (et non un simple avertissement).

## Prudence

Tant qu'il n'existe pas de calibration empirique robuste (voir [Backtesting](backtesting.md)),
les nombres restent des **estimations prudentes**, jamais des mesures. La bande qualitative est
souvent préférable au nombre isolé.

!!! quote
    Un diagnostic incertain n'est pas un échec. Un diagnostic faussement précis est une faute.
