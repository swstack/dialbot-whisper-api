from flask import Flask

from dialbot.endpoints.transcribe import transcribe_bp
from dialbot.endpoints.health import health_bp

app = Flask(__name__)

app.register_blueprint(health_bp)
app.register_blueprint(transcribe_bp, url_prefix='/api/v1')
