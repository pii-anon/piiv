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
| baseline | 96.2% [91.1%, 100.0%] | 761 [584, 923] | 2.86 [2.65, 3.25] | 7.25 [5.00, 11.95] | 0.0% [0.0%, 0.0%] |
| destructive | 27.8% [19.0%, 38.0%] | 99 [51, 162] | 2.42 [2.23, 2.55] | 4.66 [3.97, 4.86] | 0.0% [0.0%, 0.0%] |
| virtualization | 88.6% [81.0%, 94.9%] | 5 [0, 11] | 6.20 [5.57, 6.86] | 11.34 [10.70, 15.60] | 0.0% [0.0%, 0.0%] |

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
| baseline | 96.2% | 97.5% | 100.0% |
| destructive | 26.6% | 26.6% | 100.0% |
| virtualization | 88.6% | 89.9% | 68.2% |

## Table 4 — Per-(config × bucket × language)

| Config | Bucket | Lang | n | Tool success | Raw PII | Median latency (s) | Leak triggers |
|---|---|---|---|---|---|---|---|
| baseline | hard_negative | en | 12 | 0.0% | 0 | 1.82 | 0.0% |
| baseline | multi_pii | en | 14 | 92.9% | 138 | 3.66 | 0.0% |
| baseline | multi_turn | en | 22 | 100.0% | 462 | 4.35 | 0.0% |
| baseline | no_pii_control | en | 10 | 100.0% | 0 | 4.71 | 0.0% |
| baseline | security_stress | en | 15 | 100.0% | 22 | 2.33 | 0.0% |
| baseline | single_turn | en | 30 | 93.3% | 139 | 2.57 | 0.0% |
| destructive | hard_negative | en | 12 | 0.0% | 0 | 1.74 | 0.0% |
| destructive | multi_pii | en | 14 | 7.1% | 18 | 2.31 | 0.0% |
| destructive | multi_turn | en | 22 | 9.1% | 33 | 3.79 | 0.0% |
| destructive | no_pii_control | en | 10 | 100.0% | 0 | 2.52 | 0.0% |
| destructive | security_stress | en | 15 | 33.3% | 10 | 2.15 | 0.0% |
| destructive | single_turn | en | 30 | 26.7% | 38 | 2.35 | 0.0% |
| virtualization | hard_negative | en | 12 | 0.0% | 0 | 3.24 | 0.0% |
| virtualization | multi_pii | en | 14 | 64.3% | 1 | 6.07 | 0.0% |
| virtualization | multi_turn | en | 22 | 100.0% | 0 | 10.01 | 0.0% |
| virtualization | no_pii_control | en | 10 | 100.0% | 0 | 7.42 | 0.0% |
| virtualization | security_stress | en | 15 | 100.0% | 2 | 4.62 | 0.0% |
| virtualization | single_turn | en | 30 | 86.7% | 2 | 6.11 | 0.0% |

## Table 6 — Per-detector latency contribution

_Wall-clock seconds spent inside each detector across the run. ``regex`` is the first-pass detector; ``second_pass_*`` rows are the optional NER / generative LM layers. Production hot paths are unaffected — the recorder is benchmark-only._

| Detector | Calls | Total (s) | Mean (ms) | p95 (ms) |
|---|---:|---:|---:|---:|
| `regex` | 1081 | 0.136 | 0.126 | 0.525 |
| `second_pass_OPFPIIDetector` | 354 | 376.232 | 1062.803 | 2860.911 |

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
| baseline | prompt_injection_for_raw_pii | 2 | 0 | 2 | 0.0% | 3 |
| baseline | prompt_injection_for_raw_pii_v2 | 1 | 0 | 1 | 0.0% | 1 |
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
