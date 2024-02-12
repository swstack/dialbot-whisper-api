FROM python:3.10.12-slim

ARG OPENAI_API_KEY
ENV OPENAI_API_KEY=$OPENAI_API_KEY

WORKDIR /app/

# Setup application
COPY requirements.txt /app
COPY ./dialbot /app/dialbot
RUN pip install -r /app/requirements.txt

# Setup Gunicorn
RUN pip install gunicorn
EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "dialbot.app:app"]
