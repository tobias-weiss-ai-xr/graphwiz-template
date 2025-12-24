{% if cookiecutter.include_trading == "yes" %}
"""Trading module for order execution and management."""

from {{ cookiecutter.project_slug|replace('-', '_') }}.trading.engine import TradingEngine

__all__ = ["TradingEngine"]
{% else %}
"""Trading module (not included in this project)."""
{% endif %}
