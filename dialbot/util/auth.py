from functools import wraps

import jwt
from flask import jsonify, request, current_app


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
            token = token.split('Bearer ')[1]

        if not token:
            return jsonify({'message': 'Token is missing'}), 401

        try:
            data = jwt.decode(token, current_app.config['DIALBOT_AUTH_SECRET_KEY'], algorithms=['HS256'])
            # TODO: Currently no use cases for the data, but it could be used to pass user information
        except Exception as e:
            print(e)
            return jsonify({'message': 'Token is invalid'}), 401

        return f(*args, **kwargs)

    return decorated
