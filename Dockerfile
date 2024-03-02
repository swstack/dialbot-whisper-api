FROM python:3.10.12-slim

ARG DIALBOT_OPENAI_API_KEY
ARG DIALBOT_AUTH_SECRET_KEY

ENV DIALBOT_OPENAI_API_KEY=$DIALBOT_OPENAI_API_KEY
ENV DIALBOT_AUTH_SECRET_KEY=$DIALBOT_AUTH_SECRET_KEY

WORKDIR /app/

# Setup application
COPY requirements.txt /app
COPY ./dialbot /app/dialbot
RUN pip install -r /app/requirements.txt

# Setup Gunicorn
RUN pip install gunicorn
EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000","--access-logfile", "-", "dialbot.run:app"]
