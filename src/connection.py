import json

import httpx

from data.constants import H_AUTHORIZATION


def extend_header(base_header, extend_header=H_AUTHORIZATION):
    base_header.update(extend_header)
    return base_header

def get_request(url, header=H_AUTHORIZATION):
    with httpx.Client() as client:
        response = client.get(url, headers=header)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        # fixme: use log
        print(response)
        return response.status_code

def put_request(url, header=H_AUTHORIZATION):
    with httpx.Client() as client:
        response = client.put(url, headers=header)
    return json.loads(response.text)


def post_request(url, header=H_AUTHORIZATION, data=None):
    with httpx.Client() as client:
        if data:
            return json.loads(client.post(url, headers=header, json=data).text)
        else:
            return json.loads(client.post(url, headers=header).text)