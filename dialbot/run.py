import os

from dotenv import load_dotenv, find_dotenv

from dialbot.app import app, configure


dotenv_path = find_dotenv()
if dotenv_path:
    load_dotenv(dotenv_path)
else:
    print(".env file not found")

configure(
    openai_api_key=os.getenv('DIALBOT_OPENAI_API_KEY'),
    auth_secret_key=os.getenv('DIALBOT_AUTH_SECRET_KEY'),
)

# This is only used when running directly from python (not using the flask command or gunicorn)
if __name__ == '__main__':
    app.run()
