# Enums et vocabulaire contrôlé

Les listes fermées sont centralisées dans
[`common_defs.schema.json`](https://github.com/s-geffroy/SIPC/blob/main/schemas/common_defs.schema.json).
Elles garantissent un vocabulaire stable et machine-lisible.

!!! note "Convention i18n"
    La prose est en **français** ; les **enums et identifiants techniques** sont en **anglais
    MAJUSCULE** (les `object_id` suivent le motif `^[A-Z0-9_:\-.]+$`). Voir
    [Guide du dépôt](../07_implementation/guide_depot.md).

## `actor_type`
`STATE`, `SUBSTATE_ACTOR`, `INTERNATIONAL_ORGANIZATION`, `REGIONAL_ORGANIZATION`,
`MULTINATIONAL_FIRM`, `PLATFORM`, `NGO`, `ARMED_GROUP`, `TERRORIST_GROUP`, `DIASPORA`,
`EXPERT_COMMUNITY`, `FINANCIAL_INSTITUTION`, `INFORMAL_COALITION`, `CRIMINAL_NETWORK`,
`INDIVIDUAL_LEADER`, `OTHER`.

## `field_code`
`MIL`, `DIP`, `ECO`, `FIN`, `TEC`, `LEGAL`, `INST`, `SYM`, `INF`, `HUM`, `ENV`, `SOC`, `COG`,
`LOG`, `ENERGY`, `OTHER`.

## `capital_type`
`MILITARY`, `ECONOMIC`, `FINANCIAL`, `TECHNOLOGICAL`, `LEGAL`, `INSTITUTIONAL`, `SYMBOLIC`,
`INFORMATIONAL`, `HUMANITARIAN`, `LOGISTICAL`, `ENERGY`, `COGNITIVE`, `NORMATIVE`, `SOCIAL`,
`OTHER`.

## `relation_type`
`ALLIANCE`, `RIVALRY`, `DEPENDENCY`, `PROTECTION`, `COERCION`, `COMPETITION`, `COOPERATION`,
`DOMINATION`, `CONTESTATION`, `MEDIATION`, `RECOGNITION`, `NON_RECOGNITION`, `SANCTION`,
`TRADE`, `FINANCIAL_EXPOSURE`, `TECHNOLOGICAL_INTEGRATION`, `INFORMATION_INFLUENCE`,
`LEGAL_DISPUTE`, `OTHER`.

## `mechanism_type`
`CAPITAL_CONVERSION`, `DEPENDENCY_WEAPONIZATION`, `AUDIENCE_LOCK_IN`, `RECOGNITION_CRISIS`,
`SECURITY_DILEMMA`, `NORM_ACTIVATION`, `CLASSIFICATION_STRUGGLE`, `CREDIBILITY_GAP`,
`SELF_FULFILLING_PROPHECY`, `ORDER_DESYNCHRONIZATION`, `HEGEMONIC_CONTESTATION`,
`RESILIENCE_TEST`, `INSTITUTIONAL_BLOCKAGE`, `OTHER`.

## `trajectory_type`
`ESCALATION`, `DEESCALATION`, `STABILIZATION`, `FREEZE`, `INSTITUTIONALIZATION`,
`NORMALIZATION`, `FRAGMENTATION`, `DISPLACEMENT`, `RADICALIZATION`, `ORDER_TRANSFORMATION`,
`CONTAINMENT`, `CONTESTATION`, `REFORM`, `PARTIAL_COLLAPSE`, `OTHER`.

## `situation_type`
`SECURITY_TENSION`, `RECOGNITION_CONFLICT`, `TECHNOLOGY_DEPENDENCY`, `ENERGY_DEPENDENCY`,
`FINANCIAL_STRESS`, `HUMANITARIAN_CRISIS`, `INSTITUTIONAL_CRISIS`, `NORMATIVE_CONFLICT`,
`REGIONAL_ORDER_STRESS`, `HEGEMONIC_CONTESTATION`, `CRISIS`, `LATENT_TENSION`,
`ORDER_TRANSITION`, `OTHER`.

## Statuts et niveaux
- `evidence_status` : `SPECULATIVE`, `WEAKLY_SUPPORTED`, `MODERATELY_SUPPORTED`,
  `STRONGLY_SUPPORTED`, `CONTESTED`, `DISCONFIRMED`, `INSUFFICIENT_EVIDENCE`.
- `confidence_label` : `LOW`, `MEDIUM_LOW`, `MEDIUM`, `MEDIUM_HIGH`, `HIGH`.
- `analytical_status` : `DRAFT`, `REVIEW_REQUIRED`, `VALIDATED`, `CONTESTED`, `ARCHIVED`.
- `probability_band` : `LOW`, `MEDIUM_LOW`, `MEDIUM`, `MEDIUM_HIGH`, `HIGH`, `UNKNOWN`.

!!! warning "Réflexivité des classements"
    Certains enums (`HEGEMONIC_CONTESTATION`, catégories de statut) sont eux-mêmes des
    **instruments de classement**. Les employer comme descripteurs n'efface pas leur charge
    politique : l'analyste doit rester réflexif sur les catégories qu'il mobilise.
