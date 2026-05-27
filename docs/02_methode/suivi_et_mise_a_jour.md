# Suivi et mise à jour

Une analyse SIPC n'est pas un instantané définitif. La méthode est une **boucle** :

```text
produire → surveiller les signaux d'invalidation → mettre à jour → backtester → produire…
```

## Surveiller les signaux d'invalidation

Chaque signal d'invalidation (porté par le mécanisme dominant, les trajectoires, le profil de
preuve et le diagnostic) doit être assorti d'**indicateurs de suivi** (`monitoring_indicators`).
Au fil du temps, on renseigne son `monitoring_status` :

- `NOT_OBSERVED` — le signal ne s'est pas manifesté ;
- `PARTIALLY_OBSERVED` — manifestation partielle ;
- `OBSERVED` — le signal s'est déclenché → l'analyse doit être révisée.

## Réviser

Toute révision est tracée dans `revision_history` :

```json
{ "version": "2.0", "date": "2026-05-27",
  "change_summary": "…", "fired_signals": ["…"] }
```

La révision met à jour le mécanisme dominant, les trajectoires et les statuts probatoires si les
signaux observés l'imposent. Le changement de maturité (`analytical_status`) suit la logique
graduée : `DRAFT → REVIEW_REQUIRED → VALIDATED`.

## Backtester

Quand une trajectoire se dénoue, on renseigne son `outcome`
(`REALIZED` / `PARTIAL` / `NOT_REALIZED`). L'outil `tools/score_backtest.py` calcule alors un
**score de Brier** mesurant la calibration des probabilités annoncées. Voir
[Backtesting](../05_preuve/backtesting.md).

!!! tip "Pourquoi c'est crucial"
    Sans boucle de rétroaction, une méthode prédictive ne s'améliore jamais. Le suivi des
    signaux et le backtesting transforment chaque analyse en source d'apprentissage et de
    recalibration.
