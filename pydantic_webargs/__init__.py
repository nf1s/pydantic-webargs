# -*- coding: utf-8 -*-
from functools import wraps

from flask import request

__author__ = "Ahmed Nafies <ahmed.nafies@gmail.com>"
__copyright__ = "Copyright 2020, Ahmed Nafies"
__license__ = "MIT"
__version__ = "1.1.0"


BODY_METHODS = ["POST", "PUT", "PATCH"]


class Error(Exception):
    def __init__(self, message):
        self.message = message


class InvalidOperation(Error):
    pass


def validate(query, body):

    payload = None
    query_params = None
    if body and request.method not in BODY_METHODS:
        raise InvalidOperation(
            f"Http method '{request.method}' does not contain a payload,"
            "yet a Pyndatic model for body was suppied"
        )
    if body:
        payload = body(**request.json).dict()

    if query:
        params = request.args
        query_params = query(**params).dict()
    return dict(payload=payload, query=query_params)


def webargs(query=None, body=None):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            result = validate(query, body)
            kwargs.update(result)
            response = f(*args, **kwargs)
            return response

        return decorated_function

    return decorator
