{% if cookiecutter.include_neo4j == "yes" %}
"""Knowledge graph integration module."""

from {{ cookiecutter.project_slug|replace('-', '_') }}.graph.neo4j_graph import KnowledgeGraph

__all__ = ["KnowledgeGraph"]
{% else %}
"""Knowledge graph integration module (not included in this project)."""
{% endif %}
