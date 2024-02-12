FROM python:3.10.12-slim

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python -

# Install gunicorn
RUN pip install gunicorn

# Set the working directory in the container
WORKDIR /app

# Copy only the dependency files to leverage Docker cache
COPY pyproject.toml /app
COPY ./dialbot /app/dialbot

# Install project dependencies
RUN ~/.local/bin/poetry install --no-root --no-dev

# Expose the Flask port
EXPOSE 5000

# Command to run the Flask application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "dialbot:app"]
