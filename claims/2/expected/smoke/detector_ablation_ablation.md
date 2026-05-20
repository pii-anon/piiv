# Detector ablation

Dataset size: 309 queries


_Total seconds is wall-clock time inside ``metrics.detection_precision_recall_with_records``. Skipped rows mean the optional dependency was missing or the backend was unreachable — see ``status``. P/R cells carry 95% bootstrap CIs (1000 resamples, seed=42) when per-query records are available._


| Configuration | macro P (95% CI) | micro P (95% CI) | macro R (95% CI) | micro R (95% CI) | total (s) | s/query | status |
|---|---|---|---|---|---:|---:|---|
| `regex_only` | 0.648 [0.503, 0.665] | 0.908 [0.870, 0.943] | 0.594 [0.518, 0.652] | 0.692 [0.634, 0.748] | 0.02 | 0.000 | ok |
| `regex_opf_base` | 0.725 [0.575, 0.762] | 0.880 [0.842, 0.915] | 0.700 [0.626, 0.767] | 0.891 [0.856, 0.927] | 99.04 | 0.321 | ok |
| `regex_opf_routed` | 0.717 [0.662, 0.864] | 0.899 [0.866, 0.927] | 0.757 [0.701, 0.919] | 0.965 [0.944, 0.983] | 100.31 | 0.325 | ok |
| `regex_presidio` | 0.687 [0.545, 0.715] | 0.883 [0.845, 0.922] | 0.617 [0.543, 0.677] | 0.724 [0.669, 0.777] | 14.47 | 0.047 | ok |

## Routed OPF — per-language model decisions

| Configuration | Language | OPF model |
|---|---|---|
| `regex_opf_routed` | de | `de` |
| `regex_opf_routed` | en | `en` |
| `regex_opf_routed` | ru | `ru` |
