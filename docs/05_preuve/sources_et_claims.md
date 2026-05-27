# Sources et crédibilité

La règle « **source ≠ preuve** » n'est utile que si elle est modélisée. La SIPC sépare deux
dimensions, selon le **code Admiralty (OTAN)** :

- la **fiabilité de la source** (`reliability`, A–F) — propriété de la source ;
- la **crédibilité de l'information** (`credibility_grade`, 1–6) — propriété de chaque pièce de
  preuve.

## Fiabilité de la source (A–F)

| Code | Sens |
|---|---|
| `A` | totalement fiable |
| `B` | habituellement fiable |
| `C` | assez fiable |
| `D` | pas habituellement fiable |
| `E` | non fiable |
| `F` | ne peut être évaluée |

Chaque source est déclarée dans le bloc `sources` de l'analyse via un `source_profile`
(`source_id`, `name`, `source_type`, `reliability`).

## Crédibilité de l'information (1–6)

| Code | Sens |
|---|---|
| `1` | confirmée par d'autres sources |
| `2` | probablement vraie |
| `3` | possiblement vraie |
| `4` | douteuse |
| `5` | improbable |
| `6` | ne peut être évaluée |

Chaque `evidence_item` peut porter un `credibility_grade` et **doit** (tier `VALIDATED`) citer au
moins une source déclarée via `source_ids`.

## Règles outillées (tier `VALIDATED`)

- toute preuve référence ≥ 1 source existante (intégrité référentielle) ;
- avertissement si une preuve de forte intensité (`strength` élevée) repose sur une source de
  fiabilité `E`/`F`.

!!! note
    Une source très fiable peut transmettre une information douteuse, et l'inverse. Garder les
    deux axes séparés évite de confondre la qualité du messager et celle du message.
