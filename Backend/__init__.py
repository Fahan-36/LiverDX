"""
Backend package initializer.
This file makes the `Backend` directory a Python package so that
relative/top-level imports inside the package resolve correctly when
running `Backend.main` via `python -m uvicorn Backend.main:app`.
"""

__all__ = ["main", "database", "train_knn_optimized"]
