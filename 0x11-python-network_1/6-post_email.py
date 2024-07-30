#!/usr/bin/python3
"""
    python script to fetch given website
"""

import requests
import sys

if __name__ == "__main__":
    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
