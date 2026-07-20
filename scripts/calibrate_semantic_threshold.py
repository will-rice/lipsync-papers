"""Calibrate SEMANTIC_THRESHOLD via leave-one-out scoring of the corpus.

Scores every paper in papers.csv against the rest of the corpus (SemanticGate
already excludes a corpus paper from its own neighbors), prints score
percentiles, and scores known-negative abstracts to confirm separation.

Run manually when the threshold needs revisiting; commit the chosen value as
SEMANTIC_THRESHOLD in scripts/fetch_papers.py and paste the table in the PR::

    uv run python -m scripts.calibrate_semantic_threshold
"""

import logging

import torch
from tqdm import tqdm

from scripts.fetch_papers import SemanticGate, load_existing_papers

# Off-topic abstracts of the kind the blacklist exists for; their scores must
# sit clearly below the chosen threshold.
KNOWN_NEGATIVES = [
    {
        "arxiv_id": "neg-radar",
        "title": "Contactless Vital Sign Monitoring with mmWave Radar",
        "abstract": "We develop a millimeter-wave radar pipeline that estimates "
        "heart rate and respiration from chest micro-motion, with a signal "
        "processing chain robust to body movement and multipath clutter.",
    },
    {
        "arxiv_id": "neg-clinical",
        "title": "Surgical Outcomes of Cleft Lip Repair in Infants",
        "abstract": "A retrospective cohort study of primary cleft lip repair "
        "evaluating scar quality, symmetry, and complication rates across two "
        "surgical techniques over five years of follow-up.",
    },
    {
        "arxiv_id": "neg-grid",
        "title": "Grid-Forming Inverter Control for Power System Synchronization",
        "abstract": "We analyze droop-based grid-forming inverter controllers and "
        "their transient synchronization stability under large load steps in "
        "low-inertia power systems.",
    },
]

PERCENTILES = [0.01, 0.02, 0.05, 0.10, 0.25, 0.50]


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(message)s")

    corpus = list(load_existing_papers().values())
    gate = SemanticGate(corpus)
    scores = torch.tensor([gate.score(p) for p in tqdm(corpus, desc="LOO scoring")])

    logging.info("Leave-one-out score percentiles over %d corpus papers:", len(corpus))
    for q in PERCENTILES:
        logging.info("  p%-3d %.3f", int(q * 100), torch.quantile(scores, q))

    logging.info("Known-negative scores (must sit clearly below the threshold):")
    for paper in KNOWN_NEGATIVES:
        logging.info("  %.3f  %s", gate.score(paper), paper["title"])


if __name__ == "__main__":
    main()
