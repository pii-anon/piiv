# Detector ablation

Dataset size: 309 queries


_Total seconds is wall-clock time inside ``metrics.detection_precision_recall_with_records``. Skipped rows mean the optional dependency was missing or the backend was unreachable — see ``status``. P/R cells carry 95% bootstrap CIs (1000 resamples, seed=42) when per-query records are available._


| Configuration | macro P (95% CI) | micro P (95% CI) | macro R (95% CI) | micro R (95% CI) | total (s) | s/query | status |
|---|---|---|---|---|---:|---:|---|
| `regex_llm` | 0.791 [0.619, 0.801] | 0.912 [0.875, 0.946] | 0.644 [0.563, 0.718] | 0.731 [0.678, 0.783] | 104.30 | 0.338 | ok |
