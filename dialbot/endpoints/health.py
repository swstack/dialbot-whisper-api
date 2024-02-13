from flask import Blueprint, jsonify

health_bp = Blueprint('health', __name__)


@health_bp.route('/health', methods=['GET'])
def health():

    # TODO: Return real information about the health of the service
    return jsonify({'status': 'healthy', 'version': '0.0.1', 'git': '1234567'})
