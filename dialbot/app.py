import os

from flask import Flask
from openai import OpenAI

from dialbot.transcribe import transcribe_bp

app = Flask(__name__)

app.register_blueprint(transcribe_bp, url_prefix='/api/v1')

with app.app_context():
    app.openai = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

if __name__ == '__main__':
    app.run()