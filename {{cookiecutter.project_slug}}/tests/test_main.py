"""Tests for {{ cookiecutter.project_name }}."""

import pytest
from {{ cookiecutter.project_slug|replace('-', '_') }} import main


class Test{{ cookiecutter.project_name.replace(' ', '') }}:
    """Test main application class."""

    def test_initialization(self):
        """Test that the application can be initialized."""
        app = main.{{ cookiecutter.project_name.replace(' ', '') }}(config_path="config/config.example.yaml")
        assert app is not None

    def test_version(self):
        """Test that version is defined."""
        from {{ cookiecutter.project_slug|replace('-', '_') }} import __version__
        assert __version__ == "{{ cookiecutter.version }}"
