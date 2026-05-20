"""Run a fine-tuned checkpoint through the detector ablation harness.

The evaluator points the OPF detector registry at the freshly trained
checkpoint and invokes ``benchmarks.pii_evaluation.run_detector_ablation``
with the ``regex_opf_routed`` configuration. The harness writes its
per-config P/R/F1 markdown under ``benchmarks/pii_evaluation/results/``;
this module copies the relevant slice into ``runs/<slug>/eval.md`` so
training runs don't clobber each other's results.

No new metric code lives here — the harness is the source of truth.
"""
from __future__ import annotations

import logging
import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)

REPO_ROOT = Path(__file__).resolve().parent.parent
HARNESS_RESULTS_DIR = REPO_ROOT / "benchmarks" / "pii_evaluation" / "results"


def run_evaluate(
    *,
    checkpoint_dir: Path,
    locale: str,
    slug: str,
    runs_dir: Path,
    extra_argv: Optional[list[str]] = None,
) -> Path:
    """Evaluate ``checkpoint_dir`` against the ablation harness.

    Returns the path to the eval markdown copied into the run directory.
    """
    if not checkpoint_dir.exists():
        raise FileNotFoundError(f"Checkpoint directory missing: {checkpoint_dir}")

    runs_dir.mkdir(parents=True, exist_ok=True)

    env = os.environ.copy()
    # The OPF detector resolves a fine-tuned model from PII_OPF_FINETUNED_MODEL
    # (see src/piiv/config.py).
    env["PII_OPF_ENABLED"] = "true"
    env["PII_OPF_FINETUNED_MODEL"] = str(checkpoint_dir.resolve())

    cmd = [
        sys.executable, "-m", "benchmarks.pii_evaluation.run_detector_ablation",
        "--configurations", "regex_only,regex_opf_base,regex_opf_routed",
        "--locales", locale,
        "--slug", f"{slug}-eval",
    ]
    if extra_argv:
        cmd.extend(extra_argv)

    logger.info("Running ablation harness: %s", " ".join(cmd))
    rc = subprocess.run(cmd, env=env, cwd=str(REPO_ROOT)).returncode
    if rc != 0:
        raise RuntimeError(f"detector ablation harness returned exit code {rc}")

    # Harness writes results_detector_ablation_<slug>-eval.md (or similar);
    # locate the most recent matching file and copy it.
    candidates = sorted(
        list(HARNESS_RESULTS_DIR.glob(f"*{slug}-eval*.md")),
        key=lambda p: p.stat().st_mtime,
        reverse=True,
    )
    target = runs_dir / "eval.md"
    if candidates:
        shutil.copy2(candidates[0], target)
        logger.info("Copied %s -> %s", candidates[0], target)
    else:
        logger.warning(
            "No matching ablation result file found under %s for slug=%s; "
            "skipping copy.",
            HARNESS_RESULTS_DIR, slug,
        )
    return target
