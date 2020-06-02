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
