#!/usr/bin/python3
"""
    python script to fetch given website
"""

import urllib.parse, urllib.request
import sys

if __name__ == "__main__":
    data = urllib.parse.urlencode({'email': sys.argv[2]})
    data = data.encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as res:
        body = res.read()
        print(body.decode("utf-8"))
