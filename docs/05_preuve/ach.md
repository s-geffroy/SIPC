# Analyse des hypothèses concurrentes (ACH)

Exiger « au moins une contre-hypothèse » ne suffit pas si rien ne structure leur mise en
concurrence. La SIPC adopte l'**ACH** (Heuer) et les **tests de *process tracing***.

## Principe d'élimination

L'ACH renverse l'intuition : on ne cherche pas l'hypothèse la **plus confirmée**, mais on
**élimine** celles que les preuves **infirment** le plus. L'hypothèse retenue est la **moins
infirmée**.

On construit une matrice hypothèses × preuves, où chaque preuve est notée pour chaque hypothèse :

- `CONSISTENT` (`+`) — la preuve est compatible avec l'hypothèse ;
- `INCONSISTENT` (`−`) — la preuve contredit l'hypothèse ;
- `NEUTRAL` (`·`) — sans pouvoir discriminant.

`tools/render_ach.py` génère cette matrice et le décompte des inconsistances. `check_doctrine.py`
exige (tier `VALIDATED`) que l'hypothèse dominante soit bien la **moins infirmée** — sinon erreur.

## Diagnosticité et tests de process tracing

Toute preuve n'a pas le même pouvoir. On qualifie sa **diagnosticité** (`LOW`/`MEDIUM`/`HIGH`) —
une preuve diagnostique discrimine entre hypothèses — et son type de test :

| Test | Réussi | Échoué |
|---|---|---|
| `STRAW_IN_THE_WIND` | indice faible | n'infirme pas |
| `HOOP` | nécessaire, ne confirme pas | **infirme** si absent |
| `SMOKING_GUN` | **confirme** fortement si présent | n'infirme pas si absent |
| `DOUBLY_DECISIVE` | confirme **et** infirme les rivales | — |

Le tier `VALIDATED` exige au moins une preuve à diagnosticité `HIGH`.

## Débiaisage : Key Assumptions Check & premortem

- **Key Assumptions Check** (`key_assumptions`) : expliciter les hypothèses implicites, leur
  statut et l'impact si elles sont fausses.
- **Premortem** (`premortem`) : énoncer par avance les scénarios qui rendraient le diagnostic
  faux.

## Exemple

La matrice ACH du [cas Taïwan](../06_exemples/index.md) montre que l'hypothèse « conflit de
reconnaissance » est la moins infirmée (0 inconsistance), une preuve `SMOKING_GUN` à
diagnosticité `HIGH` infirmant les hypothèses rivales.
