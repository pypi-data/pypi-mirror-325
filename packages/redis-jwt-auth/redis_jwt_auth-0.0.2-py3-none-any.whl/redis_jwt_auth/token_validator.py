import jwt
from fastapi import HTTPException


class TokenValidator:
    def __init__(self, secret_key: str):
        self.secret_key = secret_key

    def decode_token(self, token):
        try:
            return jwt.decode(token, self.secret_key, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Token has expired")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail="Invalid token")