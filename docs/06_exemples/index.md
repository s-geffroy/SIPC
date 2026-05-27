# Exemples appliqués

Trois cas démontrent que la SIPC fonctionne sur des situations réelles sans devenir un
commentaire vague. Les trois analyses JSON **valident contre les schémas** et **passent le
linter doctrinal** (mécanisme dominant, contre-hypothèses, signaux d'invalidation, intégrité
référentielle).

| Cas | Mécanisme dominant | Tier | Briques testées |
|---|---|---|---|
| Détroit de Taïwan | crise de reconnaissance | **VALIDATED** | reconnaissance, dissuasion, dépendance tech, ordre régional |
| Guerre en Ukraine | activation normative | **VALIDATED** | souveraineté, normes, sanctions, résilience de coalition |
| Rivalité tech US-Chine | weaponisation de chokepoints | REVIEW_REQUIRED | dépendance, hégémonie, standards, fragmentation |

Taïwan et Ukraine sont des exemples **« gold standard »** au [tier VALIDATED](../03_ontologie/regles_validation.md)
(sources gradées, [ACH](../05_preuve/ach.md) cohérente, calibration, suivi des signaux) ;
US-Chine illustre le tier REVIEW_REQUIRED.

## Détroit de Taïwan

Situation latente mêlant souveraineté contestée, dissuasion sino-américaine et dépendance
mondiale aux semi-conducteurs. Mécanisme dominant : **conflit de reconnaissance et de
souveraineté** ; secondaires : dilemme de sécurité, weaponisation de la dépendance
technologique. Trajectoire dominante : **tension gérée** ; risque : bascule vers crise
militaire par verrouillage d'audience.

- JSON : [`examples/taiwan_strait/situation_analysis.json`](https://github.com/s-geffroy/SIPC/blob/main/examples/taiwan_strait/situation_analysis.json)

## Guerre en Ukraine

Guerre d'usure où l'**activation normative** autour de la souveraineté soutient une coalition,
la **résilience matérielle** et la fatigue politique devenant décisives. Secondaires :
weaponisation énergétique, test de résilience. Trajectoire dominante : usure prolongée ;
alternative : gel négocié.

- JSON : [`examples/ukraine_war/situation_analysis.json`](https://github.com/s-geffroy/SIPC/blob/main/examples/ukraine_war/situation_analysis.json)

## Rivalité technologique États-Unis / Chine

**Weaponisation des chokepoints technologiques** (lithographie EUV, outils avancés) produisant
un découplage sélectif. Secondaires : contestation hégémonique, désynchronisation d'ordre.
Trajectoire dominante : fragmentation gérée ; alternative : compétition encadrée.

- JSON : [`examples/us_china_technology/situation_analysis.json`](https://github.com/s-geffroy/SIPC/blob/main/examples/us_china_technology/situation_analysis.json)

## Structure d'un exemple

Chaque cas suit le même gabarit : cadrage → acteurs → champs → capitaux/dépendances →
normes/institutions → mécanisme dominant → mécanismes secondaires → trajectoires →
preuves/contre-hypothèses → diagnostic → JSON associé. Le résumé `analysis.md` de chaque cas
est **généré depuis le JSON** par `tools/render_summary.py`, garantissant la cohérence
prose/données.
