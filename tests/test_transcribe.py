import unittest
from flask import Flask
from dialbot.app import app


class TestTranscribeEndpoint(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_transcribe_endpoint(self):
        # Replace '/path/to/your/audio.mp3' with the actual file path of an MP3 file
        with open('resources/test-data.mp3', 'rb') as audio_file:
            response = self.app.post('/api/v1/transcribe', data={'audio': audio_file})

        self.assertEqual(response.status_code, 200)
        data = response.get_json()

        self.assertIn('transcription', data)
        transcription = data['transcription']

        # Add your assertions for the expected transcription result here
        # For example, you can check if it contains certain words or phrases.
        self.assertTrue(transcription.startswith("foobar"))


if __name__ == '__main__':
    unittest.main()
