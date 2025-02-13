# Redis JWT Authentication Middleware
This package provides an authentication middleware for FastAPI using Redis-based JWT validation.

## Installation
```sh
pip install redis_jwt_auth
```

## Usage
```python
from fastapi import FastAPI
from redis_jwt_auth import TokenMiddleware, CacheManager, TokenValidator

app = FastAPI()
cache_manager = CacheManager()
token_validator = TokenValidator(secret_key="your_secret_key")
app.add_middleware(TokenMiddleware, cache_manager=cache_manager, token_validator=token_validator)
```