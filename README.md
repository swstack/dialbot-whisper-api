# Dialbot Whisper API

API for ingesting large audio datasets and converting to text'

## Run from source locally

Pre-requisites:
- Python 3.10+
- Poetry (https://python-poetry.org/docs/#installation)

Install python dependencies:
```bash
poetry install --no-root
```

Run the flask application:
```bash
poetry run flask --app dialbot/prod.py run```

Run the tests:
```bash
poetry run python tests/run.py
```

## Build and run docker image locally

Build docker image:
```bash
poetry export -f requirements.txt --output requirements.txt &&
docker build --build-arg OPENAI_API_KEY=$OPENAI_API_KEY -t dialbot:latest .
```

Run docker image:
```bash
docker run -p 5000:5000 dialbot:latest
```