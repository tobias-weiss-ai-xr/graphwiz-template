"""Main entry point for {{ cookiecutter.project_name }}."""

import argparse
import sys
from pathlib import Path
from loguru import logger

{% if cookiecutter.include_neo4j == "yes" %}
from {{ cookiecutter.project_slug|replace('-', '_') }}.graph import KnowledgeGraph
{% endif %}
{% if cookiecutter.include_ai_agents == "yes" %}
from {{ cookiecutter.project_slug|replace('-', '_') }}.agents import AgentOrchestrator
{% endif %}
from {{ cookiecutter.project_slug|replace('-', '_') }}.utils.config import load_config


class {{ cookiecutter.project_name.replace(' ', '') }}:
    """Main application class."""

    def __init__(self, config_path: str = "config/config.yaml"):
        """Initialize the application.

        Args:
            config_path: Path to configuration file
        """
        self.config = load_config(config_path)
        {% if cookiecutter.include_neo4j == "yes" %}
        self.kg = None
        {% endif %}
        {% if cookiecutter.include_ai_agents == "yes" %}
        self.agent_orchestrator = None
        {% endif %}
        self._running = False

    def start(self) -> None:
        """Start the application."""
        logger.info("Starting {{ cookiecutter.project_name }} v{}", self.config.get("version", "{{ cookiecutter.version }}"))

        {% if cookiecutter.include_neo4j == "yes" %}
        # Initialize knowledge graph
        logger.info("Connecting to knowledge graph...")
        self.kg = KnowledgeGraph(self.config.get("neo4j", {}))
        self.kg.connect()
        {% endif %}

        {% if cookiecutter.include_ai_agents == "yes" %}
        # Initialize agent orchestrator
        logger.info("Initializing AI agents...")
        self.agent_orchestrator = AgentOrchestrator(
            self.config.get("agents", {}),
            self.kg if self.kg else None
        )
        {% endif %}

        # Start main application logic
        self._running = True
        logger.info("{{ cookiecutter.project_name }} started successfully")

    def stop(self) -> None:
        """Stop the application."""
        logger.info("Stopping {{ cookiecutter.project_name }}...")
        self._running = False

        {% if cookiecutter.include_neo4j == "yes" %}
        if self.kg:
            self.kg.disconnect()
        {% endif %}

        logger.info("{{ cookiecutter.project_name }} stopped")

    def is_running(self) -> bool:
        """Check if the application is running.

        Returns:
            True if running, False otherwise
        """
        return self._running


def main() -> int:
    """Main entry point.

    Returns:
        Exit code
    """
    parser = argparse.ArgumentParser(
        description="{{ cookiecutter.project_name }} - {{ cookiecutter.project_short_description }}"
    )
    parser.add_argument(
        "--config",
        default="config/config.yaml",
        help="Path to configuration file (default: config/config.yaml)"
    )
    parser.add_argument(
        "--version",
        action="version",
        version="{{ cookiecutter.project_name }} {{ cookiecutter.version }}"
    )

    args = parser.parse_args()

    # Check if config file exists
    config_path = Path(args.config)
    if not config_path.exists():
        logger.error("Configuration file not found: {}", config_path)
        logger.info("Copy config/config.example.yaml to config/config.yaml and configure it")
        return 1

    try:
        app = {{ cookiecutter.project_name.replace(' ', '') }}(str(config_path))
        app.start()

        # Keep running until interrupted
        while app.is_running():
            try:
                import time
                time.sleep(1)
            except KeyboardInterrupt:
                logger.info("Received interrupt signal")
                break

        app.stop()
        return 0

    except Exception as e:
        logger.exception("Fatal error: {}", e)
        return 1


if __name__ == "__main__":
    sys.exit(main())
