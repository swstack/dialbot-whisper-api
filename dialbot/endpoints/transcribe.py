from flask import Blueprint, request, jsonify, current_app

transcribe_bp = Blueprint('transcribe', __name__)


@transcribe_bp.route('/transcribe', methods=['POST'])
def transcribe():
    mp3_file = request.files['audio']

    if mp3_file.filename != '':
        file_data = mp3_file.read()

        with current_app.app_context():
            transcription = current_app.openai.audio.transcriptions.create(
                model='whisper-1',
                file=('file.mp3', file_data, 'audio/mpeg'),
            )

        return jsonify({'transcription': transcription.text})
