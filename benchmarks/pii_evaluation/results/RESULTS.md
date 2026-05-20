# Paper-grade evaluation results

This directory holds **every number in the paper**. A reviewer can
cross-reference each cell in the §1/§2/§3/§4 tables against the
corresponding file below without re-running the eval.

## How the data was produced

```
bash scripts/run_paper_eval.sh --phase 1,2,3,4,5 --yes
```

Two LLM families:

- **Layer-2 detector LLMs** (used in §1 cross-source matrix):
  - `nvidia/nemotron-nano-9b-v2`
  - `qwen/qwen3.5-9b`
  - `google/gemma-3-4b-it`
  - `mistralai/ministral-3b-2512`
- **Layer-2 detector LLMs** (used in §2 curated-benchmark ablation):
  - `nvidia/nemotron-nano-9b-v2:free`
  - `qwen/qwen3.5-9b`
  - `mistralai/ministral-3b-2512`
- **Eval LLMs** (used as the §3 agent):
  - `anthropic/claude-sonnet-4.6` · `anthropic/claude-haiku-4.5`
  - `openai/gpt-5.4-mini` · `openai/gpt-5.4-nano`
  - `z-ai/glm-5.1` · `z-ai/glm-4.7`
  - `openai/gpt-oss-120b:free` · `z-ai/glm-4.5-air:free`

All LLM calls go through OpenRouter (`https://openrouter.ai/api/v1`).
Cell-level resume is filename-keyed — re-running the script picks up
exactly where a prior run left off.

## Dataset SHA (frozen)

```
data/dataset_v1.sha256: cd899a0334023f0a0331bb3454fc49b07576167a77a0ea03ac2c23b71e94a0da
```

Verify with:

```
python -m benchmarks.pii_evaluation.dataset.render --check
```

## Directory layout

### Per-section paper tables (read these first)

| File | Section | Description |
|---|---|---|
| `section2_ablation_matrix.md` | §2 | Combined detector ablation — 7 paper-reported configurations on the 309-query trilingual eval-bench |
| `section3_matrix.md` | §3 | Per-model headline + per-(model × language) detail — 8 LLMs × 3 langs × 3 pipelines |
| `section3_forensics.md` | §3 | Distinct virtualization-leak triples + tool-call failure breakdown per cell |
| `section4_stress_matrix.md` | §4 | Archetype × model security-robustness matrix (`prompt_injection`, `forged_ref_token`, `zero_width_split`, `code_switched`, `hard_non_pii_mimic`, `tool_exception_leakage`) |

### Per-cell sources

| Pattern | Section | Cells | Notes |
|---|---|---:|---|
| `imported_eval_<dataset>__<detector>.md` | §1 | 21 | Three cross-source datasets (`nemotron_en`, `ai4privacy_de`, `wolframko_ru`) × 7 detector configs each (regex_only, regex_presidio, regex_opf, 4 regex_llm). 95% bootstrap CIs in every cell. |
| `detector_ablation_*.{json,md}` | §2 | 4 paper rows + 3 LLM rows | One non-LLM lineup file (`ablation`) covering `regex_only` + `regex_opf_base` + `regex_opf_routed` + `regex_presidio`, plus the three LLM-detector files reported in the paper table. |
| `results_<model>__opf-<lang>.{json,md}` | §3 | 48 | 8 eval LLMs × 3 languages = 24 cells, each as JSON + Markdown. Each .json is ~1.3 MB and contains the full per-query transcripts, tool invocations, latency, and PII boundary counts. |
| `stress_report_<model>__opf-<lang>.md` | §4 | 24 | Per-cell archetype pass-rate pivot. |
| `run_<model>__opf-<lang>.log` | §3 | 24 | Per-cell stdout/stderr stream (per-scenario summary lines + any retry/recovery messages). |

## Reading any cell directly

Each §3 `.md` includes (in this order): detector configuration, end-to-end
metrics (Table 1), detection sanity-check P/R/F1 (Table 2), per-language
detection (Table 2a), per-length-bucket detection (Table 2b), argument
fidelity and cross-turn stability (Table 3), latency contributions
(Table 4), and the per-archetype security stress report (Table 5).

Each `.json` is the authoritative source — every reported number in the
paper can be re-derived from these files alone.

## What's intentionally *not* checked in

- `vault_*.db` — SQLite ref-token mappings (internal pipeline state, not
  needed for verification).
- Older non-paper runs (smoke tests, pre-lineup deepseek runs, stale
  ablations from earlier dataset versions).

If you want to reproduce a single cell, delete its `results_*.{json,md}`
and re-run `scripts/run_paper_eval.sh --phase 3 --yes` — the resume
logic only refills that one cell.
