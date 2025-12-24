"""Post-generation hook for cookiecutter."""

import os
import shutil


def remove_unused_files():
    """Remove files that are not needed based on configuration."""
    # Read cookiecutter context
    project_slug = "{{ cookiecutter.project_slug|replace('-', '_') }}"

    {% if cookiecutter.include_neo4j == "no" %}
    # Remove Neo4j-related files
    print("Removing Neo4j integration files...")
    neo4j_files = [
        f"{project_slug}/graph",
    ]
    for path in neo4j_files:
        full_path = os.path.join(path)
        if os.path.exists(full_path):
            shutil.rmtree(full_path)
            print(f"Removed: {full_path}")
    {% endif %}

    {% if cookiecutter.include_ai_agents == "no" %}
    # Remove AI agents files
    print("Removing AI agents files...")
    agents_files = [
        f"{project_slug}/agents",
    ]
    for path in agents_files:
        full_path = os.path.join(path)
        if os.path.exists(full_path):
            shutil.rmtree(full_path)
            print(f"Removed: {full_path}")
    {% endif %}

    {% if cookiecutter.include_trading == "no" %}
    # Remove trading files
    print("Removing trading files...")
    trading_files = [
        f"{project_slug}/trading",
    ]
    for path in trading_files:
        full_path = os.path.join(path)
        if os.path.exists(full_path):
            shutil.rmtree(full_path)
            print(f"Removed: {full_path}")
    {% endif %}

    {% if cookiecutter.include_docker == "no" %}
    # Remove Docker files
    print("Removing Docker files...")
    docker_files = [
        "Dockerfile",
        "docker-compose.yml",
    ]
    for filename in docker_files:
        if os.path.exists(filename):
            os.remove(filename)
            print(f"Removed: {filename}")
    {% endif %}

    print("Post-generation cleanup complete!")


if __name__ == "__main__":
    remove_unused_files()
