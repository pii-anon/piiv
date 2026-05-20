# §2 Detector Ablation — paper matrix

Dataset size: 309 queries. All P / R cells are point estimates summed across (en + de + ru). For 95 % bootstrap CIs see the per-row `detector_ablation_<slug>.md` source files.

| Configuration | macro P | micro P | macro R | micro R | TP / FP / FN | s/query | status |
|---|---:|---:|---:|---:|---|---:|---|
| `regex_only` |  64.8% |  90.8% |  59.4% |  69.2% | 216 / 22 / 96 | 0.00 | ok |
| `regex_opf_base` |  72.5% |  88.0% |  70.0% |  89.1% | 278 / 38 / 34 | 0.32 | ok |
| `regex_opf_routed` |  71.7% |  89.9% |  75.7% |  96.5% | 301 / 34 / 11 | 0.32 | ok |
| `regex_presidio` |  68.7% |  88.3% |  61.7% |  72.4% | 226 / 30 / 86 | 0.05 | ok |
| `regex_llm__mistralai-ministral-3b-2512` |  79.1% |  91.2% |  64.4% |  73.1% | 228 / 22 / 84 | 0.34 | ok |
| `regex_llm__nvidia-nemotron-nano-9b-v2-free` |  79.1% |  91.7% |  72.2% |  77.9% | 243 / 22 / 69 | 1.75 | ok |
| `regex_llm__qwen-qwen3.5-9b` |  79.1% |  91.8% |  73.2% |  79.2% | 247 / 22 / 65 | 0.38 | ok |
