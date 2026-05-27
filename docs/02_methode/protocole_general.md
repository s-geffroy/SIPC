# Protocole général d'analyse

La SIPC s'applique selon un protocole progressif en dix étapes.

## Les dix étapes

1. **Cadrer** la situation sociale internationale (portée géographique, temporelle, champs).
2. **Identifier** acteurs et relations.
3. **Déterminer** les champs activés.
4. **Évaluer** capitaux, dépendances et vulnérabilités.
5. **Identifier** rôles, audiences, classements, légitimité et crédibilité.
6. **Cartographier** normes et institutions.
7. **Sélectionner** le mécanisme dominant.
8. **Construire** les trajectoires conditionnelles.
9. **Tester** par preuves et contre-hypothèses.
10. **Produire** le diagnostic final (risque, incertitudes, confiance, signaux d'invalidation).

## Critères d'entrée

Une situation identifiable, des acteurs pertinents, et un minimum de matière empirique
(sources déclaratives, pratiques observables ou données matérielles).

## Critères de sortie

Trois niveaux de livrable :

- `analysis.md` — diagnostic exécutif et analytique lisible ;
- `situation_analysis.json` — objet exploitable conforme à l'[ontologie](../03_ontologie/vue_ensemble.md) ;
- profils de preuve, trajectoires et diagnostic associés.

## Règle de rejet

!!! danger "Une analyse est marquée `REVIEW_REQUIRED` ou `INSUFFICIENT_EVIDENCE` si elle ne contient pas :"
    - un **mécanisme dominant** ;
    - au moins une **contre-hypothèse** ;
    - des **signaux d'invalidation** ;
    - un **statut probatoire** ;
    - un **niveau de confiance**.

Ces règles ne sont pas que doctrinales : elles sont **vérifiées par l'outillage**
(`tools/check_doctrine.py`). Voir [Règles de validation](../03_ontologie/regles_validation.md).

## Discipline anti-hypertrophie

```text
une situation ;
un mécanisme dominant ;
deux à quatre mécanismes secondaires ;
des trajectoires conditionnelles ;
des preuves, des contradictions, des signaux d'invalidation.
```

C'est cette contrainte qui empêche la SIPC de devenir une cathédrale théorique inutilisable.
