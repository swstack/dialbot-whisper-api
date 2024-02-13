# Dialbot Whisper API

API for ingesting large audio datasets and converting to text'

## Setup
Pre-requisites:
- Python 3.10+
- Poetry (https://python-poetry.org/docs/#installation)

Install python dependencies:
```bash
poetry install --no-root
```

## Run the tests

Run the tests:
```bash
poetry run python tests/run.py
```

## Running the application

There are various ways to run the application, including using the flask development server, gunicorn, or docker.

- **Run with the flask development server:**
    ```bash
    poetry run flask --app dialbot/run.py run
    ```

- **Run with gunicorn:**
    ```bash
    poetry run gunicorn --bind localhost:5000 --access-logfile - dialbot.run:app
    ```

- **Run with docker:**

    First build docker image:
    ```bash
    poetry export -f requirements.txt --output requirements.txt &&
    docker build --build-arg OPENAI_API_KEY=$OPENAI_API_KEY -t dialbot:latest .
    ```
    Run docker image:
    ```bash
    docker run -p 5000:5000 dialbot:latest
    ```
