redis-jwt-auth

A FastAPI Middleware for Secure JWT Authentication with Redis Caching

Overview

redis-jwt-auth is a FastAPI middleware that provides JWT authentication with Redis-based token caching. It enhances performance by reducing database queries and ensures single active sessions per user. The package supports token rotation, secure session management, and seamless integration into FastAPI applications.

Key Features

✅ JWT Token Validation – Decodes and verifies JWT tokens efficiently.

✅ Redis Caching – Stores access tokens, refresh tokens, and user objects in Redis for fast retrieval.

✅ Single Active Session – Ensures a user is logged in from only one device at a time.

✅ Token Rotation (Optional) – Enhances security by refreshing tokens on every request.

✅ Soft-Delete Support – Ensures inactive or deleted users cannot authenticate.

✅ Easy Middleware Integration – Plug and play support for FastAPI applications.

Installation

Install redis-jwt-auth using pip:

pip install redis-jwt-auth

Usage

1. Initialize Middleware in FastAPI

from fastapi import FastAPI
from redis_jwt_auth.middleware import TokenMiddleware

app = FastAPI()

app.add_middleware(
    TokenMiddleware,
    redis_host="localhost",
    redis_port=6379,
    secret_key="your_jwt_secret",
    enable_token_rotation=True  # Set to False if you don't want token rotation
)

2. Protect Routes

Use the middleware to protect routes automatically. The validated user will be available in request.state.user.

from fastapi import Depends, Request

@app.get("/protected-route")
async def protected_route(request: Request):
    user = request.state.user  # Retrieved from Redis cache
    return {"message": f"Welcome, {user['username']}!"}

3. Redis Caching Structure

Action

Description

On login

Tokens and user details are stored in Redis.

On request

JWT is validated, checked against Redis, and user details are fetched.

On logout

Tokens are deleted from Redis, ensuring session invalidation.

Configuration Options

Parameter

Type

Default

Description

redis_host

str

"localhost"

Redis server hostname

redis_port

int

6379

Redis server port

secret_key

str

Required

Secret key for JWT validation

enable_token_rotation

bool

False

Enables automatic token refresh

Future Enhancements

🚀 Support multiple active sessions per user

🚀 Role-based access control (RBAC)

🚀 Integration with OAuth & third-party authentication

🚀 Performance monitoring with Redis cache metrics

Contributing

Want to improve redis-jwt-auth? Feel free to submit issues or pull requests in the GitHub repository!