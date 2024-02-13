import os

from openai import OpenAI

from dialbot.app import app

with app.app_context():
    app.openai = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
