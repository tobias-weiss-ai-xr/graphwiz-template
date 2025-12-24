{% if cookiecutter.include_ai_agents == "yes" %}
"""AI agents for intelligent decision-making."""

from {{ cookiecutter.project_slug|replace('-', '_') }}.agents.orchestrator import AgentOrchestrator

__all__ = ["AgentOrchestrator"]
{% else %}
"""AI agents module (not included in this project)."""
{% endif %}
