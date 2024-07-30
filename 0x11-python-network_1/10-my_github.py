#!/usr/bin/python3
"""
    python script to fetch given website
"""
import requests
import sys

if __name__ == "__main__":
    r = requests.get(
            'https://api.github.com/users/{}'.format(sys.argv[1]),
            auth=(sys.argv[1], sys.argv[2]))
    print(sys.argv[1], sys.argv[2])
    print(r.json().get('id'))
