# Getting Started

[![CircleCI](https://circleci.com/gh/ahmednafies/pydantic-webargs.svg?style=shield)](https://circleci.com/gh/ahmednafies/pydantic-webargs) ![CircleCI](https://img.shields.io/circleci/build/github/ahmednafies/pydantic-webargs/master) [![codecov](https://codecov.io/gh/ahmednafies/pydantic-webargs/branch/master/graph/badge.svg)](https://codecov.io/gh/ahmednafies/pydantic-webargs) ![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/ahmednafies/pydantic-webargs) ![GitHub top language](https://img.shields.io/github/languages/top/ahmednafies/pydantic-webargs) ![PyPI](https://img.shields.io/pypi/v/pydantic-webargs) [![Downloads](https://pepy.tech/badge/pydantic-webargs)](https://pepy.tech/project/pydantic-webargs) ![license](https://img.shields.io/badge/license-MIT-green)
![GitHub pull requests](https://img.shields.io/github/issues-pr/ahmednafies/pydantic-webargs) ![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/ahmednafies/pydantic-webargs) ![GitHub issues](https://img.shields.io/github/issues/ahmednafies/pydantic-webargs) ![GitHub closed issues](https://img.shields.io/github/issues-closed/ahmednafies/pydantic-webargs)

A library for parsing and validating http requests for Flask web framework using pydantic library

Full code on [github](https://github.com/ahmednafies/pydantic-webargs)

## Requirements

    python >= 3.6

## How to install

```bash
pip install pydantic-webargs
```

## Dependencies

	flask
	pydantic

## How to use

```python
from flask import Flask
from pydantic import BaseModel
from pydantic_webargs import webargs

app = Flask(__name__)


class QueryModel(BaseModel):
    name: str


class BodyModel(BaseModel):
    age: int


@app.route("/post-request", methods=["POST"])
@webargs(query=QueryModel, body=BodyModel)
def example_post_endpoint(**kwargs):
    print(kwargs)
    response = kwargs
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
```
