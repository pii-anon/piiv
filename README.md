# piiv — PII Virtualization for LLM Tool-Calling Agents

> **ACSAC 2026 submission — anonymous artifact.**
> This repository accompanies a double-blind submission. All author / institution
> identifiers have been removed; model checkpoints are hosted under an anonymous
> HuggingFace account (`pii-anon/*`). The headline numbers reported in the
> paper are reproducible end-to-end by following the *Reviewer quick start* below.

`piiv` is a runtime layer for LLM-driven agents that need to call tools with
PII arguments without exposing the raw values to the model. It detects PII,
substitutes session-scoped reference tokens, stores raw values in an
encrypted vault, rehydrates tool arguments at execution time, re-anonymizes
tool results before they re-enter the LLM, and rehydrates the final
user-facing answer.

The paper has three headline claims, each backed by a fully reproducible
evaluation:

| §  | Claim | Key result |
|----|---|---|
| §1 | Our fine-tuned OPF detector beats Microsoft Presidio (industry NER baseline) on cross-source data across three languages | Micro F1 wins on EN (+0.110), DE (+0.059), RU (+0.051) — all under projection-symmetric scoring at n=1000 per corpus |
| §2 | Layered regex + per-language OPF fine-tunes beat regex-only, base OPF, and Presidio on the 309-query trilingual eval-bench | `regex_opf_routed` micro F1 0.930, recall 0.965, precision 0.899 — strongest recall/F1 of every detector evaluated |
| §3 | The full virtualization framework sharply reduces raw-PII egress to the LLM while largely preserving tool-call utility | 17,631 → 65 raw-PII transmissions (99.63% reduction; 4–12 per model under virtualization) at a mean ΔTSR of −1.8pp across 8 LLMs × 3 languages × 309 queries |

---

## Reviewer quick start

### Smoke verification (~30 min, ~$1) — recommended starting point

Confirms every pipeline works end-to-end and that the qualitative claims hold
on reduced N. **Not paper-grade**: §1 runs at n=200/corpus (vs. n=1000 in the
paper), §2 runs only the 4 non-LLM rows (vs. 7 in the paper table), and §3
runs a single English cell at `--limit 10` queries (vs. the full 8 LLMs × 3
languages × 309 queries matrix).

```bash
bash scripts/setup.sh                  # ~10-15 min: deps + spaCy NER models + .env wizard
# Edit .env, set PII_EVAL_API_KEY=sk-or-v1-... (your OpenRouter key)
bash scripts/reproduce.sh              # ~30 min, ~$1: §1 smoke + §2 (non-LLM rows) + pytest + §3 smoke
```

### Paper-grade reproduction — for matching the PDF tables exactly

Three escalation paths, smallest to largest:

```bash
# §3 only at paper N (8 LLMs × 3 langs × 309 queries), ~16-20h, ~$20-50:
bash scripts/reproduce.sh --full-section3

# Per-claim full mode (each runs the paper-grade version of that section):
bash claims/1/run.sh --full            # §1 at n=1000 × 21 cells, ~3-4 h, ~$0.05
bash claims/2/run.sh --full            # §2 with the 3 paper-reported LLM rows
bash claims/3/run.sh --full            # §3 full matrix (same as reproduce.sh --full-section3)

# Full paper sweep across §1+§2+§3+§4 — the script that produced the frozen
# reference outputs under claims/N/expected/full/:
bash scripts/run_paper_eval.sh         # ~17-21h, ~$60-120 OpenRouter
```

All scripts are idempotent; re-running re-checks each phase and resumes any
partial work. Set `OPF_MOE_TRITON=0` if you hit Triton/MoE errors on macOS —
the reviewer scripts do this automatically.

---

## What gets verified

`scripts/reproduce.sh` produces output files under
`benchmarks/pii_evaluation/results/`. The "Compare to" column below names the
reference snapshot under `claims/N/expected/` you should diff against — those
are the frozen submission-time outputs that produced the paper's PDF tables.

| Step | Time | Cost | Output | Compare to |
|---|---|---|---|---|
| §1 smoke — cross-source detection | ~10 min | $0 | `imported_eval_{nemotron_en,ai4privacy_de,wolframko_ru}__regex_{only,opf,presidio}.md` | `claims/1/expected/smoke/` (qualitative trend at n=200; paper §1 table comes from `--full` at n=1000) |
| §2 smoke — detector ablation (4 non-LLM rows) | ~15 min | $0 | `detector_ablation_*.{json,md}` | `claims/2/expected/smoke/` (paper §2 table also includes 3 LLM rows — run `--full` for those) |
| Unit tests | ~50 s | $0 | terminal output | 283 passed |
| §3 smoke | ~5 min | ~$1 | `results_anthropic-claude-haiku-4.5__opf-en.{json,md}` (1 cell, 10 queries) | `claims/3/expected/smoke/` (single-cell sanity; paper §3 numbers come from `--full` matrix) |
| §3 full (opt-in via `--full-section3`) | ~16-20h | ~$20-50 | full matrix + `section3_matrix.md` + `section3_forensics.md` | `claims/3/expected/full/` — paper §3 headline + per-language detail |

The acceptance bounds in each `claims/N/claim.txt` state exactly which
metrics must fall within which tolerances for the claim to count as
reproduced. Smoke-mode bounds are wider (200-row subsample variance);
full-mode bounds match the paper's 95% bootstrap CIs.

---

## What's where

```
piiv/
├── src/piiv/                  # Library: detector, vault, virtualizer, broker, leak guard
├── benchmarks/
│   ├── pii_evaluation/            # All §1/§2/§3 eval harnesses + dataset render
│   │   ├── run_imported_dataset_eval.py     # §1
│   │   ├── run_detector_ablation.py         # §2
│   │   ├── run_experiment.py                # §3 (per cell)
│   │   ├── run_section3_matrix.sh           # §3 (full matrix orchestration)
│   │   ├── aggregate_section3.py            # §3 results aggregator
│   │   ├── forensics_section3.py            # §3 leak + tool-failure dive
│   │   └── results/                         # Output files land here
│   ├── data_generator/             # Synthetic-data engine that produced §2's curated dataset
│   └── data_import/                # Loaders + transforms for §1's cross-source corpora
├── fine_tuning/                    # OPF fine-tune recipes + label-space definitions
├── tests/                          # library pytest suite (170 tests; no network).
│                                   # Subsystem tests live in benchmarks/*/tests/
│                                   # and fine_tuning/tests/ (113 more); all 283
│                                   # are auto-discovered by `pytest`.
├── scripts/                        # Reviewer-facing setup.sh + reproduce.sh
├── piiv.yaml                       # Runtime config (detector wiring, eval LLM defaults)
├── .env.example                    # Secrets template (copy to .env; fill PII_EVAL_API_KEY)
└── pyproject.toml                  # Install surface + optional dependency groups
```

The optional dependency groups in `pyproject.toml`:

```bash
pip install -e '.[opf]'         # Fine-tuned OPF detector (huggingface_hub + transformers + pymorphy3)
pip install -e '.[presidio]'    # Microsoft Presidio baseline (presidio-analyzer + spaCy)
pip install -e '.[benchmarks]'  # Eval harness (langchain-openai + python-dotenv)
pip install -e '.[dev]'         # pytest + benchmark deps
```

`scripts/setup.sh` installs all four; reviewers who only want to verify a
single section can pick a smaller subset.

For bit-for-bit deterministic reproduction (matching the maintainer's
exact versions of every transitive dependency), use the lockfile:

```bash
pip install -r requirements-lock.txt
```

`requirements-lock.txt` is autogenerated from `pyproject.toml` by
`uv pip compile`; the header comment records the exact regen command.

---

## Minimal library usage (no benchmarks)

```python
from cryptography.fernet import Fernet
from piiv import PIIVaultStore, PIIVirtualizer

vault = PIIVaultStore(db_path=":memory:", encryption_key=Fernet.generate_key())
scope = "session-1"
vault.open_session(scope)

virtualizer = PIIVirtualizer(vault)
safe = virtualizer.anonymize_text(scope, "Call +1 555 014 2233 about case #432")
# `safe` now contains phone_ref:<token>; raw number is in the encrypted vault
restored = virtualizer.rehydrate_text(scope, safe)
# `restored` recovers the original text
```

For a tool-calling agent that uses the full broker / leak-guard chain, see
`src/piiv/pii_tool_broker.py` and the `run_virtualization` pipeline in
`benchmarks/pii_evaluation/pipelines.py`.

---

## Layer-2 detector family

The regex first pass (Layer 1) catches every PII type with a structurally
reliable pattern. For person names and street addresses — entity types that
resist regex — `piiv` composes a second-pass detector on top of the
regex-tokenized output. Pick the mode in `piiv.yaml` (`detector.second_pass`)
or override per-run via `PII_SECOND_PASS=...`:

| Mode | Implementation | When to use |
|---|---|---|
| `none` | — | Layer 1 only; minimal latency, no name/address coverage |
| `opf` | `OPFPIIDetector` — fine-tuned token classifier ([HF: `pii-anon/opf-{en,de,ru}-v2`](https://huggingface.co/pii-anon)) | Production default. Highest accuracy on our trilingual eval suite (§2). |
| `llm` | `LLMPIIDetector` — any OpenAI-compatible chat-completions endpoint | Use a hosted small open-weight model via OpenRouter (e.g. `nvidia/nemotron-nano-9b-v2:free`) or a fully local server (LM Studio / Ollama / vLLM). Pass `--detector-llm-model <name>` at runtime. |
| `presidio` | `PresidioPIIDetector` — Microsoft Presidio with spaCy NER | Industry NER baseline. Install with `pip install -e '.[presidio]'` plus `python -m spacy download <lang>_core_news_lg`. |

All four modes plug into the same `PIIVirtualizer` and share the vault /
broker / leak-guard chain — switching modes is a one-line config change.

---

## Troubleshooting

- **macOS: Triton/MoE import errors when loading OPF** — export
  `OPF_MOE_TRITON=0` before any eval invocation. `scripts/reproduce.sh`
  sets this automatically.
- **`spacy.errors.OSError: [E050] Can't find model 'en_core_web_lg'`** —
  rerun `scripts/setup.sh`, or manually:
  `python -m spacy download en_core_web_lg de_core_news_lg ru_core_news_lg`
- **First eval invocation hangs for several minutes** — the framework's
  OPF loader is fetching the fine-tuned model (~600 MB per language) from
  HuggingFace into `~/.cache/huggingface/`. Subsequent runs are fast.
- **OpenRouter rate limit / 429 errors during §3** — the script does not
  retry; just rerun and the matrix runner will resume from where it
  stopped (results are written per-cell).
- **"PII_EVAL_API_KEY not set" warning** — §3 is skipped; §1/§2/pytest
  still run. Fill `.env` with your key and rerun to enable §3.

---

## Reproducibility notes

- All bootstrap confidence intervals: 1000 resamples, seed=42.
- Eval LLM is queried at `temperature=0.0` for determinism; OpenRouter
  honors this on all providers we tested.
- The §3 dataset is frozen at
  `benchmarks/pii_evaluation/dataset/data/dataset_v1.jsonl` with the
  SHA-256 in the matching `.sha256` file. To regenerate:
  `python -m benchmarks.pii_evaluation.dataset.render --freeze`.
- Per-cell §3 results carry per-query atoms (`per_config_atoms` in the
  result JSON) so bootstrap CIs are reproducible from the same JSON
  without rerunning the eval.

---

## License

Apache 2.0.
