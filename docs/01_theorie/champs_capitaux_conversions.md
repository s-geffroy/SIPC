# Champs, capitaux et conversions

## Définition courte

La société internationale n'est pas homogène : elle est composée de **champs** (militaire,
diplomatique, économique, financier, technologique, juridique, institutionnel, symbolique,
informationnel, humanitaire, environnemental). Chaque champ a ses règles, ses ressources et ses
formes de reconnaissance.

## Problème analytique traité

Un acteur peut être puissant dans un champ et faible dans un autre. La notion centrale est donc
la **conversion de capital** : un capital n'est stratégique que s'il peut être converti en
effet dans une situation donnée.

| Capital | Conversion possible |
|---|---|
| militaire | dissuasion, coercition, occupation |
| financier | sanctions, crédit, discipline, accès |
| technologique | dépendance, standard, verrouillage |
| symbolique | légitimité, mobilisation, réputation |
| juridique | qualification, mandat, contrainte |
| institutionnel | accès aux scènes, veto, procédure |

## Concept clé

> La puissance n'est pas seulement possession de ressources. Elle est **capacité située à
> convertir des capitaux en effets reconnus.**

## Erreurs à éviter

- Confondre stock de ressources et capacité d'effet.
- Ignorer les **contraintes de conversion** (un capital peut être bloqué dans un champ donné).

## Exemple bref

Une ONG dispose de peu de coercition matérielle mais d'un fort capital moral et médiatique,
convertible en pression réputationnelle.

## Lien avec l'ontologie JSON

Les champs sont décrits par `field_profile` et activés via `activated_fields` ; les capitaux
par [`capital_profile`](../03_ontologie/vue_ensemble.md) (`level`, `convertibility`,
`conversion_paths`, `constraints`). La conversion est aussi un [mécanisme](../04_mecanismes/index.md).
