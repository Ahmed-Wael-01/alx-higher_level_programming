#!/usr/bin/python3
"""
    python script to fetch given website
"""

import urllib.error
import urllib.request
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as res:
            print(res.read().decode('UTF-8'))
    except urllib.error.HTTPError as er:
        print('Error code:', er.code)
