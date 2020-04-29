import jwt
import os
import datetime


def get_response_template():
    return {
        'status': None,
        'msg': None,
        'data': None,
    }


def get_token(user) -> str:
    secret_key = os.environ['SECRET_KEY'] if 'SECRET_KEY' in os.environ else 'qwerty123'
    return jwt.encode({'id': user.id, 'timestamp': datetime.datetime.today().timestamp()}, secret_key, algorithm='HS256').decode()


def get_payload(token: str) -> dict or None:
    try:
        secret_key = os.environ['SECRET_KEY'] if 'SECRET_KEY' in os.environ else 'qwerty123'
        return jwt.decode(token, secret_key, algorithm='HS256')
    except Exception:  # TODO
        return None