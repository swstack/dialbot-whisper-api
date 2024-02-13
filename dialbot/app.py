from flask import Flask

from dialbot.transcribe import transcribe_bp

app = Flask(__name__)

app.register_blueprint(transcribe_bp, url_prefix='/api/v1')
