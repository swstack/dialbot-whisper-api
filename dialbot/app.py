from flask import Flask
from dialbot.api.transcribe import transcribe_bp

app = Flask(__name__)

app.register_blueprint(transcribe_bp, url_prefix='/api/v1')

if __name__ == '__main__':
    app.run()