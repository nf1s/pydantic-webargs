# Pyndatic Webargs
[![CircleCI](https://circleci.com/gh/ahmednafies/pydantic-webargs.svg?style=shield)](https://circleci.com/gh/ahmednafies/pydantic-webargs) [![codecov](https://codecov.io/gh/ahmednafies/pydantic-webargs/branch/master/graph/badge.svg)](https://codecov.io/gh/ahmednafies/pydantic-webargs) ![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/ahmednafies/pydantic-webargs) [![Downloads](https://pepy.tech/badge/pydantic-webargs)](https://pepy.tech/project/pydantic-webargs) ![license](https://img.shields.io/badge/license-MIT-green)

A library for parsing and validating http requests for flask web-framework using pydantic library 

Full documentation [here](https://ahmednafies.github.io/pydantic_webargs/)

## Requirements

	python >= 3.7

## How to install

```bash
pip install pydantic-webargs
```

## Dependencies

	flask
	pydantic

## Example


```python
from flask import Flask
from pydantic import BaseModel
from pydantic_webargs import webargs

app = Flask(__name__)


class QueryModel(BaseModel):
    name: str


class BodyModel(BaseModel):
    age: int


@app.route("/get-request", methods=["GET"])
@webargs(query=QueryModel)
def example_get_endpoint(**kwargs):
    response = kwargs
    return response


@app.route("/post-request", methods=["POST"])
@webargs(query=QueryModel, body=BodyModel)
def example_post_endpoint(**kwargs):
    print(kwargs)
    response = kwargs
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
```
