from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from .cache_manager import CacheManager
from .token_validator import TokenValidator


class TokenMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, cache_manager: CacheManager, token_validator: TokenValidator):
        super().__init__(app)
        self.cache_manager = cache_manager
        self.token_validator = token_validator

    async def dispatch(self, request: Request, call_next):
        token = request.headers.get("Authorization")
        if not token:
            raise HTTPException(status_code=401, detail="Token missing")

        token = token.split("Bearer ")[-1]
        decoded_token = self.token_validator.decode_token(token)
        user_id = decoded_token.get("user_id")
        jti = decoded_token.get("jti")

        cached_tokens = self.cache_manager.get_tokens(user_id)
        if not cached_tokens or cached_tokens.get("access_jti") != jti:
            raise HTTPException(status_code=401, detail="Invalid session, please login again")

        request.state.user = user_id
        return await call_next(request)