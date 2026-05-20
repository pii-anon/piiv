# PII Evaluation Results

Dataset size: 103 queries


## Detector configuration

| Field | Value |
|---|---|
| requested_mode | `opf` |
| effective_mode | `opf` |
| second_pass_enabled | `True` |
| fallback_to_regex_only | `False` |
| second_pass_class | `OPFPIIDetector` |
| opf_model_name | `en` |
| opf_checkpoint | `fine_tuning/runs/en-v2/checkpoint` |
| opf_policy | `en_comprehensive` |
| opf_device | `mps` |

## Table 1 — End-to-end metrics

_Note: 'Raw PII transmissions to model' is a cumulative count. It directly scans for every query's boundary PII literals, including PII introduced by tool-result fixtures, in any message handed to the LLM. Multi-turn queries replay history on every iteration, so a single value can be counted multiple times. The intended interpretation is 'how often did raw PII cross the trust boundary?', not 'how many distinct values leaked?'. The scan is detector-independent, so detector misses still count as leaks. P/R/rate cells carry 95% bootstrap CIs (1000 resamples, seed=42) when per-query atoms are available._

| Configuration | Tool-call success | Raw PII transmissions to model | Median latency (s) | p95 latency (s) | Leak-guard triggers |
|---|---|---|---|---|---|
| baseline | 96.2% [91.1%, 100.0%] | 754 [574, 918] | 8.09 [7.49, 9.27] | 24.71 [17.50, 28.24] | 0.0% [0.0%, 0.0%] |
| destructive | 27.8% [19.0%, 38.0%] | 92 [45, 152] | 6.37 [5.27, 7.02] | 17.28 [14.34, 28.91] | 0.0% [0.0%, 0.0%] |
| virtualization | 93.7% [87.3%, 98.7%] | 9 [0, 19] | 13.78 [12.42, 15.33] | 28.28 [23.53, 40.49] | 0.0% [0.0%, 0.0%] |

## Table 2 — Detection sanity check

_Per-detector P/R against the full-framework task dataset. **Macro** is the unweighted mean of the per-tag P/R rows — useful for comparing detector classes; sensitive to small-support tags (e.g. the security-stress code-switched bucket contributes 1-sample tags that drag the mean). **Micro** is support-weighted (``sum(tp) / sum(tp+fp)``), so each detected span contributes equally regardless of which tag it falls under — preferred when comparing two detectors on the same dataset. Cells carry 95% bootstrap CIs (1000 resamples, seed=42) when per-query records are available._

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[CARD]` | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 8 | 0 | 0 | 8 |
| `[DATE]` | 0.167 [0.000, 0.500] | 1.000 [0.000, 1.000] | 0.286 [0.000, 0.667] | 1 | 5 | 0 | 1 |
| `[DE_STEUER_ID]` | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0 | 0 | 1 | 1 |
| `[EMAIL]` | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 26 | 0 | 0 | 26 |
| `[IBAN]` | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1 | 0 | 0 | 1 |
| `[IP]` | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1 | 0 | 0 | 1 |
| `[LICENSE_PLATE]` | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0 | 0 | 1 | 1 |
| `[PERSONAL_ID]` | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0 | 0 | 7 | 7 |
| `[PERSON_NAME]` | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0 | 0 | 10 | 10 |
| `[PHONE]` | 0.955 [0.881, 1.000] | 0.955 [0.884, 1.000] | 0.955 [0.899, 0.989] | 42 | 2 | 2 | 44 |
| `[RU_SNILS]` | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0 | 0 | 1 | 1 |
| `[STREET_ADDRESS]` | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0 | 0 | 1 | 1 |
| `[URL]` | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1 | 0 | 0 | 1 |
| `[VIN]` | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1 | 0 | 0 | 1 |
| **macro** | 0.509 [0.277, 0.522] | 0.568 [0.281, 0.570] | 0.537 [0.277, 0.544] | 81 | 7 | 23 | 104 |
| **micro** | 0.920 [0.866, 0.974] | 0.779 [0.696, 0.855] | 0.844 [0.788, 0.892] | 81 | 7 | 23 | 104 |

## Table 2a — Detection P/R per (language × placeholder)


### Language: `en`

| Detector | Precision | Recall | TP | FP | FN | Support |
|---|---:|---:|---:|---:|---:|---:|
| `[CARD]` | 1.000 | 1.000 | 8 | 0 | 0 | 8 |
| `[DATE]` | 0.167 | 1.000 | 1 | 5 | 0 | 1 |
| `[DE_STEUER_ID]` | 0.000 | 0.000 | 0 | 0 | 1 | 1 |
| `[EMAIL]` | 1.000 | 1.000 | 26 | 0 | 0 | 26 |
| `[IBAN]` | 1.000 | 1.000 | 1 | 0 | 0 | 1 |
| `[IP]` | 1.000 | 1.000 | 1 | 0 | 0 | 1 |
| `[LICENSE_PLATE]` | 0.000 | 0.000 | 0 | 0 | 1 | 1 |
| `[PERSONAL_ID]` | 0.000 | 0.000 | 0 | 0 | 7 | 7 |
| `[PERSON_NAME]` | 0.000 | 0.000 | 0 | 0 | 10 | 10 |
| `[PHONE]` | 0.955 | 0.955 | 42 | 2 | 2 | 44 |
| `[RU_SNILS]` | 0.000 | 0.000 | 0 | 0 | 1 | 1 |
| `[STREET_ADDRESS]` | 0.000 | 0.000 | 0 | 0 | 1 | 1 |
| `[URL]` | 1.000 | 1.000 | 1 | 0 | 0 | 1 |
| `[VIN]` | 1.000 | 1.000 | 1 | 0 | 0 | 1 |
| **macro avg** | **0.509** | **0.568** | — | — | — | — |
| **micro avg** | **0.920** | **0.779** | 81 | 7 | 23 | 104 |

## Table 2b — Detection P/R by length bucket × language × placeholder

_Length buckets: ``sentence`` (single short line), ``paragraph`` (multi-line, no blank-line separator), ``multi_paragraph`` (has blank-line separator), ``structured`` (markdown table pipes, tab-aligned, or ≥3 colon-and-space lines — log/key-value text)._

| Length bucket | Lang | Detector | P | R | TP | FP | FN | Support |
|---|---|---|---:|---:|---:|---:|---:|---:|
| paragraph | en | `[DATE]` | 0.000 | 0.000 | 0 | 2 | 0 | 0 |
| paragraph | en | `[EMAIL]` | 1.000 | 1.000 | 10 | 0 | 0 | 10 |
| paragraph | en | `[PERSON_NAME]` | 0.000 | 0.000 | 0 | 0 | 2 | 2 |
| paragraph | en | `[PHONE]` | 1.000 | 1.000 | 18 | 0 | 0 | 18 |
| paragraph | en | `[STREET_ADDRESS]` | 0.000 | 0.000 | 0 | 0 | 1 | 1 |
| paragraph | en | **micro** | **0.933** | **0.903** | 28 | 2 | 3 | 31 |
| sentence | en | `[CARD]` | 1.000 | 1.000 | 8 | 0 | 0 | 8 |
| sentence | en | `[DATE]` | 0.250 | 1.000 | 1 | 3 | 0 | 1 |
| sentence | en | `[DE_STEUER_ID]` | 0.000 | 0.000 | 0 | 0 | 1 | 1 |
| sentence | en | `[EMAIL]` | 1.000 | 1.000 | 16 | 0 | 0 | 16 |
| sentence | en | `[IBAN]` | 1.000 | 1.000 | 1 | 0 | 0 | 1 |
| sentence | en | `[IP]` | 1.000 | 1.000 | 1 | 0 | 0 | 1 |
| sentence | en | `[LICENSE_PLATE]` | 0.000 | 0.000 | 0 | 0 | 1 | 1 |
| sentence | en | `[PERSONAL_ID]` | 0.000 | 0.000 | 0 | 0 | 7 | 7 |
| sentence | en | `[PERSON_NAME]` | 0.000 | 0.000 | 0 | 0 | 8 | 8 |
| sentence | en | `[PHONE]` | 0.923 | 0.923 | 24 | 2 | 2 | 26 |
| sentence | en | `[RU_SNILS]` | 0.000 | 0.000 | 0 | 0 | 1 | 1 |
| sentence | en | `[URL]` | 1.000 | 1.000 | 1 | 0 | 0 | 1 |
| sentence | en | `[VIN]` | 1.000 | 1.000 | 1 | 0 | 0 | 1 |
| sentence | en | **micro** | **0.914** | **0.726** | 53 | 5 | 20 | 73 |

## Table 3 — Argument fidelity and cross-turn stability

| Configuration | Argument exact match | Argument partial match | Cross-turn token stability |
|---|---|---|---|
| baseline | 96.2% | 96.2% | 100.0% |
| destructive | 25.3% | 26.6% | 100.0% |
| virtualization | 93.7% | 97.5% | 68.2% |

## Table 4 — Per-(config × bucket × language)

| Config | Bucket | Lang | n | Tool success | Raw PII | Median latency (s) | Leak triggers |
|---|---|---|---|---|---|---|---|
| baseline | hard_negative | en | 12 | 0.0% | 0 | 4.86 | 0.0% |
| baseline | multi_pii | en | 14 | 92.9% | 108 | 7.41 | 0.0% |
| baseline | multi_turn | en | 22 | 100.0% | 484 | 16.94 | 0.0% |
| baseline | no_pii_control | en | 10 | 100.0% | 0 | 7.26 | 0.0% |
| baseline | security_stress | en | 15 | 100.0% | 24 | 10.42 | 0.0% |
| baseline | single_turn | en | 30 | 93.3% | 138 | 7.63 | 0.0% |
| destructive | hard_negative | en | 12 | 0.0% | 0 | 4.19 | 0.0% |
| destructive | multi_pii | en | 14 | 7.1% | 12 | 3.92 | 0.0% |
| destructive | multi_turn | en | 22 | 9.1% | 33 | 10.03 | 0.0% |
| destructive | no_pii_control | en | 10 | 100.0% | 0 | 6.54 | 0.0% |
| destructive | security_stress | en | 15 | 66.7% | 10 | 7.25 | 0.0% |
| destructive | single_turn | en | 30 | 23.3% | 37 | 4.73 | 0.0% |
| virtualization | hard_negative | en | 12 | 0.0% | 0 | 6.18 | 0.0% |
| virtualization | multi_pii | en | 14 | 92.9% | 3 | 13.26 | 0.0% |
| virtualization | multi_turn | en | 22 | 100.0% | 0 | 22.85 | 0.0% |
| virtualization | no_pii_control | en | 10 | 100.0% | 0 | 10.24 | 0.0% |
| virtualization | security_stress | en | 15 | 100.0% | 2 | 12.11 | 0.0% |
| virtualization | single_turn | en | 30 | 86.7% | 4 | 13.21 | 0.0% |

## Table 6 — Per-detector latency contribution

_Wall-clock seconds spent inside each detector across the run. ``regex`` is the first-pass detector; ``second_pass_*`` rows are the optional NER / generative LM layers. Production hot paths are unaffected — the recorder is benchmark-only._

| Detector | Calls | Total (s) | Mean (ms) | p95 (ms) |
|---|---:|---:|---:|---:|
| `regex` | 1089 | 0.143 | 0.131 | 0.532 |
| `second_pass_OPFPIIDetector` | 362 | 465.785 | 1286.698 | 3767.882 |

## Table 5 — Security-stress report

| Config | Workflow | Total | Passed | Failed | Pass rate | Raw PII |
|---|---|---:|---:|---:|---:|---:|
| baseline | code_switched_id_de_steuer | 1 | 0 | 1 | 0.0% | 2 |
| baseline | code_switched_id_ru_snils | 1 | 0 | 1 | 0.0% | 2 |
| baseline | code_switched_id_us_ssn | 1 | 0 | 1 | 0.0% | 2 |
| baseline | forged_ref_token | 1 | 1 | 0 | 100.0% | 0 |
| baseline | forged_ref_token_email | 1 | 1 | 0 | 100.0% | 0 |
| baseline | hard_non_pii_mimic | 1 | 1 | 0 | 100.0% | 0 |
| baseline | hard_non_pii_mimic_v2 | 1 | 1 | 0 | 100.0% | 0 |
| baseline | prompt_injection_for_raw_pii | 2 | 0 | 2 | 0.0% | 4 |
| baseline | prompt_injection_for_raw_pii_v2 | 1 | 0 | 1 | 0.0% | 2 |
| baseline | tool_exception_leakage | 3 | 3 | 0 | 100.0% | 8 |
| baseline | zero_width_split_phone | 1 | 0 | 1 | 0.0% | 2 |
| baseline | zero_width_split_phone_v2 | 1 | 0 | 1 | 0.0% | 2 |
| destructive | code_switched_id_de_steuer | 1 | 0 | 1 | 0.0% | 2 |
| destructive | code_switched_id_ru_snils | 1 | 0 | 1 | 0.0% | 2 |
| destructive | code_switched_id_us_ssn | 1 | 0 | 1 | 0.0% | 2 |
| destructive | forged_ref_token | 1 | 1 | 0 | 100.0% | 0 |
| destructive | forged_ref_token_email | 1 | 1 | 0 | 100.0% | 0 |
| destructive | hard_non_pii_mimic | 1 | 1 | 0 | 100.0% | 0 |
| destructive | hard_non_pii_mimic_v2 | 1 | 1 | 0 | 100.0% | 0 |
| destructive | prompt_injection_for_raw_pii | 2 | 2 | 0 | 100.0% | 0 |
| destructive | prompt_injection_for_raw_pii_v2 | 1 | 1 | 0 | 100.0% | 0 |
| destructive | tool_exception_leakage | 3 | 0 | 3 | 0.0% | 0 |
| destructive | zero_width_split_phone | 1 | 0 | 1 | 0.0% | 2 |
| destructive | zero_width_split_phone_v2 | 1 | 0 | 1 | 0.0% | 2 |
| virtualization | code_switched_id_de_steuer | 1 | 0 | 1 | 0.0% | 2 |
| virtualization | code_switched_id_ru_snils | 1 | 1 | 0 | 100.0% | 0 |
| virtualization | code_switched_id_us_ssn | 1 | 1 | 0 | 100.0% | 0 |
| virtualization | forged_ref_token | 1 | 1 | 0 | 100.0% | 0 |
| virtualization | forged_ref_token_email | 1 | 1 | 0 | 100.0% | 0 |
| virtualization | hard_non_pii_mimic | 1 | 1 | 0 | 100.0% | 0 |
| virtualization | hard_non_pii_mimic_v2 | 1 | 1 | 0 | 100.0% | 0 |
| virtualization | prompt_injection_for_raw_pii | 2 | 2 | 0 | 100.0% | 0 |
| virtualization | prompt_injection_for_raw_pii_v2 | 1 | 1 | 0 | 100.0% | 0 |
| virtualization | tool_exception_leakage | 3 | 3 | 0 | 100.0% | 0 |
| virtualization | zero_width_split_phone | 1 | 1 | 0 | 100.0% | 0 |
| virtualization | zero_width_split_phone_v2 | 1 | 1 | 0 | 100.0% | 0 |
