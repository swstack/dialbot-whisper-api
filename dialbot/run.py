import os

from openai import OpenAI

from dialbot.app import app

with app.app_context():
    app.openai = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# This is only used when running directly from python (not using the flask command or gunicorn)
if __name__ == '__main__':
    app.run()
