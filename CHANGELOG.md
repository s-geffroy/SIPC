# Changelog

Format basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/) ; versionnage
sémantique.

## [2.4.1] — 2026-05-27

### Supprimé
- Section « Prompt d'implémentation LLM » du guide du dépôt et toute allusion aux LLM / à l'IA
  dans le site (le papier n'en contenait aucune).

## [2.4.0] — 2026-05-27

### Ajouté
- Nouvel exemple **Arctique** au tier VALIDATED (« gold standard ») : mécanisme dominant de
  **désynchronisation d'ordre** (ouverture physique/économique dépassant l'adaptation
  institutionnelle, Conseil de l'Arctique paralysé), ACH à trois hypothèses (preuve
  `SMOKING_GUN` sur le déficit de gouvernance), sources gradées Admiralty, Key Assumptions
  Check, premortem, `outcome` de trajectoire et `revision_history`.
- **Cinq** exemples « gold standard » désormais. Papier (corpus porté à cinq cas), page
  d'accueil, page Exemples et test de comptage (4 → 5) mis à jour.

## [2.3.1] — 2026-05-27

### Modifié
- **Papier LaTeX** : section « Études de cas » étendue au corpus des **quatre cas validés**
  (Taïwan, Ukraine, US-Chine, mer de Chine méridionale) ; abstract, section ontologie et
  conclusion mis à jour pour refléter l'ensemble du dispositif (calibration, ACH, sources, suivi).
- **Page d'accueil** : ajoute une présentation de la méthode renforcée (4 dispositifs), du
  modèle de conformité gradué, des quatre cas et du parcours complet — le site et le papier
  mentionnent désormais l'ensemble du périmètre.

## [2.3.0] — 2026-05-27

### Ajouté
- Nouvel exemple **Mer de Chine méridionale** au tier VALIDATED (« gold standard ») : mécanisme
  dominant de conversion en zone grise (coercition paramilitaire → contrôle de fait sous le seuil
  d'alliance), ACH à trois hypothèses (preuve `SMOKING_GUN` sur la calibration sous le seuil du
  traité de défense mutuelle), sources gradées Admiralty, Key Assumptions Check, premortem,
  `outcome` de trajectoire et `revision_history`.
- Quatre exemples « gold standard » désormais disponibles ; page Exemples et test de comptage
  mis à jour (3 → 4).

## [2.2.0] — 2026-05-27

### Ajouté
- Exemple **Rivalité technologique US-Chine** promu « gold standard » au tier VALIDATED : ACH à
  trois hypothèses (weaponisation des chokepoints la moins infirmée, via une preuve
  `SMOKING_GUN` sur le ciblage chirurgical des nœuds avancés), sources gradées Admiralty, Key
  Assumptions Check, premortem, `outcome` de trajectoire et `revision_history`.
- Les **trois exemples** sont désormais au tier VALIDATED ; page Exemples mise à jour.

## [2.1.0] — 2026-05-27

### Ajouté
- Exemple **Guerre en Ukraine** promu « gold standard » au tier VALIDATED : ACH à trois
  hypothèses (activation normative la moins infirmée, via une preuve `SMOKING_GUN` sur le
  soutien coûteux maintenu), sources gradées Admiralty, Key Assumptions Check, premortem,
  `outcome` de trajectoire et `revision_history`.
- `analysis.md` régénéré avec la matrice ACH.

## [2.0.0] — 2026-05-27

### Ajouté — renforcement de la méthode (4 axes)
- **Modèle de conformité gradué** adossé à `analytical_status` (DRAFT → REVIEW_REQUIRED →
  VALIDATED) dans `check_doctrine.py`.
- **Calibration probabiliste** : échelle estimative ancrée (bandes ↔ plages numériques),
  cohérence `numeric_estimate`/bande et `confidence`/`confidence_label` vérifiée ; module
  partagé `tools/sipc_rules.py`. Page `05_preuve/calibration.md`.
- **ACH + débiaisage** : hypothèses concurrentes, diagnosticité, tests de process tracing,
  matrice de consistance, Key Assumptions Check, premortem (schéma `evidence_profile`) ; outil
  `tools/render_ach.py` ; règle de cohérence ACH (hypothèse dominante = la moins infirmée).
  Page `05_preuve/ach.md`.
- **Traçabilité des sources** : nouveau schéma `source_profile` (fiabilité Admiralty A–F),
  `credibility_grade` (1–6) sur les preuves, intégrité référentielle preuve→source au tier
  VALIDATED. Page `05_preuve/sources_et_claims.md`.
- **Dynamique & rétroaction** : `revision_history`, `outcome` de trajectoire, suivi des signaux
  (`monitoring_status`) ; outil `tools/score_backtest.py` (score de Brier). Pages
  `02_methode/suivi_et_mise_a_jour.md` et `05_preuve/backtesting.md`.
- Exemple **Taïwan** promu « gold standard » au tier VALIDATED (sources, ACH, calibration,
  suivi, historique de révision).
- Tests étendus (10 → 18) : règles de calibration/ACH/sources/suivi par mutation, outils ACH et
  Brier ; papier LaTeX mis à jour (section Preuve V2).

### Modifié
- `check_doctrine.py` réécrit en tiers ; `render_summary.py` affiche la matrice ACH.
- Nouveaux enums dans `common_defs` ; `invalidation_signal` étendu (suivi). Schémas additifs et
  rétrocompatibles (les exemples existants restent valides).

## [1.1.0] — 2026-05-27

### Ajouté
- Papier académique en **LaTeX** (`paper/sipc_paper.tex`) érigé en **source de vérité** :
  version resserrée intégrant une **étude de cas développée** (détroit de Taïwan) et un
  positionnement explicite (héritages vs. apport propre).
- Compilation du PDF **en CI** via `xu-cheng/latex-action`, puis publication dans le site ;
  PDF **téléchargeable** depuis l'accueil et la page Bibliographie (`assets/sipc_paper.pdf`).
- Cible `make paper` et service Docker `latex` (TeX Live) pour la compilation locale.
- 6 références spécialisées ajoutées à la bibliographie (Jervis, Schelling, Farrell & Newman,
  Beach & Pedersen, Honneth, Ringmar).

### Modifié
- `make docs` dépend désormais de `make paper` (le PDF doit exister pour le build strict).

### Supprimé
- `references/papier_academique_long_v1.md` : remplacé par la source LaTeX faisant foi.

## [1.0.0] — 2026-05-27

### Ajouté
- Site MkDocs (thème Material, FR) : théorie, méthode, ontologie, mécanismes, preuve,
  exemples, implémentation, glossaire, limites, bibliographie.
- Ontologie JSON V1 : 13 schémas (Draft 2020-12), objet racine `situation_analysis`.
- Trois exemples complets et conformes à la doctrine : détroit de Taïwan, guerre en Ukraine,
  rivalité technologique États-Unis / Chine.
- Outillage en Docker :
  - `tools/validate_json_files.py` — validation réelle contre les schémas (registre local,
    résolution hors-ligne des `$ref`) ;
  - `tools/check_doctrine.py` — **linter doctrinal** (mécanisme dominant, contre-hypothèses,
    signaux d'invalidation, intégrité référentielle, « pas de score sans justification ») ;
  - `tools/render_summary.py` — génération des résumés `analysis.md` depuis le JSON.
- Suite `pytest` (validité des schémas, conformité des exemples, **test négatif** sur fixture
  fautive).
- CI GitHub Actions : validation + lint + tests + build strict + déploiement GitHub Pages.
- Bibliographie BibTeX, liste de lecture, papier académique de travail.

### Corrigé (par rapport aux livrables sources A/B/C/D)
- Le validateur ne testait que la syntaxe JSON et ignorait ses arguments → validation JSON
  Schema réelle, arguments pris en compte (cohérence avec la CI).
- Pattern `schema_version` élargi de `1.0.x` à `1.x[.y]`.
- Exemple de référence non conforme (preuves vides) → exemples enrichis et conformes.
- Ajout des fichiers manquants prévus par le plan B : `check_doctrine.py`, `render_summary.py`,
  trois exemples, tests, `LICENSE`, `CITATION.cff`.
