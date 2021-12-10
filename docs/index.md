# Getting Started

[![CircleCI](https://circleci.com/gh/nf1s/pydantic-webargs.svg?style=shield)](https://circleci.com/gh/nf1s/pydantic-webargs) ![CircleCI](https://img.shields.io/circleci/build/github/nf1s/pydantic-webargs/master) [![codecov](https://codecov.io/gh/nf1s/pydantic-webargs/branch/master/graph/badge.svg)](https://codecov.io/gh/nf1s/pydantic-webargs) ![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/nf1s/pydantic-webargs) ![GitHub top language](https://img.shields.io/github/languages/top/nf1s/pydantic-webargs) ![PyPI](https://img.shields.io/pypi/v/pydantic-webargs) [![Downloads](https://pepy.tech/badge/pydantic-webargs)](https://pepy.tech/project/pydantic-webargs) ![license](https://img.shields.io/badge/license-MIT-green)
![GitHub pull requests](https://img.shields.io/github/issues-pr/nf1s/pydantic-webargs) ![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/nf1s/pydantic-webargs) ![GitHub issues](https://img.shields.io/github/issues/nf1s/pydantic-webargs) ![GitHub closed issues](https://img.shields.io/github/issues-closed/nf1s/pydantic-webargs)

A library for parsing and validating http requests for Flask web framework using pydantic library

Full code on [github](https://github.com/nf1s/pydantic-webargs)

## Requirements

    python >= 3.7

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
