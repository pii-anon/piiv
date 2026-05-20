# Detector ablation

Dataset size: 309 queries


_Total seconds is wall-clock time inside ``metrics.detection_precision_recall_with_records``. Skipped rows mean the optional dependency was missing or the backend was unreachable — see ``status``. P/R cells carry 95% bootstrap CIs (1000 resamples, seed=42) when per-query records are available._


| Configuration | macro P (95% CI) | micro P (95% CI) | macro R (95% CI) | micro R (95% CI) | total (s) | s/query | status |
|---|---|---|---|---|---:|---:|---|
| `regex_llm` | 0.717 [0.572, 0.735] | 0.870 [0.830, 0.908] | 0.672 [0.592, 0.740] | 0.769 [0.717, 0.818] | 97.39 | 0.315 | ok |
