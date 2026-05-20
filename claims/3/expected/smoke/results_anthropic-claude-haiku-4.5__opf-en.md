# PII Evaluation Results

Dataset size: 10 queries


## Detector configuration

| Field | Value |
|---|---|
| requested_mode | `opf` |
| effective_mode | `opf` |
| second_pass_enabled | `True` |
| fallback_to_regex_only | `False` |
| second_pass_class | `OPFPIIDetector` |
| opf_model_name | `en` |
| opf_checkpoint | `pii-anon/opf-en-v2` |
| opf_policy | `en_comprehensive` |
| opf_device | `cpu` |

## Table 1 — End-to-end metrics

_Note: 'Raw PII transmissions to model' is a cumulative count. It directly scans for every query's boundary PII literals, including PII introduced by tool-result fixtures, in any message handed to the LLM. Multi-turn queries replay history on every iteration, so a single value can be counted multiple times. The intended interpretation is 'how often did raw PII cross the trust boundary?', not 'how many distinct values leaked?'. The scan is detector-independent, so detector misses still count as leaks. P/R/rate cells carry 95% bootstrap CIs (1000 resamples, seed=42) when per-query atoms are available._

| Configuration | Tool-call success | Raw PII transmissions to model | Median latency (s) | p95 latency (s) | Leak-guard triggers |
|---|---|---|---|---|---|
| baseline | 100.0% [100.0%, 100.0%] | 0 [0, 0] | 2.50 [2.34, 2.68] | 2.85 [2.59, 2.90] | 0.0% [0.0%, 0.0%] |
| destructive | 100.0% [100.0%, 100.0%] | 0 [0, 0] | 2.55 [2.29, 2.78] | 2.98 [2.63, 3.06] | 0.0% [0.0%, 0.0%] |
| virtualization | 100.0% [100.0%, 100.0%] | 0 [0, 0] | 4.61 [4.34, 4.97] | 5.36 [4.81, 5.44] | 0.0% [0.0%, 0.0%] |

## Table 2 — Detection sanity check

_Per-detector P/R against the full-framework task dataset. **Macro** is the unweighted mean of the per-tag P/R rows — useful for comparing detector classes; sensitive to small-support tags (e.g. the security-stress code-switched bucket contributes 1-sample tags that drag the mean). **Micro** is support-weighted (``sum(tp) / sum(tp+fp)``), so each detected span contributes equally regardless of which tag it falls under — preferred when comparing two detectors on the same dataset. Cells carry 95% bootstrap CIs (1000 resamples, seed=42) when per-query records are available._

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|

## Table 2a — Detection P/R per (language × placeholder)


### Language: `en`

| Detector | Precision | Recall | TP | FP | FN | Support |
|---|---:|---:|---:|---:|---:|---:|

## Table 2b — Detection P/R by length bucket × language × placeholder

_Length buckets: ``sentence`` (single short line), ``paragraph`` (multi-line, no blank-line separator), ``multi_paragraph`` (has blank-line separator), ``structured`` (markdown table pipes, tab-aligned, or ≥3 colon-and-space lines — log/key-value text)._

| Length bucket | Lang | Detector | P | R | TP | FP | FN | Support |
|---|---|---|---:|---:|---:|---:|---:|---:|

## Table 3 — Argument fidelity and cross-turn stability

| Configuration | Argument exact match | Argument partial match | Cross-turn token stability |
|---|---|---|---|
| baseline | 100.0% | 100.0% | 100.0% |
| destructive | 100.0% | 100.0% | 100.0% |
| virtualization | 100.0% | 100.0% | 100.0% |

## Table 4 — Per-(config × bucket × language)

| Config | Bucket | Lang | n | Tool success | Raw PII | Median latency (s) | Leak triggers |
|---|---|---|---|---|---|---|---|
| baseline | no_pii_control | en | 10 | 100.0% | 0 | 2.50 | 0.0% |
| destructive | no_pii_control | en | 10 | 100.0% | 0 | 2.55 | 0.0% |
| virtualization | no_pii_control | en | 10 | 100.0% | 0 | 4.61 | 0.0% |

## Table 6 — Per-detector latency contribution

_Wall-clock seconds spent inside each detector across the run. ``regex`` is the first-pass detector; ``second_pass_*`` rows are the optional NER / generative LM layers. Production hot paths are unaffected — the recorder is benchmark-only._

| Detector | Calls | Total (s) | Mean (ms) | p95 (ms) |
|---|---:|---:|---:|---:|
| `regex` | 40 | 0.034 | 0.845 | 0.247 |
| `second_pass_OPFPIIDetector` | 30 | 28.912 | 963.719 | 2257.126 |
