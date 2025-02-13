from setuptools import setup, find_packages

setup(
    name="redis_jwt_auth",
    version="0.0.2",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "redis",
        "pyjwt",
        "starlette"
    ],
    author="Parth Singh",
    author_email="singhparth887@gmail.com",
    description="JWT authentication middleware with Redis caching for FastAPI",
    url="https://github.com/parthsingh/redis-jwt-auth",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
