import os
import unittest
import jwt
from unittest.mock import MagicMock

from dialbot.app import app, configure

resources_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources')


class TestTranscribeEndpoint(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

        mock_response = MagicMock()
        mock_response.text = "foobar"

        jwt_secret = "test-secret"
        configure(
            openai_api_key="test-key",
            auth_secret_key=jwt_secret,
        )

        self.headers = {
            'Authorization': f'Bearer {jwt.encode({"some": "payload"}, jwt_secret, algorithm="HS256")}',
        }

        with app.app_context():
            app.openai = MagicMock()
            app.openai.audio.transcriptions.create = MagicMock(return_value=mock_response)

    def test_transcribe_endpoint(self):
        with open(os.path.join(resources_dir, 'test-data.mp3'), 'rb') as audio_file:
            response = self.app.post('/api/v1/transcribe', data={'audio': audio_file}, headers=self.headers)

        self.assertEqual(response.status_code, 200)
        data = response.get_json()

        self.assertIn('transcription', data)
        transcription = data['transcription']

        self.assertTrue(transcription.startswith("foobar"))


if __name__ == '__main__':
    unittest.main()
