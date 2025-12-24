"""
{{ cookiecutter.project_name }}.

{{ cookiecutter.project_short_description }}
"""

__version__ = "{{ cookiecutter.version }}"
__author__ = "{{ cookiecutter.author_name }}"
__email__ = "{{ cookiecutter.author_email }}"

from {{ cookiecutter.project_slug|replace('-', '_') }}.main import main

__all__ = ["main", "__version__"]
