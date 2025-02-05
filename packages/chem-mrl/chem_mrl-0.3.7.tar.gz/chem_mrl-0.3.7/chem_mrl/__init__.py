from __future__ import annotations

import logging

from sentence_transformers import LoggingHandler

__version__ = "0.3.7"

from . import (
    benchmark,
    configs,
    constants,
    datasets,
    device_manager,
    evaluation,
    losses,
    molecular_embedder,
    molecular_fingerprinter,
    trainers,
)

logging.basicConfig(
    format="%(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
    handlers=[LoggingHandler()],
)


__all__ = [
    "benchmark",
    "configs",
    "constants",
    "datasets",
    "device_manager",
    "evaluation",
    "losses",
    "molecular_embedder",
    "molecular_fingerprinter",
    "trainers",
]
