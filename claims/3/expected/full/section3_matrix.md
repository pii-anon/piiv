## §3 Full Framework — per-model summary (all languages)

| Model | Pipeline | N | TSR | Arg-EM | PII→model | Leak-guard |
|---|---|---:|---:|---:|---:|---:|
| `anthropic-claude-sonnet-4.6` | baseline | 309 |  93.2% |  93.2% |  2258 |   0.0% |
| `anthropic-claude-sonnet-4.6` | destructive | 309 |  31.2% |  30.8% |   550 |   0.0% |
| `anthropic-claude-sonnet-4.6` | virtualization | 309 |  95.8% |  95.8% |     7 |   0.0% |
| `anthropic-claude-haiku-4.5` | baseline | 309 |  91.6% |  91.6% |  2163 |   0.0% |
| `anthropic-claude-haiku-4.5` | destructive | 309 |  32.5% |  31.6% |   522 |   0.0% |
| `anthropic-claude-haiku-4.5` | virtualization | 309 |  71.3% |  71.3% |     4 |   0.0% |
| `openai-gpt-5.4-mini` | baseline | 309 |  92.0% |  92.0% |  2119 |   0.0% |
| `openai-gpt-5.4-mini` | destructive | 309 |  39.2% |  34.2% |   554 |   0.0% |
| `openai-gpt-5.4-mini` | virtualization | 309 |  93.7% |  93.7% |    12 |   0.0% |
| `openai-gpt-5.4-nano` | baseline | 309 |  90.3% |  90.3% |  2176 |   0.0% |
| `openai-gpt-5.4-nano` | destructive | 309 |  32.9% |  29.5% |   492 |   0.0% |
| `openai-gpt-5.4-nano` | virtualization | 309 |  93.7% |  93.7% |     9 |   0.0% |
| `z-ai-glm-5.1` | baseline | 309 |  96.2% |  96.2% |  2311 |   0.0% |
| `z-ai-glm-5.1` | destructive | 309 |  37.1% |  32.9% |   584 |   0.0% |
| `z-ai-glm-5.1` | virtualization | 309 |  97.0% |  97.0% |    11 |   0.0% |
| `z-ai-glm-4.7` | baseline | 309 |  94.9% |  94.9% |  2253 |   0.0% |
| `z-ai-glm-4.7` | destructive | 309 |  36.3% |  32.9% |   576 |   0.0% |
| `z-ai-glm-4.7` | virtualization | 309 |  89.5% |  89.5% |     7 |   0.0% |
| `openai-gpt-oss-120b-free` | baseline | 309 |  94.9% |  94.9% |  2066 |   0.0% |
| `openai-gpt-oss-120b-free` | destructive | 309 |  39.7% |  34.6% |   516 |   0.0% |
| `openai-gpt-oss-120b-free` | virtualization | 309 |  93.2% |  93.2% |     8 |   0.0% |
| `z-ai-glm-4.5-air-free` | baseline | 309 |  85.2% |  85.2% |  2285 |   0.0% |
| `z-ai-glm-4.5-air-free` | destructive | 309 |  30.8% |  27.8% |   504 |   0.0% |
| `z-ai-glm-4.5-air-free` | virtualization | 309 |  89.5% |  89.5% |     7 |   0.0% |

## §3 Headline — virtualization framework vs unprotected baseline

| Model | Lang | Baseline TSR | Virt TSR | Δ TSR | Destr TSR | Virt vs Destr |
|---|---|---:|---:|---:|---:|---:|
| `anthropic-claude-sonnet-4.6` | en |  94.9% |  92.4% |  -2.5pp |  25.3% | +67.1pp |
| `anthropic-claude-sonnet-4.6` | de |  93.7% |  97.5% |  +3.8pp |  46.8% | +50.6pp |
| `anthropic-claude-sonnet-4.6` | ru |  91.1% |  97.5% |  +6.3pp |  21.5% | +75.9pp |
| `anthropic-claude-haiku-4.5` | en |  91.1% |  82.3% |  -8.9pp |  25.3% | +57.0pp |
| `anthropic-claude-haiku-4.5` | de |  93.7% |  78.5% | -15.2pp |  50.6% | +27.8pp |
| `anthropic-claude-haiku-4.5` | ru |  89.9% |  53.2% | -36.7pp |  21.5% | +31.6pp |
| `openai-gpt-5.4-mini` | en |  94.9% |  93.7% |  -1.3pp |  31.6% | +62.0pp |
| `openai-gpt-5.4-mini` | de |  93.7% |  93.7% |  +0.0pp |  59.5% | +34.2pp |
| `openai-gpt-5.4-mini` | ru |  87.3% |  93.7% |  +6.3pp |  26.6% | +67.1pp |
| `openai-gpt-5.4-nano` | en |  93.7% |  92.4% |  -1.3pp |  29.1% | +63.3pp |
| `openai-gpt-5.4-nano` | de |  88.6% |  93.7% |  +5.1pp |  49.4% | +44.3pp |
| `openai-gpt-5.4-nano` | ru |  88.6% |  94.9% |  +6.3pp |  20.3% | +74.7pp |
| `z-ai-glm-5.1` | en |  96.2% |  93.7% |  -2.5pp |  27.8% | +65.8pp |
| `z-ai-glm-5.1` | de |  97.5% |  98.7% |  +1.3pp |  58.2% | +40.5pp |
| `z-ai-glm-5.1` | ru |  94.9% |  98.7% |  +3.8pp |  25.3% | +73.4pp |
| `z-ai-glm-4.7` | en |  96.2% |  88.6% |  -7.6pp |  27.8% | +60.8pp |
| `z-ai-glm-4.7` | de |  93.7% |  91.1% |  -2.5pp |  55.7% | +35.4pp |
| `z-ai-glm-4.7` | ru |  94.9% |  88.6% |  -6.3pp |  25.3% | +63.3pp |
| `openai-gpt-oss-120b-free` | en |  94.9% |  89.9% |  -5.1pp |  30.4% | +59.5pp |
| `openai-gpt-oss-120b-free` | de |  93.7% |  96.2% |  +2.5pp |  60.8% | +35.4pp |
| `openai-gpt-oss-120b-free` | ru |  96.2% |  93.7% |  -2.5pp |  27.8% | +65.8pp |
| `z-ai-glm-4.5-air-free` | en |  94.9% |  91.1% |  -3.8pp |  24.1% | +67.1pp |
| `z-ai-glm-4.5-air-free` | de |  82.3% |  92.4% | +10.1pp |  44.3% | +48.1pp |
| `z-ai-glm-4.5-air-free` | ru |  78.5% |  84.8% |  +6.3pp |  24.1% | +60.8pp |

## §3 Full Framework — per-(model, language) detail

| Model | Lang | Pipeline | N | TSR | Arg-EM | PII→model | Leak-guard |
|---|---|---|---:|---:|---:|---:|---:|
| `anthropic-claude-sonnet-4.6` | en | baseline | 103 |  94.9% |  94.9% |   764 |   0.0% |
| `anthropic-claude-sonnet-4.6` | en | destructive | 103 |  25.3% |  24.1% |    96 |   0.0% |
| `anthropic-claude-sonnet-4.6` | en | virtualization | 103 |  92.4% |  92.4% |     6 |   0.0% |
| `anthropic-claude-sonnet-4.6` | de | baseline | 103 |  93.7% |  93.7% |   796 |   0.0% |
| `anthropic-claude-sonnet-4.6` | de | destructive | 103 |  46.8% |  46.8% |   372 |   0.0% |
| `anthropic-claude-sonnet-4.6` | de | virtualization | 103 |  97.5% |  97.5% |     1 |   0.0% |
| `anthropic-claude-sonnet-4.6` | ru | baseline | 103 |  91.1% |  91.1% |   698 |   0.0% |
| `anthropic-claude-sonnet-4.6` | ru | destructive | 103 |  21.5% |  21.5% |    82 |   0.0% |
| `anthropic-claude-sonnet-4.6` | ru | virtualization | 103 |  97.5% |  97.5% |     0 |   0.0% |
| `anthropic-claude-haiku-4.5` | en | baseline | 103 |  91.1% |  91.1% |   726 |   0.0% |
| `anthropic-claude-haiku-4.5` | en | destructive | 103 |  25.3% |  24.1% |    89 |   0.0% |
| `anthropic-claude-haiku-4.5` | en | virtualization | 103 |  82.3% |  82.3% |     3 |   0.0% |
| `anthropic-claude-haiku-4.5` | de | baseline | 103 |  93.7% |  93.7% |   741 |   0.0% |
| `anthropic-claude-haiku-4.5` | de | destructive | 103 |  50.6% |  49.4% |   355 |   0.0% |
| `anthropic-claude-haiku-4.5` | de | virtualization | 103 |  78.5% |  78.5% |     1 |   0.0% |
| `anthropic-claude-haiku-4.5` | ru | baseline | 103 |  89.9% |  89.9% |   696 |   0.0% |
| `anthropic-claude-haiku-4.5` | ru | destructive | 103 |  21.5% |  21.5% |    78 |   0.0% |
| `anthropic-claude-haiku-4.5` | ru | virtualization | 103 |  53.2% |  53.2% |     0 |   0.0% |
| `openai-gpt-5.4-mini` | en | baseline | 103 |  94.9% |  94.9% |   731 |   0.0% |
| `openai-gpt-5.4-mini` | en | destructive | 103 |  31.6% |  27.8% |    94 |   0.0% |
| `openai-gpt-5.4-mini` | en | virtualization | 103 |  93.7% |  93.7% |    11 |   0.0% |
| `openai-gpt-5.4-mini` | de | baseline | 103 |  93.7% |  93.7% |   722 |   0.0% |
| `openai-gpt-5.4-mini` | de | destructive | 103 |  59.5% |  51.9% |   379 |   0.0% |
| `openai-gpt-5.4-mini` | de | virtualization | 103 |  93.7% |  93.7% |     1 |   0.0% |
| `openai-gpt-5.4-mini` | ru | baseline | 103 |  87.3% |  87.3% |   666 |   0.0% |
| `openai-gpt-5.4-mini` | ru | destructive | 103 |  26.6% |  22.8% |    81 |   0.0% |
| `openai-gpt-5.4-mini` | ru | virtualization | 103 |  93.7% |  93.7% |     0 |   0.0% |
| `openai-gpt-5.4-nano` | en | baseline | 103 |  93.7% |  93.7% |   724 |   0.0% |
| `openai-gpt-5.4-nano` | en | destructive | 103 |  29.1% |  26.6% |    81 |   0.0% |
| `openai-gpt-5.4-nano` | en | virtualization | 103 |  92.4% |  92.4% |     8 |   0.0% |
| `openai-gpt-5.4-nano` | de | baseline | 103 |  88.6% |  88.6% |   729 |   0.0% |
| `openai-gpt-5.4-nano` | de | destructive | 103 |  49.4% |  44.3% |   339 |   0.0% |
| `openai-gpt-5.4-nano` | de | virtualization | 103 |  93.7% |  93.7% |     1 |   0.0% |
| `openai-gpt-5.4-nano` | ru | baseline | 103 |  88.6% |  88.6% |   723 |   0.0% |
| `openai-gpt-5.4-nano` | ru | destructive | 103 |  20.3% |  17.7% |    72 |   0.0% |
| `openai-gpt-5.4-nano` | ru | virtualization | 103 |  94.9% |  94.9% |     0 |   0.0% |
| `z-ai-glm-5.1` | en | baseline | 103 |  96.2% |  96.2% |   754 |   0.0% |
| `z-ai-glm-5.1` | en | destructive | 103 |  27.8% |  25.3% |    92 |   0.0% |
| `z-ai-glm-5.1` | en | virtualization | 103 |  93.7% |  93.7% |     9 |   0.0% |
| `z-ai-glm-5.1` | de | baseline | 103 |  97.5% |  97.5% |   791 |   0.0% |
| `z-ai-glm-5.1` | de | destructive | 103 |  58.2% |  50.6% |   406 |   0.0% |
| `z-ai-glm-5.1` | de | virtualization | 103 |  98.7% |  98.7% |     2 |   0.0% |
| `z-ai-glm-5.1` | ru | baseline | 103 |  94.9% |  94.9% |   766 |   0.0% |
| `z-ai-glm-5.1` | ru | destructive | 103 |  25.3% |  22.8% |    86 |   0.0% |
| `z-ai-glm-5.1` | ru | virtualization | 103 |  98.7% |  98.7% |     0 |   0.0% |
| `z-ai-glm-4.7` | en | baseline | 103 |  96.2% |  96.2% |   761 |   0.0% |
| `z-ai-glm-4.7` | en | destructive | 103 |  27.8% |  26.6% |    99 |   0.0% |
| `z-ai-glm-4.7` | en | virtualization | 103 |  88.6% |  88.6% |     5 |   0.0% |
| `z-ai-glm-4.7` | de | baseline | 103 |  93.7% |  93.7% |   757 |   0.0% |
| `z-ai-glm-4.7` | de | destructive | 103 |  55.7% |  50.6% |   391 |   0.0% |
| `z-ai-glm-4.7` | de | virtualization | 103 |  91.1% |  91.1% |     2 |   0.0% |
| `z-ai-glm-4.7` | ru | baseline | 103 |  94.9% |  94.9% |   735 |   0.0% |
| `z-ai-glm-4.7` | ru | destructive | 103 |  25.3% |  21.5% |    86 |   0.0% |
| `z-ai-glm-4.7` | ru | virtualization | 103 |  88.6% |  88.6% |     0 |   0.0% |
| `openai-gpt-oss-120b-free` | en | baseline | 103 |  94.9% |  94.9% |   695 |   0.0% |
| `openai-gpt-oss-120b-free` | en | destructive | 103 |  30.4% |  26.6% |    90 |   0.0% |
| `openai-gpt-oss-120b-free` | en | virtualization | 103 |  89.9% |  89.9% |     7 |   0.0% |
| `openai-gpt-oss-120b-free` | de | baseline | 103 |  93.7% |  93.7% |   683 |   0.0% |
| `openai-gpt-oss-120b-free` | de | destructive | 103 |  60.8% |  53.2% |   342 |   0.0% |
| `openai-gpt-oss-120b-free` | de | virtualization | 103 |  96.2% |  96.2% |     1 |   0.0% |
| `openai-gpt-oss-120b-free` | ru | baseline | 103 |  96.2% |  96.2% |   688 |   0.0% |
| `openai-gpt-oss-120b-free` | ru | destructive | 103 |  27.8% |  24.1% |    84 |   0.0% |
| `openai-gpt-oss-120b-free` | ru | virtualization | 103 |  93.7% |  93.7% |     0 |   0.0% |
| `z-ai-glm-4.5-air-free` | en | baseline | 103 |  94.9% |  94.9% |   828 |   0.0% |
| `z-ai-glm-4.5-air-free` | en | destructive | 103 |  24.1% |  24.1% |   104 |   0.0% |
| `z-ai-glm-4.5-air-free` | en | virtualization | 103 |  91.1% |  91.1% |     6 |   0.0% |
| `z-ai-glm-4.5-air-free` | de | baseline | 103 |  82.3% |  82.3% |   779 |   0.0% |
| `z-ai-glm-4.5-air-free` | de | destructive | 103 |  44.3% |  39.2% |   314 |   0.0% |
| `z-ai-glm-4.5-air-free` | de | virtualization | 103 |  92.4% |  92.4% |     1 |   0.0% |
| `z-ai-glm-4.5-air-free` | ru | baseline | 103 |  78.5% |  78.5% |   678 |   0.0% |
| `z-ai-glm-4.5-air-free` | ru | destructive | 103 |  24.1% |  20.3% |    86 |   0.0% |
| `z-ai-glm-4.5-air-free` | ru | virtualization | 103 |  84.8% |  84.8% |     0 |   0.0% |
