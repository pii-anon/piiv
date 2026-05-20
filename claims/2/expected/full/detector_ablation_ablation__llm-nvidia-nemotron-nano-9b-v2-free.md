# Detector ablation

Dataset size: 309 queries


_Total seconds is wall-clock time inside ``metrics.detection_precision_recall_with_records``. Skipped rows mean the optional dependency was missing or the backend was unreachable — see ``status``. P/R cells carry 95% bootstrap CIs (1000 resamples, seed=42) when per-query records are available._


| Configuration | macro P (95% CI) | micro P (95% CI) | macro R (95% CI) | micro R (95% CI) | total (s) | s/query | status |
|---|---|---|---|---|---:|---:|---|
| `regex_llm` | 0.791 [0.646, 0.803] | 0.917 [0.881, 0.948] | 0.722 [0.650, 0.775] | 0.779 [0.728, 0.828] | 541.69 | 1.753 | ok |
