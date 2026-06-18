from jose import jwt

SECRET_KEY = "multicloudsecret"

ALGORITHM = "HS256"

def create_token(data):

    return jwt.encode(
        data,
        SECRET_KEY,
        algorithm=ALGORITHM
    )