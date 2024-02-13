import os
import unittest
from unittest.mock import MagicMock

from dialbot.app import app


class TestTranscribeEndpoint(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

        mock_response = MagicMock()
        mock_response.text = "foobar"
        with app.app_context():
            app.openai.audio.transcriptions.create = MagicMock(
                return_value=mock_response)

        os.environ['OPENAI_API_KEY'] = "fake-key"

    def test_transcribe_endpoint(self):
        with open('tests/resources/test-data.mp3', 'rb') as audio_file:
            response = self.app.post('/api/v1/transcribe', data={'audio': audio_file})

        self.assertEqual(response.status_code, 200)
        data = response.get_json()

        self.assertIn('transcription', data)
        transcription = data['transcription']

        self.assertTrue(transcription.startswith("foobar"))


if __name__ == '__main__':
    unittest.main()
