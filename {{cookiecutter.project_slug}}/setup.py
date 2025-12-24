"""Setup configuration for {{ cookiecutter.project_name }}."""

from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

setup(
    name="{{ cookiecutter.project_slug }}",
    version="{{ cookiecutter.version }}",
    author="{{ cookiecutter.author_name }}",
    author_email="{{ cookiecutter.author_email }}",
    description="{{ cookiecutter.project_short_description }}",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}",
    project_urls={
        "Bug Tracker": "https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/issues",
        "Documentation": "https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/blob/main/README.md",
        "Source Code": "https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        {% if cookiecutter.open_source_license %}
        "License :: OSI Approved :: {{ cookiecutter.license }} License",
        {% endif %}
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: {{ cookiecutter.python_version }}",
    ],
    python_requires=">={{ cookiecutter.python_version }}",
    install_requires=[
        "python-dotenv>=1.0.0",
        "pyyaml>=6.0.1",
        "loguru>=0.7.0",
        {% if cookiecutter.include_neo4j == "yes" %}
        "neo4j>=5.15.0",
        {% endif %}
        {% if cookiecutter.include_ai_agents == "yes" %}
        "langchain>=0.1.0",
        {% endif %}
        {% if cookiecutter.include_trading == "yes" %}
        "ccxt>=4.1.0",
        "pandas>=2.1.0",
        {% endif %}
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-asyncio>=0.21.0",
            "pytest-cov>=4.1.0",
            "black>=23.12.0",
            "flake8>=7.0.0",
            "mypy>=1.8.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "{{ cookiecutter.project_slug|replace('-', '_') }}={{ cookiecutter.project_slug|replace('-', '_') }}.main:main",
        ],
    },
)
