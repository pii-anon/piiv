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
| opf_model_name | `ru` |
| opf_checkpoint | `fine_tuning/runs/ru-v2/checkpoint` |
| opf_policy | `ru_comprehensive` |
| opf_device | `mps` |

## Table 1 — End-to-end metrics

_Note: 'Raw PII transmissions to model' is a cumulative count. It directly scans for every query's boundary PII literals, including PII introduced by tool-result fixtures, in any message handed to the LLM. Multi-turn queries replay history on every iteration, so a single value can be counted multiple times. The intended interpretation is 'how often did raw PII cross the trust boundary?', not 'how many distinct values leaked?'. The scan is detector-independent, so detector misses still count as leaks. P/R/rate cells carry 95% bootstrap CIs (1000 resamples, seed=42) when per-query atoms are available._

| Configuration | Tool-call success | Raw PII transmissions to model | Median latency (s) | p95 latency (s) | Leak-guard triggers |
|---|---|---|---|---|---|
| baseline | 94.9% [89.9%, 98.7%] | 735 [565, 889] | 5.23 [4.59, 5.80] | 12.16 [8.98, 13.95] | 0.0% [0.0%, 0.0%] |
| destructive | 25.3% [16.5%, 36.7%] | 86 [38, 143] | 4.28 [3.80, 4.65] | 10.89 [8.30, 12.98] | 0.0% [0.0%, 0.0%] |
| virtualization | 88.6% [81.0%, 94.9%] | 0 [0, 0] | 8.17 [7.39, 8.98] | 17.48 [14.09, 18.42] | 0.0% [0.0%, 0.0%] |

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
| `[LICENSE_PLATE]` | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1 | 0 | 0 | 1 |
| `[PERSONAL_ID]` | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0 | 0 | 2 | 2 |
| `[PERSON_NAME]` | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0 | 0 | 10 | 10 |
| `[PHONE]` | 0.955 [0.881, 1.000] | 0.955 [0.884, 1.000] | 0.955 [0.899, 0.989] | 42 | 2 | 2 | 44 |
| `[RU_SNILS]` | 1.000 [0.000, 1.000] | 0.333 [0.000, 0.800] | 0.500 [0.000, 0.889] | 2 | 0 | 4 | 6 |
| `[STREET_ADDRESS]` | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0 | 0 | 1 | 1 |
| `[URL]` | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1 | 0 | 0 | 1 |
| `[VIN]` | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1 | 0 | 0 | 1 |
| **macro** | 0.652 [0.353, 0.656] | 0.663 [0.350, 0.665] | 0.657 [0.336, 0.661] | 84 | 7 | 20 | 104 |
| **micro** | 0.923 [0.871, 0.975] | 0.808 [0.724, 0.878] | 0.862 [0.807, 0.908] | 84 | 7 | 20 | 104 |

## Table 2a — Detection P/R per (language × placeholder)


### Language: `ru`

| Detector | Precision | Recall | TP | FP | FN | Support |
|---|---:|---:|---:|---:|---:|---:|
| `[CARD]` | 1.000 | 1.000 | 8 | 0 | 0 | 8 |
| `[DATE]` | 0.167 | 1.000 | 1 | 5 | 0 | 1 |
| `[DE_STEUER_ID]` | 0.000 | 0.000 | 0 | 0 | 1 | 1 |
| `[EMAIL]` | 1.000 | 1.000 | 26 | 0 | 0 | 26 |
| `[IBAN]` | 1.000 | 1.000 | 1 | 0 | 0 | 1 |
| `[IP]` | 1.000 | 1.000 | 1 | 0 | 0 | 1 |
| `[LICENSE_PLATE]` | 1.000 | 1.000 | 1 | 0 | 0 | 1 |
| `[PERSONAL_ID]` | 0.000 | 0.000 | 0 | 0 | 2 | 2 |
| `[PERSON_NAME]` | 0.000 | 0.000 | 0 | 0 | 10 | 10 |
| `[PHONE]` | 0.955 | 0.955 | 42 | 2 | 2 | 44 |
| `[RU_SNILS]` | 1.000 | 0.333 | 2 | 0 | 4 | 6 |
| `[STREET_ADDRESS]` | 0.000 | 0.000 | 0 | 0 | 1 | 1 |
| `[URL]` | 1.000 | 1.000 | 1 | 0 | 0 | 1 |
| `[VIN]` | 1.000 | 1.000 | 1 | 0 | 0 | 1 |
| **macro avg** | **0.652** | **0.663** | — | — | — | — |
| **micro avg** | **0.923** | **0.808** | 84 | 7 | 20 | 104 |

## Table 2b — Detection P/R by length bucket × language × placeholder

_Length buckets: ``sentence`` (single short line), ``paragraph`` (multi-line, no blank-line separator), ``multi_paragraph`` (has blank-line separator), ``structured`` (markdown table pipes, tab-aligned, or ≥3 colon-and-space lines — log/key-value text)._

| Length bucket | Lang | Detector | P | R | TP | FP | FN | Support |
|---|---|---|---:|---:|---:|---:|---:|---:|
| paragraph | ru | `[DATE]` | 0.000 | 0.000 | 0 | 2 | 0 | 0 |
| paragraph | ru | `[EMAIL]` | 1.000 | 1.000 | 10 | 0 | 0 | 10 |
| paragraph | ru | `[PERSON_NAME]` | 0.000 | 0.000 | 0 | 0 | 2 | 2 |
| paragraph | ru | `[PHONE]` | 1.000 | 1.000 | 18 | 0 | 0 | 18 |
| paragraph | ru | `[STREET_ADDRESS]` | 0.000 | 0.000 | 0 | 0 | 1 | 1 |
| paragraph | ru | **micro** | **0.933** | **0.903** | 28 | 2 | 3 | 31 |
| sentence | ru | `[CARD]` | 1.000 | 1.000 | 8 | 0 | 0 | 8 |
| sentence | ru | `[DATE]` | 0.250 | 1.000 | 1 | 3 | 0 | 1 |
| sentence | ru | `[DE_STEUER_ID]` | 0.000 | 0.000 | 0 | 0 | 1 | 1 |
| sentence | ru | `[EMAIL]` | 1.000 | 1.000 | 16 | 0 | 0 | 16 |
| sentence | ru | `[IBAN]` | 1.000 | 1.000 | 1 | 0 | 0 | 1 |
| sentence | ru | `[IP]` | 1.000 | 1.000 | 1 | 0 | 0 | 1 |
| sentence | ru | `[LICENSE_PLATE]` | 1.000 | 1.000 | 1 | 0 | 0 | 1 |
| sentence | ru | `[PERSONAL_ID]` | 0.000 | 0.000 | 0 | 0 | 2 | 2 |
| sentence | ru | `[PERSON_NAME]` | 0.000 | 0.000 | 0 | 0 | 8 | 8 |
| sentence | ru | `[PHONE]` | 0.923 | 0.923 | 24 | 2 | 2 | 26 |
| sentence | ru | `[RU_SNILS]` | 1.000 | 0.333 | 2 | 0 | 4 | 6 |
| sentence | ru | `[URL]` | 1.000 | 1.000 | 1 | 0 | 0 | 1 |
| sentence | ru | `[VIN]` | 1.000 | 1.000 | 1 | 0 | 0 | 1 |
| sentence | ru | **micro** | **0.918** | **0.767** | 56 | 5 | 17 | 73 |

## Table 3 — Argument fidelity and cross-turn stability

| Configuration | Argument exact match | Argument partial match | Cross-turn token stability |
|---|---|---|---|
| baseline | 94.9% | 98.7% | 100.0% |
| destructive | 21.5% | 27.8% | 100.0% |
| virtualization | 88.6% | 89.9% | 68.2% |

## Table 4 — Per-(config × bucket × language)

| Config | Bucket | Lang | n | Tool success | Raw PII | Median latency (s) | Leak triggers |
|---|---|---|---|---|---|---|---|
| baseline | hard_negative | ru | 12 | 0.0% | 0 | 3.55 | 0.0% |
| baseline | multi_pii | ru | 14 | 92.9% | 118 | 7.81 | 0.0% |
| baseline | multi_turn | ru | 22 | 100.0% | 454 | 8.11 | 0.0% |
| baseline | no_pii_control | ru | 10 | 100.0% | 0 | 3.80 | 0.0% |
| baseline | security_stress | ru | 15 | 100.0% | 25 | 4.93 | 0.0% |
| baseline | single_turn | ru | 30 | 90.0% | 138 | 4.33 | 0.0% |
| destructive | hard_negative | ru | 12 | 0.0% | 0 | 3.61 | 0.0% |
| destructive | multi_pii | ru | 14 | 7.1% | 12 | 4.38 | 0.0% |
| destructive | multi_turn | ru | 22 | 9.1% | 34 | 6.77 | 0.0% |
| destructive | no_pii_control | ru | 10 | 100.0% | 0 | 4.39 | 0.0% |
| destructive | security_stress | ru | 15 | 100.0% | 10 | 4.09 | 0.0% |
| destructive | single_turn | ru | 30 | 13.3% | 30 | 3.52 | 0.0% |
| virtualization | hard_negative | ru | 12 | 0.0% | 0 | 5.88 | 0.0% |
| virtualization | multi_pii | ru | 14 | 78.6% | 0 | 10.10 | 0.0% |
| virtualization | multi_turn | ru | 22 | 77.3% | 0 | 13.08 | 0.0% |
| virtualization | no_pii_control | ru | 10 | 100.0% | 0 | 6.47 | 0.0% |
| virtualization | security_stress | ru | 15 | 100.0% | 0 | 5.77 | 0.0% |
| virtualization | single_turn | ru | 30 | 96.7% | 0 | 8.23 | 0.0% |

## Table 6 — Per-detector latency contribution

_Wall-clock seconds spent inside each detector across the run. ``regex`` is the first-pass detector; ``second_pass_*`` rows are the optional NER / generative LM layers. Production hot paths are unaffected — the recorder is benchmark-only._

| Detector | Calls | Total (s) | Mean (ms) | p95 (ms) |
|---|---:|---:|---:|---:|
| `regex` | 1087 | 0.155 | 0.143 | 0.532 |
| `second_pass_OPFPIIDetector` | 349 | 393.461 | 1127.395 | 3013.039 |

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
| baseline | tool_exception_leakage | 3 | 3 | 0 | 100.0% | 9 |
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
| virtualization | code_switched_id_de_steuer | 1 | 1 | 0 | 100.0% | 0 |
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
