# Changelog

Format basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/) ; versionnage
sémantique.

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
