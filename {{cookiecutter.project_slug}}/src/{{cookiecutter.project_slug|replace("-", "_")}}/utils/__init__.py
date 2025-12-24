"""Utility functions."""

from {{ cookiecutter.project_slug|replace('-', '_') }}.utils.config import load_config

__all__ = ["load_config"]
