from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="redis-jwt-auth",
    version="0.1.1",  # Increment the version
    author="Parth Singh",
    author_email="singhparth887@gmail.com",
    description="A FastAPI Middleware for Secure JWT Authentication with Redis Caching",
    long_description=long_description,
    long_description_content_type="text/markdown",  # This tells PyPI to render it properly
    url="https://github.com/parthsingh/redis-jwt-auth",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "redis",
        "pyjwt"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
