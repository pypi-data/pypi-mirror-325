from setuptools import setup, find_packages

setup(
    name="redis_jwt_auth",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "redis",
        "pyjwt",
        "starlette"
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="JWT authentication middleware with Redis caching for FastAPI",
    url="https://github.com/yourusername/redis-jwt-auth",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
