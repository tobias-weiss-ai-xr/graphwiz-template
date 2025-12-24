# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

## Overview

This project was created from the [GraphWiz Template](https://github.com/tobias-weiss-ai-xr/graphwiz-template) - a modern Python project template that includes:

{% if cookiecutter.include_neo4j == "yes" %}
- **Neo4j Integration**: Knowledge graph database connectivity
{% endif %}
{% if cookiecutter.include_ai_agents == "yes" %}
- **AI Agents**: LangChain-based AI agent orchestration
{% endif %}
{% if cookiecutter.include_trading == "yes" %}
- **Trading Engine**: CCXT integration for cryptocurrency trading
{% endif %}
- **Modern Python**: Python {{ cookiecutter.python_version }} with type hints
- **Testing**: pytest with coverage reporting
- **Code Quality**: Black, Flake8, MyPy configured
- **Logging**: Structured logging with Loguru
{% if cookiecutter.include_docker == "yes" %}
- **Docker**: Container support with docker-compose
{% endif %}
{% if cookiecutter.include_ci == "yes" %}
- **CI/CD**: GitHub Actions workflows
{% endif %}

## Installation

```bash
# Clone the repository
git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git
cd {{ cookiecutter.project_slug }}

# Create virtual environment
python{{ cookiecutter.python_version }} -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install the package in development mode
pip install -e .
```

## Configuration

Copy the example configuration and update it:

```bash
cp config/config.example.yaml config/config.yaml
cp .env.example .env
# Edit config.yaml and .env with your settings
```

{% if cookiecutter.include_docker == "yes" %}
## Docker

```bash
docker-compose up -d
```
{% endif %}

## Usage

```python
from {{ cookiecutter.project_slug|replace('-', '_') }} import main

# Your code here
```

## Development

```bash
# Run tests
pytest

# Format code
black src/

# Type checking
mypy src/

# Linting
flake8 src/
```

## Project Structure

```
{{ cookiecutter.project_slug }}/
├── src/{{ cookiecutter.project_slug|replace('-', '_') }}/  # Source code
├── config/                    # Configuration files
├── tests/                     # Test suite
├── data/                      # Data files
├── logs/                      # Application logs
└── README.md                  # This file
```

## License

{% if cookiecutter.open_source_license %}
{{ cookiecutter.license }} - see [LICENSE](LICENSE) file for details
{% else %}
Proprietary - All rights reserved
{% endif %}

## Author

**{{ cookiecutter.author_name }}** - {{ cookiecutter.author_email }}

## Acknowledgments

- Created with [GraphWiz Template](https://github.com/tobias-weiss-ai-xr/graphwiz-template)
{% if cookiecutter.include_neo4j == "yes" %}
- [Neo4j](https://neo4j.com/) - Graph database
{% endif %}
{% if cookiecutter.include_ai_agents == "yes" %}
- [LangChain](https://langchain.com/) - AI agent framework
{% endif %}
{% if cookiecutter.include_trading == "yes" %}
- [CCXT](https://ccxt.com/) - Exchange integration
{% endif %}
