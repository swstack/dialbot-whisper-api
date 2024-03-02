from flask import Flask
from openai import OpenAI

from dialbot.endpoints.health import health_bp
from dialbot.endpoints.transcribe import transcribe_bp

app = Flask(__name__)

app.register_blueprint(health_bp)
app.register_blueprint(transcribe_bp, url_prefix='/api/v1')


def configure(
    openai_api_key: str = None,
    auth_secret_key: str = None,
):
    app.config['DIALBOT_OPENAI_API_KEY'] = openai_api_key
    app.config['DIALBOT_AUTH_SECRET_KEY'] = auth_secret_key

    with app.app_context():
        app.openai = OpenAI(api_key=app.config['DIALBOT_OPENAI_API_KEY'])
