# Mécanismes causaux

Le cœur explicatif de la SIPC. Une analyse identifie **un mécanisme dominant** et deux à
quatre mécanismes secondaires. Chaque mécanisme suit le gabarit : définition minimale,
conditions d'activation, séquence typique, amplificateurs, amortisseurs, outputs possibles,
signaux d'invalidation.

## Les dix mécanismes V1

| Mécanisme (`mechanism_type`) | Définition courte |
|---|---|
| Conversion de capital (`CAPITAL_CONVERSION`) | transformation d'une ressource en effet dans un champ |
| Weaponisation de dépendance (`DEPENDENCY_WEAPONIZATION`) | conversion d'un besoin critique en contrainte |
| Verrouillage d'audience (`AUDIENCE_LOCK_IN`) | recul devenu coûteux devant une audience mobilisée |
| Crise de reconnaissance (`RECOGNITION_CRISIS`) | écart entre rang revendiqué et rang reconnu |
| Dilemme de sécurité (`SECURITY_DILEMMA`) | mesure défensive perçue comme offensive |
| Activation normative (`NORM_ACTIVATION`) | norme mobilisée pour légitimer, contraindre ou sanctionner |
| Lutte de classement (`CLASSIFICATION_STRUGGLE`) | bataille sur les catégories qui définissent le statut |
| Écart de crédibilité (`CREDIBILITY_GAP`) | menace ou promesse non crue par les audiences clés |
| Prophétie auto-réalisatrice (`SELF_FULFILLING_PROPHECY`) | anticipation qui produit le futur redouté |
| Désynchronisation d'ordre (`ORDER_DESYNCHRONIZATION`) | sous-ordres évoluant à des rythmes différents |

Mécanismes additionnels disponibles dans l'enum : `HEGEMONIC_CONTESTATION`, `RESILIENCE_TEST`,
`INSTITUTIONAL_BLOCKAGE`.

## Exemple structuré (extrait Taïwan)

```text
Mécanisme dominant : Conflit de reconnaissance et de souveraineté (RECOGNITION_CRISIS)
- Conditions : souveraineté contestée, coût d'audience symbolique élevé, valeur stratégique du statut
- Séquence : revendication → refus/ambiguïté → activation d'audience → signalement coercitif
- Amplificateurs : pression de l'audience interne, modernisation militaire, rivalité de grande puissance
- Amortisseurs : canaux discrets crédibles, coût d'une guerre majeure, interdépendance économique
- Invalidation : compromis durable de statut à faible coût
```

## Règle méthodologique

```text
Pas de trajectoire sans mécanisme.
Pas de mécanisme sans conditions d'activation.
Pas de mécanisme sans signal d'invalidation.
```

Voir comment ces mécanismes structurent les [trois exemples](../06_exemples/index.md) et la
[causalité configurationnelle](../01_theorie/causalite_preuve_limites.md).
