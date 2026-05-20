================================================================
claims/ — ACSAC AE claim reproduction
================================================================

Each subdirectory corresponds to one headline claim in the paper:
  claims/1/   §1 cross-source detection generalization
  claims/2/   §2 detector ablation
  claims/3/   §3 full virtualization framework

Per-claim contents:
  claim.txt    Plain-text claim statement and acceptance bounds
               (which metric, expected range, tolerance vs. the
               paper's headline numbers).
  run.sh       Self-contained command sequence that reproduces
               this claim end-to-end.
  expected/    Frozen reference outputs from the maintainer's
               own reproduction run, taken at submission time.

How a reproduction is verified
----------------------------------------------------------------
1. Reviewer runs `bash claims/N/run.sh`. The script writes its
   output files into benchmarks/pii_evaluation/results/ — the
   project's working directory for evaluation runs.

2. Reviewer compares the fresh output files in
   benchmarks/pii_evaluation/results/ against the frozen
   reference files in claims/N/expected/.

3. If the reproduced metrics fall within the acceptance bounds
   stated in claims/N/claim.txt, the claim is verified.

Why two copies of the result files exist
----------------------------------------------------------------
benchmarks/pii_evaluation/results/  is the WORKING DIRECTORY.
                                    Reviewer runs overwrite it.
                                    Disposable between runs.

claims/N/expected/                  is the FROZEN REFERENCE.
                                    The numbers reported in the
                                    paper came from these exact
                                    files. They are immutable
                                    after submission and must
                                    not be regenerated, or the
                                    comparison loses meaning.

The duplication is intentional and load-bearing — symlinking
expected/ to the working dir would make every reproduction
trivially "match the reference" by tautology.

Going deeper than the headline outputs
----------------------------------------------------------------
benchmarks/pii_evaluation/results/ contains the full set of
per-cell outputs the maintainer produced — many more files than
each claims/N/expected/ snapshot. Reviewers who want to drill
into individual (model, language, detector) cells beyond the
headline metrics will find them all there, including:

  - §1: regex_llm cells across 4 detector LLMs × 3 languages
        (only the regex_only / regex_opf / regex_presidio
        headline cells are in claims/1/expected/).
  - §2: per-LLM detector ablation tables across the same
        4 detector LLMs (only the non-LLM headline table
        is in claims/2/expected/).
  - §3: per-(model, language) result JSONs for all 8 eval
        LLMs and a full §4 security-robustness stress-report
        per cell (only the aggregated headline files are in
        claims/3/expected/).

Use scripts/run_paper_eval.sh to reproduce the full paper-grade
matrix end-to-end (~17–21 h, ~$60–120 OpenRouter); use
claims/N/run.sh for the headline-only verification path
(~30 min total for §1+§2+§3 smoke, ~$1).
