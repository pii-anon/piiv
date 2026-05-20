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
| opf_model_name | `de` |
| opf_checkpoint | `fine_tuning/runs/de-v2/checkpoint` |
| opf_policy | `de_comprehensive` |
| opf_device | `mps` |

## Table 1 — End-to-end metrics

_Note: 'Raw PII transmissions to model' is a cumulative count. It directly scans for every query's boundary PII literals, including PII introduced by tool-result fixtures, in any message handed to the LLM. Multi-turn queries replay history on every iteration, so a single value can be counted multiple times. The intended interpretation is 'how often did raw PII cross the trust boundary?', not 'how many distinct values leaked?'. The scan is detector-independent, so detector misses still count as leaks. P/R/rate cells carry 95% bootstrap CIs (1000 resamples, seed=42) when per-query atoms are available._

| Configuration | Tool-call success | Raw PII transmissions to model | Median latency (s) | p95 latency (s) | Leak-guard triggers |
|---|---|---|---|---|---|
| baseline | 97.5% [93.7%, 100.0%] | 791 [607, 956] | 7.49 [7.11, 8.92] | 20.21 [17.18, 20.56] | 0.0% [0.0%, 0.0%] |
| destructive | 58.2% [46.8%, 69.6%] | 406 [264, 544] | 7.20 [6.55, 8.07] | 14.22 [12.03, 21.80] | 0.0% [0.0%, 0.0%] |
| virtualization | 98.7% [94.9%, 100.0%] | 2 [0, 5] | 10.74 [9.78, 11.54] | 25.17 [21.95, 27.81] | 0.0% [0.0%, 0.0%] |

## Table 2 — Detection sanity check

_Per-detector P/R against the full-framework task dataset. **Macro** is the unweighted mean of the per-tag P/R rows — useful for comparing detector classes; sensitive to small-support tags (e.g. the security-stress code-switched bucket contributes 1-sample tags that drag the mean). **Micro** is support-weighted (``sum(tp) / sum(tp+fp)``), so each detected span contributes equally regardless of which tag it falls under — preferred when comparing two detectors on the same dataset. Cells carry 95% bootstrap CIs (1000 resamples, seed=42) when per-query records are available._

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[CARD]` | 0.889 [0.636, 1.000] | 1.000 [1.000, 1.000] | 0.941 [0.778, 1.000] | 8 | 1 | 0 | 8 |
| `[DATE]` | 0.167 [0.000, 0.500] | 1.000 [0.000, 1.000] | 0.286 [0.000, 0.667] | 1 | 5 | 0 | 1 |
| `[DE_STEUER_ID]` | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0 | 0 | 7 | 7 |
| `[EMAIL]` | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 26 | 0 | 0 | 26 |
| `[IBAN]` | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1 | 0 | 0 | 1 |
| `[IP]` | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1 | 0 | 0 | 1 |
| `[LICENSE_PLATE]` | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0 | 0 | 1 | 1 |
| `[PERSONAL_ID]` | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0 | 0 | 1 | 1 |
| `[PERSON_NAME]` | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0 | 0 | 10 | 10 |
| `[PHONE]` | 0.857 [0.643, 1.000] | 0.273 [0.146, 0.408] | 0.414 [0.240, 0.563] | 12 | 2 | 32 | 44 |
| `[RU_SNILS]` | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0 | 0 | 1 | 1 |
| `[STREET_ADDRESS]` | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0 | 0 | 1 | 1 |
| `[URL]` | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1 | 0 | 0 | 1 |
| `[VIN]` | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1 | 0 | 0 | 1 |
| **macro** | 0.494 [0.246, 0.510] | 0.519 [0.230, 0.523] | 0.506 [0.238, 0.516] | 51 | 8 | 53 | 104 |
| **micro** | 0.864 [0.778, 0.948] | 0.490 [0.389, 0.598] | 0.626 [0.529, 0.715] | 51 | 8 | 53 | 104 |

## Table 2a — Detection P/R per (language × placeholder)


### Language: `de`

| Detector | Precision | Recall | TP | FP | FN | Support |
|---|---:|---:|---:|---:|---:|---:|
| `[CARD]` | 0.889 | 1.000 | 8 | 1 | 0 | 8 |
| `[DATE]` | 0.167 | 1.000 | 1 | 5 | 0 | 1 |
| `[DE_STEUER_ID]` | 0.000 | 0.000 | 0 | 0 | 7 | 7 |
| `[EMAIL]` | 1.000 | 1.000 | 26 | 0 | 0 | 26 |
| `[IBAN]` | 1.000 | 1.000 | 1 | 0 | 0 | 1 |
| `[IP]` | 1.000 | 1.000 | 1 | 0 | 0 | 1 |
| `[LICENSE_PLATE]` | 0.000 | 0.000 | 0 | 0 | 1 | 1 |
| `[PERSONAL_ID]` | 0.000 | 0.000 | 0 | 0 | 1 | 1 |
| `[PERSON_NAME]` | 0.000 | 0.000 | 0 | 0 | 10 | 10 |
| `[PHONE]` | 0.857 | 0.273 | 12 | 2 | 32 | 44 |
| `[RU_SNILS]` | 0.000 | 0.000 | 0 | 0 | 1 | 1 |
| `[STREET_ADDRESS]` | 0.000 | 0.000 | 0 | 0 | 1 | 1 |
| `[URL]` | 1.000 | 1.000 | 1 | 0 | 0 | 1 |
| `[VIN]` | 1.000 | 1.000 | 1 | 0 | 0 | 1 |
| **macro avg** | **0.494** | **0.519** | — | — | — | — |
| **micro avg** | **0.864** | **0.490** | 51 | 8 | 53 | 104 |

## Table 2b — Detection P/R by length bucket × language × placeholder

_Length buckets: ``sentence`` (single short line), ``paragraph`` (multi-line, no blank-line separator), ``multi_paragraph`` (has blank-line separator), ``structured`` (markdown table pipes, tab-aligned, or ≥3 colon-and-space lines — log/key-value text)._

| Length bucket | Lang | Detector | P | R | TP | FP | FN | Support |
|---|---|---|---:|---:|---:|---:|---:|---:|
| paragraph | de | `[DATE]` | 0.000 | 0.000 | 0 | 2 | 0 | 0 |
| paragraph | de | `[EMAIL]` | 1.000 | 1.000 | 10 | 0 | 0 | 10 |
| paragraph | de | `[PERSON_NAME]` | 0.000 | 0.000 | 0 | 0 | 2 | 2 |
| paragraph | de | `[PHONE]` | 1.000 | 0.278 | 5 | 0 | 13 | 18 |
| paragraph | de | `[STREET_ADDRESS]` | 0.000 | 0.000 | 0 | 0 | 1 | 1 |
| paragraph | de | **micro** | **0.882** | **0.484** | 15 | 2 | 16 | 31 |
| sentence | de | `[CARD]` | 0.889 | 1.000 | 8 | 1 | 0 | 8 |
| sentence | de | `[DATE]` | 0.250 | 1.000 | 1 | 3 | 0 | 1 |
| sentence | de | `[DE_STEUER_ID]` | 0.000 | 0.000 | 0 | 0 | 7 | 7 |
| sentence | de | `[EMAIL]` | 1.000 | 1.000 | 16 | 0 | 0 | 16 |
| sentence | de | `[IBAN]` | 1.000 | 1.000 | 1 | 0 | 0 | 1 |
| sentence | de | `[IP]` | 1.000 | 1.000 | 1 | 0 | 0 | 1 |
| sentence | de | `[LICENSE_PLATE]` | 0.000 | 0.000 | 0 | 0 | 1 | 1 |
| sentence | de | `[PERSONAL_ID]` | 0.000 | 0.000 | 0 | 0 | 1 | 1 |
| sentence | de | `[PERSON_NAME]` | 0.000 | 0.000 | 0 | 0 | 8 | 8 |
| sentence | de | `[PHONE]` | 0.778 | 0.269 | 7 | 2 | 19 | 26 |
| sentence | de | `[RU_SNILS]` | 0.000 | 0.000 | 0 | 0 | 1 | 1 |
| sentence | de | `[URL]` | 1.000 | 1.000 | 1 | 0 | 0 | 1 |
| sentence | de | `[VIN]` | 1.000 | 1.000 | 1 | 0 | 0 | 1 |
| sentence | de | **micro** | **0.857** | **0.493** | 36 | 6 | 37 | 73 |

## Table 3 — Argument fidelity and cross-turn stability

| Configuration | Argument exact match | Argument partial match | Cross-turn token stability |
|---|---|---|---|
| baseline | 97.5% | 100.0% | 100.0% |
| destructive | 50.6% | 57.0% | 100.0% |
| virtualization | 98.7% | 98.7% | 68.2% |

## Table 4 — Per-(config × bucket × language)

| Config | Bucket | Lang | n | Tool success | Raw PII | Median latency (s) | Leak triggers |
|---|---|---|---|---|---|---|---|
| baseline | hard_negative | de | 12 | 0.0% | 0 | 13.27 | 0.0% |
| baseline | multi_pii | de | 14 | 100.0% | 129 | 8.96 | 0.0% |
| baseline | multi_turn | de | 22 | 100.0% | 496 | 11.49 | 0.0% |
| baseline | no_pii_control | de | 10 | 100.0% | 0 | 5.36 | 0.0% |
| baseline | security_stress | de | 15 | 100.0% | 23 | 7.14 | 0.0% |
| baseline | single_turn | de | 30 | 93.3% | 143 | 7.01 | 0.0% |
| destructive | hard_negative | de | 12 | 0.0% | 0 | 4.65 | 0.0% |
| destructive | multi_pii | de | 14 | 42.9% | 58 | 8.50 | 0.0% |
| destructive | multi_turn | de | 22 | 50.0% | 251 | 9.51 | 0.0% |
| destructive | no_pii_control | de | 10 | 100.0% | 0 | 5.19 | 0.0% |
| destructive | security_stress | de | 15 | 100.0% | 11 | 7.47 | 0.0% |
| destructive | single_turn | de | 30 | 53.3% | 86 | 7.24 | 0.0% |
| virtualization | hard_negative | de | 12 | 0.0% | 0 | 7.74 | 0.0% |
| virtualization | multi_pii | de | 14 | 100.0% | 0 | 12.90 | 0.0% |
| virtualization | multi_turn | de | 22 | 100.0% | 0 | 16.94 | 0.0% |
| virtualization | no_pii_control | de | 10 | 100.0% | 0 | 7.84 | 0.0% |
| virtualization | security_stress | de | 15 | 100.0% | 0 | 9.56 | 0.0% |
| virtualization | single_turn | de | 30 | 96.7% | 2 | 10.53 | 0.0% |

## Table 6 — Per-detector latency contribution

_Wall-clock seconds spent inside each detector across the run. ``regex`` is the first-pass detector; ``second_pass_*`` rows are the optional NER / generative LM layers. Production hot paths are unaffected — the recorder is benchmark-only._

| Detector | Calls | Total (s) | Mean (ms) | p95 (ms) |
|---|---:|---:|---:|---:|
| `regex` | 1121 | 0.136 | 0.121 | 0.530 |
| `second_pass_OPFPIIDetector` | 368 | 407.504 | 1107.348 | 2805.761 |

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
| destructive | prompt_injection_for_raw_pii | 2 | 1 | 1 | 50.0% | 1 |
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
