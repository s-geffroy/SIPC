# Causalité, preuve et limites

## Définition courte

La SIPC n'explique pas par une cause unique. Elle utilise une **causalité configurationnelle**.

```text
effet international =
  configuration initiale + mécanismes activés + seuils franchis
  + séquence d'interactions + rétroactions + verrouillages
  + conditions d'invalidation
```

## Règle méthodologique centrale

```text
Pas de trajectoire sans mécanisme.
Pas de mécanisme sans conditions d'activation.
Pas d'analyse sérieuse sans signal d'invalidation.
```

Une analyse standard identifie : un **mécanisme dominant**, deux à quatre mécanismes secondaires
au maximum, les seuils critiques, la séquence, les rétroactions et les signaux qui feraient
changer l'analyse. Voir [Mécanismes](../04_mecanismes/index.md) et [Méthode](../02_methode/protocole_general.md).

## Triangulation probatoire

Le danger principal de la SIPC est de **produire des interprétations intelligentes mais
insuffisamment prouvées**. La parade est la triangulation : relier sources déclaratives,
comportements observables, données matérielles, séquence temporelle, réactions d'audience,
contre-hypothèses, contradictions et signal d'invalidation. Voir [Preuve](../05_preuve/triangulation_probatoire.md).

!!! quote "Phrase centrale"
    Un diagnostic incertain n'est pas un échec. Un diagnostic faussement certain est une faute.

## Limites explicites

- Pas de certitude absolue ; dépendance à la qualité des sources.
- Risque de surinterprétation des intentions.
- Nécessité de distinguer plausibilité et preuve, et de hiérarchiser les mécanismes.

Voir la page [Limites](../limites.md).

## Lien avec l'ontologie JSON

`mechanism_profile` (conditions, séquence, invalidation), `trajectory_profile` (conditions,
bifurcations), `evidence_profile` (items, contre-hypothèses, statut probatoire),
`diagnostic_profile` (confiance, incertitudes).
