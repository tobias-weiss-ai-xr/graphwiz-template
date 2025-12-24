# GraphWiz Template

**A modern Cookiecutter template for creating Python projects with Neo4j knowledge graphs, AI agents, and best practices.**

## Features

This template generates a Python project with:

### Optional Components (selected during generation)
- **Neo4j Integration**: Knowledge graph database connectivity
- **AI Agents**: LangChain-based AI agent orchestration
- **Trading Engine**: CCXT integration for cryptocurrency trading
- **Docker Support**: Container configuration with docker-compose
- **CI/CD**: GitHub Actions workflows

### Always Included
- **Modern Python**: Python 3.10+ with type hints
- **Testing**: pytest with coverage reporting
- **Code Quality**: Black, Flake8, MyPy configured
- **Logging**: Structured logging with Loguru
- **Configuration**: YAML-based configuration management
- **Virtual Environment**: .venv directory structure

## Quick Start

### Prerequisites

1. Install Cookiecutter:
```bash
pip install cookiecutter
```

### Generate a Project

```bash
cookiecutter gh:tobias-weiss-ai-xr/graphwiz-template
```

You'll be prompted for:
- Project name and description
- Author information
- Python version (3.10, 3.11, or 3.12)
- License type
- Optional components (Neo4j, AI agents, trading, Docker, CI/CD)

### Generated Project Structure

```
your-project/
├── src/your_project/          # Source code
│   ├── agents/                # AI agents (if enabled)
│   ├── graph/                 # Neo4j integration (if enabled)
│   ├── trading/               # Trading engine (if enabled)
│   ├── analysis/              # Data analysis module
│   ├── utils/                 # Utility functions
│   └── main.py                # Main entry point
├── config/                    # Configuration files
├── tests/                     # Test suite
├── data/                      # Data files
├── logs/                      # Application logs
├── Dockerfile                 # (if Docker enabled)
├── docker-compose.yml         # (if Docker enabled)
├── requirements.txt           # Python dependencies
├── setup.py                   # Package setup
├── pyproject.toml             # Modern Python config
└── README.md                  # Generated documentation
```

## Development

### Setup Generated Project

```bash
cd your_project

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install the package
pip install -e .

# Configure
cp config/config.example.yaml config/config.yaml
cp .env.example .env

# Run tests
pytest

# Run the application
your-project
```

{% if cookiecutter.include_docker == "yes" %}
### Using Docker

```bash
docker-compose up -d
```
{% endif %}

## Template Options

| Option | Values | Description |
|--------|--------|-------------|
| `project_name` | string | Name of your project |
| `project_slug` | auto | URL-friendly identifier |
| `python_version` | 3.10, 3.11, 3.12 | Python version |
| `include_neo4j` | yes, no | Include Neo4j integration |
| `include_ai_agents` | yes, no | Include AI agent framework |
| `include_trading` | yes, no | Include trading engine |
| `include_docker` | yes, no | Include Docker configuration |
| `include_ci` | yes, no | Include CI/CD workflows |
| `license` | MIT, Apache-2.0, GPL-3.0, BSD-3 | License type |

## Examples

### Minimal Project (Python only)
```bash
cookiecutter gh:tobias-weiss-ai-xr/graphwiz-template
# Select: include_neo4j=no, include_ai_agents=no, include_trading=no, include_docker=no
```

### Full-Stack Project
```bash
cookiecutter gh:tobias-weiss-ai-xr/graphwiz-template
# Select: include_neo4j=yes, include_ai_agents=yes, include_trading=yes, include_docker=yes
```

### Knowledge Graph Application
```bash
cookiecutter gh:tobias-weiss-ai-xr/graphwiz-template
# Select: include_neo4j=yes, include_ai_agents=yes, include_trading=no
```

## Customization

The template uses Cookiecutter's Jinja2 templating. You can fork this template and customize it for your needs.

Key template files:
- `cookiecutter.json` - User prompts and defaults
- `{{cookiecutter.project_slug}}/` - Generated project template
- `hooks/post_gen_project.py` - Post-generation cleanup script

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - see LICENSE file for details

## Author

**GraphWiz** - [info@graphwiz.ai](mailto:info@graphwiz.ai)

## Acknowledgments

- [Cookiecutter](https://cookiecutter.readthedocs.io/) - Project template system
- [Neo4j](https://neo4j.com/) - Graph database platform
- [LangChain](https://langchain.com/) - AI agent framework
- [CCXT](https://ccxt.com/) - Exchange integration library
