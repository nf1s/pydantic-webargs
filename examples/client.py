import requests

host = "http://0.0.0.0:8000"


def get_request():
    params = dict(name="my_name")
    response = requests.get(f"{host}/get-request", params=params)
    return response.json()


def post_request():
    params = dict(name="my_name")
    payload = dict(age=29)
    response = requests.post(f"{host}/post-request", params=params, json=payload)
    return response.json()


if __name__ == "__main__":
    print(get_request())
    print(post_request())
