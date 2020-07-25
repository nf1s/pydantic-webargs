from examples.server import app
import pytest
import json
from pydantic_webargs import InvalidOperation
from pydantic import ValidationError


@pytest.fixture
def client():
    app.config["TESTING"] = True
    yield app.test_client()


def test_webargs_query(client):
    params = dict(name="ahmed")
    response = client.get("/get-request", query_string=params)
    expected_response = dict(payload=None, query=params)
    assert response.status_code == 200
    assert response.json == expected_response


def test_webargs_payload(client):
    data = dict(age=29)
    params = dict(name="ahmed")
    response = client.post(
        "/post-request",
        query_string=params,
        data=json.dumps(data),
        content_type="application/json",
    )
    expected_response = dict(payload=data, query=params)
    assert response.status_code == 200
    assert response.json == expected_response


def test_webargs_query_invalid(client):
    params = dict(name="ahmed")
    with pytest.raises(InvalidOperation):
        client.get("/get-request-invalid", query_string=params)


def test_webargs_query_invalid_args(client):
    params = dict(age=1234)
    with pytest.raises(ValidationError):
        client.get("/get-request-invalid-args", query_string=params)
