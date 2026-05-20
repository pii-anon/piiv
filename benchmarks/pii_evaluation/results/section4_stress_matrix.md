# §4 Security Robustness — archetype × model matrix

Rows are attack archetypes (`prompt_injection`, `forged_ref_token`, `zero_width_split`, `code_switched`, `hard_non_pii_mimic`, `tool_exception_leakage`). Columns are the eval LLMs. Each cell summarises results across the three language slices (en + de + ru) from the §3 matrix. A cell is `—` when the model has no security-stress queries in its result set.

## Virtualization pass-rate by (archetype × model)

| Archetype | `anthropic-claude-sonnet-4.6` | `anthropic-claude-haiku-4.5` | `openai-gpt-5.4-mini` | `openai-gpt-5.4-nano` | `z-ai-glm-5.1` | `z-ai-glm-4.7` | `openai-gpt-oss-120b-free` | `z-ai-glm-4.5-air-free` |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `prompt_injection` | 100% (9/9) | 100% (9/9) | 100% (9/9) | 100% (9/9) | 100% (9/9) | 100% (9/9) | 100% (9/9) | 100% (9/9) |
| `forged_ref_token` | 100% (6/6) | 100% (6/6) | 100% (6/6) | 100% (6/6) | 100% (6/6) | 100% (6/6) | 100% (6/6) | 100% (6/6) |
| `zero_width_split` | 100% (6/6) | 100% (6/6) | 100% (6/6) | 100% (6/6) | 100% (6/6) | 100% (6/6) | 100% (6/6) | 100% (6/6) |
| `code_switched` | 89% (8/9) | 89% (8/9) | 89% (8/9) | 89% (8/9) | 89% (8/9) | 89% (8/9) | 89% (8/9) | 89% (8/9) |
| `hard_non_pii_mimic` | 100% (6/6) | 100% (6/6) | 100% (6/6) | 100% (6/6) | 100% (6/6) | 100% (6/6) | 100% (6/6) | 100% (6/6) |
| `tool_exception_leakage` | 100% (9/9) | 100% (9/9) | 100% (9/9) | 100% (9/9) | 100% (9/9) | 100% (9/9) | 100% (9/9) | 100% (9/9) |

## Raw-PII transmissions under virtualization (0 is the only acceptable value)

| Archetype | `anthropic-claude-sonnet-4.6` | `anthropic-claude-haiku-4.5` | `openai-gpt-5.4-mini` | `openai-gpt-5.4-nano` | `z-ai-glm-5.1` | `z-ai-glm-4.7` | `openai-gpt-oss-120b-free` | `z-ai-glm-4.5-air-free` |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `prompt_injection` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `forged_ref_token` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `zero_width_split` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `code_switched` | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 |
| `hard_non_pii_mimic` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `tool_exception_leakage` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## Raw-PII transmissions under unprotected baseline (reference; expected to be high)

| Archetype | `anthropic-claude-sonnet-4.6` | `anthropic-claude-haiku-4.5` | `openai-gpt-5.4-mini` | `openai-gpt-5.4-nano` | `z-ai-glm-5.1` | `z-ai-glm-4.7` | `openai-gpt-oss-120b-free` | `z-ai-glm-4.5-air-free` |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `prompt_injection` | 11 | 14 | 16 | 14 | 17 | 15 | 15 | 19 |
| `forged_ref_token` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `zero_width_split` | 12 | 12 | 11 | 11 | 12 | 12 | 12 | 11 |
| `code_switched` | 19 | 14 | 17 | 18 | 19 | 18 | 18 | 17 |
| `hard_non_pii_mimic` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `tool_exception_leakage` | 23 | 24 | 24 | 24 | 24 | 26 | 23 | 26 |
