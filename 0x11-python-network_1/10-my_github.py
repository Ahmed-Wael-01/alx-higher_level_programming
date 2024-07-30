#!/usr/bin/python3
"""
    python script to fetch given website
"""
from requests.auth import HTTPBasicAuth
import requests
import sys

if __name__ == "__main__":
    basic = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get(
            'https://api.github.com/users/{}'.format(sys.argv[1]),
            auth=basic)
    print(r.json().get('id'))
