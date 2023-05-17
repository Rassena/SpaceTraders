import json

import httpx

from data.constants import H_AUTHORIZATION


def extend_header(base_header: {}, extend_header=H_AUTHORIZATION):
    base_header.update(extend_header)
    return base_header

def get_request(url, header=H_AUTHORIZATION):
    with httpx.Client() as client:
        response = client.get(url, headers=header)
    return json.loads(response.text)


def put_request(url, header=H_AUTHORIZATION):
    with httpx.Client() as client:
        response = client.put(url, headers=header)
    return json.loads(response.text)


def post_request(url, header=H_AUTHORIZATION, data=None):
    with httpx.Client() as client:
        response = client.post(url, headers=header, json=data)
    return json.loads(response.text)
