# redis-jwt-auth: A FastAPI Middleware for Secure JWT Authentication with Redis Caching  

## Overview  
`redis-jwt-auth` is a FastAPI middleware that provides JWT authentication with Redis-based token caching. It enhances performance by reducing database queries and ensures single active sessions per user. The package supports token rotation, secure session management, and seamless integration into FastAPI applications.  

## Key Features  
✅ **JWT Token Validation** – Decodes and verifies JWT tokens efficiently.  
✅ **Redis Caching** – Stores access tokens, refresh tokens, and user objects in Redis for fast retrieval.  
✅ **Single Active Session** – Ensures a user is logged in from only one device at a time.  
✅ **Token Rotation (Optional)** – Enhances security by refreshing tokens on every request.  
✅ **Soft-Delete Support** – Ensures inactive or deleted users cannot authenticate.  
✅ **Easy Middleware Integration** – Plug-and-play support for FastAPI applications.  

---

## **Installation**  
Install `redis-jwt-auth` using pip:  

```sh
pip install redis-jwt-auth
