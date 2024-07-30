#!/usr/bin/python3
"""
    python script to fetch given website
"""

import requests
import sys

if __name__ == "__main__":
    r = requests.post(sys.argv[1])
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
