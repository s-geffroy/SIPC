# Backtesting

Une méthode prédictive ne s'améliore que si elle **confronte ses prévisions au réel**. La SIPC
prévoit une boucle de rétroaction et un score de calibration.

## Résultat des trajectoires

Quand une trajectoire se dénoue, on renseigne son bloc `outcome` :

- `PENDING` — en cours d'observation ;
- `REALIZED` — la trajectoire s'est réalisée ;
- `PARTIAL` — partiellement ;
- `NOT_REALIZED` — ne s'est pas réalisée.

## Score de Brier

`tools/score_backtest.py` compare la probabilité annoncée (le `numeric_estimate`, ou à défaut le
point médian de la `probability_band`, voir [Calibration](calibration.md)) au résultat observé
(1 si `REALIZED`, 0 si `NOT_REALIZED`) :

$$\text{Brier} = \frac{1}{N}\sum_{i=1}^{N} (p_i - o_i)^2$$

- **0** = prévision parfaite ;
- **0,25** = équivalent au hasard sur une prévision à 50 % ;
- plus le score est bas, mieux l'analyste est calibré.

```bash
docker compose run --rm sipc python tools/score_backtest.py examples
```

## Usage

Le backtesting alimente la [mise à jour](../02_methode/suivi_et_mise_a_jour.md) : un analyste
systématiquement sur-confiant (Brier élevé alors qu'il annonce des probabilités extrêmes) doit
**resserrer ses bandes**. C'est le mécanisme par lequel la SIPC vise une calibration empirique
progressive plutôt qu'une confiance déclarative.
