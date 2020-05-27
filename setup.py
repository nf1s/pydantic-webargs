# -*- coding: utf-8 -*-
import io
import re

from setuptools import setup

with io.open("README.md") as f:
    long_description = f.read()

with io.open("pydantic_webargs/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

setup(
    name="pydantic_webargs",
    version=version,
    description="Sanic Pydatic",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://ahmednafies.github.io/pydantic_webargs/",
    author="Ahmed Nafies",
    author_email="ahmed.nafies@gmail.com",
    license="MIT",
    packages=["pydantic_webargs"],
    install_requires=["sanic", "pydantic"],
    extras_require={
        "dev": [
            "pipenv",
            "pytest",
            "coverage",
            "flake8",
            "ipdb",
            "pre-commit",
            "black",
        ],
        "docs": ["mkdocs", "mkdocs-material"],
    },
    project_urls={
        "Documentation": "https://ahmednafies.github.io/pydantic_webargs/",
        "Source": "https://github.com/ahmednafies/pydantic_webargs",
    },
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    zip_safe=False,
    python_requires=">=3.6",
)
