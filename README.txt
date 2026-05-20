================================================================
piiv — ACSAC 2026 Artifact (Anonymous Submission)
================================================================

This artifact accompanies a double-blind ACSAC 2026 submission.
The paper PDF carries the full motivation, design, and analysis.

ACSAC AE entry points
----------------------------------------------------------------
install.sh           One-shot dependency installer.
use.txt              Intended use, limitations, ethical scope.
license.txt          License pointer (full text in LICENSE).
claims/README.txt    How the claims/ + results/ split works.
claims/1/            §1 cross-source detection generalization.
claims/2/            §2 detector ablation.
claims/3/            §3 full virtualization framework.

Each claims/N/ contains:
  claim.txt          Plain-text claim statement + acceptance bounds
                     (which metric, expected range, tolerance vs.
                     the paper's headline numbers).
  run.sh             Self-contained command sequence that reproduces
                     this claim end-to-end.
  expected/          Frozen reference outputs from the maintainer's
                     submission-time run (do not regenerate).

How verification works
----------------------------------------------------------------
A reviewer runs `bash claims/N/run.sh`. The script writes its
output to benchmarks/pii_evaluation/results/ (the working
directory for evaluations). Reviewer compares those fresh files
against the frozen reference files in claims/N/expected/. If
metrics fall within the acceptance bounds in claim.txt, the
claim is verified.

benchmarks/pii_evaluation/results/ also contains the full set of
per-cell outputs the maintainer produced (more files than each
expected/ snapshot — per-LLM detector cells, full §3 matrix,
§4 stress reports). Reviewers wanting to drill below the
headline numbers will find everything there. See
claims/README.txt for the full layout explanation.

Reviewer quick start
----------------------------------------------------------------
Each claims/N/run.sh runs in --smoke mode by default and accepts
a --full flag for paper-grade reproduction. SMOKE mode confirms
each pipeline works end-to-end on reduced N; FULL mode reproduces
the exact PDF tables.

1) bash install.sh
2) edit .env, set PII_EVAL_API_KEY=sk-or-v1-...  (OpenRouter key;
                                                  required for §3
                                                  and for §1/§2 --full)

3) SMOKE verification (fast, qualitative trends only):
   bash claims/1/run.sh   # ~10 min smoke, no API cost
                          # 9 cells (3 corpora x 3 non-LLM detectors)
                          # at n=200/corpus
   bash claims/2/run.sh   # ~15 min smoke, no API cost
                          # 4 non-LLM detector configs on the 309-query bench
   bash claims/3/run.sh   # ~5 min smoke, ~$1 OpenRouter
                          # 1 cell (en x claude-haiku-4.5 x 10 queries)

   Paper-grade reproduction (matches PDF tables exactly):
   bash claims/1/run.sh --full   # ~3-4 h, ~$0.05; 21 cells at n=1000
   bash claims/2/run.sh --full   # adds the 3 paper-reported LLM detector rows
   bash claims/3/run.sh --full   # ~16-20h, ~$20-50; full 8 LLMs x 3 langs matrix

scripts/reproduce.sh runs all three claims in SMOKE mode back-to-back
(~30 min, ~$1). Pass --full-section3 to upgrade §3 only.

scripts/run_paper_eval.sh is the canonical paper-grade orchestrator
(8 LLMs, full §1+§2+§3+§4 sweep, ~17-21h, ~$60-120) and is the
script that produced the reference outputs under claims/N/expected/full/.

For library usage, repository layout, dependency groups, and the
full reviewer-facing walkthrough, see README.md. The README.md
content is not duplicated here to avoid drift; this file is the
AE-spec signpost.
