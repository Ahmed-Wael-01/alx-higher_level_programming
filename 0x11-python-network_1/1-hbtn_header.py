#!/usr/bin/python3
"""
    python script to fetch given website
"""

import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as res:
        print(dict(res.headers).get("X-Request-Id"))
