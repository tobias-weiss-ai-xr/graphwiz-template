{% if cookiecutter.include_docker == "yes" %}
FROM python:{{ cookiecutter.python_version }}-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Install the package
RUN pip install -e .

# Create necessary directories
RUN mkdir -p data logs

# Set Python path
ENV PYTHONPATH=/app/src

# Default command
CMD ["{{ cookiecutter.project_slug|replace('-', '_') }}"]
{% endif %}
