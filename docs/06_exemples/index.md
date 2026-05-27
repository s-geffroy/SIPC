# Exemples appliqués

Huit cas démontrent que la SIPC fonctionne sur des situations réelles sans devenir un
commentaire vague. Les huit analyses JSON **valident contre les schémas** et **passent le
linter doctrinal** (mécanisme dominant, contre-hypothèses, signaux d'invalidation, intégrité
référentielle).

| Cas | Mécanisme dominant | Tier | Briques testées |
|---|---|---|---|
| Détroit de Taïwan | crise de reconnaissance | **VALIDATED** | reconnaissance, dissuasion, dépendance tech, ordre régional |
| Guerre en Ukraine | activation normative | **VALIDATED** | souveraineté, normes, sanctions, résilience de coalition |
| Rivalité tech US-Chine | weaponisation de chokepoints | **VALIDATED** | dépendance, hégémonie, standards, fragmentation |
| Mer de Chine méridionale | conversion en zone grise | **VALIDATED** | coercition de zone grise, droit de la mer, alliances, fait accompli |
| Arctique | désynchronisation d'ordre | **VALIDATED** | environnement, gouvernance bloquée, militarisation, plateau continental |
| Sahel central | conversion souverainiste | **VALIDATED** | insurrection, coups d'État, réalignement, recomposition régionale |
| Corée du Nord | conversion du capital nucléaire | **VALIDATED** | dissuasion, survie du régime, reconnaissance, non-prolifération |
| Gouvernance mondiale de l'IA | lutte de classement (standards) | **VALIDATED** | standards, déficit de gouvernance, hégémonie, dépendance au calcul |

Les huit cas sont des exemples **« gold standard »** au [tier VALIDATED](../03_ontologie/regles_validation.md) :
sources gradées (Admiralty), [ACH](../05_preuve/ach.md) cohérente (hypothèse dominante la moins
infirmée, départagée par une preuve `SMOKING_GUN`), calibration ancrée et suivi des signaux
d'invalidation.

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

## Mer de Chine méridionale

**Conversion incrémentale de capital paramilitaire en contrôle de fait** (zone grise), calibrée
sous le seuil déclenchant le traité de défense mutuelle États-Unis–Philippines. Secondaires :
lutte de classement juridique (droits historiques vs UNCLOS), activation normative de la liberté
de navigation, dilemme de sécurité régional. Trajectoire dominante : normalisation du contrôle de
fait ; alternative : affrontement armé limité déclenché par un incident.

- JSON : [`examples/south_china_sea/situation_analysis.json`](https://github.com/s-geffroy/SIPC/blob/main/examples/south_china_sea/situation_analysis.json)

## Arctique

**Désynchronisation d'ordre** : l'ouverture physique et économique de l'Arctique (fonte des
glaces, route maritime du Nord) dépasse la capacité d'adaptation des institutions, et la
paralysie du Conseil de l'Arctique prive la région de coordination. Secondaires : blocage
institutionnel, conversion de capital militaire, lutte de classement sur le plateau continental.
Trajectoire dominante : gouvernance fragmentée ; alternative : coexistence gérée par la basse
politique.

- JSON : [`examples/arctic/situation_analysis.json`](https://github.com/s-geffroy/SIPC/blob/main/examples/arctic/situation_analysis.json)

## Sahel central

**Conversion d'un capital souverainiste en légitimité de régime** : des juntes transforment
l'insécurité et un capital symbolique anti-occidental en légitimité interne et en réalignement
(retrait français, partenariat russe), recomposant l'ordre régional (AES contre CEDEAO).
Secondaires : recomposition de la dépendance sécuritaire, lutte de classement sur la légitimité
du pouvoir, contestation de l'ordre régional. Trajectoire dominante : consolidation autoritaire
souverainiste ; alternative : fragmentation territoriale.

- JSON : [`examples/sahel/situation_analysis.json`](https://github.com/s-geffroy/SIPC/blob/main/examples/sahel/situation_analysis.json)

## Corée du Nord

**Conversion du capital nucléaire en garantie de survie du régime** : l'arme nucléaire fonctionne
d'abord comme assurance contre un changement de régime imposé, ce qui rend la dénucléarisation
structurellement improbable et borne le marchandage. Secondaires : crise de reconnaissance du
statut nucléaire, activation de la norme de non-prolifération, weaponisation croisée de la
dépendance économique. Trajectoire dominante : statut nucléaire de fait enraciné sous dissuasion
gérée ; alternative : escalade de crise par provocation ou méprise.

- JSON : [`examples/north_korea/situation_analysis.json`](https://github.com/s-geffroy/SIPC/blob/main/examples/north_korea/situation_analysis.json)

## Gouvernance mondiale de l'IA

*(L'intelligence artificielle est ici la **situation analysée**, non un outil d'analyse.)*

**Lutte de classement sur les catégories et standards** : qui fixe les définitions (« IA à haut
risque », « modèle de pointe ») et le régime de conformité oriente la gouvernance mondiale.
Secondaires : désynchronisation d'ordre (capacités vs régulation), contestation hégémonique,
weaponisation de la dépendance au calcul. Trajectoire dominante : régimes réglementaires
fragmentés ; alternative : convergence sur des standards minimaux interopérables.

- JSON : [`examples/ai_governance/situation_analysis.json`](https://github.com/s-geffroy/SIPC/blob/main/examples/ai_governance/situation_analysis.json)

## Structure d'un exemple

Chaque cas suit le même gabarit : cadrage → acteurs → champs → capitaux/dépendances →
normes/institutions → mécanisme dominant → mécanismes secondaires → trajectoires →
preuves/contre-hypothèses → diagnostic → JSON associé. Le résumé `analysis.md` de chaque cas
est **généré depuis le JSON** par `tools/render_summary.py`, garantissant la cohérence
prose/données.
